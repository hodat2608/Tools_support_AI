from glob import glob                                                           
import os, shutil
from TOAN import Test

TM = Test.getPath1()

def themnhan(TM):
    txt = glob(TM + '*.txt')
    cnt = len(txt)
    os.makedirs(TM + 'TEMP', exist_ok=True)
    out_dir = TM + 'TEMP/'
    # 0.501271 0.513333 0.955085 0.926667 rs466
    # 0.495000 0.515000 0.950000 0.948333 m100
    for filename in txt:
        tam = '0.495000 0.515000'
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
                    if int(tmp[0]) <= 5:
                        if int(tmp[0]) == 0:
                            tam = tmp[1] + ' ' + tmp[2]
                out.writelines('13 ' + tam + ' 0.950000 0.948333') 
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf)
        f.close()
        out.close()
        os.replace(out_dir + tenf, filename)
        cnt -= 1
        print(cnt)

def chianhan(TM):
    txt = glob(TM + '*.txt')
    os.makedirs(TM + 'TEMP',exist_ok=True)
    out_dir = TM + 'TEMP/'
    cnt = len(txt)
    sd = 5 #so dong
    sc = 5 #so cot
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
            out = open(out_dir + tenf,'w')
            i = j = 6
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0])==13:
                        w = float(tmp[3])/sc
                        d = float(tmp[4])/sd
                        y = float(tmp[2]) - float(tmp[4])/2 #y_min
                        for r in range(sd):
                            x = float(tmp[1]) - float(tmp[3])/2 #x_min
                            for c in range(sc):
                                if i < 16 or i > 20:
                                    line = str(j) + ' ' +  str(x + w/2) + ' ' + str(y + d/2) + ' ' + str(w) + ' ' + str(d) + '\n'
                                    out.writelines(line)
                                x += w
                                i += 1
                                j=i if i<19 else j - 1
                            y += d
                    else:
                        out.writelines(line)
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf)
        f.close() 
        out.close()
        os.replace(out_dir + tenf, filename)
        cnt -= 1
        print(cnt)

def xoanhan(TM):
    txt = glob(TM + '*.txt')
    os.makedirs(TM + 'TEMP', exist_ok=True)
    out_dir = TM + 'TEMP/'
    cnt = len(txt)
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
                    # ['6','7','8','9','10','11','12']
                    if tmp[0] not in ['6','10','13']:                    
                        out.writelines(line)
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf)
        f.close() 
        out.close()
        os.replace(out_dir + tenf, filename)
        cnt -= 1
        print(cnt)

def thaynhan(TM):
    txt = glob(TM + '*.txt')
    os.makedirs(TM + 'TEMP', exist_ok=True)
    out_dir = TM + 'TEMP/'
    cnt = len(txt)
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
                    if int(tmp[0])==7:
                        line = '6'+ line[1:]
                    if int(tmp[0])==8:
                        y=float(tmp[2])
                        y = y + (float(tmp[4])/2) if y < 0.5 else y - (float(tmp[4])/2)
                        line = '7 ' + tmp[1] + ' ' + str(y) + ' ' + tmp[3] + ' ' + tmp[4] + '\n'
                    if int(tmp[0])==9:
                        line = '8'+ line[1:]
                    if int(tmp[0])==11:
                        line = '9'+ line[2:]
                    if int(tmp[0])==12:
                        line = '10'+ line[2:]
                    if int(tmp[0])==14:
                        line = '11'+ line[2:]
                    if int(tmp[0])==15:
                        line = '12'+ line[2:]
                    out.writelines(line)
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf)        
        f.close() 
        out.close()
        os.replace(out_dir + tenf, filename)
        cnt -= 1
        print(cnt)
    shutil.rmtree(out_dir)
def thaynhan1(TM):     
    txt = glob(TM + '*.txt')
    try :
        os.makedirs(TM + 'TEMP', exist_ok=True)
    except :
        pass 
    out_dir = TM + 'TEMP/'
    cnt = len(txt)
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
                    if int(tmp[0])==12:
                        line = '5'+ line[2:]
                    out.writelines(line)
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf) 
        out.close()
        os.replace(out_dir + tenf, filename) 
        cnt -= 1
        print(cnt)
    print('compelted')
    shutil.rmtree(out_dir)

def thaynhan2(TM):       
    txt = glob(TM + '*.txt')
    try:
        os.mkdir(TM + 'TXT')
    except :
        pass
    out_dir = TM + 'TXT/'
    cnt = len(txt)
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
                    if int(tmp[0]) == 5:
                        if float(tmp[3]) > 0.13 and float(tmp[4]) > 0.16 :
                            line = '6'+ line[1:]    
                    if int(tmp[0])==6:
                        line = '7'+ line[1:]
                    if int(tmp[0])==7:
                        line = '8'+ line[1:]
                    if int(tmp[0])==8:
                        line = '9'+ line[1:]
                    if int(tmp[0])==9:
                        line = '10'+ line[1:]
                    if int(tmp[0])==10:
                        line = '11'+ line[2:]      
                    if int(tmp[0])==11:
                        line = '12'+ line[2:]          
                    out.writelines(line)
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf) 
        out.close()
        cnt -= 1
        os.replace(out_dir + tenf, filename)
        print(cnt)
    print('compelted')
    shutil.rmtree(out_dir)
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
                  
        outers = ['6','7','8','9','10','11','12'] #NHAN OK CAM1
        inners = ['1','2','5'] 
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
                            if w0 > 0.242375/4 or h0 > 0.2796666/4:
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
                            #bui chi 0.142375 0.1896666
                            #divat 0.025000 0.033333
                            if w0 > 0.242375/4 or h0 > 0.2796666/4:
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
chianhan(TM)
xoanhan(TM)
thaynhan(TM)
xoanhanok(TM)
