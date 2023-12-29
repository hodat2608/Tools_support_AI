import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 
import time


layout_locnhan_list = [[sg.Text('')],
            [sg.Text('Chọn thư mục gốc ')],
            [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_locnhan'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True) ],

            [sg.Text('')],

            [sg.Text('Chọn thư mục lưu ')],
            [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_SAVE_locnhan'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True) ],

            [sg.Text('')],

            [sg.Text('Chọn Stt nhãn '), sg.Input(size=(30,10), font=('Helvetica',12), key='TMP1'),sg.Text('Copy or Move files chứa nhãn này!')],
            [sg.Text('')],

            [sg.Button('MOVE', size=(7,1), font=('Helvetica',10),key= 'move_file'),sg.Text(size=(40,1), key='-OUTPUT8-')],]
window = sg.Window('All Tools', layout_locnhan_list, grab_anywhere=False, size=(640, 530), return_keyboard_events=True, finalize=True)

def progress_loc_nhan_move_list():
    import threading
    layout = [[sg.Text('Progress move...'),sg.Text('',key='percent')],
                [sg.ProgressBar(max_value=100, orientation='h', size=(40, 30), key='progress_1')]]

    main_window = sg.Window('move', layout, finalize=True)
    current_value = 1
    main_window['progress_1'].update(current_value)

    threading.Thread(target=move,args=(main_window,),daemon=True).start()

    while True:
        window, event, values = sg.read_all_windows()
        if event == 'Exit':
            break
        if event.startswith('update_'):
            print(f'event: {event}, value: {values[event]}')
            key_to_update = event[len('update_'):]
            window[key_to_update].update(values[event])
            window.refresh()
            continue
        # process any other events ...
    window.close()

def move_list(rr):
    TM_ORI = values['input_folder_locnhan'] 
    TM_SAV = values['input_folder_SAVE_locnhan'] 
    txt = glob(TM_ORI + '/*.txt')
    out_dir = TM_SAV + '/'
    txt1 = glob(out_dir + '*.txt')
    label_outer1 = values['TMP1'].split(',')
    print(label_outer1)
    c = 0
    i=g=0
    lst=[]
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
            #out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    for u in label_outer1:
                        if int(tmp[0]) == int(u):
                            c += 1
                            lst.append(tenf)
                            if os.path.exists(filename[:-3]+'jpg'):
                                shutil.move(filename[:-3]+'jpg' , out_dir + tenf[:-3] + 'jpg')
                                print(f'{c}_{tenf}')                       
                            break 
        else:
            try :
                shutil.copyfile(filename, out_dir + tenf)
                print(tenf)
            except:
                pass
        i+=1 
        if g != int(100 * (i/(len(txt)))):
            g = int(100 * (i/(len(txt))))
        rr.write_event_value('update_progress_1', g)
        rr.write_event_value('update_percent', str(g) + '%')

    for i in lst :
        shutil.move(TM_ORI +'/' + i, out_dir + i)
        txt = glob(out_dir + '*.txt')
        c = 0
        for filename in txt:
            tenf = os.path.basename(filename)
            if not os.path.exists(filename[:-3] +'jpg'):
                c+=1
                os.remove(filename)
                print(c , tenf) 
    print('completed')   
    print('Tong Files', len(txt))
    
    time.sleep(1)
    if len(txt1) > 0 :
        print('there are', len(txt1) , 'file')
    else:
        print('no file')
    rr.write_event_value('Exit', '')

while True:             
    event, values = window.read(timeout=20)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'move_file':
        progress_loc_nhan_move_list()
        

    

    