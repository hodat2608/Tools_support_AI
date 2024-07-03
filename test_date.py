import datetime
import re,os

# def extract_date_from_filename(filename):
#     match = re.search(r'(/d{4})_(/d{2})_(/d{2})', filename)
#     if match:
#         year = int(match.group(1))
#         month = int(match.group(2))
#         day = int(match.group(3))
#         return year, month, day
#     return None

# def is_valid_date(year, month, day):
#     try:
#         datetime.datetime(year, month, day)
#         return True
#     except ValueError:
#         return False

# def main():
#     current_date = datetime.datetime.now()
#     filename = "2024_06_22_Dem_ray.xlsx"  # Đây là tên file của bạn
#     date_components = extract_date_from_filename(filename)
#     if date_components:
#         year, month, day = date_components
#         # Kiểm tra xem ngày tháng năm có hợp lệ không
#         if is_valid_date(year, month, day):
#             file_date = datetime.datetime(year, month, day)
#             # So sánh ngày trong tên file với ngày hiện tại
#             if file_date.date() == current_date.date():
#                 print("Tên file hợp lệ và trùng với ngày hiện tại.")
#             else:
#                 print("Tên file hợp lệ nhưng không trùng với ngày hiện tại.")
#         else:
#             print("Tên file không hợp lệ.")
#     else:
#         print("Không tìm thấy ngày tháng năm trong tên file.")

# if __name__ == "__main__":
#     main()


def extract_date_from_filename(filename):
        match = re.search(r'(/d{4})_(/d{2})_(/d{2})', filename)
        if match:
            year = int(match.group(1))
            month = int(match.group(2))
            day = int(match.group(3))
            return year, month, day
        return None

def is_valid_date(year, month, day):
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False
            
def filter_day_new(filename):
    # processed_files = read_processed_files()
    # filenames = glob.glob(dir_path)
    # for filename in filenames:
    base_name = os.path.basename(filename)
    date_components = extract_date_from_filename(filename)
    if date_components:
        year, month, day = date_components
        if is_valid_date(year, month, day):
            date_str = base_name.split('_')[0:3]
            date_str = '_'.join(date_str)
            file_date = datetime.datetime.strptime(date_str, '%Y_%m_%d').date()
            current_date = datetime.date.today()       
            if file_date >= current_date :
                # processed_files.add(filename)
                # write_processed_file(filename)
                return filename
            else:
                return None
        else:
            print("Tên file không hợp lệ.")
            return None
    else:
        print("Không tìm thấy ngày tháng năm trong tên file.")
        return None
filename = "2024_06_22_Dem_ray.xlsx" 
print(filter_day_new(filename))