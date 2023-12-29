from glob import glob
import os,shutil
from TOAN import Test
TM = Test.getPath1()     
def ganokTC(TM):
    txt = glob(TM + '*.txt')
    try :
        os.mkdir(TM + 'dat')
    except:
        pass
    out_dir = TM + 'dat/'
    cnt = len(txt)
    nhan_lam_chuan = ['0 0.486875 0.741667 0.206250 0.233333'] #nhan so 1 
    nhanso2 =        ['1 0.490000 0.499167 0.413750 0.528333'] #nhan so 2
    nhanso3 =        ['2 0.199687 0.322083 0.166875 0.140833'] #nhan so 3
    nhanso4 =        ['3 0.807813 0.328750 0.221875 0.135833'] #nhan so 4
    nhanso5 =        ['4 0.938438 0.585000 0.118125 0.348333'] #nhan so 5
    nhanso6 =        ['5 0.051250 0.570000 0.101250 0.355000'] #nhan so 6

    nhan_lam_chuan = nhan_lam_chuan[0].split()
    nhanso2 = nhanso2[0].split()
    nhanso3 = nhanso3[0].split()
    nhanso4 = nhanso4[0].split()
    nhanso5 = nhanso5[0].split()
    nhanso6 = nhanso6[0].split()

    x_nhan_lam_chuan = float(nhan_lam_chuan[1])
    y_nhan_lam_chuan = float(nhan_lam_chuan[2])
    x_nhanso_2 = float(nhanso2[1])
    y_nhanso_2 = float(nhanso2[2])
    x_nhanso_3 = float(nhanso3[1])
    y_nhanso_3 = float(nhanso3[2])
    x_nhanso_4 = float(nhanso4[1])
    y_nhanso_4 = float(nhanso4[2])
    x_nhanso_5 = float(nhanso5[1])
    y_nhanso_5 = float(nhanso5[2])
    x_nhanso_6 = float(nhanso6[1])
    y_nhanso_6 = float(nhanso6[2])
  
    wh_nhan_lam_chuan = nhan_lam_chuan[3]+' '+nhan_lam_chuan[4]
    wh_nhanso_2 = nhanso2[3]+' '+nhanso2[4]
    wh_nhanso_3 = nhanso3[3]+' '+nhanso3[4]
    wh_nhanso_4 = nhanso4[3]+' '+nhanso4[4]
    wh_nhanso_5 = nhanso5[3]+' '+nhanso5[4]
    wh_nhanso_6 = nhanso6[3]+' '+nhanso6[4]

    stt_nhan_so_2 = int(nhanso2[0])
    stt_nhan_so_3 = int(nhanso3[0])
    stt_nhan_so_4 = int(nhanso4[0])
    stt_nhan_so_5 = int(nhanso5[0])
    stt_nhan_so_6 = int(nhanso6[0])

    space = ' '
    xuong_hang = '\n'

    for filename in txt:
        tenf = os.path.basename(filename)
        if tenf != 'classes.txt' and tenf != 'lastclasses.txt':
            out = open(out_dir + tenf,'w')
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    tmp = line.split()
                    if int(tmp[0])< 10:
                        if int(tmp[0]) == 0:
                            tam_nhan_so_2 = str(float(tmp[1]) + float(abs(x_nhan_lam_chuan-x_nhanso_2))) + ' ' + str(float(tmp[2]) - float(abs(y_nhan_lam_chuan-y_nhanso_2)))
                            tam_nhan_so_3 = str(float(tmp[1]) - float(abs(x_nhan_lam_chuan-x_nhanso_3))) + ' ' + str(float(tmp[2]) - float(abs(y_nhan_lam_chuan-y_nhanso_3)))
                            tam_nhan_so_4 = str(float(tmp[1]) + float(abs(x_nhan_lam_chuan-x_nhanso_4))) + ' ' + str(float(tmp[2]) - float(abs(y_nhan_lam_chuan-y_nhanso_4)))
                            tam_nhan_so_5 = str(float(tmp[1]) + float(abs(x_nhan_lam_chuan-x_nhanso_5))) + ' ' + str(float(tmp[2]) - float(abs(y_nhan_lam_chuan-y_nhanso_5)))
                            tam_nhan_so_6 = str(float(tmp[1]) - float(abs(x_nhan_lam_chuan-x_nhanso_6))) + ' ' + str(float(tmp[2]) - float(abs(y_nhan_lam_chuan-y_nhanso_6)))
                    out.writelines(line) 
                out.writelines( str(stt_nhan_so_2) + space + str(tam_nhan_so_2) + space + str(wh_nhanso_2) + xuong_hang + 
                                str(stt_nhan_so_3) + space + str(tam_nhan_so_3) + space + str(wh_nhanso_3) + xuong_hang +
                                str(stt_nhan_so_4) + space + str(tam_nhan_so_4) + space + str(wh_nhanso_4) + xuong_hang +
                                str(stt_nhan_so_5) + space + str(tam_nhan_so_5) + space + str(wh_nhanso_5) + xuong_hang +
                                str(stt_nhan_so_6) + space + str(tam_nhan_so_6) + space + str(wh_nhanso_6) + xuong_hang )  
        else : 
            shutil.copyfile(filename, out_dir + tenf)
            print(tenf)
        f.close()
        out.close()
        # os.replace(out_dir + tenf, filename)
        cnt -= 1
        print(cnt)
    print('compelted')
    # shutil.rmtree(out_dir)

ganokTC(TM)