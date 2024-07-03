import glob
import os
import shutil
import os
from collections import Counter
import matplotlib.pyplot as plt
from TOAN import Test
path = Test.getPath()
all_label = []
label = {}

if path[-1] != "/":
    path = path + "/"

try:
    with open(path + "classes.txt", "r") as file:
        Lines = file.readlines()
        for it,line in enumerate(Lines):
            label[str(it)] = line[:-1]
except:
    print("You dont have file classes.txt")

for i in glob.glob(path + "*.txt"):
    if i[-11:] == "classes.txt":
        continue


    with open(i, "r") as file:
        Lines = file.readlines()
        for line in Lines:
            all_label.append(line.strip().split(" ")[0])


label_dict = dict(Counter(all_label))


for key1, value1 in label_dict.items():
    print(key1," : ",value1)

to_remove = []
to_add = {}

for key1, value1 in label_dict.items():
    for key2, value2 in label.items():
        if key1 == key2:
            to_remove.append(key1)
            to_add[value2] = value1
            
for key in to_remove:
    del label_dict[key]
    
label_dict.update(to_add)

plt.figure(figsize=(300, 300))
# plt.bar(range(len(label_dict)), list(label_dict.values()), align='center')
plt.bar(range(len(label_dict)), list(label_dict.values()), align='center', width=0.5)

# Hiển thị giá trị trên thanh bar
for i, v in enumerate(label_dict.values()):
    plt.text(i, v + 1, str(v), ha='center')

# , rotation=45
plt.xticks(range(len(label_dict)), list(label_dict.keys()), ha="center")

plt.show()
