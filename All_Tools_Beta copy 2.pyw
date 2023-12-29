import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 
import time
from os.path import getsize

sg.theme('DarkAmber') 

UNITS_MAPPING = [
    (1<<50, ' PB'),
    (1<<40, ' TB'),
    (1<<30, ' GB'),
    (1<<20, ' MB'),
    (1<<10, ' KB'),
    (1, (' byte', ' bytes')),
]

def pretty_size(bytes, units=UNITS_MAPPING):
    for factor, suffix in units:
        if bytes >= factor:
            break
    amount = int(bytes / factor)

    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return str(amount) + suffix

def Progress():
    sg.theme('DarkAmber') 
    layout = [[sg.Text('Deleting...')],
              [sg.ProgressBar(800, orientation='h', size=(20,20), key='progress')],
              [sg.Cancel()]]
    window = sg.Window('').Layout(layout)
    for i in range(800):
        event, values = window.Read(timeout=0)
        if event == 'Cancel' or event == None:
            break
        window['progress'].UpdateBar(i+1)
    window.Close()


layout_locnhan = [[sg.Text('')],
            [sg.Text('Chọn thư mục gốc ')],
            [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_locnhan'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True) ],

            [sg.Text('')],

            [sg.Text('Chọn thư mục lưu ')],
            [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_SAVE_locnhan'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True) ],

            [sg.Text('')],

            [sg.Text('Chọn Stt nhãn '), sg.Input(size=(4,5), font=('Helvetica',12), key='TMP1'),sg.Text('Copy files chứa nhãn này!')],

             [sg.Text('')],

            [sg.Text('Chọn Stt nhãn '), sg.Input(size=(4,5), font=('Helvetica',12), key='TMP2'),sg.Text('Copy files không chứa nhãn này!')],

            [sg.Text('')],

            [sg.Button('COPY', size=(7,1), font=('Helvetica',10),key= 'copy_file'),sg.Text(size=(40,1), key='-OUTPUT7-')],
            [sg.Text('')],
            [sg.Button('MOVE', size=(7,1), font=('Helvetica',10),key= 'move_file'),sg.Text(size=(40,1), key='-OUTPUT8-')],]

layout_xoanhanok = [
            [sg.Text('Chọn thư mục gốc')],
            [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_xoanhanok'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True)],
            
            
            [sg.Text('')],

            [sg.Text('Chọn camera (cho line 75) ', size =(20,1)),
            sg.Button('CAM1', size=(5,1), font=('Helvetica',10),key= 'button_outter_cam1'),sg.Text(size=(40,1), key='-OUTPUT1-')],
            [sg.Text('',size =(20,1)),
            sg.Button('CAM2', size=(5,1), font=('Helvetica',10),key= 'button_outter_cam2'),sg.Text(size=(40,1), key='-OUTPUT2-')],

            [sg.Text('')],

            [sg.Text('Stt các nhãn ok muốn xóa (cho line khác)', size =(30,1)),
            sg.Input(size=(30,1), font=('Helvetica',12), key='input_outer_xoanhanok1')],

            [sg.Text('')],

            [sg.Text('Stt nhãn đầu vào: ',size =(12,1)),
             sg.Input(size=(5,1), font=('Helvetica',12), key='input_inner')],

            [sg.Text('')],

            [sg.Text('W_Min', size = (12,1)),sg.Input(size=(5,1),font=('Helvetica',12), key='input_w_min')],
            [sg.Text('H_Min', size = (12,1)),sg.Input(size=(5,1), font=('Helvetica',12), key='input_h_min')],
            [sg.Text('')],
            [sg.Button('SET', size=(10,1), font=('Helvetica',10),key= 'SET_input'),sg.Text(size=(40,1), key='-OUTPUT10-')],

            [sg.Text('')],
            [sg.Text('')],

            [sg.Button('RUN>NHÃN ĐÔI', size=(14,1), font=('Helvetica',10),key= 'RUN_CAM1'),
             sg.Button('RUN>NHÃN ĐƠN', size=(14,1), font=('Helvetica',10),key= 'RUN_CAM2')],]    

layout_xoafiletheosoduoi = [[sg.Text('Chọn thư mục gốc')],
            [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_xoafiletheosoduoi'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True) ],

            [sg.Text('Chọn số đuôi file muốn xóa'), sg.Input(size=(6,5), font=('Helvetica',12), key='name_end_file')],

            [sg.Text('')],

            [sg.Button('DELETE', size=(7,1), font=('Helvetica',10),key= 'delete_file'),sg.Text(size=(50,1), key='-OUTPUT3-')],
            [sg.Text(size=(7,1)),sg.Text(size=(50,1), key='-OUTPUT4-')],]

layout = [[sg.TabGroup([[ sg.Tab('Lọc nhãn', layout_locnhan),
                        sg.Tab('Xóa Nhãn Ok', layout_xoanhanok),
                        sg.Tab('Xóa file theo số đuôi', layout_xoafiletheosoduoi)]])
            ]]

window = sg.Window('All Tools', layout, grab_anywhere=False, size=(640, 530), return_keyboard_events=True, finalize=True)

def clearinput():
        for key in values:
            try:
                window['TMP1'].update('')
                window['input_folder_SAVE_locnhan'].update('')
            except:
                window['TMP2'].update('')
        return None


def progress_loc_nhan_copy():
    import threading
    layout = [[sg.Text('Processing copy...'),sg.Text('',key='percent')],
                [sg.ProgressBar(max_value=100, orientation='h', size=(40,30), key='progress_1')],
                 [sg.Text('Size on disk: '),sg.Text('',key='filesize')]]

    main_window = sg.Window('task', layout, finalize=True)
    current_value = 1
    main_window['progress_1'].update(current_value)

    threading.Thread(target=copy,args=(main_window,),daemon=True).start()

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

def progress_loc_nhan_copy_expt():
    import threading
    layout = [[sg.Text('Processing copy expt...'),sg.Text('',key='percent')],
                [sg.ProgressBar(max_value=100, orientation='h', size=(50, 20), key='progress_1')]]

    main_window = sg.Window('Test', layout, finalize=True)
    current_value = 1
    main_window['progress_1'].update(current_value)

    threading.Thread(target=copy_expt,args=(main_window,),daemon=True).start()

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

def progress_loc_nhan_move():
    import threading
    layout = [[sg.Text('Progress...'),sg.Text('',key='percent')],
                [sg.ProgressBar(max_value=100, orientation='h', size=(40, 30), key='progress_1')],
               ]

    main_window = sg.Window('Task', layout, finalize=True)
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
        
def copy(er):
    TM = values['input_folder_locnhan'] + '/'
    TM_SAV = values['input_folder_SAVE_locnhan'] 
    TMP = int(values['TMP1'])
    txt = glob(TM + '/*.txt')
    out_dir = TM_SAV + '/' 
    i = g = 0
    c = 0
    tongfile = 0
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt':
            #out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0]) == TMP:
                        Filesize = getsize(filename[:-3] + 'jpg')
                        tongfile += int(Filesize)
                        c += 1
                        shutil.copyfile(filename, out_dir + tenf)
                        shutil.copyfile(filename[:-3] + 'jpg', out_dir + tenf[:-3] + 'jpg')
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf)
        i+=1 
        if g != int(100 * (i/(len(txt)))):
            g = int(100 * (i/(len(txt))))
        er.write_event_value('update_progress_1', g)
        er.write_event_value('update_percent', str(g) + '%')
        er.write_event_value('update_filesize',str(pretty_size(tongfile)) + ' bytes')
    time.sleep(2)
    er.write_event_value('Exit', '')

def copy_expt(er):
    TM = values['input_folder_locnhan'] + '/'
    TM_SAV = values['input_folder_SAVE_locnhan'] 
    TMP = int(values['TMP2'])
    txt = glob(TM + '/*.txt')
    out_dir = TM_SAV + '/' 
    i = g = 0
    c = 0
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt':
            with open(filename, 'r') as f:
                a =0 
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0]) == TMP:
                        a=1
                if a==0:
                    c += 1                                                                                    
                    shutil.copy(filename , out_dir + tenf)
                    shutil.copy(filename[:-3] + 'jpg', out_dir + tenf[:-3] + 'jpg')
        else : 
            shutil.copy(filename, out_dir + tenf)
            print(tenf)
        i+=1 
        if g != int(100 * (i/(len(txt)))):
            g = int(100 * (i/(len(txt))))
        er.write_event_value('update_progress_1', g)
        er.write_event_value('update_percent', str(g) + '%')
    time.sleep(2)
    er.write_event_value('Exit', '')

def move(rr):
    TM_ORI = values['input_folder_locnhan'] 
    TM_SAV = values['input_folder_SAVE_locnhan'] 
    TMP = int(values['TMP1'])
    txt = glob(TM_ORI + '/*.txt')
    out_dir = TM_SAV + '/'
    c = 0
    i=g=0
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt':
            #out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0]) == TMP:
                        c += 1
                        f.close()
                        if os.path.exists(filename):
                            shutil.move(filename , out_dir + tenf)
                        if os.path.exists(filename[:-3]+'jpg'):
                            shutil.move(filename[:-3]+'jpg' , out_dir + tenf[:-3] + 'jpg')
                            print(c , "-" , tenf)
                            window['-OUTPUT8-'].update('Done!') 
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
    time.sleep(2)
    rr.write_event_value('Exit', '')

while True:             
    event, values = window.read(timeout=20)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'button_outter_cam1' :
        cam1 = ['5','6','7','8','9','10','11'] 
        window['-OUTPUT1-'].update('selected cam1')
        
    if event == 'button_outter_cam2' :    
        cam2 = ['5','6','7','8','9','10','11','12','13','14','15','16']
        window['-OUTPUT2-'].update('selected cam2')
       
    if event == 'SET_input' :
        path_1 = values['input_folder_xoanhanok'] + '/'
        label_inner = values['input_inner']
        w_min = float(values['input_w_min'])
        h_min = float(values['input_h_min'])
        label_outer1 = values['input_outer_xoanhanok1'].split(',')
        window['-OUTPUT10-'].update('Ready for Run!') 

    if event == 'copy_file':
        try: 
            progress_loc_nhan_copy()
        except:
            progress_loc_nhan_copy_expt()
        clearinput()

    if event == 'move_file':
        progress_loc_nhan_move()
        clearinput()

    if event == 'RUN_CAM1' :
        cnt = 0
        import glob 
        import os
        for i in glob.glob(path_1 + '*.txt'):
            tenf = os.path.basename(i)
            file = open(i, 'r')
            Lines = file.readlines()
            names = []
            files = []
            for line in Lines:
                num = line.split()[0]
                names.append(num)
            try:           
                outers = cam1  
            except:
                outers = label_outer1   
            inner = label_inner
            for outer in outers:
                if inner in names and outer in names:
                    for index,line in enumerate(Lines):      
                        if line.strip().split()[0] == outer:
                            myindex =0
                            x4 = float(line.strip().split()[1])
                            y4 = float(line.strip().split()[2])
                            w4 = float(line.strip().split()[3])
                            h4 = float(line.strip().split()[4])
                            xmin = x4 - w4/2
                            xmax = x4 + w4/2
                            ymin = y4 - h4/2
                            ymax = y4 + h4/2
                            myindex = index 
                            #print(myindex)
                            break
                    for line in Lines:   
                        if line.strip().split()[0] == inner:
                            x0 = float(line.strip().split()[1])
                            y0 = float(line.strip().split()[2])
                            w0 = float(line.strip().split()[3])
                            h0 = float(line.strip().split()[4])
                            #bui chi 0.021250 0.028333
                            #divat 0.025000 0.033333
                            if w0 > w_min  and h0 > h_min:
                                if xmin < x0 < xmax  and ymin < y0 < ymax:
                                    for index,line in enumerate(Lines):  
                                        if line.strip().split()[0] == outer and index == myindex:
                                            files.append(line)
                    with open(i, 'w') as f:
                        for line in Lines:
                            if line not in files:
                                f.write(line)
                            else:
                                cnt += 1 
                                print('done', tenf)

                if inner in names and outer in names:
                    for index,line in enumerate(Lines):      
                        if line.strip().split()[0] == outer:
                            myindex =0
                            x4 = float(line.strip().split()[1])
                            y4 = float(line.strip().split()[2])
                            w4 = float(line.strip().split()[3])
                            h4 = float(line.strip().split()[4])
                            xmin = x4 - w4/2
                            xmax = x4 + w4/2
                            ymin = y4 - h4/2
                            ymax = y4 + h4/2
                            myindex = index 
                            #print(myindex)
            
                    for line in Lines:   
                        if line.strip().split()[0] == inner:
                            x0 = float(line.strip().split()[1])
                            y0 = float(line.strip().split()[2])

                            w0 = float(line.strip().split()[3])
                            h0 = float(line.strip().split()[4])
                            #bui chi 0.021250 0.028333
                            #divat 0.025000 0.033333
                            if w0 > w_min  and h0 > h_min:
                                if xmin < x0 < xmax  and ymin < y0 < ymax:
                                    for index,line in enumerate(Lines):  
                                        if line.strip().split()[0] == outer and index == myindex:
                                            files.append(line)
                    with open(i, 'w') as f:
                        for line in Lines:
                            if line not in files:
                                f.write(line)
                            else:
                                cnt += 1 
                                print('done', tenf)              

    if event == 'RUN_CAM2' :
        cnt = 0
        import glob 
        import os
        for i in glob.glob(path_1 + '*.txt'):
            tenf = os.path.basename(i)
            file = open(i, 'r')
            Lines = file.readlines()
            names = []
            files = []
            for line in Lines:
                num = line.split()[0]
                names.append(num)
            try:           
                outers = cam2  
            except:
                outers = label_outer1
            inner = str(label_inner)
            for outer in outers:
                if inner in names and outer in names:
                    for index,line in enumerate(Lines):      
                        if line.strip().split()[0] == outer:
                            myindex =0
                            x4 = float(line.strip().split()[1])
                            y4 = float(line.strip().split()[2])
                            w4 = float(line.strip().split()[3])
                            h4 = float(line.strip().split()[4])
                            xmin = x4 - w4/2
                            xmax = x4 + w4/2
                            ymin = y4 - h4/2
                            ymax = y4 + h4/2
                            myindex = index 
                            #print(myindex)
                            break
                    for line in Lines:   
                        if line.strip().split()[0] == inner:
                            x0 = float(line.strip().split()[1])
                            y0 = float(line.strip().split()[2])
                            w0 = float(line.strip().split()[3])
                            h0 = float(line.strip().split()[4])
                            #bui chi 0.021250 0.028333
                            #divat 0.025000 0.033333
                            if w0 > w_min  and h0 > h_min:
                                if xmin < x0 < xmax  and ymin < y0 < ymax:
                                    for index,line in enumerate(Lines):  
                                        if line.strip().split()[0] == outer and index == myindex:
                                            files.append(line)
                    with open(i, 'w') as f:
                        for line in Lines:
                            if line not in files:
                                f.write(line)
                            else:
                                cnt += 1 
                                print('finished', tenf)

    if event == 'delete_file' :
        TM = values['input_folder_xoafiletheosoduoi'] + '/' 
        NUM = values['name_end_file']   
        txt = glob(TM + '*.txt')
        os.mkdir(TM + 'TXT')
        out_dir = TM + 'TXT/'
        cnt = len(txt)
        c = 0
        for filename in txt:
            tenf = os.path.basename(filename)
            tenfi = tenf.split()
            for i in tenfi:
                if i[20:26] == str(NUM):
                    shutil.move(filename , out_dir + tenf)
                    shutil.move(filename[:-3]+'jpg' , out_dir + tenf[:-3] + 'jpg')
                    Progress()
                    window['-OUTPUT3-'].update('deleted file ' + tenf )
                    c+=1
                    break
                # else:  
                #     time.sleep(2)
                #     sg.popup_cancel('No such file or directory of ', NUM )    
                #     break              
        shutil.rmtree(out_dir)
window.close()
    