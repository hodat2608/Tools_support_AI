import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 
import time 

def Progress():
    global ht
    sg.theme('DarkAmber') 
    layout = [[sg.Text('A custom progress meter')],
              [sg.ProgressBar(100, orientation='h', size=(20,20), key='progress')],
              [sg.Cancel()]]
    window = sg.Window('Custom Progress Meter').Layout(layout)
    
    event, values = window.Read(timeout=0)
    if event == 'Cancel':
        window.Close()

    popup_window = sg.Window('Pprogress', layout , finalize=True)
    curren


sg.theme('DarkAmber') 
layout = [[sg.Text('CHOOSE FOLDER')],
            [sg.Input(size=(60,1), font=('Helvetica',12), key='input_folder'),
             sg.FolderBrowse(size=(12,1), font=('Helvetica',10),key= 'TM',enable_events=True) ],
            [sg.Text('CHOOSE TMP'), sg.Input(size=(5,5), font=('Helvetica',12), key='TMP')],
            [sg.Text('')],
            [sg.Button('MOVE', size=(5,1), font=('Helvetica',10),key= 'move_file')],
            [sg.ProgressBar(max_value=100, orientation='h', size=(20,20), key='progress')],
            [sg.Text('Copying'), sg.Text('',key='percent')],
                       
]
window = sg.Window('Lọc Nhãn', layout, grab_anywhere=False, size=(640, 300), return_keyboard_events=True, finalize=True)
progress_bar = window.FindElement('progress')
while True:             
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'move_file':
        TMP = int(values['TMP'])
        TM = values['input_folder'] + '/' 
        txt = glob(TM + '*.txt')
        os.mkdir(TM + 'TXT')
        out_dir = TM + 'TXT/'
        #cnt = len(txt)
        c = 0
        i = ht = 0
        for filename in txt:                
            i +=1
            tenf = os.path.basename(filename)
            if  tenf != 'classes.txt':
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
                            print(c , tenf)  
            else :
                shutil.copyfile(filename, out_dir + tenf)
                print(tenf)  
            if ht != int(100 * (i/len(txt))):
                ht = int(100 * (i/len(txt)))
            progress_bar.Update(ht)
            window['percent'].Update(str(ht) + '%')                                                          
window.close()
    
