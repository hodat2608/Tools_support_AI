from glob import glob                                                           
import shutil,os
from TOAN import Test

# def loc_kim(folder_path):
#     try :
#         os.mkdir(folder_path + 'kim')
#         os.mkdir(folder_path + 'ko_kim')
#     except:
#             pass
#     out_dir1 = folder_path + 'kim/'
#     out_dir2 = folder_path + 'ko_kim/'
#     all_files = os.listdir(folder_path)
#     file_list = [file_name for file_name in all_files if file_name.endswith(".jpg")]
#     for index, file_name in enumerate(file_list, start=0):
#         if file_name.endswith(".jpg"):
#             if int(index) % 2 == 0: 
#                 shutil.move(folder_path+file_name,out_dir1+file_name)
#             else:
#                 shutil.move(folder_path+file_name,out_dir2+file_name)

folder_path = Test.getPath1()
def them_nhan(folder_path):
    try :
        os.mkdir(folder_path + 'dat')
    except:
            pass
    out_dir = folder_path + 'dat/'
    all_files = os.listdir(folder_path)
    file_list = [file_name for file_name in all_files if file_name.endswith(".txt")]
    for index, file_name in enumerate(file_list, start=0):
        if file_name.endswith(".txt"):
            if int(index) % 2 == 0: 
                out = open(out_dir + file_name,'w')
                with open(folder_path + file_name, 'r') as f:
                    while True:
                        line = f.readline()
                        if not line:
                            break
                        out.writelines(line) 
                    out.writelines('3 0.946078 0.698242 0.107843 0.283203')
            else :
                continue 
        f.close()
        out.close()
        os.replace(out_dir + file_name, folder_path + file_name)
    print('compelted')
    shutil.rmtree(out_dir)
            

def gannhanok(folder_path):
    txt = glob(folder_path + '*.txt')
    try :
        os.mkdir(folder_path + 'dat')
    except:
        pass
    out_dir = folder_path + 'dat/'
    cnt = len(txt)
    line1 = ['2 0.504902 0.286621 0.977124 0.549805']
    line2 = ['3 0.510621 0.722168 0.802288 0.321289']
    line3 = ['0 0.520016 0.943604 0.292484 0.112793']
    i = line1[0].split()
    y = line2[0].split()
    j = line3[0].split()

    x1 = float(i[1])
    y1 = float(i[2])
    x2 = float(y[1])
    y2 = float(y[2])
    x3 = float(j[1])
    y3 = float(j[2])
    wh1 = y[3]+' '+y[4]+'\n'
    wh2 = i[3]+' '+i[4]+'\n'
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
                            tam1 = str(float(tmp[1]) - float(x3-x1)) + ' ' + str(float(tmp[2]) - float(y3-y1))
                            tam2 = str(float(tmp[1]) - float(x3-x2)) + ' ' + str(float(tmp[2]) - float(y3-y2))
                    out.writelines(line) 
                out.writelines('6 ' + tam1 + ' '+ wh2 + '7 ' + tam2 + ' ' +  wh1) 
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

def chia_nhan_ok(folder_path):
    txt1 = glob(folder_path + '*.txt')
    try :
        os.mkdir(folder_path + 'dat1')
    except:
        pass
    out_dir1 = folder_path + 'dat1/'
    cnt1 = len(txt1)
    sd = 2 #so dong
    sc = 3 #so cot
    sd_ok2 = 1
    sc_ok2 = 3
    for filename in txt1:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
            out = open(out_dir1 + tenf,'w')       
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    
                    if int(tmp[0])==6:
                        i = 6
                        w = float(tmp[3])/sc
                        d = float(tmp[4])/sd
                        y = float(tmp[2]) - float(tmp[4])/2 #y_min
                        for r in range(sd):
                            x = float(tmp[1]) - float(tmp[3])/2 #x_min
                            for c in range(sc):
                                line = str(i) + ' ' +  str(x + w/2) + ' ' + str(y + d/2) + ' ' + str(w) + ' ' + str(d) + '\n'
                                out.writelines(line)
                                x += w
                                i += 1                                
                            y += d
                    elif int(tmp[0])==7:
                        i = 12
                        w = float(tmp[3])/sc_ok2
                        d = float(tmp[4])/sd_ok2
                        y = float(tmp[2]) - float(tmp[4])/2 #y_min
                        for r in range(sd_ok2):
                            x = float(tmp[1]) - float(tmp[3])/2 #x_min
                            for c in range(sc_ok2):
                                line = str(i) + ' ' +  str(x + w/2) + ' ' + str(y + d/2) + ' ' + str(w) + ' ' + str(d) + '\n'
                                out.writelines(line)
                                x += w
                                i += 1                                
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

