import sqlite3,keyboard
from datetime import datetime
import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 
import threading
import time
import imp
sg.theme('Darkblue') 

# layout = [  
#             [sg.T('1.Họ Tên', font='Any 10', text_color = 'orange')],
#             [sg.Input(size=(int(0.7*48),1), font=('Helvetica',12), key='input_Name6', text_color='white',enable_events= True)],
#             [sg.Text('')],
#             [sg.T('2.Ngày/Tháng/Năm sinh', font='Any 10', text_color = 'orange')],
#             [sg.Input(size=(int(0.7*48),1), font=('Helvetica',12), key='input_Name6', text_color='navy',enable_events= True)],
#             [sg.Text('')],
#             [sg.T('3.Địa chỉ', font='Any 10', text_color = 'orange')],
#             [sg.Input(size=(int(0.7*48),1), font=('Helvetica',12), key='input_Name6', text_color='navy',enable_events= True)],
#             [sg.Text('')],
#             [sg.T('4.Mã Sinh Viên', font='Any 10', text_color = 'orange')],
#             [sg.Input(size=(int(0.7*48),1), font=('Helvetica',12), key='input_Name6', text_color='navy',enable_events= True)],
#             [sg.Text('')],

#             [sg.Text('CHOOSE FOLDER save', key = '-output1-')],
#             [sg.Input(size=(20,1), font=('Helvetica',12), key='SEARCH',tooltip='nhap masv'),
#             [sg.Button('show', size=(5,1), font=('Helvetica',10),key= 'show')],]
#             # sg.Combo(('ids','MASV','AGE'),default_value='MASV', font=('Helvetica',12), key='keypath'),]
                       
# ]
# window = sg.Window('Lọc Nhãn', layout, grab_anywhere=False, size=(1000,500), return_keyboard_events=True, finalize=True)

conn = sqlite3.connect('Test_sql/test_1.db')
data1 = conn.execute('SELECT * FROM TEST_1').fetchall()
def submit_efect():
    for i in range(1000):
        if not sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, message='Wait a sencond', no_titlebar=False, time_between_frames=50, text_color='black', background_color='white'):
            break
    sg.PopupAnimated(None)
    sg.Popup('Bạn đã đăng ký thành công', title='Ping',background_color= 'white',text_color='black',button_color='lightblue')

class keysearch_database:
    def heading():
        headings1=[]
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TEST_1 ')
        for column in cursor.description:
            headings1.append((column[0]))
        return headings1

    def key_search():
        global key,a
        kq1 = []
        conn = sqlite3.connect('Test_sql/test_1.db')
        c = conn.cursor()
        key_search = key  
        if a == 1:   
            c.execute(" SELECT * FROM test_1 WHERE Name = " + str(key_search))
        if a == 2: 
            c.execute(" SELECT * FROM test_1 WHERE MASV = " + str(key_search))
        if a == 3:
            c.execute(" SELECT * FROM test_1 WHERE ids = " + str(key_search))
        records = c.fetchall()
        for row in records: 
            kq1.append(list(row))
        return kq1
    def key_search1() :
        v = keysearch_database.key_search()
        return v
    def maketable():
        global b
        b = keysearch_database.key_search() 
        right_click_menu = ['&Right click menu', ['&Delete' , '&Modify']]
        sg.theme('DarkBlue') 
        headings = keysearch_database.heading()
        layoutfordisplay= [[sg.Input(size=(10,1), font=('Helvetica',12), key='key_search')],
                            [sg.Button('Reattach',key='alo123')],
                            [sg.Combo(values= str(headings[0]))],
            [sg.Table(  values= b,
                        headings = headings, 
                        max_col_width= 25,
                        auto_size_columns = True,
                        display_row_numbers = True,
                        justification = 'center', 
                        num_rows =30,                        
                        key = 'PATIENTTABLE',
                        row_height = 20,
                        enable_events = True,
                        expand_x=False,
                        expand_y=True,
                        vertical_scroll_only=False,
                        enable_click_events=True,
                        right_click_menu=right_click_menu,
                        tooltip = 'all' )]]   
        window = sg.Window('show', layoutfordisplay, modal= True )
        while True:
            event, values = window.read(timeout=20)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Delete':
                try:
                    row_index = values['PATIENTTABLE'][0]
                    row_id = data1[row_index][5]
                    print(row_id)
                    conn.execute(f"DELETE FROM TEST_1 WHERE ids={row_id}")
                    conn.commit()
                    data = conn.execute('SELECT * FROM TEST_1').fetchall()
                    data_list = [list(row) for row in data]  
                    window['PATIENTTABLE'].update(values=data_list)
                    b = 0
                except :
                    sg.popup('no values to del')
            # elif event == 'Modify':
            #         row_index = values['PATIENTTABLE'][0]
            #         # Lấy dữ liệu của dòng đó
            #         data = window['PATIENTTABLE'].get()[row_index]                    
            #         # Hiển thị cửa sổ popup để người dùng chỉnh sửa thông tin
            #         edit_layout = [
            #             [sg.Text('Name:'), sg.Input(data[0], key='-NAME-')],
            #             [sg.Text('Age:'), sg.Input(data[1], key='-AGE-')],
            #             [sg.Text('MaSV:'), sg.Input(data[2], key='-CITY-')],
            #             [sg.Button('Save'), sg.Button('Cancel')]
            #         ]
            #         edit_window = sg.Window('Edit', edit_layout)
            #         while True:
            #             edit_event, edit_values = edit_window.read()
            #             if edit_event == sg.WIN_CLOSED or edit_event == 'Cancel':
            #                 break
            #             elif edit_event == 'Save':
            #                 # Cập nhật lại dữ liệu trên bảng
            #                 new_data = [edit_values['-NAME-'], edit_values['-AGE-'], edit_values['-CITY-']]
            #                 window['-TABLE-'].update({row_index: new_data})
            #                 break
            #         edit_window.close()
