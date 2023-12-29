# import PySimpleGUI as sg
# def submit_efect():
#     for i in range(1000):
#         if not sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, message='Wait a sencond', no_titlebar=False, time_between_frames=50, text_color='black', background_color='white'):
#             break
#     sg.PopupAnimated(None)
#     sg.Popup('Bạn đã đăng ký thành công', title='Ping',background_color= 'white',text_color='black',button_color='black')
# submit_efect()

import PySimpleGUI as sg

# Tạo một bảng dữ liệu mẫu
headings = ['Name', 'Age', 'Gender']
data = [['John Smith', 25, 'Male'], ['Jane Doe', 30, 'Female']]
table = sg.Table(values=data, headings=headings, max_col_width=25, auto_size_columns=True, display_row_numbers=True, justification='center', num_rows=30, key='PATIENTTABLE', row_height=20, enable_events=True, expand_x=False, expand_y=True, vertical_scroll_only=False, enable_click_events=True, tooltip='all')

# Tạo cửa sổ và đặt chế độ full screen
layout = [[table]]
window = sg.Window('Table Example', layout)

# Chạy vòng lặp sự kiện
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'PATIENTTABLE':
        # Xóa dữ liệu khi nhấp chuột trái vào một dòng
        if values[event] and values[event][0] == 'TABLE_DELETE_EVENT':
            row_index = values[event][1][0]
            del data[row_index]
            table.Update(values=data)

# Đóng cửa sổ
window.close()

