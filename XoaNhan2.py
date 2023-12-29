# from glob import glob                                                           
# import os
# TM = 'E:/02.RS4F5_X75_NQVNHC/DE_TRANG/CAMERA1/FILE_LABEL/DA_XEM/'         
# txt = glob(TM + '*.txt')
# os.makedirs(TM + 'TEMP', exist_ok=True)
# out_dir = TM + 'TEMP/'
# cnt = len(txt)
# for filename in txt:
#     tenf = os.path.basename(filename)
#     out = open(out_dir + tenf,'w')
#     with open(filename, 'r') as f:
#         while True:
#             line = f.readline()
#             if not line:
#                 break
#             tmp = line.split()
            
#             if tmp[0] not in ['6','7','8','9','10','11','12']:
#             # if int(tmp[0]) < 6:
#                 out.writelines(line)
#     f.close() 
#     out.close()
#     #Thay the file
#     os.replace(out_dir + tenf, filename)
#     cnt -= 1
#     print(cnt)

from glob import glob                                                           
import os,shutil
from TOAN import Test
TM = Test.getPath1()        
txt = glob(TM + '*.txt')
save_path = Test.getPath2()
c = len(txt)
lines_to_delete = []
for filename in txt:
    tenf = os.path.basename(filename)
    out = open(save_path + tenf,'w')
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            if tenf == 'classes.txt':
                continue 
            if int(tmp[0]) != 6 :
                out.writelines(line)
            else:
                out.writelines(line)




                        
