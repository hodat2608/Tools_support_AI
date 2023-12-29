from PIL import Image

# Đường dẫn tới bức ảnh lớn và bức ảnh nhỏ
large_image_path = "C:/Users/CCSX009/Pictures/2023-09-19_15-43-46-956864-C1.jpg"
small_image_path = "C:/Users/CCSX009/Pictures/hothandhat.png"

# Tọa độ x, y của bức ảnh nhỏ trên bức ảnh lớn
x = 898
y = 496

# Đọc bức ảnh lớn
large_image = Image.open(large_image_path)

# Đọc bức ảnh nhỏ
small_image = Image.open(small_image_path)

# Đảm bảo kích thước bức ảnh nhỏ không vượt quá kích thước bức ảnh lớn
small_image = small_image.resize((min(small_image.width, large_image.width - x), min(small_image.height, large_image.height - y)))

# Đè bức ảnh nhỏ lên bức ảnh lớn tại tọa độ x, y
large_image.paste(small_image, (x, y))

# Lưu bức ảnh sau khi đã đè lên
large_image.save('duong_dan_cho_buc_anh_sau_khi_da_de.png')

# Đóng các bức ảnh
large_image.close()
small_image.close()
