import cv2
from picamera2 import Picamera2
from ultralytics import YOLO
from ultralytics import solutions
from main_interface import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QTableWidget,QTableWidgetItem,QWidget
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer
import pandas as pd
import resource_rc
from PySide6.QtCore import Qt
import minimalmodbus
import serial
import time
import sys
import os
import openpyxl
from openpyxl import Workbook
from datetime import datetime
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class MyServer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        global time_mouse_change
        self.setupUi(self)
        self.setWindowTitle("Passive Avoidance Test")
        self.instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 10)  # port name, slave address (in decimal)
        self.instrument.serial.timeout = 3
        self.U = self.instrument.read_register(0, 0)/100  # Registernumber, number of decimals
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.load_mearsure)  # Khi h?t th?i gian, g?i load_mearsure
        self.timer.start(1000) 
        # ledstatus = input("Give in 0 or 1 to turn on or off the led: ")
        # instrument.write_register(2, int(ledstatus), 0) 
        # Initialize the Picamera2
        self.picam2 = Picamera2()
        self.picam2.preview_configuration.main.size = (1280, 700)
        self.picam2.preview_configuration.main.format = "RGB888"
        self.picam2.preview_configuration.align()
        self.picam2.configure("preview")
        self.picam2.start()
        # Load the YOLO model
        self.model = YOLO("best1.pt")
        # Initialize heatmap generation using the ultralytics solution
        self.heatmap = solutions.Heatmap(colormap=cv2.COLORMAP_PARULA, show=True, model="best1.pt", classes=[1])
        # Setup the tracking QLabel for displaying the frame
        self.tracking = QLabel(self.grouptrack)  # Assuming self.grouptrack is your layout/container
        self.tracking.setGeometry(60, 30, 507, 245)  # Set to the desired size
        
         
        self.group_main.setVisible(False)
        self.group_output.setVisible(False)
        self.resize(1208, 300)  # �i?u ch?nh k�ch thu?c c?a s? sao cho v?a d? (thay d?i chi?u cao cho ph� h?p)
        # Optional: Create a timer for continuous frame capture (initially stopped)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera_feed)
        # Connect button_start to start camera feed
        self.button_start.clicked.connect(self.on_button_start_clicked)
        self.previous_state = "Start"
        self.state_str = "Start"
        # B? d?m th?i gian (timer) d? x? l� 5 gi�y
        self.right_border_timer = None
        self.mouse_in_right_position = False
    def load_mearsure(self):
        try:
            # �?c gi� tr? t? Modbus
            self.U = self.instrument.read_register(0, 0) / 100  # �i?n �p
            self.I = self.instrument.read_register(1, 0) / 10   # D�ng di?n
            # Hi?n th? c�c gi� tr? l�n QLCDNumber
            self.volt.display(self.U)
            self.amp.display(self.I)
            # In ra gi� tr? d? debug
            # print(f"C?p nh?t gi� tr?: �i?n �p = {self.U}, D�ng di?n = {self.I}")
        except Exception as e:
            print(f"Doc ko dc {e}")
    def on_button_start_clicked(self):
        # When the button is clicked, start capturing frames and stop automatic updates
        id = self.idmouse.currentText()
        st = self.status.currentText()
        dr = self.drug.currentText()
        runtime = self.runtime.value()  # L?y gi� tr? runtime t? QSpinBox
        # T?o thu m?c luu tr?
        global folder
        folder = self.create_folder(id, st, dr)
        global excel_file
        excel_file = os.path.join(folder, "data.xlsx")
        print(excel_file)
        # self.load_excel_file(excel_file)
        # Show the group_output after the button is clicked
        self.group_output.setVisible(True)
        self.group_excel.setVisible(True)
        self.timer.start(30)  # Start the timer with 30 ms interval
        self.update_camera_feed()  # Also call update_camera_feed immediately      
        # Show the group_output after the button is clicked
        self.group_output.setVisible(True)
        self.previous_time = datetime.now()
    def get_mouse_x_coordinates(results):
        if results and len(results) > 0:
            boxes = results[0].boxes
            if boxes is not None and len(boxes) > 0:
                class_ids = boxes.cls
                
                for i, box in enumerate(boxes):
                    class_id = int(class_ids[i].item())
                    
                    # Kiểm tra nếu đây là chuột (class_id=1 cho lab-mouse)
                    if class_id == 1:
                        # Lấy tọa độ bounding box
                        bbox = box.xyxy[0].cpu().numpy()
                        x1, y1, x2, y2 = map(int, bbox)
                        
                        # Trả về tọa độ x1, x2
                        return x1, x2
        
        # Trả về None nếu không phát hiện chuột
        return None, None
    def update_camera_feed(self):
        self.group_main.setVisible(True)
        self.group_output.setVisible(True)
        # Thay d?i k�ch thu?c c?a s? sao cho ph� h?p v?i n?i dung
        self.resize(1208, 882)
        # Capture frame-by-frame
        frame = self.picam2.capture_array()
        # Run YOLO inference on the frame
        results = self.model(frame)
        # Extract boxes and class information
        boxes = results[0].boxes
        class_ids = boxes.cls  # Get class IDs for each box
        # Generate the heatmap for the current frame
        im0_with_heatmap = self.heatmap.generate_heatmap(frame)
        image_path = os.path.join(folder, 'heatmap_image.jpg')

