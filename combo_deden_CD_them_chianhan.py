from glob import glob                                                           
import shutil,os
from TOAN import Test
TM = Test.getPath1()        
def ganok(TM):
    txt = glob(TM + '*.txt')
    try :
        os.mkdir(TM + 'dat')
    except:
        pass
    out_dir = TM + 'dat/'
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
                    if int(tmp[0])<6:
                        if int(tmp[0])== 0 or int(tmp[0])== 1 or int(tmp[0])== 3:
                            tam = str(float(tmp[1]) + 0.0185) + ' ' + str(float(tmp[2]) + 0.211667)
                    out.writelines(line) 
                out.writelines('6 ' + tam + ' 0.908750 0.859167\n') 
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

def chia(TM):
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

ganok(TM)
chia(TM)

