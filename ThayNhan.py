from glob import glob                                                           
import os, shutil
from TOAN import Test

TM = Test.getPath1()      
def thaynhan1(TM):       
    txt = glob(TM + '*.txt')
    try:
        os.mkdir(TM + 'TXT')
    except :
        pass
    out_dir = TM + 'TXT/'
    cnt = len(txt)
    line1 = ['6 0.123333 0.255000 0.161667 0.196667']
    line2 = ['0 0.493750 0.515833 0.365833 0.150000']
    i = line1[0].split()
    y = line2[0].split()
    x1 = float(i[1])
    y1 = float(i[2])
    x2 = float(y[1])
    y2 = float(y[2])
    # wh = y[3]+' '+y[4]+'\n'
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
                    if int(tmp[0]) == 4 :
                        if float(tmp[1]) < 0.5: 
                            tam1 = str(float(tmp[1])+0.009166) + ' ' + str(float(tmp[2]) - 0.257083) 
                        else:
                            tam2 = str(float(tmp[1])-0.004583) + ' ' + str(float(tmp[2]) + 0.257083) 
                    else:
                        if int(tmp[0])==0:
                            tam1 = str(float(tmp[1]) - float(x2-x1)) + ' ' + str(float(tmp[2]) - float(y2-y1))
                            tam2 = str(float(tmp[1]) + float(x2-x1)) + ' ' + str(float(tmp[2]) + float(y2-y1))
                    out.writelines(line)
                out.writelines('6 ' + tam1 + ' 0.151667 0.190000\n' + '6 ' + tam2 + ' 0.151667 0.190000\n')
            out.close()
            cnt -= 1
            # os.replace(out_dir + tenf, filename)
            print(cnt)
    print('compelted')
    # shutil.rmtree(out_dir)

thaynhan1(TM)

