import os,glob,shutil
from glob import glob  
from datetime import datetime

TM = 'C:/Users/AI004/Desktop/test/'
txt = glob(TM + '*.jpg')
try :
    os.mkdir(TM + 'TOAN')
except:
    pass
out_dir = TM + 'TOAN/'
# now = datetime.datetime.now()
time_data1 = "11/08/22 02:35:14"
format_data1 = "%d/%m/%y %H:%M:%S"
date1 = datetime.strptime(time_data1, format_data1)
print(date1)

time_data2 = "01/06/23 02:35:14"
format_data2 = "%d/%m/%y %H:%M:%S"
date2 = datetime.strptime(time_data2, format_data2)
print(date2)
c = 0
for filename in txt:
    tenf = os.path.basename(filename)
    #out = open(out_dir + tenf,'w')
    import datetime
    m_time = os.path.getmtime(filename)
    dt_m = datetime.datetime.fromtimestamp(m_time)
    if date1 < dt_m < date2:
        shutil.copyfile(filename, out_dir + tenf)
        c+=1
        print(c, tenf, dt_m)
        
