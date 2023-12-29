# # from glob import glob                                                           
# # import os
# # import shutil 
# # TM = 'C:/Users/AI004/Desktop/test/'
# # txt = glob(TM + '*.txt')
# # try:
# #     os.mkdir(TM + 'dat')
# # except:
# #     pass
# # out_dir = TM + 'dat/'
# # for filename in txt:
# #     tenf = os.path.basename(filename)
# #     if tenf == 'classes.txt':
# #         out = open(out_dir + tenf,'w')
# #         with open(filename, 'r') as f:
# #             while True:
# #                 line = f.readline()
# #                 if not line:
# #                     break
# #                 print(line[0])
# #                 tmp = line.split() 
# #                 out.writelines(line) 
# #                 if str(line[0]) == 'c': 
# #                     for i in range(1,13):
# #                         out.writelines('\n')
# #                         out.writelines(str(i))
        
from glob import glob
from tkinter.tix import Tree
import os, cv2, torch, time, datetime, shutil
import numpy as np 
import PySimpleGUI as sg
import traceback
import sqlite3                    
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
    
from TOAN import Test
dir_path = Test.getPath1()  + '*jpg'
save_path = Test.getPath2()
filenames = glob(dir_path)
for filename1 in filenames:
    print(filename1)
    img1_save = cv2.imread(filename1)
    name_folder_ng = time_to_name()
    cv2.imwrite(save_path+ str(name_folder_ng) + '-C4.jpg' ,img1_save)
    try:
        shutil.copy(filename1[:-3] + 'txt', save_path + str(name_folder_ng)+'-C4.txt')
    except:
        pass

