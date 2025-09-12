import cv2
from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Mở video
cap = cv2.VideoCapture("video.mp4")

# Lấy thông tin video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
duration_seconds = total_frames / fps if fps > 0 else 0
minutes = int(duration_seconds // 60)
seconds = int(duration_seconds % 60)

# In thông tin video
print(f"Thông tin video:")
print(f"- Tổng số frame: {total_frames}")
print(f"- FPS: {fps:.2f}")
print(f"- Thời lượng: {minutes} phút {seconds} giây ({duration_seconds:.2f} giây)")

# Lấy kích thước frame đầu tiên để tạo heatmap
ret, first_frame = cap.read()
if not ret:
    print("Không thể đọc video")
    exit()
frame_height, frame_width = first_frame.shape[:2]
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset về frame đầu tiên

# Tạo một ma trận để lưu heatmap
heatmap = np.zeros((frame_height, frame_width), dtype=np.uint32)

model = YOLO("best.pt")

frame_count = 0  # Đếm số frame đã xử lý
mouse_tracked_frames = 0  # Đếm số frame đã track được chuột

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    frame_count += 1  # Tăng biến đếm frame
    current_time = frame_count / fps  # Tính thời gian hiện tại
    
    # Xử lý frame hiện tại bằng model
    results = model.track(frame, persist=True)
    
    # Tạo bản sao của frame để vẽ lên đó
    annotated_frame = frame.copy()
    
    mouse_detected = False  # Flag để đánh dấu frame có phát hiện chuột
    
    if results and len(results) > 0:
        border = None
        lab_mouse = None
        
        boxes = results[0].boxes
        if boxes is not None and len(boxes) > 0:
            class_ids = boxes.cls
            
            for i, box in enumerate(boxes):
                class_id = int(class_ids[i].item())  # Chuyển tensor thành integer
                
                if class_id == 0:  # 'border' là class 0
                    border = box.xyxy[0].cpu().numpy()  # Chuyển tensor thành numpy array
                    # Vẽ border với màu xanh lá (BGR: 0, 255, 0)
                    x1, y1, x2, y2 = map(int, border)
                    cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, "Border", (x1, y1 - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    
                elif class_id == 1:  # 'lab-mouse' là class 1
                    lab_mouse = box.xyxy[0].cpu().numpy()
                    mouse_detected = True  # Đánh dấu đã phát hiện chuột
                    
                    # Vẽ lab-mouse với màu đỏ (BGR: 0, 0, 255)
                    x1, y1, x2, y2 = map(int, lab_mouse)
                    cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.putText(annotated_frame, "Mouse", (x1, y1 - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    
                    # Tô màu khu vực bounding box của chuột (điều chỉnh độ mờ với alpha)
                    overlay = annotated_frame.copy()
                    cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 0, 255), -1)  # -1 để tô đầy
                    alpha = 0.3  # Độ mờ (0: trong suốt hoàn toàn, 1: đục hoàn toàn)
                    annotated_frame = cv2.addWeighted(overlay, alpha, annotated_frame, 1 - alpha, 0)
                    
                    # Cập nhật heatmap - tăng giá trị ở vị trí chuột
                    heatmap[y1:y2, x1:x2] += 1
            
            # Nếu phát hiện chuột, tăng biến đếm
            if mouse_detected:
                mouse_tracked_frames += 1
                
            print(f"Frame {frame_count}/{total_frames} | Thời gian: {current_time:.2f}s | Border: {border}, Lab Mouse: {lab_mouse}")
    
    # Thêm thông tin frame và thời gian vào frame
    cv2.putText(annotated_frame, f"Frame: {frame_count}/{total_frames} | Time: {current_time:.2f}s", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    # Thêm thông tin về số frame đã track được chuột
    cv2.putText(annotated_frame, f"Mouse tracked: {mouse_tracked_frames} frames", 
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow("Tracking", annotated_frame)
    
    # Thoát khi nhấn 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(f"\nĐã xử lý {frame_count}/{total_frames} frames ({(frame_count/total_frames)*100:.1f}%)")
print(f"Đã track được chuột trong {mouse_tracked_frames}/{total_frames} frames ({(mouse_tracked_frames/total_frames)*100:.1f}%)")

# Xác định diện tích xuất hiện trên 50 lần và dưới 50 lần
under_50_mask = (heatmap > 0) & (heatmap < 50)
over_50_mask = heatmap >= 50

# Tính diện tích pixel
under_50_area = np.sum(under_50_mask)
over_50_area = np.sum(over_50_mask)

print(f"Diện tích xuất hiện dưới 50 lần: {under_50_area} pixels")
print(f"Diện tích xuất hiện từ 50 lần trở lên: {over_50_area} pixels")

# Hiển thị chi tiết heatmap
plt.figure(figsize=(12, 10))

# Áp dụng colormap để hiển thị chi tiết số lần xuất hiện
plt.imshow(heatmap, cmap='hot')
plt.colorbar(label="Số lần xuất hiện")
plt.title("Chi tiết heatmap xuất hiện của chuột")

# Lưu hình ảnh chi tiết
plt.savefig("mouse_detailed_heatmap.png")
print("Đã lưu hình ảnh chi tiết heatmap vào mouse_detailed_heatmap.png")

# Tạo phân loại màu sắc chi tiết với 8 mức
plt.figure(figsize=(12, 10))

# Tạo mask cho từng mức
mask_below_3 = (heatmap > 0) & (heatmap < 3)          # Tím
mask_below_30 = (heatmap >= 3) & (heatmap < 30)       # Chàm
mask_below_90 = (heatmap >= 30) & (heatmap < 90)      # Lam
mask_below_150 = (heatmap >= 90) & (heatmap < 150)    # Lục
mask_below_210 = (heatmap >= 150) & (heatmap < 210)   # Vàng
mask_below_270 = (heatmap >= 210) & (heatmap < 270)   # Cam
mask_below_300 = (heatmap >= 270) & (heatmap < 300)   # Đỏ nhạt
mask_above_300 = (heatmap >= 300)                     # Đỏ đậm

# Tạo colormap tùy chỉnh với 9 màu (bao gồm cả màu đen cho giá trị 0)
custom_colors = [(0, 0, 0),          # Đen (không xuất hiện)
                 (0.5, 0, 0.5),      # Tím (<3)
                 (0.29, 0, 0.51),    # Chàm (3-30)
                 (0, 0, 1),          # Lam (30-90)
                 (0, 1, 0),          # Lục (90-150)
                 (1, 1, 0),          # Vàng (150-210)
                 (1, 0.65, 0),       # Cam (210-270)
                 (0.8, 0, 0),        # Đỏ nhạt (270-300)
                 (0.5, 0, 0)]        # Đỏ đậm (>300)

custom_cmap = mcolors.ListedColormap(custom_colors)

# Tạo mảng để áp dụng colormap
classified_heatmap = np.zeros_like(heatmap)
classified_heatmap[mask_below_3] = 1      # Tím
classified_heatmap[mask_below_30] = 2     # Chàm
classified_heatmap[mask_below_90] = 3     # Lam
classified_heatmap[mask_below_150] = 4    # Lục
classified_heatmap[mask_below_210] = 5    # Vàng
classified_heatmap[mask_below_270] = 6    # Cam
classified_heatmap[mask_below_300] = 7    # Đỏ nhạt
classified_heatmap[mask_above_300] = 8    # Đỏ đậm

# Thiết lập bounds và norm để áp dụng colormap chính xác
bounds = [0, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]
norm = mcolors.BoundaryNorm(bounds, custom_cmap.N)

plt.imshow(classified_heatmap, cmap=custom_cmap, norm=norm)

# Thêm colorbar
cbar = plt.colorbar(ticks=[0.25, 1, 2, 3, 4, 5, 6, 7, 8])
cbar.set_ticklabels(['Không xuất hiện', 
                     '<3 (0.1s)', 
                     '<30 (1s)', 
                     '<90 (3s)', 
                     '<150 (5s)', 
                     '<210 (7s)', 
                     '<270 (9s)', 
                     '<300 (10s)', 
                     '>300 (>10s)'])

plt.title("Phân loại chi tiết khu vực theo tần suất xuất hiện của chuột")

# Nếu có border frame cuối cùng, vẽ nó lên heatmap để tham khảo
if 'border' in locals() and border is not None:
    x1, y1, x2, y2 = map(int, border)
    plt.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], 'w-', linewidth=2)

# Hiển thị số lượng pixel trong mỗi vùng
counts = [
    np.sum(classified_heatmap == 0),
    np.sum(classified_heatmap == 1),
    np.sum(classified_heatmap == 2),
    np.sum(classified_heatmap == 3),
    np.sum(classified_heatmap == 4),
    np.sum(classified_heatmap == 5),
    np.sum(classified_heatmap == 6),
    np.sum(classified_heatmap == 7),
    np.sum(classified_heatmap == 8)
]

# In ra thống kê
total_pixels = sum(counts[1:])  # Không tính vùng không xuất hiện
print("\nThống kê phân loại khu vực:")
print(f"- Không xuất hiện: {counts[0]} pixels")
print(f"- <3 (0.1s): {counts[1]} pixels ({counts[1]/total_pixels*100:.1f}% khu vực active)")
print(f"- <30 (1s): {counts[2]} pixels ({counts[2]/total_pixels*100:.1f}% khu vực active)")
print(f"- <90 (3s): {counts[3]} pixels ({counts[3]/total_pixels*100:.1f}% khu vực active)")
print(f"- <150 (5s): {counts[4]} pixels ({counts[4]/total_pixels*100:.1f}% khu vực active)")
print(f"- <210 (7s): {counts[5]} pixels ({counts[5]/total_pixels*100:.1f}% khu vực active)")
print(f"- <270 (9s): {counts[6]} pixels ({counts[6]/total_pixels*100:.1f}% khu vực active)")
print(f"- <300 (10s): {counts[7]} pixels ({counts[7]/total_pixels*100:.1f}% khu vực active)")
print(f"- >300 (>10s): {counts[8]} pixels ({counts[8]/total_pixels*100:.1f}% khu vực active)")
print(f"- Tổng khu vực active: {total_pixels} pixels")

# Lưu hình ảnh phân loại chi tiết
plt.savefig("detailed_classification.png", dpi=300, bbox_inches='tight')
print("Đã lưu phân loại chi tiết vào detailed_classification.png")

plt.show()

cap.release()
cv2.destroyAllWindows()