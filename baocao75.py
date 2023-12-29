import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 
import time

layout_locnhan = [[sg.Text('')],
    [sg.Text('Chọn thư mục chứa ảnh NG ')],
    [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_locnhan'),
        sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'NG',enable_events=True)],

    [sg.Text('')],

    [sg.Text('Chọn thư mục chứa ảnh OK ')],
    [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_SAVE_locnhan'),
        sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'OK',enable_events=True) ],

    [sg.Text('')],

    [sg.Text('Chọn đường dẫn thư mục chứa các thư mục lưu ảnh ')],
    [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_SAVE_locnhan'),
        sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'PATH_SAVE',enable_events=True) ],

    [sg.Text('')],

    [sg.Text('Tạo tên folder hạng mục '), sg.Input(size=(15,10), font=('Helvetica',12), key='HANGMUC')],

    [sg.Text('')],

    [sg.Button('RUN', size=(7,1), font=('Helvetica',10),key= 'RUN'),sg.Text(size=(40,1), key='-OUTPUT8-')],]

window = sg.Window('All Tools', layout_locnhan, grab_anywhere=False, size=(640, 530), return_keyboard_events=True, finalize=True)

def abc(out_dir):
    folders = ['NG', 'OK']
    opts = ['OPT1', 'OPT2', 'OPT3'] 
    for folder in folders:
        for opt in opts:
            current_path = os.path.join(values[folder], opt)
            images = glob(os.path.join(current_path, '*.jpg'))
            for image in images:
                tenf = os.path.basename(image)
                shutil.move(image, os.path.join(out_dir, tenf))
                if len(glob(os.path.join(out_dir, '*.jpg'))) == 5 : 
                    subfolders = [f for f in os.listdir(out_dir) if os.path.isdir(os.path.join(out_dir, f))]
                    a = len(subfolders) + 1
                    stt_pcs = os.path.join(out_dir,str(a))
                    os.mkdir(stt_pcs)
                    for file_to_move in glob(os.path.join(out_dir, '*.jpg')):
                        shutil.move(file_to_move, stt_pcs)
                        

while True:             
    event, values = window.read(timeout=20)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == 'RUN' :
        try:
            os.mkdir(os.path.join(values['PATH_SAVE'],values['HANGMUC']))
        except:
            pass
        out_dir = os.path.join(values['PATH_SAVE'],values['HANGMUC'])
        print(out_dir)
    
        # while True: 
        abc(out_dir)
        
