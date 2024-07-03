

import PySimpleGUI as sg

# Hàm lưu giá trị vào tệp tin
def save_values(values_1,values_2,values_3):
    with open('choose_model.txt', 'w') as file:
        file.write(f'width={values_1}\nheight={values_2}\nconfidence={values_3}')

# Hàm đọc giá trị từ tệp tin
def load_values():
    result = []
    with open('choose_model.txt') as lines:
        for line in lines:
            _, value = line.strip().split('=')
            result.append(int(value.strip()))
    return result

file_weights = [("Text Files", "*.txt")]

layout_option1 = [
    [sg.Frame('', [
        [sg.Frame('', [
            [sg.Text('Confidence', size=(12, 1), font=('Helvetica', 15), text_color='red'),
             sg.Slider(range=(1, 100), default_value=30, orientation='h', size=(60, 20), font=('Helvetica', 11), disabled=True, key='conf_thres1')],
            [sg.Text('')],
            [sg.Text('Thiết định kích thước bụi chì nằm trong cuộn cảm : ', size=(40, 1), font=('Helvetica', 15), text_color='red'),
             sg.Text('With min', size=(8, 1), font=('Helvetica', 15), text_color='red'),
             sg.InputText(default_text=load_values()[0], size=(7, 1), font=('Helvetica', 15), key='W_min_bc_cc', text_color='navy'),
             sg.Text('Height min', size=(8, 1), font=('Helvetica', 15), text_color='red'),
             sg.InputText(default_text=load_values()[1], size=(7, 1), font=('Helvetica', 15), key='H_min_bc_cc', text_color='navy'),
             sg.Slider(range=(1,100),default_value=load_values()[2],orientation='h',size=(28,15),font=('Helvetica',10), key= 'bc_cc_Conf_1'),
             ],
             [sg.Button('Save Data', size=(12,1),  font=('Helvetica',12),key='SaveData3', )],
             [sg.Button('Load Data', size=(12,1),  font=('Helvetica',12),key='Load_Data', )]
        ], relief=sg.RELIEF_FLAT),
    ], ])
]]

window = sg.Window('My Window', layout_option1, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'SaveData3':
        save_values(str(values['W_min_bc_cc']),str(values['H_min_bc_cc']),int(values['bc_cc_Conf_1']))
    
    

window.close()
