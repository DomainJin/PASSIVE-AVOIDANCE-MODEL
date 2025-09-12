import cv2
import os
import time
from datetime import datetime
import subprocess

def record_video(duration=10, output_folder=None, filename="recording.mp4"):
    """
    Quay video từ camera trong thời gian xác định và lưu vào file
    
    Args:
        duration (int): Thời gian quay video (giây)
        output_folder (str): Thư mục lưu video (None để tự động tạo)
        filename (str): Tên file video
    
    Returns:
        str: Đường dẫn đến file video đã lưu hoặc None nếu có lỗi
    """
    # Tạo thư mục đầu ra nếu chưa được chỉ định
    if output_folder is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_folder = f"test_video_{timestamp}"
    
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, filename)
    
    print(f"Khởi tạo camera...")
    cap = cv2.VideoCapture(0)
    
    # Kiểm tra camera đã mở thành công chưa
    if not cap.isOpened():
        print("Lỗi: Không thể mở camera!")
        return None
    
    # Đợi camera khởi động và ổn định
    print("Đợi camera ổn định...")
    for i in range(10):
        ret, _ = cap.read()
        time.sleep(0.1)
    
    # Đọc một frame để lấy kích thước
    ret, test_frame = cap.read()
    if not ret:
        print("Lỗi: Không thể đọc frame từ camera!")
        cap.release()
        return None
    
    # Lấy kích thước frame và thiết lập VideoWriter
    height, width, _ = test_frame.shape
    fps = 60  # Thay đổi từ 30 lên 60 fps
    
    print(f"Kích thước video: {width}x{height}, FPS: {fps}")
    print(f"Định dạng đầu ra: {output_path}")
    
    # Tạo VideoWriter với codec MP4V
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    if not out.isOpened():
        print("Lỗi: Không thể tạo file video đầu ra!")
        cap.release()
        return None
    
    # Ghi video
    start_time = time.time()
    frame_count = 0
    
    print(f"Bắt đầu quay video ({duration} giây)...")
    print("Nhấn 'q' để dừng quay sớm.")
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Lỗi: Mất kết nối với camera!")
                break

            # Tính toán tọa độ trung điểm khung hình
            center_x = width // 2
            center_y = height // 2
            center_text = f"Center: ({center_x}, {center_y})"
            cv2.putText(frame, center_text, (center_x - 100, center_y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Thêm timestamp vào video
            current_time = time.time() - start_time
            elapsed = f"{int(current_time)}s / {duration}s"
            cv2.putText(frame, elapsed, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (0, 255, 0), 2)
            
            # Ghi frame vào video
            out.write(frame)
            frame_count += 1

            # Hiển thị frame
            cv2.imshow('Recording...', frame)
            
            # Kiểm tra nếu đã đủ thời gian hoặc người dùng nhấn 'q'
            if cv2.waitKey(1) & 0xFF == ord('q') or current_time >= duration:
                break
                
            # In tiến độ mỗi giây
            if frame_count % fps == 0:
                print(f"Đã quay {int(current_time)}/{duration} giây | {frame_count} frames")
    
    except Exception as e:
        print(f"Lỗi trong quá trình quay: {e}")
    
    finally:
        # Đảm bảo giải phóng tài nguyên
        end_time = time.time()
        actual_duration = end_time - start_time
        
        # Thêm vài frame cuối trước khi đóng
        for _ in range(5):
            ret, frame = cap.read()
            if ret:
                out.write(frame)
        
        # Giải phóng tất cả tài nguyên
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
        # Kiểm tra file đầu ra
        if os.path.exists(output_path):
            file_size_mb = os.path.getsize(output_path) / (1024*1024)
            print(f"Hoàn thành! Đã quay {frame_count} frames trong {actual_duration:.1f} giây")
            print(f"Video đã được lưu tại: {output_path}")
            print(f"Kích thước file: {file_size_mb:.2f} MB")
            
            return output_path
        else:
            print("Lỗi: File đầu ra không tồn tại!")
            return None

def open_folder(path):
    """Mở thư mục trong Explorer"""
    if os.path.exists(path):
        if os.name == 'nt':  # Windows
            subprocess.run(['explorer', os.path.abspath(path)])
        elif os.name == 'posix':  # macOS, Linux
            subprocess.run(['xdg-open', path])
        print(f"Đã mở thư mục: {path}")
    else:
        print(f"Thư mục không tồn tại: {path}")

if __name__ == "__main__":
    # Cấu hình thời gian quay video (giây)
    recording_duration = 10  # 10 giây
    
    print("=== CHƯƠNG TRÌNH QUAY VIDEO ===")
    print(f"Thời gian quay: {recording_duration} giây")
    input("Nhấn Enter để bắt đầu quay...")
    
    # Tạo thư mục với timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"test_video_{timestamp}"
    
    # Quay video
    video_path = record_video(
        duration=recording_duration, 
        output_folder=folder_name, 
        filename="recording.mp4"
    )
    
    if video_path:
        # Mở thư mục chứa video sau khi quay xong
        open_folder(os.path.dirname(video_path))