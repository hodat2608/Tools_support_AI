from glob import glob                                                           
import shutil,os
from TOAN import Test
TM = Test.getPath1()
def xoanhanok(TM):
    path = TM  + '*.txt'
    cnt = 0
    import glob 
    for i in glob.glob(path):
        tenf = os.path.basename(i)
        if tenf == 'classes.txt' and tenf == 'lastclasses.txt':
            continue
        file = open(i, 'r')
        Lines = file.readlines()
        names = []
        files = []
        for line in Lines:
            num = line.split()[0]
            names.append(num)
                  
        outers = ['6','7','8','9','10','11','12','13','14','15','16','17']
        inners = ['2','4','5']
        for inner in inners: 
            for outer in outers:
                if inner in names and outer in names:
                    for index,line in enumerate(Lines):      
                        if line.strip().split()[0] == outer:
                            myindex =0
                            x4 = float(line.strip().split()[1])
                            y4 = float(line.strip().split()[2])
                            w4 = float(line.strip().split()[3])
                            h4 = float(line.strip().split()[4])
                            xmin = x4 - w4/2
                            xmax = x4 + w4/2
                            ymin = y4 - h4/2
                            ymax = y4 + h4/2
                            myindex = index 
                            #print(myindex)
                            break
                    for line in Lines:   
                        if line.strip().split()[0] == inner:
                            x0 = float(line.strip().split()[1])
                            y0 = float(line.strip().split()[2])
                            w0 = float(line.strip().split()[3])
                            h0 = float(line.strip().split()[4])
                            #bui chi 0.013750 0.018333
                            #divat 0.025000 0.033333
                            if w0 > 0.242375/4 or h0 > 0.2796666/4:
                                if xmin < x0 < xmax  and ymin < y0 < ymax:
                                    for index,line in enumerate(Lines):  
                                        if line.strip().split()[0] == outer and index == myindex:
                                            files.append(line)
                    with open(i, 'w') as f:
                        for line in Lines:
                            if line not in files:
                                #print('HAHA')
                                f.write(line)
                            else:
                                cnt += 1 
                                print(cnt)

                if inner in names and outer in names:
                    for index,line in enumerate(Lines):      
                        if line.strip().split()[0] == outer:
                            myindex =0
                            x4 = float(line.strip().split()[1])
                            y4 = float(line.strip().split()[2])
                            w4 = float(line.strip().split()[3])
                            h4 = float(line.strip().split()[4])
                            xmin = x4 - w4/2
                            xmax = x4 + w4/2
                            ymin = y4 - h4/2
                            ymax = y4 + h4/2
                            myindex = index 
                            #print(myindex)
            
                    for line in Lines:   
                        if line.strip().split()[0] == inner:
                            x0 = float(line.strip().split()[1])
                            y0 = float(line.strip().split()[2])

                            w0 = float(line.strip().split()[3])
                            h0 = float(line.strip().split()[4])
                            #bui chi 0.142375 0.1896666
                            #divat 0.025000 0.033333
                            if w0 > 0.242375/4 or h0 > 0.2796666/4:
                                if xmin < x0 < xmax  and ymin < y0 < ymax:
                                    for index,line in enumerate(Lines):  
                                        if line.strip().split()[0] == outer and index == myindex:
                                            files.append(line)
                    with open(i, 'w') as f:
                        for line in Lines:
                            if line not in files:
                                #print('HAHA')
                                f.write(line)
                            else:
                                cnt += 1 
                                print(cnt)    


xoanhanok(TM)
