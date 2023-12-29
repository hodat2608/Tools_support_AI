from glob import glob                                                           
import shutil, os, cv2
from TOAN import Test
 
TM = Test.getPath1()
os.makedirs(TM + '/TEMP',exist_ok=True)
img = glob(TM +'*.jpg')
cnt=0
for i in img:
    tenf  = os.path.basename(i)
    image = cv2.imread(i, 1)
    ROI = image[0:1200, 220:1400]
    cv2.imwrite(TM + 'TEMP/' + tenf, ROI)
    # out = open(TM + 'TEMP/' + tenf[:-3]+'txt','w')
    # with open(i[:-3]+'txt', 'r') as f:
    #     while True:
    #         line = f.readline()
    #         if not line:
    #             break
    #         tmp = line.split()
    #         x = round(float(tmp[1])*1600/1180 - 220/1180,6)
    #         w = round(float(tmp[3])*1600/1180,6)
    #         out.writelines(tmp[0] + ' ' + str(x) + ' ' + tmp[2] + ' ' + str(w) + ' ' + tmp[4] + '\n') 
    # f.close()
    # out.close()
    os.replace(TM + 'TEMP/' + tenf, i)
    # os.replace(TM + 'TEMP/' + tenf[:-3]+'txt',i[:-3]+'txt')
    cnt += 1
    print(cnt)
shutil.rmtree(TM + 'TEMP/' )
print('Completed!')

