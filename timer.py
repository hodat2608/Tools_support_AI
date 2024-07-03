from glob import glob                                                           
import os,shutil,cv2
from TOAN import Test

TM1 = Test.getPath1()
def doiten(TM1):
    fname = glob(TM1 + '*.bmp')
    for filename in fname:
        os.rename(filename , filename[:-4] + '.jpg' )
        # print(filename)
        # txt_file = os.path.splitext(filename)[0] + '.txt'
        # with open(txt_file, 'w') as file:
        #     file.write('0 0.126923 0.478846 0.249231 0.526923')

def roi(TM1):
    filenames = glob(TM1 + '*.jpg')
    for filename1 in filenames:
        print(filename1)
        img1_orgin = cv2.imread(filename1)
        img1_orgin = img1_orgin[190:970,300:1600]    
        cv2.imwrite(filename1,img1_orgin )

doiten(TM1)
roi(TM1)
     