import cv2

# Đọc ảnh gốc
image = cv2.imread("//d9140522/G/02.RS4F5_X75_NQVNHC/DE_DEN/CAMERA1/FILE_LABEL/20221212/train/images/2022-08-09_20-55-33-095608.jpg")

# Cắt vùng quan tâm
roi = image[0:1200, 180:1380]

# Hiển thị ảnh cắt ra màn hình
cv2.imshow('ROI', roi)

# Lưu ảnh cắt thành một tệp mới (nếu cần)
cv2.imwrite('ten_anh_roi.jpg', roi)

# Chờ người dùng nhấn phím bất kỳ trước khi đóng cửa sổ hiển thị
cv2.waitKey(0)
cv2.destroyAllWindows()
