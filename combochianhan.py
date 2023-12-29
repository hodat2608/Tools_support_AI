from glob import glob                                                           
import os
import shutil 
TM = 'Z:/02.RS4F5_X75_NQVNHC/X75/DEN/20221227/CD/'
txt = glob(TM + '*.txt')
try :
    os.mkdir(TM + 'TOAN')
except:
    pass
out_dir = TM + 'TOAN/'
cnt = len(txt)
line1 = ' 0.502188 0.41375 0.981875	0.8125\n'


#TM2 = 'Z:/02.RS4F5_X75_NQVNHC/New folder/TOAN/'
txt1 = glob(out_dir + '*.txt')
try :
    os.mkdir(out_dir + 'TOAN1')
except:
    pass
out_dir1 = out_dir + 'TOAN1/'
cnt1 = len(txt1)
c = 0
sd = 2 #so dong
sc = 3 #so cot
def ganok(txt,out_dir,line1,cnt):
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
                    if int((tmp[0])) < 5:
                        out.writelines(line)
                out.writelines('5' + line1)
        else:
            try :
                shutil.copyfile(filename, out_dir + tenf)
                print(tenf)
            except:
                pass
        f.close()
        out.close()
        #os.replace(out_dir + tenf, filename)
        cnt-=1
        print('da gan nhan ok', cnt)
    print('completed') 

def chia(txt1,out_dir1,sd,sc,cnt1):
    for filename in txt1:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt':
            out = open(out_dir1 + tenf,'w')
            i=5
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0])==5:
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
                print(tenf)
            except:
                pass
        f.close() 
        out.close()
        #Thay the file
        os.replace(out_dir1 + tenf, filename)
        cnt1 -= 1
        print(cnt1)
    #Xoa thu muc tam TEMP
    shutil.rmtree(out_dir1)

ganok(txt,out_dir,line1,cnt)
chia(txt1,out_dir1,sd,sc,cnt1)
