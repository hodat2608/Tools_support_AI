import numpy as np
from PIL import Image
from skimage.morphology import dilation, disk

# Open image and make into Numpy array
PILim = Image.open('C:/Users/CCSX009/Pictures/Camera Roll/3.png').convert('RGB')
RGBim = np.array(PILim)
h, w = RGBim.shape[0], RGBim.shape[1]

# Make a single channel 24-bit image rather than 3 channels of 8-bit each
RGB24 = (RGBim[...,0].astype(np.uint32)<<10) | (RGBim[...,1].astype(np.uint32)<<5)

# Make list of unique colours
UniqueColours = np.unique(RGB24)

# Create result image
result = np.zeros((h,w),dtype=np.uint8)

# Make mask for any particular colour - same size as original image
mask = np.zeros((h,w), dtype=np.uint8)

# Make disk-shaped structuring element for morphology
selem = disk(1)

# Iterate over unique colours
for i,u in enumerate(UniqueColours):
   # Turn on all pixels matching this unique colour, turn off all others
   mask = np.where(RGB24==u,100,0)
   # Dilate (fatten) the mask by 1 pixel
   mask = dilation(mask,selem)
   # Add all activated pixels to result image
   result = result + mask

# Save result
Image.fromarray(result.astype(np.uint8)).save('result.png')