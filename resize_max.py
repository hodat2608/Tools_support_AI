from glob import glob                                                           
import os,shutil
from TOAN import Test
TM = Test.getPath1()        
txt = glob(TM + '*.txt')
save_path = Test.getPath2()
c = len(txt)
for filename in txt:
    tenf = os.path.basename(filename)
    out = open(save_path + tenf,'w')
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.split()
            if tenf == 'classes.txt':
                continue           
            if int(tmp[0]) == 3 :
                if float(tmp[3]) <= 0.010833 and float(tmp[4]) <= 0.010833:
                    c-=1
                    f.close()
                    if os.path.exists(filename):
                        shutil.move(filename , save_path + tenf)
                    if os.path.exists(filename[:-3]+'jpg'):
                        shutil.move(filename[:-3]+'jpg' , save_path + tenf[:-3] + 'jpg')
                    print(f'{c}_{tenf}')   
                    break
                    # w = 0.008125 - float(tmp[3])
                    # h = 0.010833 - float(tmp[4])
                    # line = '6' + ' ' + str(tmp[1]) + ' ' + str(tmp[2]) + ' ' + str(float(tmp[3]) + w) + ' ' + str(float(tmp[4]) + h ) + '\n'
                    # out.writelines(line)
            #     else :
            #         out.writelines(line) 
            # else :
            #     out.writelines(line)
        # out.writelines(line)
    # f.close()
    # out.close()
    c-=1
    print('compelted')
                    

