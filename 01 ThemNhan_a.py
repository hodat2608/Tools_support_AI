from glob import glob                                                           
import os,shutil
from TOAN import Test
# TM = Test.getPath1()
# txt = glob(TM + '*.txt')
# cnt = len(txt)
# os.makedirs(TM + 'TEMP', exist_ok=True)
# out_dir = TM + 'TEMP/'
# for filename in txt:
#     tam = '0.490000 0.481667'
#     tenf = os.path.basename(filename)
#     out = open(out_dir + tenf,'w')
#     with open(filename, 'r') as f:
#         while True:
#             line = f.readline()
#             out.writelines(line)
#             if not line:
#                 break
#             tmp = line.split()
#             print(tmp[0])
#             if int(tmp[0]) == 0:
#                 tam = tmp[1] + ' ' + tmp[2]
#         out.writelines('9 ' + tam + ' 0.721875 0.959167') 
#     f.close()
#     out.close()
#     os.replace(out_dir + tenf, filename)
#     cnt -= 1
#     print(cnt)
# shutil.rmtree(out_dir)

TM = Test.getPath1()

def themnhan(TM):
    txt = glob(TM + '*.txt')
    cnt = len(txt)
    os.makedirs(TM + 'TEMP', exist_ok=True)
    out_dir = TM + 'TEMP/'
    for filename in txt:
        tam = '0.490000 0.481667'
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
            out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    out.writelines(line)
                    if not line:
                        break
                    tmp = line.split()
                    print(tmp)
                    if int(tmp[0]) == 0:
                        tam = tmp[1] + ' ' + tmp[2]
                out.writelines('9 ' + tam + ' 0.721875 0.959167') 
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf)
        f.close()
        out.close()
        os.replace(out_dir + tenf, filename)
        cnt -= 1
        print(cnt)

def xoanhanok(TM):
    path = TM  + '*.txt'
    cnt = 0
    import glob 
    for i in glob.glob(path):
        tenf = os.path.basename(i)
        if tenf == 'classes.txt' and tenf == 'lastclasses.txt':
            continue
        file = open(i, 'r')
        Lines = file.readlines()
        names = []
        files = []
        for line in Lines:
            num = line.split()[0]
            names.append(num)
                  
        outers = ['9']
        inners = ['1','2','5'] 
        w = 1
        h = 1
        for inner in inners: 
            for outer in outers:
                if inner in names and outer in names:
                    for index,line in enumerate(Lines):      
                        if line.strip().split()[0] == outer:
                            myindex =0
                            x4 = float(line.strip().split()[1])
                            y4 = float(line.strip().split()[2])
                            w4 = float(line.strip().split()[3])
                            h4 = float(line.strip().split()[4])
                            xmin = x4 - w4/2
                            xmax = x4 + w4/2
                            ymin = y4 - h4/2
                            ymax = y4 + h4/2
                            myindex = index 
                            #print(myindex)
                            break
                    for line in Lines:   
                        if line.strip().split()[0] == inner:
                            x0 = float(line.strip().split()[1])
                            y0 = float(line.strip().split()[2])
                            w0 = float(line.strip().split()[3])
                            h0 = float(line.strip().split()[4])
                            #bui chi 0.013750 0.018333
                            #divat 0.025000 0.033333
                            if w0 > float(w) or h0 > float(h):
                                if xmin < x0 < xmax  and ymin < y0 < ymax:
                                    for index,line in enumerate(Lines):  
                                        if line.strip().split()[0] == outer and index == myindex:
                                            files.append(line)
                    with open(i, 'w') as f:
                        for line in Lines:
                            if line not in files:
                                #print('HAHA')
                                f.write(line)
                            else:
                                cnt += 1 
                                print(cnt)

                if inner in names and outer in names:
                    for index,line in enumerate(Lines):      
                        if line.strip().split()[0] == outer:
                            myindex =0
                            x4 = float(line.strip().split()[1])
                            y4 = float(line.strip().split()[2])
                            w4 = float(line.strip().split()[3])
                            h4 = float(line.strip().split()[4])
                            xmin = x4 - w4/2
                            xmax = x4 + w4/2
                            ymin = y4 - h4/2
                            ymax = y4 + h4/2
                            myindex = index 
                            #print(myindex)
            
                    for line in Lines:   
                        if line.strip().split()[0] == inner:
                            x0 = float(line.strip().split()[1])
                            y0 = float(line.strip().split()[2])

                            w0 = float(line.strip().split()[3])
                            h0 = float(line.strip().split()[4])
                            if w0 > float(w) or h0 > float(h):
                                if xmin < x0 < xmax  and ymin < y0 < ymax:
                                    for index,line in enumerate(Lines):  
                                        if line.strip().split()[0] == outer and index == myindex:
                                            files.append(line)
                    with open(i, 'w') as f:
                        for line in Lines:
                            if line not in files:
                                #print('HAHA')
                                f.write(line)
                            else:
                                cnt += 1 
                                print(cnt) 


themnhan(TM)
xoanhanok(TM)