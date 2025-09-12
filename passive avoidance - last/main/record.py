import cv2
from picamera2 import Picamera2

from ultralytics import YOLO

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)  # Smaller resolution
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate = 30  # Set to 30 FPS explicitly
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# Use a smaller YOLO model for higher performance
model = YOLO("yolo11n.pt")  # Use the smallest available model

# Set inference size smaller
results = model.track(frame, persist=True, imgsz=320)  # Smaller image size

# Check model is loaded properly
print(f"Model loaded: {model}")
print(f"Available classes: {model.names}")

# Make sure class_id 1 corresponds to 'lab-mouse'
expected_class_id = 1
if expected_class_id < len(model.names):
    print(f"Class {expected_class_id} is: {model.names[expected_class_id]}")
else:
    print(f"Error: Model doesn't have class_id {expected_class_id}")

frame_count = 0  # Initialize frame counter

# For video files, pre-buffer frames
frame_buffer = []
max_buffer_size = 30  # Buffer 30 frames

# First, fill buffer
for _ in range(max_buffer_size):
    success, frame = cap.read()
    if not success:
        break
    frame_buffer.append(frame)

# Use threading for better performance
import threading

# Create thread-safe frame buffer
from queue import Queue
frame_buffer = Queue(maxsize=10)

def capture_frames():
    while True:
        frame = picam2.capture_array()
        if not frame_buffer.full():
            frame_buffer.put(frame)

# Start capture thread
thread = threading.Thread(target=capture_frames)
thread.daemon = True
thread.start()

# Main loop processes frames from the buffer
while True:
    if not frame_buffer.empty():
        frame = frame_buffer.get()
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("Camera", annotated_frame)
    
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()