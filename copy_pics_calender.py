import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 
import time
import os,shutil 
from datetime import datetime

sg.theme('DarkAmber') 

layout = [[sg.Text('Thư mục gốc: ')],
            [sg.Input(size=(60,1), font=('Helvetica',12), key='input_folder'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True) ],

            [sg.Text('')],

            [sg.Text('Files modified date from (yyyy-mm-dd hh:mm:ss)')],
            [sg.In(key='-CAL1-', ), sg.CalendarButton('Calendar', target='-CAL1-')],

            [sg.Text('')],

            [sg.Text('Files modified date from (yyyy-mm-dd hh:mm:ss)')],
            [sg.In(key='-CAL2-', ), sg.CalendarButton('Calendar', target='-CAL2-')],

            [sg.Text('')],

            [sg.Text('Thư mục lưu: ')],
            [sg.Input(size=(60,1), font=('Helvetica',12), key='input_folder_save'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True) ],

            [sg.Text('')],

            [sg.Button('COPY', size=(7,1), font=('Helvetica',10),key= 'copy_file'),sg.Text(size=(40,1), key='-OUTPUT30-')],]
                       


window = sg.Window('Lọc Nhãn', layout, grab_anywhere=False, size=(640, 400), return_keyboard_events=True, finalize=True)

def clearinput():
        for key in values:
            try:
                #window['TMP1'].update('')
                window['input_folder_save'].update('')
            except:
                window['TMP2'].update('')
        return None

def progress_loc_nhan_copy_celender():
    import threading
    layout = [[sg.Text('Processing copy...'),sg.Text('',key='percent')],
                [sg.ProgressBar(max_value=100, orientation='h', size=(40,30), key='progress_1')],
                [sg.Text('total file: '),sg.Text('',key='lentxt')]
                ]

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

def copy(er):
    from glob import glob  
    from datetime import datetime
    TM = values['input_folder'] + '/'
    TM_SAV = values['input_folder_save'] 
    #TMP = int(values['TMP1'])
    txt = glob(TM + '/*.jpg')
    out_dir = TM_SAV + '/' 
    i = g = 0
    c = 0
    #time_data1 = "11/08/22 02:35:14"
    # time_data1 = values['start_date']
    # format_data1 = "%d/%m/%y %H:%M:%S"
    date1 = datetime.strptime(values['-CAL1-'], '%Y-%m-%d %H:%M:%S')
    print(date1)

    #time_data2 = "2/10/22 02:35:14"
    # time_data2 = values['end_date']
    # format_data2 = "%d/%m/%y %H:%M:%S"
    date2 = datetime.strptime(values['-CAL2-'], '%Y-%m-%d %H:%M:%S')
    print(date2)
    for filename in txt:
        tenf = os.path.basename(filename)
    #out = open(out_dir + tenf,'w')
        import datetime
        m_time = os.path.getmtime(filename)
        dt_m = datetime.datetime.fromtimestamp(m_time)
        if date1 < dt_m < date2:
            y = len(txt)
            shutil.copyfile(filename, out_dir + tenf)
            c+=1 
        i +=1
        if g != int(100 * (i/(len(txt)))):
            g = int(100 * (i/(len(txt))))
        er.write_event_value('update_progress_1', g)
        er.write_event_value('update_percent', str(g) + '%')
        er.write_event_value('update_lentxt', str(y) + 'file') 
    time.sleep(2)
    er.write_event_value('Exit', '')


while True:             
    event, values = window.read(timeout=20)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'copy_file':
        progress_loc_nhan_copy_celender()
        clearinput()
        