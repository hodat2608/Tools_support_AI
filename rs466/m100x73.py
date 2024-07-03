from glob import glob                                                           
import shutil,os
import PySimpleGUI as sg
from TOAN import Test

layout = [
    [sg.Text('Chọn một trong hai tùy chọn:')],
    [sg.Radio('CÓ PTC         ', 'RADIO1', default=True), sg.Radio('KHÔNG CÓ PTC', 'RADIO1')],
    [sg.Text('')],
    [sg.Button('OK')]
]

window = sg.Window('Chọn tùy chọn', layout, size= (300,200))

class YS_PTC:
    def ganok(TM):
        txt = glob(TM + '*.txt')
        cnt = len(txt)
        os.makedirs(TM + 'TEMP', exist_ok=True)
        out_dir = TM + 'TEMP/'
        # 0.501271 0.513333 0.955085 0.926667 rs466
        # 0.495000 0.515000 0.950000 0.948333 m100
        for filename in txt:
            tam = '0.501271 0.513333'
            tenf = os.path.basename(filename)
            if tenf != 'classes.txt':
                out = open(out_dir + tenf,'w')
                with open(filename, 'r') as f:
                    while True:
                        line = f.readline()
                        out.writelines(line)
                        if not line:
                            break
                        tmp = line.split()
                        if int(tmp[0]) <= 9:
                            if int(tmp[0]) == 0:
                                tam = tmp[1] + ' ' + tmp[2]
                    out.writelines('10 ' + tam + ' 0.955085 0.935000') 
                f.close()
                out.close()
                os.replace(out_dir + tenf, filename)
                cnt -= 1
                print(cnt)
            else:
                try :
                    shutil.copyfile(filename, out_dir + tenf)
                except:
                    pass
        shutil.rmtree(out_dir) 
        print('completed')
    def chia(TM):
        sd = 5 
        sc = 5 
        txt1 = glob(TM + '*.txt')
        try :
            os.mkdir(TM + 'dat1')
        except:
            pass
        out_dir = TM + 'dat1/'
        cnt1 = len(txt1)
        for filename in txt1:
            tenf = os.path.basename(filename)
            if tenf != 'classes.txt':
                out = open(out_dir + tenf,'w')
                i=10
                with open(filename, 'r') as f:
                    while True:
                        line = f.readline()
                        if not line:
                            break
                        tmp = line.split()
                        if int(tmp[0])==10:
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
                f.close() 
                out.close()
                os.replace(out_dir + tenf, filename)
                cnt1 -= 1
                print(cnt1)
            else:
                try :
                    shutil.copyfile(filename, out_dir + tenf)
                except:
                    pass
        shutil.rmtree(out_dir)
        print('completed')
    def xoanhanok(TM):
        txt = glob(TM + '*.txt')
        try:
            os.mkdir(TM + 'TXT')
        except:
            pass
        out_dir = TM + 'TXT/'
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
                        if tmp[0] not in ['10','12','14','20','21','22','23','24','30','32','34']:
                            out.writelines(line)
                f.close()
                out.close()
                cnt-=1
                os.replace(out_dir + tenf, filename)
                print(cnt)
            else:
                try :
                    shutil.copyfile(filename, out_dir + tenf)
                except:
                    pass
        print('compelted')
        shutil.rmtree(out_dir)  
    def move_nhan(TM):
        txt = glob(TM + '*.txt')
        os.makedirs(TM + 'TEMP', exist_ok=True)
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
                        if int(tmp[0])==17:
                            tmp2 = float(tmp[2]) - (float(tmp[4]) / 2) 
                            line = '17' + ' ' + str(tmp[1]) + ' ' + str(tmp2) + ' ' + str((tmp[3])) + ' ' + str((tmp[4]) ) + '\n'
                            out.writelines(line)
                        elif int(tmp[0])==27:
                            tmp3 = float(tmp[2]) + (float(tmp[4]) / 2) 
                            line = '27' + ' ' + str(tmp[1]) + ' ' + str(tmp3) + ' ' + str((tmp[3])) + ' ' + str((tmp[4]) ) + '\n'
                            out.writelines(line)
                        else :
                            out.writelines(line) 
                    out.writelines(line)
                f.close()
                out.close()
                cnt-=1
                os.replace(out_dir + tenf, filename)
                print(cnt)
            else:
                try :
                    shutil.copyfile(filename, out_dir + tenf)
                except:
                    pass
        print('compelted')
        shutil.rmtree(out_dir)                 
    def thaynhan(TM):
        txt = glob(TM + '*.txt')
        os.mkdir(TM + 'TXT')
        out_dir = TM + 'TXT/'
        cnt = len(txt)
        for filename in txt:
            tenf = os.path.basename(filename)
            if tenf != 'classes.txt' :
                out = open(out_dir + tenf,'w')
                with open(filename, 'r') as f:
                    while True:
                        line = f.readline()
                        if not line:
                            break
                        tmp = line.split()
                        if int(tmp[0])==11:
                            line = '10'+ line[2:]
                        if int(tmp[0])== 13 :
                            line = '11'+ line[2:]
                        if int(tmp[0])==15:
                            line = '12'+ line[2:]
                        if int(tmp[0])==16:
                            line = '13'+ line[2:]
                        if int(tmp[0])== 17 :
                            line = '14'+ line[2:]
                        if int(tmp[0])==18:
                            line = '15'+ line[2:]
                        if int(tmp[0])==19:
                            line = '16'+ line[2:] 
                        if int(tmp[0])==25:
                            line = '16'+ line[2:]
                        if int(tmp[0])== 26 :
                            line = '15'+ line[2:]
                        if int(tmp[0])==27:
                            line = '14'+ line[2:]
                        if int(tmp[0])==28:
                            line = '13'+ line[2:]
                        if int(tmp[0])== 29 :
                            line = '12'+ line[2:]
                        if int(tmp[0])==31:
                            line = '11'+ line[2:]
                        if int(tmp[0])==33:
                            line = '10'+ line[2:] 
                        out.writelines(line)
                out.close()
                cnt -= 1
                os.replace(out_dir + tenf, filename)
                print(cnt, tenf)
            else:
                try :
                    shutil.copyfile(filename, out_dir + tenf)
                except:
                    pass               
        print('compelted')
        shutil.rmtree(out_dir) 
    
    def xoanhanokunder_coptc(TM):
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
            outers = ['10','11','12','13','14','15','16'] #NHAN OK CAM1
            inners = ['3','4','5','6','7','9'] 
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
                                if w0 > 0.242375/6 or h0 > 0.2796666/6:
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
                                if w0 > 0.242375/6 or h0 > 0.2796666/6:
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
      
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'OK':
        if values[0] == True:
            TM = Test.getPath1() 
            YS_PTC.ganok(TM)
            YS_PTC.chia(TM)
            YS_PTC.xoanhanok(TM)
            YS_PTC.move_nhan(TM)
            YS_PTC.thaynhan(TM)
            YS_PTC.xoanhanokunder_coptc(TM)
window.close()

