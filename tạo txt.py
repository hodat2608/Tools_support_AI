
import os
import glob

import os
import glob

path = 'C:/Users/CCSX009/Pictures/Camera Roll/New folder/'
images_path = os.path.join(path, '*.jpg')

for image_path in glob.glob(images_path):
    txt_file = os.path.splitext(image_path)[0] + '.txt'
    with open(txt_file, 'w') as file:
        file.write('')
