from glob import glob
import os
import shutil
from TOAN import Test


TM = Test.getPath() 
txt = glob(TM + '*.txt')
cnt = len(txt)
os.mkdir(TM +'loc 1 nhan choi')
outdir = TM +'loc 1 nhan choi/'
a = []
for filename in txt:           
    tenf = os.path.basename(filename)
    # out = open(outdir + tenf,'w')
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break        
            tmp = line.split()
            if int(tmp[0]) == 11:
                a.append(tmp[0])   
            c = a.count('11')     
    if c == 2:
        print('good')
    else:
        shutil.move(filename , outdir + tenf)
        shutil.move(filename[:-3]+'jpg' , outdir + tenf[:-3] + 'jpg')
        print(tenf)
    a = []
              
