
import glob
from datetime import datetime, timedelta
import cv2
import shutil
import os



from TOAN import Test

path = Test.getPath1() + '*.txt'
path_1 = Test.getPath2()
path_2 = Test.getPath3()
mytime1 = 2
mytime2 = 3


def loc1(path, path_1, path_2, mytime1):
    for i in glob.glob(path):

        file = open(i, "r")
        if i[-11:] == "classes.txt":
            continue

        Lines = file.readlines()

        label = "3"
        list_delete = []
        for line in Lines:
            if line.strip().split(" ")[0] == label:
                for b in reversed(range(len(i))):
                    if i[b] == "\\":
                        position = b
                        break 
                
                name = i[(position+1):]

                group = name[11:].split("-")

                string_date = ":".join(group[:-2])

                mydate = datetime.strptime(string_date, "%H:%M:%S")

                for t in range(mytime1+1):
                    abc = i[(position+1):(position+12)] + (mydate - timedelta(seconds=t)).strftime('%H-%M-%S')
                    n_path = path_1+ abc
                    for o in glob.glob(path_1+"*.jpg"):
                        if n_path[-19:] == o[-34:-15]:
                            print('ok')
                            if os.path.exists(o):
                                shutil.copy(o, path_2 + abc + o[-15:])
                            else:
                                continue

                break
    print('completed')

def loc2(path, path_1, path_2, mytime2):
    for i in glob.glob(path):

        file = open(i, "r")
        if i[-11:] == "classes.txt":
            continue

        Lines = file.readlines()

        label = "1"
        list_delete = []
        for line in Lines:
            if line.strip().split(" ")[0] == label:
                for b in reversed(range(len(i))):
                    if i[b] == "\\":
                        position = b
                        break 
                
                name = i[(position+1):]

                group = name[11:].split("-")

                string_date = ":".join(group[:-2])

                mydate = datetime.strptime(string_date, "%H:%M:%S" )

                for t in range(mytime2+1):
                    abc = i[(position+1):(position+12)] + (mydate - timedelta(seconds=t)).strftime('%H-%M-%S')
                    n_path = path_1+ abc
                    for o in glob.glob(path_1+"*.jpg"):
                        if n_path[-19:] == o[-34:-15]:
                            print('ok')
                            if os.path.exists(o):
                                shutil.copy(o, path_2 + abc + o[-15:])
                            else:
                                continue

                break
    print('completed')
        

loc1(path, path_1, path_2, mytime1)
# loc2(path, path_1, path_2, mytime2)
                
