from glob import glob                                                           
import os,shutil
from TOAN import Test

TM = Test.getPath1()  
# def thaynhan(TM):     
#     txt = glob(TM + '*.txt')
#     try :
#         os.makedirs(TM + 'TEMP', exist_ok=True)
#     except :
#         pass 
#     out_dir = TM + 'TEMP/'
#     cnt = len(txt)
#     for filename in txt:
#         tenf = os.path.basename(filename)
#         if tenf != 'classes.txt':
#             out = open(out_dir + tenf,'w')
#             with open(filename, 'r') as f:
#                 while True:
#                     line = f.readline()
#                     if not line:
#                         break
#                     tmp = line.split()
#                     if int(tmp[0])== 1: 
#                         line = tmp[0] + ' ' + tmp[1]+ ' ' + tmp[2]+ ' 0.231250 0.161667\n'
#                         #line = tmp[0] + ' ' + tmp[1]+ ' ' + str(float(tmp[2])- 0.015) + ' ' + tmp[3] + ' '+ tmp[4]+'\n'
#                     out.writelines(line)
#                 out.writelines(line)
#             out.close()
#             os.replace(out_dir + tenf, filename) 
#             cnt -= 1
#             print(cnt, '-', tenf)
#     print('compelted')
#     shutil.rmtree(out_dir)

# def thaynhan1(TM):       
#     txt = glob(TM + '*.txt')
#     try:
#         os.mkdir(TM + 'TXT')
#     except :
#         pass
#     out_dir = TM + 'TXT/'
#     cnt = len(txt)
#     for filename in txt:
#         tenf = os.path.basename(filename)
#         if tenf != 'classes.txt':
#             out = open(out_dir + tenf,'w')
#             with open(filename, 'r') as f:
#                 while True:
#                     line = f.readline()
#                     if not line:
#                         break
#                     tmp = line.split()
#                     if int(tmp[0]) == 5:
#                         if float(tmp[3]) > 0.21 and float(tmp[4]) > 0.21 :
#                             line = '6'+ line[1:]    
#                     if int(tmp[0])==6:
#                         line = '7'+ line[1:]
#                     if int(tmp[0])==7:
#                         line = '8'+ line[1:]
#                     if int(tmp[0])==8:
#                         line = '9'+ line[1:]
#                     if int(tmp[0])==9:
#                         line = '10'+ line[1:]
#                     if int(tmp[0])==10:
#                         line = '11'+ line[2:]      
#                     if int(tmp[0])==11:
#                         line = '12'+ line[2:] 
#                     if int(tmp[0])==12:
#                         line = '13'+ line[2:]      
#                     if int(tmp[0])==13:
#                         line = '14'+ line[2:]      
#                     if int(tmp[0])==14:
#                         line = '15'+ line[2:]      
#                     if int(tmp[0])==15:
#                         line = '16'+ line[2:]    
#                     if int(tmp[0])==16:
#                         line = '17'+ line[2:]    
#                     out.writelines(line)
#             out.close()
#             cnt -= 1
#             os.replace(out_dir + tenf, filename)
#             print(cnt ,'-', tenf )
#     print('compelted')
#     shutil.rmtree(out_dir)

# thaynhan(TM)
# #thaynhan1(TM)

def line90(TM):     
    txt = glob(TM + '*.txt')
    try :
        os.makedirs(TM + 'TEMP', exist_ok=True)
    except :
        pass 
    out_dir = TM + 'TEMP/'
    cnt = len(txt)
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt':
            out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()                  
                    # try:                                     
                    #     if int(tmp[0])==6: 
                    #         # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==7: 
                    #         # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==8: 
                    #     # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==9: 
                    #         # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==10: 
                    #         # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==11: 
                    #         # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==12: 
                    #         # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==13: 
                    #         # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==14: 
                    #         # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==15: 
                    #     # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==16: 
                    #         # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     if int(tmp[0])==17: 
                    #         # if float(tmp[2]) < 0.5:
                    #         line = str(tmp[0]) + ' ' + str(float(tmp[1]) + 0.014375 ) + ' ' + str(float(tmp[2]) - 0.01333) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    # except :
                    #     pass
                        # else:
                        #     line = str(tmp[0]) + ' ' + str(float(tmp[1])+ 0.004)+ ' ' + str(float(tmp[2]) - 0.004) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    if int(tmp[0])== 1: #taychoi
                        line = tmp[0] + ' ' + str(float(tmp[1]))+ ' ' + str(float(tmp[2]))+ ' '+'0.182500 0.080000\n'
                    # if int(tmp[0])== 2: #chaudien 
                    #     line = tmp[0] + ' ' + str(float(tmp[1]))+ ' ' + str(float(tmp[2]))+ ' '+'0.117500 0.175833\n'
                    # if int(tmp[0])== 8: 
                    #     if float(tmp[1]) > 0.5 :         
                    #         line = tmp[0] + ' ' + str(float(tmp[1]))+ ' ' + str(float(tmp[2]) + 0.015) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                    #     else : 
                    #         line = tmp[0] + ' ' + str(float(tmp[1]))+ ' ' + str(float(tmp[2]) - 0.015) +  ' ' + str(tmp[3]) + ' ' + str(tmp[4]) + '\n'
                        # print(line)
                    out.writelines(line)
                out.writelines(line)
            out.close()
            os.replace(out_dir + tenf, filename) 
            cnt -= 1
            print(cnt, '-', tenf)
    print('compelted')

    shutil.rmtree(out_dir)

def ganokTC(TM):
    txt = glob(TM + '*.txt')
    try :
        os.mkdir(TM + 'dat')
    except:
        pass
    out_dir = TM + 'dat/'
    cnt = len(txt)
    line1 = ['0 0.538125 0.451250 0.132500 0.132500']
    line2 = ['6 0.692813 0.473333 0.176875 0.126667']
    i = line1[0].split()
    y = line2[0].split()
    x1 = float(i[1])
    y1 = float(i[2])
    x2 = float(y[1])
    y2 = float(y[2])
    wh = y[3]+' '+y[4]+'\n'

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
                        if int(tmp[0])==2:
                            tam = str(float(tmp[1]) - float(x2-x1)) + ' ' + str(float(tmp[2]) - float(y2-y1))
                    out.writelines(line) 
                out.writelines('3 ' + tam + ' '+ '0.132500 0.132500\n')
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

line90(TM)

# ganokTC(TM)