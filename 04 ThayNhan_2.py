from glob import glob                                                           
import os
TM = 'C:/DAT12795/DEN/CAM1/DATA_GỐC/20230131/'
txt = glob(TM + '*.txt')
os.makedirs(TM + 'TEMP', exist_ok=True)
out_dir = TM + 'TEMP/'
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
    f.close() 
    out.close()
    #Thay the file
    os.replace(out_dir + tenf, filename)
    cnt -= 1
    print(cnt)
