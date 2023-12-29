from glob import glob                                                           
import os,shutil
from TOAN import Test

TM = Test.getPath1() 
def thaynhan_84(TM):
    txt = glob(TM + '*.txt')
    os.mkdir(TM + 'TXT11')
    out_dir = TM + 'TXT11/'
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
                if int(tmp[0])==10:
                    line = '9' + line[2:]
                if int(tmp[0])==11:
                    line = '10' + line[2:]
                if int(tmp[0])==12:
                    line = '11' + line[2:]
                if int(tmp[0])==13:
                    line = '12' + line[2:]
                out.writelines(line)
        out.close()
        cnt -= 1
        os.replace(out_dir + tenf, filename)
        print(cnt, tenf)
    print('compelted')
    shutil.rmtree(out_dir)

# def timnhan_55(TM):
#     txt = glob(TM + '*.txt')  
#     cnt = len(txt)
#     for filename in txt:
#         tenf = os.path.basename(filename)   
#         with open(filename, 'r') as f:
#             while True:
#                 line = f.readline()
#                 if not line:
#                     break
#                 tmp = line.split()               
#                 if int(tmp[0])==9:
#                     if float(tmp[1]) > 0.5 :
#                         print('sai nhan so 1', tenf)
#                 if int(tmp[0])==10:
#                     if float(tmp[1]) < 0.5 :
#                         print('sai nhan so 2', tenf)
#         # cnt -= 1        
        # print(cnt, tenf)
    # print('compelted')

# timnhan_55(TM)
thaynhan_84(TM)