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
            # ['6','7','8','9','10','11','12']
            if tmp[0] not in ['6','10','13']:
                out.writelines(line)
    f.close() 
    out.close()
    #Thay the file
    os.replace(out_dir + tenf, filename)
    cnt -= 1
    print(cnt)
