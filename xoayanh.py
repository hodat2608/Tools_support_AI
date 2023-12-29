from PIL import Image
import os

def rotate_images_in_folder(folder_path):
    # Kiểm tra xem thư mục tồn tại hay không
    if not os.path.exists(folder_path):
        print("Thư mục không tồn tại.")
        return
    
    # Lấy danh sách tên tập tin trong thư mục
    file_list = os.listdir(folder_path)
    
    for file_name in file_list:
        # Lấy đường dẫn đầy đủ của tập tin
        file_path = os.path.join(folder_path, file_name)
        
        try:
            # Mở ảnh
            image = Image.open(file_path)
            
            # Xoay ảnh 90 độ theo chiều kim đồng hồ
            rotated_image = image.transpose(Image.ROTATE_270)
            
            # Lưu ảnh xoay vào thư mục gốc với tên tương tự và đuôi .rotated.jpg
            rotated_file_path = os.path.join(folder_path, file_name.split('.')[0] + ".jpg")
            rotated_image.save(rotated_file_path)
            
            print(f"Đã xoay và lưu {file_name} thành công.")
        
        except Exception as e:
            print(f"Lỗi khi xử lý {file_name}: {e}")

if __name__ == "__main__":
    folder_path = "Y:/X75/kt75cu/excel/trang/c2/2023-08-15N"
    rotate_images_in_folder(folder_path)
