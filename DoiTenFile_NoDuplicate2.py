from glob import glob                                                           
import os,shutil
from TOAN import Test

TM1 = Test.getPath()
def doiten(TM1):
    fname = glob(TM1 + '*.jpg')
    c = len(fname)
    for filename in fname:
        print(filename)
        os.rename(filename , filename[:-4] + '_lx.jpg' )
        os.rename(filename[:-3] + 'txt' , filename[:-4] + '_lx.txt' )
        c-=1 

# def locangtheoten(TM1):
#     fname = glob(TM1 + '*.jpg')
#     c = len(fname)
#     for filename in fname:
#         tenf = os.path.basename(filename)
#         if 'Nới_Lỏng' in tenf :
#             os.rename(filename , filename[:-13] + '-QC.jpg' )
#             os.rename(filename[:-3] + 'txt' , filename[:-13] + '-QC.txt' )
#             # # if os.path.exists(TM1 + tenf):
#             #     os.rename(TM1 + tenf, TM1 + tenf[2:6]+'-'+ tenf[6:8] + '-'+tenf[8:10] + tenf[10:])
#             # # if os.path.exists(TM1 + tenf[:-3] +'txt'):
#             #     os.rename(TM1 + tenf[:-3] +'txt', TM1 + tenf[2:6]+'-'+ tenf[6:8] + '-'+tenf[8:10] + tenf[10:30]+'txt')
#         # else:
#         #     continue
#             # print(tenf[-7:-4])
#             # os.remove(filename)
#             # if os.path.exists(filename[:-3] +'txt'):
#             #     os.remove(filename[:-3] +'txt')
#             # # shutil.move(filename, TM2 + tenf)
#             # # shutil.move(filename[:-3] + 'jpg' , TM2 + tenf[:-3] + 'jpg')
#             # c-=1 
#             # print(c)
#     print('DONE')

doiten(TM1)
# locangtheoten(TM1)


# input_str = "dat123thanhho2806@gmail.com"
# index_of_first_digit = next((index for index, char in enumerate(input_str) if char.isdigit()), None)

# if index_of_first_digit is not None:
#     letters_part = input_str[:index_of_first_digit]
#     digits_part = input_str[index_of_first_digit:]
#     print("Letters part:", letters_part)
#     print("Digits part:", digits_part)
# else:
#     letters_part = input_str
#     digits_part = ""

#     print("Letters part:", letters_part)
#     print("Digits part:", digits_part)
