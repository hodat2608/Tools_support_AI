from glob import glob                                                           
import os,shutil
from TOAN import Test

TM = Test.getPath1() 
def move(TM):  
    txt = glob(TM + '*.txt')
    try:
        os.mkdir(TM + 'TXT')
    except :
        pass
    out_dir = TM + 'TXT/'
    cnt = len(txt)
    mylist = []
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
                    if tenf == 'classes.txt':
                        continue
                    if int(tmp[0]) == 5:
                        if float(tmp[3]) == float(tmp[4]):
                            cnt -= 1
                            if os.path.exists(filename[:-3]+'jpg'):
                                mylist.append(tenf)
                                shutil.move(filename[:-3]+'jpg' , out_dir + tenf[:-3] + 'jpg')
                                print(f'{cnt}_{tenf}')
    for i in mylist :
        shutil.move(TM + i, out_dir + i) 
    print('Tong Files', len(txt))  

def xoa_txt_ko_co_jpg(TM):
    txt = glob(TM + 'TXT/' + '*.txt')
    c = 0
    for filename in txt:
        tenf = os.path.basename(filename)
        if not os.path.exists(filename[:-3] +'jpg'):
            c+=1
            os.remove(filename)
            print(c , tenf) 
    print('completed')   


move(TM)
xoa_txt_ko_co_jpg(TM)




