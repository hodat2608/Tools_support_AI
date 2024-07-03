from glob import glob                                                           
import os,shutil
from TOAN import Test

TM = Test.getPath() 
def thaynhan_84(TM):
    txt = glob(TM + '*.txt')
    os.makedirs(TM + 'txt', exist_ok=True)
    out_dir = TM + 'txt/'
    cnt = len(txt)
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf == 'classes.txt':
            pass
        out = open(out_dir + tenf,'w')
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                tmp = line.split()
                if int(tmp[0])==2:
                    if float(tmp[3]) > 0.024718 :#35px
                        line = '8' + line[1:]
                out.writelines(line)
        out.close()
        cnt -= 1
        os.replace(out_dir + tenf, filename)
        print(cnt, tenf)
    print('compelted')
    shutil.rmtree(out_dir)

thaynhan_84(TM)