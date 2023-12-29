from glob import glob                                                           
import os,shutil
from TOAN import Test

TM = Test.getPath1()       
txt = glob(TM + '*.txt')
os.mkdir(TM + 'TXT')
out_dir = TM + 'TXT/'
cnt = len(txt)
for filename in txt:
    tenf = os.path.basename(filename)
    out = open(out_dir + tenf,'w')
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            if int(tmp[0])==1:
                line = '3'+ line[1:]
            if int(tmp[0])== 3 :
                line = '1'+ line[1:]
            if int(tmp[0])==2:
                line = '7'+ line[1:]
            if int(tmp[0])==4:
                line = '2'+ line[1:]
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
    print(cnt, tenf)
print('compelted')
shutil.rmtree(out_dir)
