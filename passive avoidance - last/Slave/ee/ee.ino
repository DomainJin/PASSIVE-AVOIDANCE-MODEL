// #include <Wire.h>
#include <ZMPT101B.h>
#include <ModbusRtu.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h> 

LiquidCrystal_I2C lcd(0x27, 16, 2);

#define TXEN  3

#define SENSITIVITY 500.0f
ZMPT101B voltageSensor(A0, 50.0);
ZMPT101B voltageSensor2(A1, 50.0);

uint16_t au8data[16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0 }; // Dữ liệu Modbus
int ledstatus = 0; // Trạng thái LED
int ledpin = 4; // Chân điều khiển LED
int door = 0;
int servo = 9;
int goc;
Servo myServo;

Modbus slave(10, Serial, TXEN); // Khởi tạo Modbus slave

void setup() {
  Serial.begin(19200);  // Thiết lập baudrate cho giao tiếp serial
  pinMode(ledpin, OUTPUT);
  pinMode(6, OUTPUT);
  myServo.attach(servo); 
  slave.start(); // Khởi tạo slave Modbus
  
  voltageSensor.setSensitivity(SENSITIVITY);
  voltageSensor2.setSensitivity(SENSITIVITY);
  delay(2000);

  // Màn hình LCD
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("PASSIVE AVOIDANCE");
  lcd.setCursor(0, 1);
  lcd.print("Voltage Current");
  delay(2000);
}

void loop() {
  
  float voltage = voltageSensor.getRmsVoltage();  // Đọc điện áp
  float voltage2 = voltageSensor2.getRmsVoltage();  // Đọc điện áp
  float current;
  current = (voltage - voltage2)/19.5;
  // Cập nhật dữ liệu vào các register Modbus
  uint16_t volt = (int)(voltage * 100);
  uint16_t amp = (int)(current * 10);
  au8data[0] = volt;  // Lưu điện áp (nhân với 100 để tránh sử dụng số thập phân)
  au8data[1] = amp;  // Lưu dòng điện (nhân với 1000 để gửi mA)
  au8data[2] = ledstatus;  // Lưu trạng thái của đèn LED vào register 2
  au8data[3] = door;
  // Gửi dữ liệu qua Modbus RTU
  slave.poll(au8data, 16);  // Gửi các giá trị qua RS485

  // Hiển thị lên màn hình LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Voltage: ");
  lcd.setCursor(9, 0);
  lcd.print(voltage);
  
  lcd.setCursor(0, 1);
  lcd.print("Current: ");
  lcd.setCursor(9, 1);
  lcd.print(current);
  if (ledstatus != au8data[2]) {
    ledstatus = au8data[2];  // Lấy giá trị từ register để điều khiển LED
    digitalWrite(ledpin, ledstatus);  // Bật/tắt LED
    digitalWrite(6, ledstatus);
    // myServo.write(20);
  }

    // Điều khiển cửa (door control)
  int currentPosition = myServo.read();
  if (au8data[3] == 0) { // Yêu cầu đóng cửa
    if (currentPosition != 150) {
      myServo.write(150); // Góc đóng cửa
      door = 0; // Cập nhật trạng thái cửa
    }
  } else if (au8data[3] == 1) { // Yêu cầu mở cửa
    if (currentPosition != 20) {
      myServo.write(20); // Góc mở cửa
      door = 1; // Cập nhật trạng thái cửa
    }
  }


  

}
