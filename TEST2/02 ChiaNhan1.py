from glob import glob
import os
from TOAN import Test

TM = Test.getPath1()
txt = glob(TM + "/*.txt")
os.makedirs(TM + "/TEMP", exist_ok=True)

out_dir = TM + "/TEMP/"
cnt = len(txt)
sd = 3  # so dong
sc = 4  # so cot
for filename in txt:
    tenf = os.path.basename(filename)
    out = open(out_dir + tenf, "w")
    i = 6
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            if int(tmp[0]) == 6 and float(tmp[3]) > 0.8:
                w = float(tmp[3]) / sc
                d = float(tmp[4]) / sd
                y = float(tmp[2]) - float(tmp[4]) / 2  # y_min
                for r in range(sd):
                    x = float(tmp[1]) - float(tmp[3]) / 2  # x_min
                    for c in range(sc):
                        line = (
                            str(i)
                            + " "
                            + str(round(x + w / 2,6))
                            + " "
                            + str(round(y + d / 2,6))
                            + " "
                            + str(round(w,6))
                            + " "
                            + str(round(d,6))
                            + "\n"
                        )
                        out.writelines(line)
                        x += w
                        i += 1
                    y += d
            else:
                out.writelines(line)
    f.close()
    out.close()
    # Thay the file
    os.replace(out_dir + tenf, filename)
    cnt -= 1
    print(cnt)
