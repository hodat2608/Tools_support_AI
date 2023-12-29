from glob import glob
import os
import shutil
from TOAN import Test


TM = Test.getPath1() 
txt = glob(TM + '*.txt')
cnt = len(txt)
# os.mkdir(TM +'loc 1 nhan choi')
# outdir = TM +'loc 1 nhan choi/'
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
            if int(tmp[0]) == 10:
                # if float(tmp[1]) < 0.5:
                #     print(tenf)
                a.append(tmp[0])   
            # out.writelines(line)
            c = a.count('10')     
    if c == 2 :
        # if float(tmp[1]) < 0.5:
        #     out.writelines('1 0.513892 0.900596 0.184416 0.08221/n')
        # else : 
        #     out.writelines('1 0.497228 0.103369 0.18648 0.084005/n')
        print(tenf)
    a = []
              
