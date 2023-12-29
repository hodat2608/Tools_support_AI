import sqlite3
import datetime


import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 
import threading
import time
from datetime import datetime
sg.theme('DarkAmber') 
layout = [[sg.Text('CHOOSE FOLDER')],
            [sg.Input(size=(60,1), font=('Helvetica',12), key='date_of_birth')],
             [sg.Button('MOVE', size=(5,1), font=('Helvetica',10),key= 'move_file'),sg.Text(size=(40,1), key='-OUTPUT1-')]]

window = sg.Window('Lọc Nhãn', layout, size=(640, 300))


while True:             
    event, values = window.read(timeout=20)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'move_file':
        date = values['date_of_birth']
        print(date)
        formatted_date = datetime.strptime(str(date), "%d/%m/%y").date()
        window['-OUTPUT1-'].update(formatted_date)
        print(type(formatted_date))

window.close()     
