<p align="center">
  <b>PASSIVE-AVOIDANCE-MODEL</b><br>
  (Mô hình Tránh né Thụ Động)
</p>

<div align="center" style="padding: 20px;">
  <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/6583335991999.gif" alt="Demo GIF" style="border: 4px solid #3b82f6; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 400px; max-width: 100%;">
</div>

**Mô tả mô hình:** Mô hình tránh né thụ động được biết đến là một mô hình hiệu quả để thử nghiệm khả năng ghi nhớ của chuột. Mô hình này dựa trên sự mâu thuẫn giữa bản năng sợ hãi vùng không gian mở, có ánh sáng và âm thanh lớn của các loài gặm nhấm với phản xạ trốn tránh có điều kiện vùng không gian nguy hiểm đã được nhận diện trước đó. Dựa trên đặc điểm sinh học này, mô hình được thiết kế gồm buồng tối (khu vực ưa thích của chuột) trở thành vị trí nguy hiểm (bị điện giật), trong khi buồng sáng lại là vị trí an toàn (không bị điện giật)

<div align="center" style="padding: 20px;">
  <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/1-s2.0-S0031938421003395-gr4%20(1).jpg" alt="Demo GIF" style="border: 4px solid #3b82f6; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 400px; max-width: 100%;">
</div>

**Mô tả thí nghiệm:** Có rất nhiều đối tượng chuột cần kiểm tra. Ví dụ: chuột bình thường; chuột bị suy giảm trí nhớ; chuột được tiêm thuốc A, B hoặc C. Kỳ vọng của mô hình là xuất ra được những kết qủa trực quan, giúp các nhà nghiên cứu có thể dễ dàng so sánh thói quen, sức ghi nhớ của từng đối tượng, từ đó đưa ra kết luận về độ hiệu quả của thuốc. </br> 

**Thiết kế mô hình:** Mô hình sử dụng Raspberry Pi 5 là CPU chính, ngoài ra còn có Arduino Uno đóng vai trò là Slave giao tiếp qua RS485.</br>

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/z6467928565299_853e6ee72afcc6890cd4149009f50812.jpg" width="300"><br>
<!--       <sub>Label 1</sub> -->
    </td>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/z6465882181084_780e7d805036a116f6c0ec2465a7737a.jpg" width="300"><br>
<!--       <sub>Label 2</sub> -->
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/z6466307538672_22e379f1685e11b8497f6b66c36e3158.jpg" width="300"><br>
<!--       <sub>Label 3</sub> -->
    </td>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/z6465820293366_4b3cad2a51519628072dd59174eb67f8.jpg" width="300"><br>
<!--       <sub>Label 4</sub> -->
    </td>
  </tr>
</table>

**Các chức năng của mô hình** </br>
  • Nhận diện và giám sát chuột, từ đó vẽ bảng đồ mật độ di chuyển chủa chuột theo thời gian (heatmap). </br>
  <div align="center" style="padding: 20px;">
  <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/IMG_0579.JPG" alt="Demo GIF" style="border: 4px solid #3b82f6; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 600px; max-width: 100%;"> </br>
  <sub>Xử lý ảnh bằng bằng model được train bởi thuật toán Ultralytics YOLO</sub>
</div>

Kết quả heatmap từ một số thuật toán
<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/detailed_mouse_classification.png" width="300"><br>
<!--       <sub>Label 1</sub> -->
    </td>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/mouse_detailed_heatmap.png" width="300"><br>
<!--       <sub>Label 2</sub> -->
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/2.jpg" width="300"><br>
<!--       <sub>Label 3</sub> -->
    </td>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/Untitled.png" width="300"><br>
<!--       <sub>Label 4</sub> -->
    </td>
  </tr>
</table>
  • Gây kích thích tiêu cực khi chuột đi vào buồng tối: giật điện với điện áp từ 12 đến 24VAC, cường độ dòng điện 0.8 đến 1.5mA mà người dùng muốn hiệu chỉnh. </br>
  <table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/333.png" width="300"><br>
<!--       <sub>Label 1</sub> -->
    </td>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/4.jpg" width="300"><br>
<!--       <sub>Label 2</sub> -->
    </td>
  </tr>
</table>
  • Có giao diện cho người dùng dễ dàng vận hành và xuất ra kết quả trực quan sau mỗi lần khởi chạy thí nghiệm. </br>
  <table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/222.png" width="600"><br>
      <sub>Giao diện người dùng được thiết kế bằng Qt Designer</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/111.png" width="600"><br>
      <sub>Các thư mục kết quả sau mỗi lần chạy, tên thư mục được định dạng bởi: "thời điểm chạy thí nghiệm (yyyy-mm-dd hh:mm:ss)"-"Id Mouse"-"Status Mouse"-"Drug" khi người dùng khai báo thông tin trước khi chạy</sub>
    </td>
  </tr>
</table>

<p align="center">
  
</p>
<div align="center" style="padding: 20px;">
  <img src="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/blob/main/passive%20avoidance%20-%20last/access/6154869952638.gif" alt="Demo GIF" style="border: 4px solid #3b82f6; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 800px; max-width: 100%;"> </br>
  <sub>Màn hình cảm ứng giúp người dùng dễ dàng thao tác</sub>
</div>


<p align="center">
  ------------------------------------------------------------------ </br>
  <b>Tất cả thông tin trên chỉ là tóm tắt sơ lược</b><br>
</p>

<p align="center">
  <a href="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/tree/main/passive%20avoidance%20-%20last/docs">_Xem tài liệu mô tả chi tiết_</a><br>
  <a href="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/tree/main/passive%20avoidance%20-%20last/main">_Xem source code Raspberry_</a><br>
  <a href="https://github.com/DomainJin/PASSIVE-AVOIDANCE-MODEL/tree/main/passive%20avoidance%20-%20last/Slave">_Xem source code Arduino_</a>
</p>




