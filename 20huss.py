# import argparse

# def main(args):
#     print(f"Welcome, {args.name}!")
#     if args.verbose:
#         print("Verbose mode is on!")
#     if args.square:
#         print(f"The square of {args.square} is {args.square ** 2}") 

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Argument Parsing Example")

#     # Thêm các đối số bạn muốn xử lý
#     parser.add_argument('name', type=str, help='Your name')
#     parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose mode')
#     parser.add_argument('--square', type=int, help='Square the number')

#     # Phân tích các đối số từ dòng lệnh
#     args = parser.parse_args()

#     # Gọi hàm main và truyền các đối số đã phân tích
#     main(args)

# from pathlib import Path

# path = r'D:/TAM_SAT_M100_A75/FILE_TRAIN/20240520/train/images'
# parent_dir = Path(path).parent

# print(parent_dir)
from pathlib import Path

image_path = r'D:/TAM_SAT_M100_A75/FILE_TRAIN/20240520/train/images/abc.jpg'
labels_path = Path(image_path).parent

print(labels_path)