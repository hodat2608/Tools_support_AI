# # import PySimpleGUI as sg

# # # Định nghĩa layout cho bảng
# # layout = [
# #     [sg.Table(values=[['Alice', 25, 'New York'], ['Bob', 30, 'Los Angeles']], 
# #               headings=['Name', 'Age', 'City'], 
# #               auto_size_columns=False, 
# #               num_rows=10, 
# #               key='-TABLE-', 
# #               enable_events=True, 
# #               select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
# #     [sg.Button('Exit')]
# # ]

# # # Tạo cửa sổ
# # window = sg.Window('Table', layout)

# # # Vòng lặp chính
# # while True:
# #     event, values = window.read()

# #     if event == sg.WIN_CLOSED or event == 'Exit':
# #         break

# #     # Xử lý sự kiện double click trên bảng
# #     if event == '-TABLE-' and len(values['-TABLE-']) > 0 and values['-TABLE-'][0] != 0:
# #         # Lấy chỉ số của dòng được chọn
# #         row_index = values['-TABLE-'][0]
# #         # Lấy dữ liệu của dòng đó
# #         data = window['-TABLE-'].get()[row_index]
        
# #         # Hiển thị cửa sổ popup để người dùng chỉnh sửa thông tin
# #         edit_layout = [
# #             [sg.Text('Name:'), sg.Input(data[0], key='-NAME-')],
# #             [sg.Text('Age:'), sg.Input(data[1], key='-AGE-')],
# #             [sg.Text('City:'), sg.Input(data[2], key='-CITY-')],
# #             [sg.Button('Save'), sg.Button('Cancel')]
# #         ]
# #         edit_window = sg.Window('Edit', edit_layout)
# #         while True:
# #             edit_event, edit_values = edit_window.read()
# #             if edit_event == sg.WIN_CLOSED or edit_event == 'Cancel':
# #                 break
# #             elif edit_event == 'Save':
# #                 # Cập nhật lại dữ liệu trên bảng
# #                 new_data = [edit_values['-NAME-'], edit_values['-AGE-'], edit_values['-CITY-']]
# #                 window['-TABLE-'].update({row_index: new_data})
# #                 break
# #         edit_window.close()

# # # Đóng cửa sổ
# # window.close()
# import os
# import cv2
# from glob import glob
# folder_path = "C:/Users/CCSX009/Desktop/luuxuatc3"
# folder1 = folder_path + '/'
# fname = glob(folder1 + '*.jpg')
# for filename in fname:
#     tenf = os.path.basename(filename)

# img_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

# img_files = sorted(img_files)
# # cv2.namedWindow('Image Viewer', cv2.WINDOW_NORMAL)

# for img_file in img_files:

#     img = cv2.imread(img_file)

   
#     cv2.imshow('Image Viewer', img)

    
#     key = cv2.waitKey(200)

   
#     while key == ord('p'):
#         cv2.imshow(str(img_file), img)
#         key = cv2.waitKey(0)
#         print(img_file)

    
#     if key == ord('n'):
#         continue

   
#     if key == 27:
#         break

# # Hủy các cửa sổ đang hiển thị
# cv2.destroyAllWindows()
from glob import glob                                                           
import shutil,os
import PySimpleGUI as sg

import PySimpleGUI as sg

from TOAN import Test
class PTC:
    TM = Test.getPath1()
    def ganok(TM):  
        txt = glob(TM + '*.txt')
        cnt = len(txt)
        os.makedirs(TM + 'TEMP', exist_ok=True)
        out_dir = TM + 'TEMP/'
        # 0.501271 0.513333 0.955085 0.926667 rs466
        # 0.495000 0.515000 0.950000 0.948333 m100
        for filename in txt:
            tam = '0.501271 0.513333'
            tenf = os.path.basename(filename)
            if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
                out = open(out_dir + tenf,'w')
                with open(filename, 'r') as f:
                    while True:
                        line = f.readline()
                        out.writelines(line)
                        if not line:
                            break
                        tmp = line.split()
                        if int(tmp[0]) < 5:
                            if int(tmp[0]) == 0:
                                tam = tmp[1] + ' ' + tmp[2]
                    out.writelines('8 ' + tam + ' 0.955085 0.935000') 
            else : 
                shutil.copyfile(filename, out_dir + tenf)
                print(tenf)
            f.close()
            out.close()
            os.replace(out_dir + tenf, filename)
            cnt -= 1
            print(cnt)
        shutil.rmtree(out_dir) 
