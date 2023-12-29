from glob import glob                                                           
import os,shutil
from TOAN import Test

TM = Test.getPath1()
# TM_save = Test.getPath2()
c = 0      
fname = glob(TM + '*.lnk')
# fname = os.listdir(TM)
for filename in fname:
    # tenf = os.path.basename(filename) 
    os.remove(filename)
    # print(tenf)
    # if (str(tenf[0:2])) == 'BC':
    # if (str(tenf[-7:-4])) == '3CD':Shortcut
    # if 'Shortcut' in tenf:
    #     shutil.move(filename , TM_save + tenf)
    #     print(tenf)
    # else:
    #     continue
        # os.remove(filename[:-3] + 'txt')
        # c += 1
        # # os.rename(filename, TM + tenf[2:6] + '-' + tenf[6:8] + '-' + tenf[8:10] + tenf[10:])
        # # os.rename(filename[:-3] + 'txt', TM + tenf[2:6] + '-' + tenf[6:8] + '-' + tenf[8:10] + tenf[10:26] + '.txt')
        # # print(tenf[-14:-8])
        # if os.path.exists(filename):
        #     shutil.move(filename , TM_save + tenf)
        # if os.path.exists(filename[:-3]+'txt'):
        #     shutil.move(filename[:-3]+'txt' , TM_save + tenf[:-3] + 'txt')
        # print(f'{c}_{tenf}') 
        
    # else :
    #     os.remove(filename)
    #     # os.remove(filename[:-3]+'txt')
    #     print(f'{c}_{tenf}') 


