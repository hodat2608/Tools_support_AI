from glob import glob                                                           
import shutil, os.path

tm = '//D9090222/g/a883/CAM1/'
src = '//D9090222/g/a883/CAM1/mau/2023-07-26_00-01-59-1380.jfz.txt'

img = glob(tm + '*.jpg')
cnt=0
for i in img:
        f  = os.path.basename(i) 
        shutil.copyfile(src, tm + f[:-3] + 'txt')
        cnt += 1
        print(cnt)
print('Completed!')
