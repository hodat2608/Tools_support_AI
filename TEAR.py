# import PySimpleGUI as sg
# from glob import glob                                                           
# import os
# import shutil 
# import time

# layout_locnhan = [[sg.Text('')],
#     [sg.Text('Chọn thư mục chứa ảnh')],
#     [sg.Input(size=(55,1), font=('Helvetica',12), key='path_src'),
#         sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'path_src',enable_events=True)],

#     [sg.Text('')],

#     [sg.Text('Chọn đường dẫn thư mục chứa các thư mục lưu ảnh ')],
#     [sg.Input(size=(55,1), font=('Helvetica',12), key='PATH_SAVE'),
#         sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'PATH_SAVE',enable_events=True) ],

#     [sg.Text('')],

#     [sg.Text('Tạo tên folder hạng mục '), sg.Input(size=(15,10), font=('Helvetica',12), key='HANGMUC')],

#     [sg.Text('')],

#     [sg.Button('RUN', size=(7,1), font=('Helvetica',10),key= 'RUN'),sg.Text(size=(40,1), key='-OUTPUT8-')],]

# window = sg.Window('All Tools', layout_locnhan, grab_anywhere=False, size=(640, 530), return_keyboard_events=True, finalize=True)

# def abc(out_dir):
#     for root, dirs, files in os.walk(values['path_src']):
#         for file in files:
#             src_path = os.path.join(root, file)
#             tenf = os.path.basename(src_path)
#             shutil.move(src_path, os.path.join(out_dir, tenf))
#             if len(glob(os.path.join(out_dir, '*.jpg'))) == 5 : 
#                 subfolders = [f for f in os.listdir(out_dir) if os.path.isdir(os.path.join(out_dir, f))]
#                 a = len(subfolders) + 1
#                 stt_pcs = os.path.join(out_dir,str(a))
#                 os.mkdir(stt_pcs)
#                 for file_to_move in glob(os.path.join(out_dir, '*.jpg')):
#                     shutil.move(file_to_move, stt_pcs)
                        

# while True:             
#     event, values = window.read(timeout=20)
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break
    
#     if event == 'RUN' :
#         try:
#             os.mkdir(os.path.join(values['PATH_SAVE'],values['HANGMUC']))
#         except:
#             pass
#         out_dir = os.path.join(values['PATH_SAVE'],values['HANGMUC'])
#         print(out_dir)
    
#         while True: 
#             abc(out_dir)
        
# my_list = [1, 2, 3, 4, 5]

# # Loại bỏ và trả về phần tử ở vị trí index 2
# removed_element = my_list.pop(4)

# print("Danh sách sau khi loại bỏ:", my_list)
# print("Phần tử đã loại bỏ:", removed_element)
my_list = ['apple', 'banana', 'orange', 'grape']
# Thêm một chuỗi mới vào danh sách
# my_list.append('kiwi')

# Loại bỏ phần tử ở vị trí 1
my_list.pop("banana")

# Truy cập phần tử ở vị trí 2
element_at_index_2 = my_list[2]

# In danh sách sau các thay đổi
print(my_list)
