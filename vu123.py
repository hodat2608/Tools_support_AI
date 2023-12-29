# path1 = ''
# path2 = ''
# with open(path1, "r") as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break

import os

def find_parent_folder_with_file(file_path):
    parent_folder = os.path.dirname(file_path)
    return os.path.basename(parent_folder)

file_path = '//d9090222/G/New folder (9)/a/b/c/d/g/i.jpg'
parent_folder_name = find_parent_folder_with_file(file_path)
print("Parent folder containing 'i.jpg':", parent_folder_name)
