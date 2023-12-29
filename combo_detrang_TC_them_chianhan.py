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
                    if int(tmp[0])== 1:
                        tam = str(float(tmp[1]) - 0.010312) + ' ' + str(float(tmp[2]) + 0.020417)
                    out.writelines(line)
                out.writelines('18 ' + tam + ' 0.028125 0.030833\n') 
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

ganok(TM)

