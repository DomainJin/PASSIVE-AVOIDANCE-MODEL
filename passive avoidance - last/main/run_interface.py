import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QPropertyAnimation, Property
from app.main_interface_fixed import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Setup additional UI effects
        self.ui.setup_ui_effects(self)
        
        # Create the start button
        self.start_button = self.ui.create_button_from_label(self)
        self.start_button.clicked.connect(self.handle_start)
        
        # Setup blink effect timer
        self.blink_timer = QTimer(self)
        self.blink_timer.timeout.connect(lambda: self.ui.blink_effect(self))
        self.blink_timer.start(1000)  # Blink every 1 second
        self.blink_on = False
        
        # Setup glow effect
        self.glow_timer = QTimer(self)
        self.glow_value = 0
        self.glow_increasing = True
        self.glow_timer.timeout.connect(lambda: self.ui.button_glow(self))
        self.glow_timer.start(50)  # Update every 50ms
        
        # For button rotation property
        self._button_rotation = 0
    
    def get_button_rotation(self):
        return self._button_rotation
        
    def set_button_rotation(self, value):
        self._button_rotation = value
        
    # Define property for animation
    button_rotation = Property(int, get_button_rotation, set_button_rotation)
    
    def handle_start(self):
        # Get input values
        id_mouse = self.ui.idmouse.currentText()
        status = self.ui.status.currentText()
        drug = self.ui.drug.currentText()
        runtime = self.ui.runtime.value()
        
        # Show startup message
        self.ui.show_startup_message(self, id_mouse, status, drug, runtime)
        
        # Animate group visibility
        self.ui.animate_group_visibility(self, show=True)
        
    def turn_on_camera(self):
        # This function would be called after the start button animation
        # Here you would initialize your camera or tracking system
        self.ui.tracking.setText("Camera Initialized...\nTracking Started")
        
        # You could add more implementation here for actual camera setup
        
def run_application():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_application()