# Save the image
        cv2.imwrite(image_path, im0_with_heatmap)
        # Initialize variables for the border and lab-mouse

        x1, x2 = get_mouse_x_coordinates(results)
        height, width = frame.shape[:2]
    
    # Tính tọa độ x chính giữa
        x_center = width // 2
        if x1 is not None and x2 is not None:
            current_time = time.time()
            if x2 < x_center:  # Lab-mouse is to the left of the border
                print("Lab-mouse is to the left of the border")
                self.state_str = "Black box to White box"
                
                self.instrument.write_register(2, 0, 0)
            elif x1 > x_center:  # Lab-mouse is to the right of the border
                print("Lab-mouse is to the right of the border")
                self.state_str = "White box to Black box"
                time_mouse_change = current_time
                # Start or reset the timer if the mouse moves to the right
                if not self.mouse_in_right_position:
                    self.mouse_in_right_position = True
                    self.start_right_border_timer()
        if self.state_str != self.previous_state:
            self.save_change(self.previous_state)
            self.previous_state = self.state_str 
        # Visualize or handle the rest of the processingsss
        annotated_frame = results[0].plot()
        # Convert OpenCV frame (BGR) to QImage (RGB)
        rgb_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        height, width, channel = rgb_frame.shape
        bytes_per_line = 3 * width
        q_image = QImage(rgb_frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        # Convert heatmap (BGR) to QImage (RGB)
        rgb_frame1 = cv2.cvtColor(im0_with_heatmap, cv2.COLOR_BGR2RGB)
        height1, width1, channel1 = rgb_frame1.shape
        bytes_per_line1 = 3 * width1
        q_heatmap = QImage(rgb_frame1.data, width1, height1, bytes_per_line1, QImage.Format_RGB888)
        # Resize the frames to fit within 507x245 while maintaining aspect ratio
        new_width, new_height = self.calculate_aspect_ratio_resize(width, height, 507, 245)
        resized_image = q_image.scaled(new_width, new_height)
        resized_heatmap = q_heatmap.scaled(new_width, new_height)
        # Update QLabel with the resized image
        self.tracking.setPixmap(QPixmap.fromImage(resized_image))
        self.heatmap_label.setPixmap(QPixmap.fromImage(resized_heatmap))
        self.load_excel_file()
        total_time_on,total_time_off = self.total_time(excel_file)
        print(f"Total Time White: {total_time_on} second")
        print(f"Total Time Black: {total_time_off} second")
        self.create_chart(total_time_on,total_time_off)
        self.load_image(folder)
    def calculate_aspect_ratio_resize(self, original_width, original_height, target_width, target_height):
        # Calculate aspect ratios
        aspect_ratio = original_width / original_height
        target_aspect_ratio = target_width / target_height
        if aspect_ratio > target_aspect_ratio:
            # If the image is wider than the target size, adjust width
            new_width = target_width
            new_height = int(target_width / aspect_ratio)
        else:
            # If the image is taller than the target size, adjust height
            new_height = target_height
            new_width = int(target_height * aspect_ratio)
        return new_width, new_height
    
    
    def load_image(self,folder):
        image = os.path.join(folder, 'chart.png')
        pixmap = QPixmap(image)
        scaled_pixmap = pixmap.scaled(511, 188, Qt.AspectRatioMode.KeepAspectRatio)
        self.chart.setPixmap(scaled_pixmap)
    def create_folder(self, x, y, z):
        current_time = datetime.now()
            # Format the date and time in YYYY-MM-DD HH:MM:SS
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        folder_name = f"{formatted_time}_{x}_{y}_{z}"
        os.makedirs(folder_name, exist_ok=True)
        return folder_name
    
    
    def your_slot_function(self):
        # Your implementation here
        pass
# Run the application
if __name__ == "__main__":
    app = QApplication([])
    window = MyServer()
    window.show()
    app.exec()
