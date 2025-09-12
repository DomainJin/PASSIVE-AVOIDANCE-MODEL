# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'interface.ui'
#
# Created by: Qt User Interface Compiler version 6.8.1
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTimer, QEasingCurve, 
    QPropertyAnimation, QParallelAnimationGroup, QSequentialAnimationGroup, 
    QAbstractAnimation)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHeaderView, QLCDNumber, QLabel, QMainWindow,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QWidget, QPushButton, QGraphicsDropShadowEffect, QMessageBox)
from PySide6 import QtGui
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1208, 900)  # Reduced height since we're removing group_output
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"\n"
"background-color:  rgb(170, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(-1, -1, 1221, 71))
        self.groupBox_3.setStyleSheet(u"background-color:rgb(28, 167, 252)")
        self.tdtu = QLabel(self.groupBox_3)
        self.tdtu.setObjectName(u"tdtu")
        self.tdtu.setGeometry(QRect(0, -10, 121, 91))
        self.tdtu.setPixmap(QPixmap(u":/newPrefix/tdtu.png"))
        self.phar = QLabel(self.groupBox_3)
        self.phar.setObjectName(u"phar")
        self.phar.setGeometry(QRect(1110, 0, 101, 81))
        self.phar.setPixmap(QPixmap(u":/newPrefix/duoc.jpeg"))
        self.title = QLabel(self.groupBox_3)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(420, 20, 441, 31))
        font = QFont()
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.title.setWordWrap(True)
        self.title.setOpenExternalLinks(False)
        self.group_input = QGroupBox(self.centralwidget)
        self.group_input.setObjectName(u"group_input")
        self.group_input.setGeometry(QRect(29, 89, 1151, 101))
        font1 = QFont()
        font1.setPointSize(24)
        self.group_input.setFont(font1)
        self.group_input.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.button_start = QPushButton(self.group_input)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(1000, 0, 111, 121))
        self.button_start.setIcon(QIcon(u":/newPrefix/start.png"))
        self.button_start.setIconSize(QSize(100, 100))
        self.button_start.setStyleSheet(u"""
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgba(200, 255, 200, 100);
            }
            QPushButton:pressed {
                background-color: rgba(150, 255, 150, 150);
                margin: 2px;
            }
        """)
        self.button_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.status = QComboBox(self.group_input)
        self.status.addItem("")
        self.status.addItem("")
        self.status.addItem("")
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(270, 50, 111, 31))
        self.status.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.group_input)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 61, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.label.setFont(font2)
        self.idmouse = QComboBox(self.group_input)
        self.idmouse.addItem("")
        self.idmouse.addItem("")
        self.idmouse.addItem("")
        self.idmouse.setObjectName(u"idmouse")
        self.idmouse.setEnabled(True)
        self.idmouse.setGeometry(QRect(90, 50, 111, 31))
        self.idmouse.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.idmouse.setMinimumContentsLength(5)
        self.label_1 = QLabel(self.group_input)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(220, 50, 41, 31))
        self.label_1.setFont(font2)
        self.label_2 = QLabel(self.group_input)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 50, 41, 31))
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.group_input)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(580, 50, 61, 31))
        self.label_3.setFont(font2)
        self.drug = QComboBox(self.group_input)
        self.drug.addItem("")
        self.drug.addItem("")
        self.drug.addItem("")
        self.drug.setObjectName(u"drug")
        self.drug.setGeometry(QRect(440, 50, 111, 31))
        self.drug.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.runtime = QSpinBox(self.group_input)
        self.runtime.setObjectName(u"runtime")
        self.runtime.setGeometry(QRect(650, 50, 45, 45))
        self.volt = QLCDNumber(self.group_input)
        self.volt.setObjectName(u"volt")
        self.volt.setGeometry(QRect(770, 60, 64, 23))
        self.amp = QLCDNumber(self.group_input)
        self.amp.setObjectName(u"amp")
        self.amp.setGeometry(QRect(910, 60, 64, 23))
        self.label_4 = QLabel(self.group_input)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(730, 40, 91, 21))
        self.label_4.setFont(font2)
        self.label_5 = QLabel(self.group_input)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(870, 40, 81, 21))
        self.label_5.setFont(font2)
        self.group_main = QGroupBox(self.centralwidget)
        self.group_main.setObjectName(u"group_main")
        self.group_main.setGeometry(QRect(30, 200, 1151, 680))
        self.group_main.setFont(font1)
        self.group_main.setStyleSheet(u"border-color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 186, 116)")
        self.grouptrack = QGroupBox(self.group_main)
        self.grouptrack.setObjectName(u"grouptrack")
        self.grouptrack.setGeometry(QRect(20, 50, 1110, 890))
        font3 = QFont()
        font3.setPointSize(14)
        self.grouptrack.setFont(font3)
        self.grouptrack.setLayoutDirection(Qt.LeftToRight)
        self.grouptrack.setAutoFillBackground(False)
        self.grouptrack.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.gridLayout_4 = QGridLayout(self.grouptrack)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tracking = QLabel(self.grouptrack)
        self.tracking.setObjectName(u"tracking")
        self.tracking.setEnabled(True)
        self.tracking.setMaximumSize(QSize(1000, 505))
        font4 = QFont()
        font4.setKerning(False)
        self.tracking.setFont(font4)
        self.tracking.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.tracking.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.tracking, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.group_main.raise_()
        self.groupBox_3.raise_()
        self.group_input.raise_()

        # Make the tracking section wider since heatmap is removed
        self.grouptrack.setGeometry(QRect(20, 50, 1110, 600))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Software Detect Object", None))
        self.groupBox_3.setTitle("")
        self.tdtu.setText("")
        self.phar.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"PASSIVE AVOIDANCE TEST", None))
        self.group_input.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.button_start.setText("")
        self.status.setItemText(0, QCoreApplication.translate("MainWindow", u"Canxi", None))
        self.status.setItemText(1, QCoreApplication.translate("MainWindow", u"Vitamin", None))
        self.status.setItemText(2, QCoreApplication.translate("MainWindow", u"Dopamine", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"ID Mouse:", None))
        self.idmouse.setItemText(0, QCoreApplication.translate("MainWindow", u"JERRY-123", None))
        self.idmouse.setItemText(1, QCoreApplication.translate("MainWindow", u"MICKEY-456", None))
        self.idmouse.setItemText(2, QCoreApplication.translate("MainWindow", u"SPEEDY-789", None))

        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Drug:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Run time:", None))
        self.drug.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.drug.setItemText(1, QCoreApplication.translate("MainWindow", u"Amnesia", None))
        self.drug.setItemText(2, QCoreApplication.translate("MainWindow", u"Injected", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Voltage (VAC):", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Current (mA):", None))
        self.group_main.setTitle(QCoreApplication.translate("MainWindow", u"Operation", None))
        self.grouptrack.setTitle(QCoreApplication.translate("MainWindow", u"Tracking", None))
        self.tracking.setText(QCoreApplication.translate("MainWindow", u"Tracking", None))
        
        # Change font for labels
        font = QtGui.QFont()
        font.setFamily("Arial")  # Font family
        font.setPointSize(10)    # Font size
        font.setBold(True)       # Bold
        font2 = QtGui.QFont()
        font2.setFamily("Times New Roman")
        font2.setPointSize(12)
        font2.setItalic(True)
        # Apply font to specific labels
        self.label.setFont(font)
        self.label_1.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font2)
        self.label_5.setFont(font2)
        # Add more labels as needed
    
        # If you want different fonts for different labels
        # font2 = QtGui.QFont()
        # font2.setFamily("Times New Roman")
        # font2.setPointSize(12)
        # font2.setItalic(True)
        # self.label_3.setFont(font2)
    # retranslateUi
    
    # UI related functions moved from run_main.py
    def setup_ui_effects(self, parent):
        # Thêm hiệu ứng đổ bóng cho các khung nhóm
        self.add_shadow(parent, self.group_input)
        self.add_shadow(parent, self.group_main)
        
        # Làm tròn góc cho các nhóm bằng cách cập nhật stylesheet đúng cách
        input_style = self.group_input.styleSheet() + "; border-radius: 15px;"
        main_style = self.group_main.styleSheet() + "; border-radius: 15px;"
        
        self.group_input.setStyleSheet(input_style)
        self.group_main.setStyleSheet(main_style)
        
        # Tạo nút đóng ứng dụng
        self.close_button = QPushButton("✕", parent)
        self.close_button.setGeometry(1170, 10, 30, 30)
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 0, 0, 0);
                color: white;
                font-weight: bold;
                font-size: 16px;
                border: none;
            }
            QPushButton:hover {
                background-color: red;
            }
        """)
        self.close_button.clicked.connect(parent.close)
        
        # Thiết lập giá trị mặc định và phạm vi cho runtime
        self.runtime.setRange(1, 3600)  # 1 giây đến 1 giờ
        self.runtime.setValue(30)  # Giá trị mặc định 30 giây
        self.runtime.setSuffix(" s")  # Hiển thị đơn vị giây
        self.runtime.setStyleSheet("background-color: white; font-size: 14px; font-weight: bold;")
        
        # Hiệu ứng hover cho combobox
        combobox_style = """
            QComboBox {
                border: 1px solid #76797C;
                border-radius: 5px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
            }
            QComboBox:hover {
                border: 1px solid #3DAEE9;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: darkgray;
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            QComboBox::down-arrow {
                image: url(:/newPrefix/down_arrow.png);
            }
        """
        self.idmouse.setStyleSheet(combobox_style)
        self.status.setStyleSheet(combobox_style)
        self.drug.setStyleSheet(combobox_style)
        
    def add_shadow(self, parent, widget):
        shadow = QGraphicsDropShadowEffect(parent)
        shadow.setBlurRadius(15)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 150))
        widget.setGraphicsEffect(shadow)
    
    def blink_effect(self, parent):
        # Hiệu ứng nhấp nháy cho title và các label khác
        if hasattr(parent, "blink_on") and parent.blink_on:
            self.title.setStyleSheet("color: rgb(255, 255, 255);")
            parent.blink_on = False
        else:
            self.title.setStyleSheet("color: rgb(255, 255, 0);")  # Màu vàng
            parent.blink_on = True
    
    def create_button_from_label(self, parent):
        # Tạo QPushButton ở cùng vị trí với QLabel button_start
        self.start_button = QPushButton(self.group_input)
        self.start_button.setGeometry(self.button_start.geometry())
        self.start_button.setCursor(Qt.PointingHandCursor)
        self.start_button.setStyleSheet("background-color: transparent;")
        self.start_button.clicked.connect(lambda: self.start_button_animation(parent))
        
        # Thêm hiệu ứng hover cho nút start
        self.start_button.enterEvent = lambda e: self.button_hover_effect(parent, True)
        self.start_button.leaveEvent = lambda e: self.button_hover_effect(parent, False)
        
        # Đảm bảo hình ảnh vẫn hiển thị
        self.button_start.raise_()
        
        return self.start_button
        
    def button_hover_effect(self, parent, hover):
        # Hiệu ứng khi di chuột qua nút start
        if hover:
            # Tăng kích thước nút khi di chuột qua
            parent.start_button_animation = QPropertyAnimation(self.button_start, b"geometry")
            parent.start_button_animation.setDuration(200)
            rect = self.button_start.geometry()
            parent.start_button_animation.setStartValue(rect)
            
            # Tăng kích thước 10% và giữ vị trí trung tâm
            width_increase = int(rect.width() * 0.1)
            height_increase = int(rect.height() * 0.1)
            new_rect = QRect(
                rect.x() - width_increase//2, 
                rect.y() - height_increase//2,
                rect.width() + width_increase,
                rect.height() + height_increase
            )
            parent.start_button_animation.setEndValue(new_rect)
            parent.start_button_animation.setEasingCurve(QEasingCurve.InOutQuad)
            parent.start_button_animation.start()
            self.start_button.setGeometry(new_rect)
        else:
            # Trở về kích thước ban đầu
            parent.start_button_animation = QPropertyAnimation(self.button_start, b"geometry")
            parent.start_button_animation.setDuration(200)
            rect = self.button_start.geometry()
            parent.start_button_animation.setStartValue(rect)
            
            original_rect = QRect(1000, 0, 111, 121)  # Kích thước ban đầu
            parent.start_button_animation.setEndValue(original_rect)
            parent.start_button_animation.setEasingCurve(QEasingCurve.InOutQuad)
            parent.start_button_animation.start()
            self.start_button.setGeometry(original_rect)
            
    def start_button_animation(self, parent):
        # Hiệu ứng nút khi được nhấn - đa hiệu ứng
        # 1. Hiệu ứng sóng nước
        self.ripple_effect(parent)
        
        # 2. Hiệu ứng phóng to thu nhỏ
        parent.pulse_animation = QPropertyAnimation(self.button_start, b"geometry")
        parent.pulse_animation.setDuration(200)
        rect = self.button_start.geometry()
        parent.pulse_animation.setStartValue(rect)
        
        # Phóng to 20%
        width_increase = int(rect.width() * 0.2)
        height_increase = int(rect.height() * 0.2)
        expanded_rect = QRect(
            rect.x() - width_increase//2, 
            rect.y() - height_increase//2,
            rect.width() + width_increase,
            rect.height() + height_increase
        )
        parent.pulse_animation.setEndValue(expanded_rect)
        parent.pulse_animation.setEasingCurve(QEasingCurve.OutQuad)
        parent.pulse_animation.finished.connect(lambda: self.start_shrink_animation(parent))
        parent.pulse_animation.start()
        
    def start_shrink_animation(self, parent):
        # Thu nhỏ trở lại
        parent.shrink_animation = QPropertyAnimation(self.button_start, b"geometry")
        parent.shrink_animation.setDuration(300)
        rect = self.button_start.geometry()
        parent.shrink_animation.setStartValue(rect)
        
        # Quay về kích thước gốc
        original_rect = QRect(1000, 0, 111, 121)
        parent.shrink_animation.setEndValue(original_rect)
        parent.shrink_animation.setEasingCurve(QEasingCurve.OutBounce)
        parent.shrink_animation.finished.connect(lambda: self.start_blink_animation(parent))
        parent.shrink_animation.start()
    
    def start_blink_animation(self, parent):
        # 3. Hiệu ứng nhấp nháy sau khi phóng to thu nhỏ
        parent.blink_animation = QTimer(parent)
        parent.blink_animation.timeout.connect(lambda: self.toggle_button_visibility(parent))
        parent.blink_count = 0
        parent.blink_animation.start(100)  # Nhấp nháy cách mỗi 100ms
    
    def ripple_effect(self, parent):
        # Hiệu ứng sóng nước tỏa ra từ nút Start
        center = self.button_start.geometry().center()
        
        # Tạo 3 vòng sóng
        for i in range(3):
            ripple = QLabel(parent)
            ripple.setStyleSheet("background-color: rgba(0, 150, 255, 150); border-radius: 50%;")
            
            # Kích thước ban đầu
            size = 20
            ripple.setGeometry(center.x() - size/2, center.y() - size/2, size, size)
            ripple.show()
            # Animation cho vòng sóng
            anim_group = QParallelAnimationGroup(parent)
            
            # Animation phóng to
            anim_size = QPropertyAnimation(ripple, b"geometry")
            anim_size.setDuration(1500 + i*200)  # Thời gian khác nhau cho mỗi vòng
            anim_size.setStartValue(QRect(center.x() - size/2, center.y() - size/2, size, size))
            anim_size.setEndValue(QRect(center.x() - 200/2, center.y() - 200/2, 200, 200))
            anim_size.setEasingCurve(QEasingCurve.OutQuad)
            
            # Animation làm mờ dần
            anim_opacity = QPropertyAnimation(ripple, b"windowOpacity")
            anim_opacity.setDuration(1500 + i*200)
            anim_opacity.setStartValue(0.8)
            anim_opacity.setEndValue(0.0)
            anim_opacity.setEasingCurve(QEasingCurve.OutQuad)
            
            anim_group.addAnimation(anim_size)
            anim_group.addAnimation(anim_opacity)
            
            # Delay giữa các vòng sóng
            QTimer.singleShot(i * 300, lambda a=anim_group: a.start())
            
            # Xóa label khi animation kết thúc
            anim_opacity.finished.connect(lambda ripple=ripple: ripple.deleteLater())
        
    def toggle_button_visibility(self, parent):
        if self.button_start.isVisible():
            self.button_start.hide()
        else:
            self.button_start.show()
            
        parent.blink_count += 1
        if parent.blink_count >= 6:  # Nhấp nháy 3 lần (6 trạng thái)
            parent.blink_animation.stop()
            self.button_start.show()
            # Thêm hiệu ứng xoay trước khi bắt đầu
            self.start_spin_animation(parent)
            
    def start_spin_animation(self, parent):
        # Hiệu ứng xoay 360 độ bằng cách sử dụng transformation
        self.button_start.rotation = 0  # Thuộc tính tùy biến
        
        # Tạo hiệu ứng
        parent.spin_animation = QPropertyAnimation(parent, b"button_rotation")        
        parent.spin_animation.setDuration(800)
        parent.spin_animation.setStartValue(0)
        parent.spin_animation.setEndValue(360)
        parent.spin_animation.setEasingCurve(QEasingCurve.OutBack)
        parent.spin_animation.valueChanged.connect(lambda value: self.update_button_rotation(parent, value))
        parent.spin_animation.finished.connect(lambda: parent.turn_on_camera())
        parent.spin_animation.start()
    
    def update_button_rotation(self, parent, value):
        # Cập nhật rotation và repaint button
        self.button_start.rotation = value
        self.button_start.setStyleSheet(f"""
            QPushButton {{
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                transform: rotate({value}deg);
            }}
            QPushButton:hover {{
                background-color: #45a049;
            }}
        """)
            
    def animate_group_visibility(self, parent, show=True):
        # Hiệu ứng slide khi hiện/ẩn các nhóm
        
        # Chuẩn bị các nhóm để hiển thị nhưng đặt ở vị trí ngoài màn hình (nếu đang hiển thị)
        if show:
            self.group_main.setVisible(True)
            
            # Thay đổi kích thước cửa sổ
            parent.resize(1208, 600)  # Adjusted height due to removal of group_output
            
            # Animation cho group_main
            parent.anim1 = QPropertyAnimation(self.group_main, b"geometry")
            parent.anim1.setDuration(800)
            start_rect = QRect(30, -300, 1151, 371)  # Bắt đầu từ trên màn hình
            end_rect = QRect(30, 200, 1151, 371)     # Kết thúc ở vị trí cuối
            parent.anim1.setStartValue(start_rect)
            parent.anim1.setEndValue(end_rect)
            parent.anim1.setEasingCurve(QEasingCurve.OutBounce)  # Hiệu ứng nảy
            
            # Bắt đầu animation
            parent.anim1.start()
        else:
            # Animation để ẩn (có thể làm ngược lại động tác hiển thị)
            # Animation cho group_main
            parent.anim1 = QPropertyAnimation(self.group_main, b"geometry")
            parent.anim1.setDuration(500)
            start_rect = self.group_main.geometry()
            end_rect = QRect(30, -300, 1151, 371)
            parent.anim1.setStartValue(start_rect)
            parent.anim1.setEndValue(end_rect)
            parent.anim1.setEasingCurve(QEasingCurve.InBack)
            
            # Sau khi animation kết thúc, ẩn các nhóm
            parent.anim1.finished.connect(lambda: self.group_main.setVisible(False))
            
            # Bắt đầu animation
            parent.anim1.start()
    
    def show_startup_message(self, parent, id, status, drug, runtime):
        # Hiển thị thông báo chuẩn bị thử nghiệm
        msg = QMessageBox(parent)
        msg.setWindowTitle("Passive Avoidance Test")
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"<h3>Thử nghiệm đã bắt đầu</h3>")
        msg.setInformativeText(f"""
        <b>ID chuột:</b> {id}<br>
        <b>Trạng thái:</b> {status}<br>
        <b>Thuốc:</b> {drug}<br>
        <b>Thời gian chạy:</b> {runtime} giây<br><br>
        Hệ thống đang theo dõi và ghi nhận dữ liệu...
        """)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setStyleSheet("""
        QMessageBox {
            background-color: #f0f0f0;
        }
        QLabel {
            color: #003366;
            font-size: 14px;
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 5px 15px;
            font-weight: bold;
            min-width: 80px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        """)
        msg.exec()
        
    def button_glow(self, parent):
        # Hiệu ứng nút start phát sáng
        if parent.glow_increasing:
            parent.glow_value += 10
            if parent.glow_value >= 100:
                parent.glow_increasing = False
        else:
            parent.glow_value -= 10
            if parent.glow_value <= 0:
                parent.glow_increasing = True
                
        # Tính toán màu dựa trên giá trị
        r = 255
        g = 255 - parent.glow_value
        b = 255 - parent.glow_value
        
        # Áp dụng hiệu ứng phát sáng
        shadow = QGraphicsDropShadowEffect(parent)
        shadow.setBlurRadius(20 + parent.glow_value/5)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(r, g, b, 150 + parent.glow_value))
        self.button_start.setGraphicsEffect(shadow)
        
        # Kết thúc hiệu ứng sau 2 giây
        if not hasattr(parent, 'glow_counter'):
            parent.glow_counter = 0
        
        parent.glow_counter += 1
        if parent.glow_counter > 40:  # Khoảng 2 giây (40 * 50ms)
            parent.glow_effect.stop()
            self.start_button.setEnabled(True)
