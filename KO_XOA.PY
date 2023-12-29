from glob import glob                                                           
import os
import shutil
TM = 'C:/Users/AI004/Desktop/DATA_20230205/'          
txt = glob(TM + '*.txt')
try:
    os.mkdir(TM + 'TXT1')
except:
    pass
out_dir = TM + 'TXT1/'
c = len(txt)
for filename in txt:
    tenf = os.path.basename(filename)
    if tenf != 'classes.txt':
        out = open(out_dir + tenf,'w')
        with open(filename, 'r') as f:
            cls0 = 0
            while True:
                line = f.readline()
                if not line:
                    break
                tmp = line.split()
                #if tmp[0] not in ['2']:
                if tmp[0] in ['0','3','4','6','7','8','9','10','11','12']:
                # if int(tmp[0]) != 5 :
                #     if int(tmp[0]) != 6 :
                #         if int(tmp[0]) != 7 :
                #             if int(tmp[0]) != 8 :
                #                 if int(tmp[0]) != 9 :
                #                     if int(tmp[0]) != 10 :
                #                         if int(tmp[0]) != 11 :                                            
                #                             # if int(tmp[0]) != 12 :
                #                             #     if int(tmp[0]) != 13 :
                #                             #         if int(tmp[0]) != 14 :
                #                             #             if int(tmp[0]) != 15 :
                #                             #                 if int(tmp[0]) != 16:
                    #out.writelines(line)
                    #f.close()
                    shutil.copy(filename , out_dir + tenf)
                    shutil.copy(filename[:-3]+'jpg' , out_dir + tenf[:-3] + 'jpg')
        f.close()
        out.close()
        c-=1
        #os.replace(out_dir + tenf, filename)
        print(c, tenf)
print('compelted')
#shutil.rmtree(out_dir)
