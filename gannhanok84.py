from glob import glob                                                           
import shutil,os
from TOAN import Test
TM = Test.getPath1()        
def CAM1_84_ganok(TM):
    txt = glob(TM + '*.txt')
    try :
        os.mkdir(TM + 'dat')
    except:
        pass
    out_dir = TM + 'dat/'
    cnt = len(txt)
    
    line1 = ['0 0.318750 0.400833 0.172500 0.150000']
    line2 = ['14 0.508125 0.465417 0.875000 0.899167'] # tieu chuan ok

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
                        if int(tmp[0])==0:  
                            tam = str(float(tmp[1]) + float(x2-x1)) + ' ' + str(float(tmp[2]) + float(y2-y1))
                    out.writelines(line) 
                out.writelines('14 ' + tam + ' '+ wh)
                # out.writelines('14 0.508125 0.465417 0.875000 0.899167')
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
def CAM1_84_chia(TM):
    txt1 = glob(TM + '*.txt')
    try :
        os.mkdir(TM + 'dat1')
    except:
        pass
    out_dir1 = TM + 'dat1/'
    cnt1 = len(txt1)
    sd = 4 #so dong
    sc = 4 #so cot
    for filename in txt1:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
            out = open(out_dir1 + tenf,'w')
            i = 14 
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0])==14:
                        w = float(tmp[3])/sc
                        d = float(tmp[4])/sd
                        y = float(tmp[2]) - float(tmp[4])/2 #y_min
                        for r in range(sd):
                            x = float(tmp[1]) - float(tmp[3])/2 #x_min
                            for c in range(sc):
                                line = str(i) + ' ' +  str(x + w/2) + ' ' + str(y + d/2) + ' ' + str(w) + ' ' + str(d) + '\n'
                                out.writelines(line)
                                x += w
                                i +=1
                            y += d
                    else:
                        out.writelines(line) 
        else:
            try :
                shutil.copyfile(filename, out_dir1 + tenf)
            except:
                pass
        f.close() 
        out.close()
        os.replace(out_dir1 + tenf, filename)
        cnt1 -= 1
        print(cnt1)
    shutil.rmtree(out_dir1)
def CAM1_84_thaynhan(TM):
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
                if int(tmp[0])==14:
                    line = '14'+ line[2:]
                if int(tmp[0])==15:
                    line = '18'+ line[2:]
                if int(tmp[0])==16:
                    line = '19'+ line[2:]
                if int(tmp[0])==17 :
                    line = '14'+ line[2:]
                if int(tmp[0])==18:
                    line = '15'+ line[2:]
                if int(tmp[0])==19:
                    line = '20'+ line[2:]
                if int(tmp[0])==20:
                    line = '21'+ line[2:]
                if int(tmp[0])==21:
                    line = '15'+ line[2:]
                if int(tmp[0])==22:
                    line = '16'+ line[2:]
                if int(tmp[0])==23 :
                    line = '22'+ line[2:]
                if int(tmp[0])==24:
                    line = '23'+ line[2:]
                if int(tmp[0])== 25 :
                    line = '16'+ line[2:]
                if int(tmp[0])==26:
                    line = '17'+ line[2:]
                if int(tmp[0])==27 :
                    line = '24'+ line[2:]
                if int(tmp[0])==28:
                    line = '25'+ line[2:]
                if int(tmp[0])== 29 :
                    line = '17'+ line[2:]
                out.writelines(line)
        out.close()
        cnt -= 1
        os.replace(out_dir + tenf, filename)
        print(cnt, tenf)
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
    line1 = ['3 0.540937 0.432917 0.131875 0.130833']
    line2 = ['2 0.695312 0.464167 0.176875 0.135000']
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
                        if int(tmp[0])== 2:
                            tam = str(float(tmp[1]) - float(x2-x1)) + ' ' + str(float(tmp[2]) - float(y2-y1))
                    out.writelines(line) 
                out.writelines('3 ' + tam + ' '+ '0.131875 0.130833\n')
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf)
        f.close()
        out.close()
        # os.replace(out_dir + tenf, filename)
        cnt -= 1
        print(cnt)
    print('compelted')
    # shutil.rmtree(out_dir)
def chiaTC(TM):
    txt1 = glob(TM + '*.txt')
    try :
        os.mkdir(TM + 'dat1')
    except:
        pass
    out_dir1 = TM + 'dat1/'
    cnt1 = len(txt1)
    sd = 3 #so dong
    sc = 4 #so cot
    for filename in txt1:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
            out = open(out_dir1 + tenf,'w')
            i = 6 
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0])==6:
                        w = float(tmp[3])/sc
                        d = float(tmp[4])/sd
                        y = float(tmp[2]) - float(tmp[4])/2 #y_min
                        for r in range(sd):
                            x = float(tmp[1]) - float(tmp[3])/2 #x_min
                            for c in range(sc):
                                line = str(i) + ' ' +  str(x + w/2) + ' ' + str(y + d/2) + ' ' + str(w) + ' ' + str(d) + '\n'
                                out.writelines(line)
                                x += w
                                i +=1
                            y += d
                    else:
                        out.writelines(line) 
        else:
            try :
                shutil.copyfile(filename, out_dir1 + tenf)
            except:
                pass
        f.close() 
        out.close()
        os.replace(out_dir1 + tenf, filename)
        cnt1 -= 1
        print(cnt1)
    shutil.rmtree(out_dir1)
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

        inners = ['4','5','6','7','8','9','10','11','12','13',]
        outers = ['14','15','16','17','18','19','20','21','22','23','24','25']
        # inners =['9']
        # outers =['12']
        # for i in range(14,26):
        #     outers.append(i)
        # for a in range(4,14):
        #     inners.append(a)
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
                            if w0 > 0.3/4 or h0 > 0.3/4:
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
                            if w0 > 0.3/4 or h0 > 0.3/4:
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

# CAM1_84_ganok(TM)
# CAM1_84_chia(TM)
# CAM1_84_thaynhan(TM)
xoanhanok(TM)