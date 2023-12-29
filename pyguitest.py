import PySimpleGUI as sg
import subprocess
import sqlite3,keyboard
from datetime import datetime


form = sg.FlexForm('Script launcher')

layout =  [
                
                [[[sg.Text("Anything printed will display here!")],
                      [sg.Multiline( font=('Helvetica',14), write_only=True, autoscroll=True, auto_refresh=True,reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True,size=(100,100))]
                      ]],
                [ sg.SimpleButton('EXIT')],
                
              ]

window = sg.Window('All Tools', layout, grab_anywhere=False, size=(1000, 700), return_keyboard_events=True, finalize=True)
conn = sqlite3.connect('Test_sql/test_1.db')
while True: 
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TEST_1 WHERE time_end IS ?',(None,))
    rows = cursor.fetchall()
    for x in rows: 
        # if x[5] == 8:
        print('NAME',':', x[0])
        print('AGE' , ':',x[1])
        print('ADD' ,':', x[2])
        print('MASV' , ':',x[3])
        print('GIOITINH' ,':', x[4])
        print('IDS' , ':', x[5])
        print('Date Resgister' , ':', x[6])
        print('-' * 80)
        current_time = datetime.now()
        conn.execute('UPDATE TEST_1 SET time_end=?  WHERE ids = ? ',(current_time, x[5]))
        conn.commit()
    cursor.close    
            
                
    event, values = window.read(timeout=20)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
