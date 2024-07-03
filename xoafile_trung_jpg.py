from glob import glob                                                           
import os
import shutil
from TOAN import Test

TM_goc= Test.getPath()  
txt_goc = glob(TM_goc + '*.jpg')

TM_trung = Test.getPath1()  
txt_trung = glob(TM_trung + '*.jpg')

TM_SAVE = Test.getPath2()  
c = 0
for filename in txt_trung:
    tenf = os.path.basename(filename)
    # print(TM_goc + tenf[:-7] + '.jpg')
    if os.path.exists(TM_goc + tenf) :
        c+=1
        if os.path.exists(filename):
            shutil.move(filename, TM_SAVE + tenf ) 
        if os.path.exists(filename[:-3]):
            shutil.move(filename[:-3]+ 'txt' , TM_SAVE + tenf[:-3] + 'txt')
        print(c, 'da xoa' , tenf) 
    else:
        print('threr is no file...')
        break





