from glob import glob                                                           
import os
import shutil
from TOAN import Test
import re
TM = Test.getPath1()    
txt = glob(TM + '*.txt')
try:
    os.mkdir(TM + 'TXT')
except :
    pass
out_dir = TM + 'TXT/'
out_dir1 = TM + 'TXT/*.jpg'
c = 0
def file1(out_dir,c,txt):
    for filename in txt:
        tenf = os.path.basename(filename)
        delimiters = '_','-','.'
        split_string = re.split('|'.join(map(re.escape, delimiters)), tenf)
        if set(['C1']).issubset(set(split_string)):
            c +=1
            if os.path.exists(filename):
                shutil.move(filename , out_dir + tenf)
            if os.path.exists(filename[:-3]+'jpg'):
                shutil.move(filename[:-3]+'jpg' , out_dir + tenf[:-3] + 'jpg')
                print(f'{c}_{tenf}')   
        else :
            continue
def file2(out_dir1,TM,c):
    for filename in glob(out_dir1):
        tenf = os.path.basename(filename)
        if os.path.exists(TM + tenf[:-7] + '.jpg' ) :
            c+=1
            os.remove(filename) 
            os.remove(filename[:-3]+ '.txt')
            print(c, 'da xoa' , tenf) 
        else:
            print('threr is no file...')
            break


# file1(out_dir,c,txt)
file2(out_dir1,TM,c)
   
