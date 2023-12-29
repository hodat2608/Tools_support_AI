import glob
import os
import shutil
import os
path = "F:/vu_ikl/bc/*.txt"
move = "F:/vu_ikl/rs/"

list_dau = [['<','<'],['>','<'],['<','>'],['>','>']]
list_wh = [[0,13],[13,17],[17,21],[21,25],[25,30],[30,100]]
go = 0
for i in glob.glob(path):

    list_c = []
    label_new = []
    if i[-11:] == "classes.txt":
        continue

    # Modify the x values in the file
    with open(i, "r") as file:
        Lines = file.readlines()
        path_img = i[:-4] + ".jpg"
        name_file = os.path.basename(i)
        name_img = name_file[:-4] + ".jpg"
        for line in Lines:
            if line == "":
                continue

            if int(line.strip().split(" ")[0]) == 1:
                x = float(line.strip().split(" ")[1])
                y = float(line.strip().split(" ")[2])
                w = float(line.strip().split(" ")[3])*1200
                h = float(line.strip().split(" ")[4])*1200
                
                for item1,ld in enumerate(list_dau):
                    if (ld[0] == '>' and x >= 0.5) or (ld[0] == '<' and x < 0.5):
                        if (ld[1] == '>' and y >= 0.5) or (ld[1] == '<' and y < 0.5):
                            for wh in list_wh:
                                if wh[0] <= w <= wh[1] or wh[0] <= w <= wh[1]:
                                    new_path = move + str(item1) + "_" + str(wh[0]) + "_" + str(wh[1])
                                    print(new_path)
                                    if not os.path.isdir(new_path):
                                        os.mkdir(new_path)

                                    shutil.move(path_img, new_path + "/" + name_img)
                                    go = 1

                                    break
                            break

                break
    if go == 1:
        go = 0
        shutil.move(i, new_path + "/" + name_file)

                    
 
