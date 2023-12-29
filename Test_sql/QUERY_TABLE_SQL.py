import sqlite3,keyboard
from datetime import datetime
import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 
import threading
import time
conn = sqlite3.connect('test_1.db')

sg.theme('DarkAmber') 

layout = [
            [sg.Text('CHOOSE FOLDER save', key = '-output1-')],
            [sg.Input(size=(20,1), font=('Helvetica',12), key='SEARCH'),
            [sg.Button('MOVE', size=(5,1), font=('Helvetica',10),key= 'move_file')],
            [sg.Button('show', size=(5,1), font=('Helvetica',10),key= 'show')],]
                       
]
window = sg.Window('Lọc Nhãn', layout, grab_anywhere=False, size=(640, 300), return_keyboard_events=True, finalize=True)

def getdatabase():
    kq = []
    conn = sqlite3.connect('Test_sql/test_1.db')
    c = conn.cursor()
    query = " SELECT NAME, AGE, ADDRESS , MASV , GIOITINH , time_start from test_1 "
    c.execute(query)
    for row in c: 
        kq.append(list(row))
    return kq
def truyvan() :
    c = getdatabase()
    return c

def maketable():
    b = truyvan() 
    sg.theme('DarkBlue') 
    headings = ['NAME', 'AGE', 'ADDRESS' , 'MASV' , 'GIOITINH' , 'time_start']
    layoutfordisplay= [[sg.Input(size=(10,1), font=('Helvetica',12), key='key_search')],
                        [sg.Button('Reattach',key='alo123')],
        [sg.Table(  values= b,
                    headings = headings, 
                    max_col_width= 35,
                    auto_size_columns = True,
                    display_row_numbers = True,
                    justification = 'left', 
                    num_rows =30,
                    row_colors=[
                    (i, 'white', 'green') for i in range(0,  5)] + [
                    (i, 'white', 'blue')  for i in range(5,  10)] + [
                    (i, 'white', 'black') for i in range(10, 15)],
                    key = 'PATIENTTABLE',
                    row_height = 20,
                    enable_events = True,
                    tooltip = 'all' )]]   
    window = sg.Window('show', layoutfordisplay, modal= True )
    while True:
        event, values = window.read(timeout=20)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

def keysearch():
    kq1 = []
    conn = sqlite3.connect('Test_sql/test_1.db')
    c = conn.cursor() 
    if event == 'move_file':
        keysearch1 = int(values['SEARCH'])
        c.execute(" SELECT * FROM test_1 WHERE AGE = " + int(keysearch1) )
        
        for row in c: 
            kq1.append(list(row))
        return kq1

def keysearch1() :
    a = keysearch()
    return a


while True:
        event, values = window.read(timeout=20)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break  
        elif event == 'show':
            maketable()   

window.close()



    # for x in rows: 
    #     #if x[5] == 8 :
    #     print('NAME',':', x[0])
    #     print('AGE' , ':',x[1])
    #     print('ADD' ,':', x[2])
    #     print('MASV' , ':',x[3])
    #     print('GIOITINH' ,':', x[4])
    #     print('IDS' , ':', x[5])
    #     print('Date Resgister' , ':', x[6])
    #     print('-' * 80)
    #     current_time = datetime.now()
    #     conn.execute('UPDATE TEST_1 SET time_end=?  WHERE ids = ? ',(current_time, x[5]))
    #     conn.commit()
    # cursor.close    
            
    # if keyboard.is_pressed("q"):
    #     print("Exit")
    #     break