import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 

sg.theme('DarkAmber') 

layout_locnhan = [[sg.Text('CHOOSE FOLDER')],
            [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_locnhan'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True) ],

            [sg.Button('SET', size=(3,1), font=('Helvetica',10),key= 'button_TM')],

            [sg.Text('CHOOSE TMP'), sg.Input(size=(4,5), font=('Helvetica',12), key='TMP')],

            [sg.Button('SET', size=(3,1), font=('Helvetica',10),key= 'button_TMP')],

            [sg.Text('')],

            [sg.Button('MOVE', size=(5,1), font=('Helvetica',10),key= 'move_file')],]

layout_xoanhanok = [[sg.Text('CHOOSE FOLDER')],
            [sg.Input(size=(55,1), font=('Helvetica',12), key='input_folder_xoanhanok'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True)],
            [sg.Button('SET', size=(5,1), font=('Helvetica',10),key= 'button_input_folder')],

            [sg.Text('')],

            [sg.Text('Choose outter'),
            sg.Button('CAM1', size=(5,1), font=('Helvetica',10),key= 'button_outter_cam1'),sg.Text(size=(40,1), key='-OUTPUT1-')],
            [sg.Text('                    '),
            sg.Button('CAM2', size=(5,1), font=('Helvetica',10),key= 'button_outter_cam2'),sg.Text(size=(40,1), key='-OUTPUT2-')],

            [sg.Text('')],

            [sg.Text('Choose inner  '),
             sg.Input(size=(5,1), font=('Helvetica',12), key='input_inner')],
            [sg.Text('Choose w_min'),sg.Input(size=(5,1),font=('Helvetica',12), key='input_w_min')],
            [sg.Text('Choose h_min'),sg.Input(size=(5,1), font=('Helvetica',12), key='input_h_min')],
            #[sg.Text('')],
            [sg.Button('SET', size=(5,1), font=('Helvetica',10),key= 'SET_input')],

            [sg.Text('')],
            [sg.Text('')],

            [sg.Button('RUN', size=(5,1), font=('Helvetica',10),key= 'RUN_1')],]    

layout = [[sg.TabGroup([[ sg.Tab('lọc nhãn', layout_locnhan),
                        sg.Tab('Xóa Nhãn Ok', layout_xoanhanok)]])
            ]]

window = sg.Window('All Tools', layout, grab_anywhere=False, size=(640, 450), return_keyboard_events=True, finalize=True)

while True:             
    event, values = window.read(timeout=20)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'button_TM' :
        TM = values['input_folder_locnhan'] + '/' 

    if event == 'button_TMP' :
        TMP = int(values['TMP'])


    if event == 'button_input_folder' :
        path_1 = values['input_folder_xoanhanok'] + '/' 


    if event == 'button_outter_cam1' :
        cam1 = ['5','6','7','8','9','10','11'] 
        window['-OUTPUT1-'].update('selected cam1')
        
    if event == 'button_outter_cam2' :    
        cam2 = ['5','6','7','8','9','10','11','12','13','14','15','16']
        window['-OUTPUT2-'].update('selected cam2')
       
    if event == 'SET_input' :
        label_inner = values['input_inner']
        w_min = float(values['input_w_min'])
        h_min = float(values['input_h_min'])
        
    if event == 'move_file':
        txt = glob(TM + '*.txt')
        os.mkdir(TM + 'TXT')
        out_dir = TM + 'TXT/'
        cnt = len(txt)
        c = 0
        for filename in txt:
            tenf = os.path.basename(filename)
            #out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0]) == TMP:
                        c += 1
                        shutil.copyfile(filename, out_dir + tenf)
                        shutil.copyfile(filename, out_dir + tenf[:-3] + 'jpg')
                        print(tenf)  
                        break 
    if event == 'RUN_1' :
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
                #print(names)
            outers = cam2
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
                                #print('HAHA')
                                f.write(line)
                            else:
                                cnt += 1 
                                print('finished', tenf)

                                  
window.close()
    