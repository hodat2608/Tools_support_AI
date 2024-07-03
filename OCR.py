import cv2
import pytesseract
from PIL import Image
import pytesseract
import numpy as np
# Đọc hình ảnh đầu vào
filename = 'OCR.jpg'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)