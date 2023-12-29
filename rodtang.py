from PIL import Image
import os, cv2
# input_path = r'C:\Users\CCSX009\Desktop\rod\2023-11-30_08-24-41-023051-C1.jpg'

# # image = Image.open(input_path)
# img1_orgin = cv2.imread(input_path)
# # Xoay ảnh theo góc -45 độ
# rotated_image = img1_orgin.rotate(-270)

# rotated_image.show()

input_path = r'C:\Users\CCSX009\Desktop\rod\2023-11-30_08-24-41-023051-C1.jpg'

img1_orgin = cv2.imread(input_path)
rotated_image = cv2.rotate(img1_orgin, cv2.ROTATE_90_COUNTERCLOCKWISE)  # Adjust rotation angle as needed

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()