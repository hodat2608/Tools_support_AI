from glob import glob
import os
from TOAN import Test

TM = Test.getPath("Hay chon thu muc chua .txt")
txt = glob(TM + "/*.txt")
os.makedirs(TM + "/TEMP", exist_ok=True)
out_dir = TM + "/TEMP/"
cnt = len(txt)
for filename in txt:
    tenf = os.path.basename(filename)
    out = open(out_dir + tenf, "w")
    with open(filename, "r") as f:
        chk1=chk2=False
        tam = "0.459375 0.466250"
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            if int(tmp[0]) < 6:
                out.writelines(line)
            else:
                if int(tmp[0]) == 6:
                    x1= float(tmp[1])
                    y1 = float(tmp[2])
                    chk1=True
                if int(tmp[0]) == 17:
                    x2= float(tmp[1])
                    y2 = float(tmp[2])
                    chk2=True
        if chk1 and chk2:
            tam = str((x1+x2)/2) + ' ' + str((y1+y2)/2)
        out.writelines("6 " + tam + " 0.850000 0.754167\n")
        # 6 0.497219112 0.449135326 0.894 0.833

    f.close()
    out.close()
    os.replace(out_dir + tenf, filename)
    cnt -= 1
    print(cnt,end='\r')
