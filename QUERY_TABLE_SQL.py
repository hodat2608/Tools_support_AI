import sqlite3,keyboard
from datetime import datetime
import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 
import threading
import time
import imp

conn = sqlite3.connect('Test_sql/test_1.db')

def heading():
    headings1=[]
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TEST_1 ')
    for column in cursor.description:
        headings1.append((column[0]))
    return headings1
abc = heading()
print(str(abc[0]))
def getdatabase():
    kq = []
    conn = sqlite3.connect('Test_sql/test_1.db')
    c = conn.cursor()
    query = " SELECT Name, AGE, ADDRESS , MASV , GIOITINH ,ids, time_start ,time_start, time_end from test_1 "
    c.execute(query)
    for row in c: 
        kq.append(list(row))
    return kq
def truyvan() :
    c = getdatabase()
    return c

def maketable():
    global key
    b = truyvan() 
    sg.theme('DarkBlue') 
    headings = heading()
    layoutfordisplay= [[sg.Input(size=(10,1), font=('Helvetica',12), key='key_search')],
                        [sg.Button('Reattach',key='alo123')],
                        [sg.Button('search',key='alo1234')],
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
        elif event == 'alo123':        
            imp.reload(maketable())
        elif event == 'alo1234':  
            key = values['key_search']
            print(key)
        
    

            

maketable()


