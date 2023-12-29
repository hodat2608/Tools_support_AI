from glob import glob                                                           
import os,shutil
from TOAN import Test

TM = Test.getPath1()    
txt = glob(TM + '*.txt')
try:
    os.mkdir(TM + 'TXT')
except:
    pass
out_dir = TM + 'TXT/'
cnt = len(txt)
a = 0
b=[]
for filename in txt:
    tenf = os.path.basename(filename)
    out = open(out_dir + tenf,'w')
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            if int(tmp[0]) == 2 :
                b.append(line)
            out.writelines(line) 
            
        if len(b) == 1 :
            c = b[0]
            cac_so = c.split()
            if float(cac_so[1]) > 0.5:
                a = 1
            else :
                a = 2    
    if a == 1:
        out.writelines('2 0.135833 0.507917 0.115000 0.167500\n')   
    if a == 2 : 
        out.writelines('2 0.886250 0.497917 0.117500 0.169167\n')
    b =[]
    a =0 
    out.close()
    # os.replace(out_dir + tenf, filename) 
    cnt -= 1
    print(cnt, '-', tenf)
    print('compelted')

# shutil.rmtree(out_dir)