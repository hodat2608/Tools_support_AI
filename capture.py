import pyautogui
import time
from PIL import ImageGrab
import datetime

from openpyxl.styles import Alignment
from openpyxl import Workbook
from datetime import date

def time_to_name():
    current_time = datetime.datetime.now()
    name_folder = str(current_time)
    name_folder = list(name_folder)
    for i in range(len(name_folder)):
        if name_folder[i] == ':':
            name_folder[i] = '-'
        if name_folder[i] == ' ':
            name_folder[i] ='_'
        if name_folder[i] == '.':
            name_folder[i] ='-'
    name_folder = ''.join(name_folder)
    return name_folder
def capture_screen():
    path = 'C:/TOOLS/capture/'
    x = 100
    y = 150
    width = 800
    height = 600
    today = datetime.date.today()
    try:
        name_folder_ng = time_to_name()
        screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
        screenshot.save(path+name_folder_ng+'.jpg')                        
    except Exception as e:
        print(f"Lỗi khi chụp màn hình: {e}")

capture_screen()