class database:
    def heading():
        headings1=[]
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TEST_1 ')
        for column in cursor.description:
            headings1.append((column[0]))
        return headings1

    def getdatabase():
        kq = []
        conn = sqlite3.connect('Test_sql/test_1.db')
        c = conn.cursor()
        query = " SELECT Name, AGE, ADDRESS , MASV , GIOITINH , ids, time_start ,time_start, time_end from test_1 "
        c.execute(query)
        for row in c: 
            kq.append(list(row))
        return kq
    def truyvan() :
        c = database.getdatabase()
        return c

    def maketable():
        global key,a,b
        b = database.truyvan() 
        sg.theme('DarkBlue') 
        headings = database.heading()
        layoutfordisplay= [[sg.Button('UPDATE',key='update')],
                           [sg.Combo(values= [str(headings[3]),str(headings[5])],default_value=str(headings[5]),font=('Helvetica',10),size=(10, 50),text_color='white',enable_events= True, key='choose_model'),sg.Input(size=(10,1), font=('Helvetica',12), key='key_search')],
                            [sg.Button('SEARCH',key='SEARCH')],
            [sg.Table(  values= b,
                        headings = headings, 
                        max_col_width=25,
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='center',
                        num_rows=20,
                        # alternating_row_color=sg.theme_button_color()[1],
                        key='-TABLE-',
                        selected_row_colors='red on yellow',
                        enable_events=True,
                        select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                        expand_x=True,
                        expand_y=True,
                        vertical_scroll_only=False,
                        enable_click_events=True, 
                        tooltip = 'all' 
                        )],
        ]
        window = sg.Window('show', layoutfordisplay, resizable=True, finalize=True).Finalize()
        window.Maximize()
        while True:
            event, values = window.read(timeout=20)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'update':  
              imp.reload(database.maketable())                      
            elif event == 'SEARCH':                   
                if values['key_search'] == '' or values['key_search'] == None:
                    sg.popup_error('CHUA NHAP', title='Lỗi')
                else:
                    if str(values['choose_model']) == 'Name':
                        a = 1
                        key = values['key_search']
                        keysearch_database.maketable() 
                    elif str(values['choose_model']) == 'MASV':  
                        a = 2
                        key = values['key_search']
                        keysearch_database.maketable() 
                    elif str(values['choose_model']) == 'ids':  
                        a = 3
                        key = values['key_search']
                        keysearch_database.maketable() 
            elif b == 0:  
                data = conn.execute('SELECT * FROM TEST_1').fetchall()
                data_list = [list(row) for row in data]  
                window['-TABLE-'].update(values=data_list)
                
database.maketable()