def thay_nhan_doi_xung(folder_path):
    txt = glob(folder_path + '*.txt')
    os.mkdir(folder_path + 'TXT')
    out_dir = folder_path + 'TXT/'
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
                if int(tmp[0])==7:
                    line = '9'+ line[1:]
                if int(tmp[0])==8:
                    line = '6'+ line[1:]
                if int(tmp[0])== 9 :
                    line = '7'+ line[1:]
                if int(tmp[0])==10:
                    line = '10'+ line[2:]
                if int(tmp[0])== 11 :
                    line = '7'+ line[2:]
                if int(tmp[0])== 12 :
                    line = '8'+ line[2:]
                if int(tmp[0])== 13 :
                    line = '11'+ line[2:]
                if int(tmp[0])== 14 :
                    line = '8'+ line[2:]
                out.writelines(line)
            
        out.close()
        cnt -= 1
        os.replace(out_dir + tenf, filename)
        print(cnt, tenf)
    print('compelted')
    shutil.rmtree(out_dir)

def thaynhan1(folder_path):
    txt = glob(folder_path + '*.txt')
    os.mkdir(folder_path + 'TXT')
    out_dir = folder_path + 'TXT/'
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
                if int(tmp[0])==6:
                    line = '5'+ line[1:]
                if int(tmp[0])== 7 :
                    line = '6'+ line[1:]
                if int(tmp[0])==8:
                    line = '7'+ line[1:]
                if int(tmp[0])== 9 :
                    line = '8'+ line[1:]
                if int(tmp[0])==10:
                    line = '9'+ line[2:]
                if int(tmp[0])==11 :
                    line = '10'+ line[2:]
                out.writelines(line)
        out.close()
        cnt -= 1
        os.replace(out_dir + tenf, filename)
        print(cnt, tenf)
    print('compelted')
    shutil.rmtree(out_dir)

def xoanhanok(folder_path):
    path = folder_path  + '*.txt'
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
                  
        outers = ['5','6','7','8','9','10',]
        inners = ['1','2','3','4']
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
                            if w0 > 0.242375/4 or h0 > 0.2796666/4:
                                if xmin < x0 < xmax  and ymin < y0 < ymax:
                                    for index,line in enumerate(Lines):  
                                        if line.strip().split()[0] == outer and index == myindex:
                                            files.append(line)
                    with open(i, 'w') as f:
                        for line in Lines:
                            if line not in files:
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
            
                    for line in Lines:   
                        if line.strip().split()[0] == inner:
                            x0 = float(line.strip().split()[1])
                            y0 = float(line.strip().split()[2])

                            w0 = float(line.strip().split()[3])
                            h0 = float(line.strip().split()[4])
                            if w0 > 0.242375/4 or h0 > 0.2796666/4:
                                if xmin < x0 < xmax  and ymin < y0 < ymax:
                                    for index,line in enumerate(Lines):  
                                        if line.strip().split()[0] == outer and index == myindex:
                                            files.append(line)
                    with open(i, 'w') as f:
                        for line in Lines:
                            if line not in files:
                                f.write(line)
                            else:
                                cnt += 1 
                                print(cnt)    


gannhanok(folder_path)
chia_nhan_ok(folder_path)
thay_nhan_doi_xung(folder_path)
thaynhan1(folder_path)
xoanhanok(folder_path)