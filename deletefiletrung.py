from glob import glob                                                           
import os
import shutil
from TOAN import Test


TM_khong_xoa= Test.getPath()  
txt_goc_TM_khong_xoa = glob(TM_khong_xoa + '*.jpg')

TM_phai_xoa= Test.getPath1()  
txt_TM_phai_xoa = glob(TM_phai_xoa + '*.jpg')

out_dir = Test.getPath2()  
c = 0
for filename in txt_goc_TM_khong_xoa:
    tenf = os.path.basename(filename)
    if os.path.exists(TM_phai_xoa + tenf):
        shutil.move(TM_phai_xoa + tenf , out_dir + tenf)
        if os.path.exists(TM_phai_xoa + tenf[:-3]+'txt'):
            shutil.move(TM_phai_xoa + tenf[:-3]+'txt' , out_dir + tenf[:-3] + 'txt')
    else:
        continue
