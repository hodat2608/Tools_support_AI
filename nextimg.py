import PySimpleGUI as sg
import os
import time

# Đường dẫn đến thư mục chứa các ảnh
image_folder = '//d9140522/E/a88/New folder (2)'

# Lấy danh sách tất cả các tệp ảnh trong thư mục
image_files = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Sắp xếp danh sách tệp ảnh
image_files.sort()

# Thiết lập cấu hình giao diện
layout = [
    [sg.Image(key='-IMAGE-')],
    [sg.Slider(range=(1, 1000), orientation='h', default_value=500, key='-SPEED-')],
    [sg.Button('Next'), sg.Button('Exit')]
]

window = sg.Window('Image Viewer', layout, finalize=True)

image_index = 0
speed = 0.001  # Tốc độ mặc định (0.001 giây)

while True:
    event, values = window.read(timeout=int(speed * 1000))  # Chuyển đổi giây sang mili giây

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Next':
        image_index = (image_index + 1) % len(image_files)

    image_file = image_files[image_index]
    window['-IMAGE-'].update(filename=image_file)

    # Lấy tốc độ mới từ slider và chuyển đổi thành giây
    new_speed = values['-SPEED-'] / 1000
    if new_speed != speed:
        speed = new_speed

window.close()
