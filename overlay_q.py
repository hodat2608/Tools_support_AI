import cv2
import numpy as np

# Load image
img = cv2.imread('C:/Users/CCSX009/Desktop/1/2023-03-31_08-14-40-225087-C1.jpg')

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Threshold on the "value" channel to extract bright areas
mask = cv2.inRange(hsv, (0, 0, 200), (255, 255, 255))
mask = cv2.bitwise_not(mask)

# Create new image with only bright areas
bright_areas = cv2.bitwise_and(img, img, mask=mask)

# Load another image to overlay bright areas onto
overlay_img = cv2.imread('C:/Users/CCSX009/Desktop/2/2022-12-26_07-55-46-011050-C1.jpg')

# Resize bright areas image to match size of overlay image
bright_areas_resized = cv2.resize(bright_areas, overlay_img.shape[:2][::-1])

# Add bright areas to overlay image
result = cv2.addWeighted(overlay_img, 1, bright_areas_resized, 0.5, 0)

# Display result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
