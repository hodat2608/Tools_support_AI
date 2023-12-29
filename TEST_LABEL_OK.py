

def themnhan(TM):
    txt = glob(TM + '*.txt')
    cnt = len(txt)
    os.makedirs(TM + 'TEMP', exist_ok=True)
    out_dir = TM + 'TEMP/'
    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
            out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    out.writelines(line)
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0]) < 5:
                        print('chua gan nhan ok ', tenf)
                    else:
                        continue
                    