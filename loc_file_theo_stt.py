import PySimpleGUI as sg
from glob import glob                                                           
import os
import shutil 
import time
from TOAN import Test
TM = Test.getPath1()
txt = glob(TM + '*.txt')
os.makedirs(TM + 'move', exist_ok=True)
out_dir = TM + 'move/'
lst=[] 
for filename in txt:
    tenf = os.path.basename(filename)
    if tenf == 'note.txt':
        with open(filename, 'r') as f:           
            while True:
                line = f.readline()
                if not line:
                    break
                tmp = line.split()
                for r in range(len(tmp)):
                    lst.append(tmp[r])
file_count = 0
for _, _, files in os.walk(TM[:-1]):
    for file in files:
        if file.endswith('.jpg'):
            file_count += 1
            for i in range(len(lst)):
                if file_count == int(lst[i]) :
                    print(file)                    
                    shutil.move(TM[:-1] + '/' + file, out_dir + file)
                    shutil.move(TM[:-1] + '/' + file[:-3] + 'txt', out_dir + file[:-3] + 'txt' )
                    print('done')
        


