from TOAN import Test
from glob import glob                                                           
import os, shutil
folder_path = Test.getPath1()
# def thaynhan(TM):
# TM = 'C:/Users/CCSX009/Desktop/SSS/'
# txt = glob(TM + '*.txt')
# os.makedirs(TM + 'TEMP', exist_ok=True)
# out_dir = TM + 'TEMP/'
# c = len(txt)
# for filename in txt:
#     tenf = os.path.basename(filename)
#     if tenf != 'classes.txt' and tenf != 'lastclasses.txt': 
#         out = open(out_dir + tenf,'w')
#         with open(filename, 'r') as f:
#             while True:
#                 line = f.readline()
#                 if not line:
#                     break
#                 tmp = line.split()
#                 if int(tmp[0])==15:
#                     tmp2 = float(tmp[2]) - (float(tmp[4]) / 2) 
#                     line = '15' + ' ' + str(tmp[1]) + ' ' + str(tmp2) + ' ' + str((tmp[3])) + ' ' + str((tmp[4]) ) + '\n'
#                     out.writelines(line)
#                 elif int(tmp[0])==25:
#                     tmp3 = float(tmp[2]) + (float(tmp[4]) / 2) 
#                     line = '25' + ' ' + str(tmp[1]) + ' ' + str(tmp3) + ' ' + str((tmp[3])) + ' ' + str((tmp[4]) ) + '\n'
#                     out.writelines(line)
#                 else :
#                     out.writelines(line) 
#             out.writelines(line)
#         f.close()
#         out.close()
#         c-=1
#         print('compelted')    


# txt = glob(TM + '*.txt')
# try:
#     os.mkdir(TM + 'TXT')
# except:
#     pass
# out_dir = TM + 'TXT/'
# c = 0
# for filename in txt:
#     tenf = os.path.basename(filename)
#     if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
#         out = open(out_dir + tenf,'w')
#         with open(filename, 'r') as f:
#             cls0 = 0
#             while True:
#                 line = f.readline()
#                 if not line:
#                     break
#                 tmp = line.split()
#                 # if tmp[0] not in ['6','7','8','9','10','11','12','13','14','15','16','17']:
#                 if tmp[0] not in ['8','10','12','18','19','20','21','22','28','30','32']:
#                 # if tmp[0] not in ['6','7','8','9','10','11','12']:
#                 #if tmp[0] in ['0', '1', '3']:
#                 #if tmp[0] not in ['13']:
#                 # if tmp[0] not in ['6']:
#                     out.writelines(line)
#         f.close()
#         out.close()
#         c+=1
#         os.replace(out_dir + tenf, filename)
#         print(c, tenf)
# print('compelted')
# shutil.rmtree(out_dir)          

def gannhanok(folder_path):
    txt = glob(folder_path + '*.txt')
    try :
        os.mkdir(folder_path + 'dat')
    except:
        pass
    out_dir = folder_path + 'dat/'
    cnt = len(txt)
    linelamchuan = ['0 0.520016 0.943604 0.292484 0.112793']
    line1 = ['1 0.544375 0.445417 0.136250 0.132500']
    line2 = ['2 0.700625 0.472083 0.177500 0.142500']
    line3 = ['3 0.469687 0.457083 0.130625 0.142500']
    lamchuan = linelamchuan[0].split()
    k = line1[0].split()
    i = line2[0].split()
    y = line3[0].split()
    xlamchuan = float(lamchuan[1])
    ylamchuan = float(lamchuan[2])
    x1 = float(k[1])
    y1 = float(k[2])
    x2 = float(i[1])
    y2 = float(i[2])
    x3 = float(y[1])
    y3 = float(y[2])
    wh_line1 = k[3]+' '+k[4]+'\n'
    wh_line2 = i[3]+' '+i[4]+'\n'
    wh_line3 = y[3]+' '+y[4]+'\n'
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
            out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0])<6:
                        if int(tmp[0])==0:
                            tam1 = str(float(tmp[1]) - float(xlamchuan-x1)) + ' ' + str(float(tmp[2]) - float(ylamchuan-y1))
                            tam2 = str(float(tmp[1]) - float(xlamchuan-x2)) + ' ' + str(float(tmp[2]) - float(ylamchuan-y2))
                            tam3 = str(float(tmp[1]) - float(xlamchuan-x3)) + ' ' + str(float(tmp[2]) - float(ylamchuan-y3))
                    out.writelines(line) 
                out.writelines('1 ' + tam1 + ' '+ wh_line1 + '2 ' + tam2 + ' ' +  wh_line2 + '3 ' + tam3 + ' ' +  wh_line3) 
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf)
        f.close()
        out.close()
        os.replace(out_dir + tenf, filename)
        cnt -= 1
        print(cnt)
    print('compelted')
    shutil.rmtree(out_dir)

gannhanok(folder_path)