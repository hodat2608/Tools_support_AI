from glob import glob                                                           
import os,shutil
from TOAN import Test

TM= Test.getPath1()          
txt = glob(TM + '*.txt')
TM_SAVE = Test.getPath3()  
cnt = len(txt)
for filename in txt:
    tenf = os.path.basename(filename)
    out = open(TM_SAVE + tenf,'w')
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            if int(tmp[0])== 1 :
                if float(tmp[3]) <=  0.013125:
                    cnt-=1
                    shutil.copy(filename, TM_SAVE + tenf ) 
                    shutil.copy(filename[:-3]+ 'jpg' , TM_SAVE + tenf[:-3] + 'jpg')
                    print(cnt,tenf) 
