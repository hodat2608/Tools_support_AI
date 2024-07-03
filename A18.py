from glob import glob
import os,shutil
from TOAN import Test
TM = Test.getPath()     
def ganokTC(TM):
    txt = glob(TM + '*.txt')
    try :
        os.mkdir(TM + 'dat')
    except:
        pass
    out_dir = TM + 'dat/'
    cnt = len(txt)
    nhan_lam_chuan = ['0 0.137692 0.486538 0.256923 0.526923'] #nhan so 1 
    nhanso2 =        ['1 0.287692 0.485256 0.063077 0.698718'] #nhan so 2
    nhanso3 =        ['2 0.580000 0.233974 0.543077 0.370513'] #nhan so 3
    nhanso4 =        ['3 0.580769 0.705769 0.541538 0.434615'] #nhan so 4
    nhanso5 =        ['4 0.585769 0.453205 0.533077 0.080769'] #nhan so 5
    nhanso6 =        ['4 0.905000 0.497436 0.108462 0.969231'] #nhan so 6

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
                            tam_nhan_so_2 = str(float(tmp[1]) + float(abs(x_nhan_lam_chuan-x_nhanso_2))) + ' ' + str(float(tmp[2]) + float(abs(y_nhan_lam_chuan-y_nhanso_2)))
                            tam_nhan_so_3 = str(float(tmp[1]) + float(abs(x_nhan_lam_chuan-x_nhanso_3))) + ' ' + str(float(tmp[2]) - float(abs(y_nhan_lam_chuan-y_nhanso_3)))
                            tam_nhan_so_4 = str(float(tmp[1]) + float(abs(x_nhan_lam_chuan-x_nhanso_4))) + ' ' + str(float(tmp[2]) + float(abs(y_nhan_lam_chuan-y_nhanso_4)))
                            tam_nhan_so_5 = str(float(tmp[1]) + float(abs(x_nhan_lam_chuan-x_nhanso_5))) + ' ' + str(float(tmp[2]) - float(abs(y_nhan_lam_chuan-y_nhanso_5)))
                            tam_nhan_so_6 = str(float(tmp[1]) + float(abs(x_nhan_lam_chuan-x_nhanso_6))) + ' ' + str(float(tmp[2]) + float(abs(y_nhan_lam_chuan-y_nhanso_6)))
                    out.writelines(line) 
                out.writelines( 
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