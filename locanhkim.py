import cv2
import numpy as np

def find_difference(image_path1, image_path2):
    # Đọc ảnh từ đường dẫn
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # Tính toán sự khác biệt giữa hai ảnh
    difference = cv2.absdiff(image1, image2)

    # Chuyển ảnh sự khác biệt sang ảnh đen trắng
    gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

    # Áp dụng ngưỡng để tách lấy vùng khác biệt
    _, thresholded = cv2.threshold(gray_difference, 30, 255, cv2.THRESH_BINARY)

    # Tìm các contour trong vùng khác biệt
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Vẽ contour lên ảnh gốc (ảnh 1)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Hiển thị ảnh 1 và ảnh khác biệt
    cv2.imshow('Image 1', image1)
    cv2.imshow('Difference', difference)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Đường dẫn đến hai bức ảnh
image_path1 ="C:/Users/CCSX009/Desktop/VO_LN/20230713/CAM2/2023-07-19_09-57-58-049067.jpg"
image_path2 = "C:/Users/CCSX009/Desktop/VO_LN/20230713/CAM2/2023-07-19_09-57-58-013779.jpg"
# Tìm và hiển thị điểm khác biệt giữa hai bức ảnh
find_difference(image_path1, image_path2)