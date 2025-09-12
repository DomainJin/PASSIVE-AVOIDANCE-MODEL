import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap, QPainter, QPen, QColor
from main_interface_fixed import Ui_MainWindow
from ultralytics import YOLO
from datetime import datetime
import os
import time
import threading
from queue import Queue
from PySide6.QtCore import Signal as pyqtSignal, Slot as pyqtSlot, QThread

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    
    def __init__(self, camera_id=0, model_path="yolov8n.pt"):
        super().__init__()
        self.camera_id = camera_id
        self.model_path = model_path
        self._run_flag = True
        
    def run(self):
        # Load the YOLOv8 model
        try:
            self.model = YOLO(self.model_path)
            print(f"Model loaded: {self.model}")
        except Exception as e:
            print(f"Error loading model: {e}")
            return

        # Capture from webcam
        self.cap = cv2.VideoCapture(self.camera_id)
        if not self.cap.isOpened():
            print("Error: Cannot open camera")
            return
            
        while self._run_flag:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Cannot read frame")
                break
                
            # Process with YOLO (tracking)
            results = self.model.track(frame, persist=True)
            
            # Get frame with annotations (boxes) but WITHOUT text
            annotated_frame = frame.copy()
            
            if results and len(results) > 0:
                boxes = results[0].boxes
                if boxes is not None and len(boxes) > 0:
                    class_ids = boxes.cls
                    
                    for i, box in enumerate(boxes):
                        class_id = int(class_ids[i].item())
                        
                        # Check if this is lab-mouse (class ID 1)
                        if class_id == 1:
                            # Get bounding box coordinates
                            lab_mouse = box.xyxy[0].cpu().numpy()
                            x1, y1, x2, y2 = map(int, lab_mouse)
                            
                            # Draw ONLY the bounding box (no text)
                            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                            
                            # Add a highlight for visibility
                            overlay = annotated_frame.copy()
                            cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 0, 255), -1)
                            cv2.addWeighted(overlay, 0.3, annotated_frame, 0.7, 0, annotated_frame)
            
            # Emit signal with just the frame
            self.change_pixmap_signal.emit(annotated_frame)
            
            # Small sleep to prevent CPU overload
            time.sleep(0.001)
        
        # Clean up
        self.cap.release()
    
    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class Myserver(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Passive Avoidance Test")
        
        # Khởi tạo biến camera
        self.cap = None
        self.camera_timer = None
        
        # Khởi tạo model YOLO
        try:
            self.model = YOLO("best.pt")
            print("Model YOLO đã được tải thành công!")
        except Exception as e:
            print(f"Lỗi khi tải model YOLO: {e}")
            self.model = None
            
        # Set window properties
        self.setWindowTitle("Interface Test")
        
        # Kết nối nút start với hàm xử lý
        self.button_start.clicked.connect(self.on_button_start_clicked)
        
        # Thiết lập video thread cho tracking
        self.setup_tracking_video()
        
        self.show()    
    def on_button_start_clicked(self):
        # This function will be called when the start button is clicked
        self.tracking.setText("Tracking started")
        print("Start button clicked, tracking started.")
        
        id = self.idmouse.currentText()
        st = self.status.currentText()
        dr = self.drug.currentText()
        rt = self.runtime.value()  # Thời gian chạy (giây)
        
        # Đảm bảo runtime tối thiểu là 5 giây để tránh video 0 giây
        if rt < 5:
            rt = 5
            print(f"Runtime đã được điều chỉnh lên tối thiểu 5 giây")
            
        print(f"ID: {id}, Status: {st}, Drug: {dr}, Runtime: {rt} giây")
        
        # Tạo thư mục để lưu video
        self.folder_path = self.create_folder(id, st, dr)
        
        # Hiển thị nhóm Operation
        self.group_main.setVisible(True)
        
        # Khởi động camera và bắt đầu quay video
        self.start_recording(self.folder_path, rt)
    def start_recording(self, folder_path, runtime):
        """Bắt đầu quay video trong thời gian runtime (giây) và lưu vào thư mục folder_path"""
        # Khởi tạo camera nếu chưa được khởi tạo
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                QMessageBox.critical(self, "Lỗi", "Không thể mở camera!")
                return
                
        # Đợi camera khởi động hoàn toàn và đọc 5 frame ban đầu để camera ổn định
        for _ in range(5):
            ret, _ = self.cap.read()
            if not ret:
                QMessageBox.critical(self, "Lỗi", "Không thể đọc frame từ camera!")
                return
            # Đợi một chút giữa các frame
            QApplication.processEvents()
        
        # Đọc kích thước thực tế của frame
        ret, test_frame = self.cap.read()
        if not ret or test_frame is None:
            QMessageBox.critical(self, "Lỗi", "Không thể đọc frame từ camera!")
            return
            
        # Lấy kích thước frame thực tế
        height, width = test_frame.shape[:2]
        
        # Định nghĩa codec và tạo VideoWriter
        try:
            # Thử dùng H264 trước (tương thích tốt hơn với MP4)
            fourcc = cv2.VideoWriter_fourcc(*'H264')
        except:
            # Nếu không thành công, dùng MP4V
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            
        fps = 30.0  # Giảm xuống còn 20fps để đảm bảo xử lý kịp thời
        video_size = (width, height)  # Sử dụng kích thước thực từ frame
        
        video_filename = os.path.join(folder_path, f"recording.mp4")
        print(f"Đang chuẩn bị ghi video vào: {video_filename}")
        print(f"Kích thước video: {video_size[0]}x{video_size[1]}, FPS: {fps}")
        
        self.video_writer = cv2.VideoWriter(video_filename, fourcc, fps, video_size)
        
        # Lưu thời điểm bắt đầu và thời gian quay
        self.recording_start_time = datetime.now()
        self.recording_duration = runtime
        
        # Khởi tạo QTimer để cập nhật frame
        if self.camera_timer is None:
            self.camera_timer = QTimer()
            self.camera_timer.timeout.connect(self.update_frame)
        
        # Bắt đầu timer
        self.camera_timer.start(30)  # Cập nhật mỗi 30ms (~33fps)
        
        # Hiển thị thông báo
        self.tracking.setText(f"Đang quay video: 0/{runtime}s")
        
        # Set up another timer to stop recording after runtime seconds
        QTimer.singleShot(runtime * 1000, self.stop_recording)
        
    def update_frame(self):
        """Cập nhật frame từ camera và ghi vào file video"""
        if self.cap is None or not self.cap.isOpened():
            return
            
        # Đọc frame từ camera
        ret, frame = self.cap.read()
        if not ret:
            return
            
        # Thực hiện dự đoán YOLO trên frame
        detected_mouse = False
        mouse_center = None
        if self.model is not None:
            results = self.model.predict(source=frame, show=False)
            # Lấy frame đã được xử lý với các bounding box
            if len(results) > 0:
                # Lấy kết quả từ model
                result = results[0]
                
                # Vẽ các bounding box
                frame_with_boxes = result.plot()
                
                # Kiểm tra có phát hiện chuột không
                if len(result.boxes) > 0:
                    detected_mouse = True
                    # Lấy thông tin box đầu tiên (giả sử là chuột)
                    box = result.boxes[0]
                    # Lấy tọa độ box (x1, y1, x2, y2)
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    
                    # Tính toán trung tâm
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    mouse_center = (center_x, center_y)
                    
                    # Vẽ dấu chữ thập tại trung tâm
                    cv2.drawMarker(frame_with_boxes, mouse_center, (0, 255, 255), 
                                  markerType=cv2.MARKER_CROSS, markerSize=20, thickness=2)
                    
                    # Hiển thị tọa độ trung tâm
                    cv2.putText(frame_with_boxes, f"Center: ({center_x}, {center_y})", 
                               (center_x - 100, center_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 
                               0.7, (0, 255, 255), 2)
                    
                    # Hiển thị confidence score
                    confidence = float(box.conf[0])
                    cv2.putText(frame_with_boxes, f"Conf: {confidence:.2f}", 
                               (center_x - 100, center_y + 20), cv2.FONT_HERSHEY_SIMPLEX, 
                               0.7, (0, 255, 255), 2)
            else:
                frame_with_boxes = frame
        else:
            frame_with_boxes = frame
            
        # Thêm thông báo trạng thái tracking
        status_text = "Mouse detected" if detected_mouse else "No mouse detected"
        cv2.putText(frame_with_boxes, status_text, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255) if not detected_mouse else (0, 255, 0), 2)
            
        # Ghi vào file video
        if hasattr(self, 'video_writer') and self.video_writer is not None:
            self.video_writer.write(frame_with_boxes)
        
        # Hiển thị frame trong giao diện
        self.show_frame_on_label(frame_with_boxes)        # Cập nhật thời gian quay đã trôi qua
        if hasattr(self, 'recording_start_time') and hasattr(self, 'recording_duration'):
            elapsed = (datetime.now() - self.recording_start_time).total_seconds()
            remaining = max(0, self.recording_duration - elapsed)
            self.tracking.setText(f"Đang quay video: {int(elapsed)}/{self.recording_duration}s")
            
            # Debug log
            if int(elapsed) % 5 == 0:  # Log mỗi 5 giây
                frames_written = self.video_writer.get(cv2.CAP_PROP_FRAME_COUNT) if hasattr(self, 'video_writer') else 0
                print(f"Đã ghi {int(elapsed)}s | Khoảng {int(frames_written)} frames")
    def show_frame_on_label(self, frame):
        """Hiển thị frame lên giao diện"""
        # Chuyển BGR (OpenCV) sang RGB (Qt)
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        
        # Hiển thị lên label tracking với kích thước tối ưu
        self.tracking.setPixmap(pixmap)
        self.tracking.setScaledContents(True)
        
        # Đảm bảo label hiển thị rõ ràng
        self.tracking.setMinimumSize(400, 300)  # Đặt kích thước tối thiểu để đảm bảo hiển thị
    def stop_recording(self):
        """Dừng quay video và đóng file"""
        print("Đang kết thúc quá trình ghi video...")
        
        # Đảm bảo dữ liệu được ghi hết trước khi đóng
        if hasattr(self, 'video_writer') and self.video_writer is not None:
            # Thêm vài frame cuối để đảm bảo video đủ dài
            if self.cap is not None and self.cap.isOpened():
                for _ in range(10):  # Thêm 10 frame cuối
                    ret, frame = self.cap.read()
                    if ret:
                        self.video_writer.write(frame)
        
        # Dừng timer
        if self.camera_timer is not None and self.camera_timer.isActive():
            self.camera_timer.stop()
            print("Đã dừng camera timer")
            
        # Đóng writer
        if hasattr(self, 'video_writer') and self.video_writer is not None:
            self.video_writer.release()
            self.video_writer = None
            print("Đã đóng video writer")
        
        # Kiểm tra file video
        video_path = os.path.join(self.folder_path, "recording.mp4")
        if os.path.exists(video_path):
            file_size = os.path.getsize(video_path) / (1024*1024)  # Size in MB
            print(f"Video đã được lưu: {video_path}")
            print(f"Kích thước file: {file_size:.2f} MB")
            
            if file_size < 0.1:  # Nếu file nhỏ hơn 0.1MB (~100KB)
                print("Cảnh báo: File video có kích thước rất nhỏ, có thể bị lỗi!")
        else:
            print("Cảnh báo: Không tìm thấy file video!")
            
        # Thông báo
        self.tracking.setText(f"Video đã được lưu vào {self.folder_path}")
        QMessageBox.information(self, "Hoàn thành", f"Quá trình ghi video đã hoàn thành!\nVideo đã được lưu vào thư mục {self.folder_path}")
    
    def create_folder(self, x, y, z):
        current_time = datetime.now()
        # Format the date and time without invalid characters for Windows
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        folder_name = f"{formatted_time}_{x}_{y}_{z}"
        os.makedirs(folder_name, exist_ok=True)
        return folder_name

    def closeEvent(self, event):
        """Dọn dẹp tài nguyên khi đóng ứng dụng"""
        # Dừng quay video nếu đang quay
        if hasattr(self, 'video_writer') and self.video_writer is not None:
            self.video_writer.release()
            self.video_writer = None
            
        # Dừng timer nếu đang chạy
        if hasattr(self, 'camera_timer') and self.camera_timer and self.camera_timer.isActive():
            self.camera_timer.stop()
        
        # Giải phóng camera nếu đang mở
        if self.cap is not None and self.cap.isOpened():
            self.cap.release()
            self.cap = None
        
        # Dừng video thread nếu đang chạy
        if hasattr(self, 'video_thread'):
            self.video_thread.stop()
        
        event.accept()

    def setup_tracking_video(self):
        # Make sure self.tracking is a QLabel
        
        # Set up the video thread
        self.video_thread = VideoThread()
        self.video_thread.change_pixmap_signal.connect(self.update_tracking_image)
        
        # Start thread
        self.video_thread.start()

    @pyqtSlot(np.ndarray)
    def update_tracking_image(self, cv_img):
        """Updates the tracking label with a new opencv image"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        
        # Scale to fit the label while maintaining aspect ratio
        p = qt_image.scaled(self.tracking.width(), self.tracking.height(), 
                            Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.tracking.setPixmap(QPixmap.fromImage(p))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Myserver()
    sys.exit(app.exec())
