# import shutil
# total, used, free = shutil.disk_usage("/")
# disk_info = f"Disk Info: Total={total}, Used={used}, Free={free}"
# print(disk_info)

import shutil

total, used, free = shutil.disk_usage("K:\\")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))