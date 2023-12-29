from glob import glob                                                           
import os, shutil

TM ='C:/DAT12795/DEN/CAM1/DATA_GỐC/20230131/'  #Thu muc chua file labels

txt = glob(TM + '*.txt')
os.makedirs(TM + 'TEMP',exist_ok=True)
out_dir = TM + 'TEMP/'
cnt = len(txt)
sd = 5 #so dong
sc = 5 #so cot
for filename in txt:
    tenf = os.path.basename(filename)
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
    f.close() 
    out.close()
    #Thay the file
    os.replace(out_dir + tenf, filename)
    cnt -= 1
    print(cnt)

