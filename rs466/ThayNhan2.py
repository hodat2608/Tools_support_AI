from glob import glob                                                           
import os,shutil
from TOAN import Test

TM = Test.getPath1()  
def thaynhan(TM):     
    txt = glob(TM + '*.txt')
    try :
        os.makedirs(TM + 'TEMP', exist_ok=True)
    except :
        pass 
    out_dir = TM + 'TEMP/'
    cnt = len(txt)
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt':
            out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0])==5:
                        line = '6'+ line[1:]
                    out.writelines(line)
            out.close()
            os.replace(out_dir + tenf, filename) 
            cnt -= 1
            print(cnt, '-', tenf)
    print('compelted')
    shutil.rmtree(out_dir)

def thaynhan1(TM):       
    txt = glob(TM + '*.txt')
    try:
        os.mkdir(TM + 'TXT')
    except :
        pass
    out_dir = TM + 'TXT/'
    cnt = len(txt)
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt':
            out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0])==6:
                        line = '8'+ line[1:]
                    if int(tmp[0])==7:
                        line = '9'+ line[1:]
                    if int(tmp[0])==8:
                        line = '10'+ line[1:]
                    if int(tmp[0])==9:
                        line = '11'+ line[1:]
                    if int(tmp[0])==10:
                        line = '12'+ line[2:]      
                    if int(tmp[0])==11:
                        line = '13'+ line[2:] 
                    if int(tmp[0])==12:
                        line = '14'+ line[2:]         
                    out.writelines(line)
            out.close()
            cnt -= 1
            os.replace(out_dir + tenf, filename)
            print(cnt ,'-', tenf )
    print('compelted')
    shutil.rmtree(out_dir)

thaynhan(TM)
#thaynhan1(TM)
