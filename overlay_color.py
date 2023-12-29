# # import cv2
# # import numpy as np

# # def nothing(x):
# #     pass


# # # Tạo trackbar
# # cv2.namedWindow('image')
# # cv2.createTrackbar('Brightness', 'image', 0, 255, nothing)
# # cv2.createTrackbar('Contrast', 'image', 0, 254, nothing)

# # cv2.createTrackbar('H', 'image', 0, 255, nothing)
# # cv2.createTrackbar('S', 'image', 0, 255, nothing)
# # cv2.createTrackbar('V', 'image', 0, 255, nothing)


# # cv2.createTrackbar('Saturation', 'image', 0, 255, nothing)

# # # Hiển thị ảnh gốc
# # # img = cv2.imread('image.jpg')
# # # cv2.imshow('image', img)

# # # Chờ người dùng nhấn phím bất kỳ để thoát
# # while True:
# #     img = cv2.imread("F:/vu_abc/t1.jpg")

# #     # Lấy giá trị từ các trackbar
# #     brightness = cv2.getTrackbarPos('Brightness', 'image')
# #     contrast = cv2.getTrackbarPos('Contrast', 'image')

# #     # Lấy giá trị của các trackbar
# #     h = cv2.getTrackbarPos('H', 'image')
# #     s = cv2.getTrackbarPos('S', 'image')
# #     v = cv2.getTrackbarPos('V', 'image')

# #     saturation = cv2.getTrackbarPos('Saturation', 'image')

    
# #     # Tăng giảm brightness và contrast
# #     brightness = int(brightness)
# #     contrast = int(contrast)
# #     img = cv2.addWeighted(img, 1 + contrast/127, np.zeros(img.shape, dtype=img.dtype), 0, brightness - contrast)
    
# #     # Thay đổi màu sắc ảnh
# #     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# #     hsv[:, :, 0] = h
# #     hsv[:, :, 1] = s
# #     hsv[:, :, 2] = v
# #     img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# #     # Tăng giảm saturation
# #     saturation = int(saturation)
# #     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# #     hsv[:,:,1] = hsv[:,:,1] * (saturation/255.0)
# #     img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


# #     cv2.imshow('image', img)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# # # Giải phóng bộ nhớ
# # cv2.destroyAllWindows()


# import cv2
# import numpy as np
# import click


# def red_green(image):
#     print("Change colors...")
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             image[i][j] = np.array([image[i][j][0], image[i][j][2],
#                                     image[i][j][1]])

#     return image


# def green_blue(image):
#     print("Change colors...")
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             image[i][j] = np.array([image[i][j][1], image[i][j][0],
#                                     image[i][j][2]])

#     return image


# def blue_red(image):
#     print("Change colors...")
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             image[i][j] = np.array([image[i][j][2], image[i][j][1],
#                                     image[i][j][0]])

#     return image


# @click.command()
# @click.option("-i", "--image", help="Path to image. Can be a relative path.")
# @click.option("-c", "--changer", default="red-green", help="Specify the changer. Can be red-green, green-blue or blue-red")
# @click.option("-r", "--result", default="new.jpg", help="Specify the images name.")
# def main(image, changer, result):
#     print("Load image...")
#     img = cv2.imread(image)
#     print("Determine changer...")
#     if changer == "red-green":
#         new_img = red_green(img)
#         cv2.imwrite(result, new_img)
#         print("Successful.")
#     elif changer == "green-blue":
#         new_img = green_blue(img)
#         cv2.imwrite(result, new_img)
#         print("Successful.")
#     elif changer == "blue-red":
#         new_img = blue_red(img)
#         cv2.imwrite(result, new_img)
#         print("Successful.")
#     else:
#         print("Changer does not exist.")


# if __name__ == "__main__":
#     main()

import math
import cv2
import glob
from PIL import Image, ImageEnhance
import os
import numpy as np
anh_can_doi_mau = "C:/Users/CCSX009/Desktop/BUICHI_768/KO_TU/*.jpg"
# anh_mau = "C:/Users/CCSX009/Desktop/MAU/2023-03-29_14-39-08-637244-C1.jpg"
# txt_mau = "C:/Users/CCSX009/Desktop/MAU/2023-03-29_14-39-08-637244-C1.txt"
anh_mau = "C:/Users/CCSX009/Desktop/BUICHI_768/MAU/2023-04-01_17-22-55-869666-C1.jpg"
txt_mau = "C:/Users/CCSX009/Desktop/BUICHI_768/MAU/2023-04-01_17-22-55-869666-C1.txt"
save_dir_change = "C:/Users/CCSX009/Desktop/BUICHI_768/SAVE_CHANGE/"



for path in glob.glob(anh_can_doi_mau):
    img = Image.open(path)
    enhancer = ImageEnhance.Brightness(img)
    enhanced_img = enhancer.enhance(2) 
    enhanced_img.save("r1.jpg")

    img = cv2.imread("r1.jpg")
    imgs1 = cv2.imread(anh_mau)

    hls_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    origin = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    hls_imgs1 = cv2.cvtColor(imgs1, cv2.COLOR_BGR2HLS)

    hls_img[:, :, 0] =  hls_imgs1[:, :, 0]
    # print(max((hls_img[:, :, 0])[0]))
    # max_val = float('-inf')

    # for i in range(hls_img.shape[0]):
    #     for j in range(hls_img.shape[1]):
    #         if hls_img[i][j][0] not in list(range(0,20)):
    #             hls_img[i][j][0] = hls_imgs1[i][j][0]


    with open(txt_mau, "r") as file:
        Lines = file.readlines()
        for j, line in enumerate(Lines):
            if int(line.strip().split(" ")[0]) == 0 :
                x = float(line.strip().split(" ")[1])
                y = float(line.strip().split(" ")[2])
                w = float(line.strip().split(" ")[3])
                h = float(line.strip().split(" ")[4])
                x0 = int((x - w/2)*1200)
                x1 = int((x + w/2)*1200)
                y0 = int((y - h/2)*1200)
                y1 = int((y + h/2)*1200)

                for j in range(x0,x1):
                    for i in range(y0,y1):
                        hls_img[i][j][0] = origin[i][j][0]

                # for i in range(0,1200):
                #     for j in range(0,1600):
                #         hls_img[i][j][0] = origin[i][j][0]

                # for j in range(600,1000):
                #     for i in range(50,250):
                #         if hls_img[i][j][0] in list(range(0,90)):

                #             hls_img[i][j][0] = origin[i][j][0]

                # for j in range(220,430):
                #     for i in range(470,770):
                #         hls_img[i][j][0] = origin[i][j][0]

                # for j in range(700,930):
                #     for i in range(1000,1200):    
                #         hls_img[i][j][0] = origin[i][j][0]

                # for j in range(1150,1360):
                #     for i in range(470,780):
                #         hls_img[i][j][0] = origin[i][j][0]


                img = cv2.cvtColor(hls_img, cv2.COLOR_HLS2BGR)

                name = os.path.basename(path)
                
                cv2.imwrite(save_dir_change + name,img)
