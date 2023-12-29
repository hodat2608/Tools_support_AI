# # import numpy as np
# # import matplotlib.pyplot as plt
# # from PIL import Image, ImageDraw
# # import colorsys
# # import cv2
# # def on_click(event):
# #     if event.xdata is not None and event.ydata is not None:
# #         x = int(event.xdata)
# #         y = int(event.ydata)
# #         # rgb = (image[y, x] * 255).astype(int)

# #         img = Image.open(image_path)
# #         # Convert image to HSV color space
# #         img2 = cv2.imread(image_path)
# #         hsv_img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
# #         h, s, v = hsv_img[y, x]

# #         # img = Image.open(image_path).convert("RGBA")
# #         r, g, b = img.getpixel((x, y))
# #         # h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
# #         # print(f"Selected point (x, y): ({x}, {y})")
# #         print(f"RGB value: {r ,g ,b, h,s,v}")

# # image_path = 'C:/Users/CCSX009/Pictures/Camera Roll/2023-07-26_00-05-10-2300.jfz.jpg'  # Thay thế bằng đường dẫn thực tế đến bức ảnh
# # image = plt.imread(image_path)

# # fig, ax = plt.subplots()
# # ax.imshow(image)
# # ax.set_title('Click a point to get RGB value')

# # cid = fig.canvas.mpl_connect('button_press_event', on_click)
# # plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image, ImageDraw
# import colorsys
# import cv2
# def on_click(event):
#     if event.xdata is not None and event.ydata is not None:
#         x = int(event.xdata)
#         y = int(event.ydata)
#         # rgb = (image[y, x] * 255).astype(int)

#         img = Image.open(image_path)
#         # Convert image to HSV color space
#         img2 = cv2.imread(image_path)
#         hsv_img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
#         h, s, v = hsv_img[y, x]

#         # img = Image.open(image_path).convert("RGBA")
#         r, g, b = img.getpixel((x, y))
#         # h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
#         # print(f"Selected point (x, y): ({x}, {y})")
#         print(f"RGB value: {r ,g ,b, h,s,v}")

# image_path = 'C:/Users/CCSX009/Pictures/Camera Roll/New folder/2023-07-26_00-05-10-2300.jfz.jpg'  # Thay thế bằng đường dẫn thực tế đến bức ảnh
# image = plt.imread(image_path)

# fig, ax = plt.subplots()
# ax.imshow(image)
# ax.set_title('Click a point to get RGB value')

# cid = fig.canvas.mpl_connect('button_press_event', on_click)
# plt.show()


# # R: 80 100
# # G: 80 100 
# # B: 60 80


# # from PIL import Image

# # def scan_image(image_path):
# #     # Load the image
# #     img = Image.open(image_path)
# #     width, height = img.size
    
# #     # Loop through all pixels
# #     for y in range(height):
# #         for x in range(width):
# #             r, g, b = img.getpixel((x, y))
            
# #             # Check if RGB values are within the specified range
# #             if 155 <= r <= 175 and 152 <= g <= 172 and 172 <= b <= 192:
# #                 print(f"Found pixel at ({x}, {y}) with RGB values: ({r}, {g}, {b})")

# # # Replace 'image_path' with the actual path to your image file
# # image_path = '1.jpg'
# # scan_image(image_path)


# # R: 80 100
# # G: 80 100 
# # B: 60 80
# # 25 35
# # 55 65
# # 85 95
# # 25  <= h <= 35 and 55 <= s <= 65 and 85 <= v <= 95
# from PIL import Image, ImageDraw

# def draw_points(image_path):
#     # Load the image
#     img = Image.open(image_path)
#     width, height = img.size

#     # img = img[:,0:int(width/2)]
#     img2 = cv2.imread(image_path)
#     # img2 = img2[:,0:int(width/2)]
#     hsv_img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    
#     # Create a new image to draw the points on
#     # draw = ImageDraw.Draw(img)
    
#     # Loop through all pixels
#     for y in range(int(height/2)):
#         for x in range(int(width/2)):
#             r, g, b = img.getpixel((x, y))
#             h, s, v = hsv_img[y, x]
                

#             r1, g1, b1 = img.getpixel((x+1, y))
#             h1, s1, v1 = hsv_img[y, x+1]

#             r2, g2, b2 = img.getpixel((x, y+1))
#             h2, s2, v2 = hsv_img[y+1, x]
                
#             # Check if RGB values are within the specified range
#             # if 80 + 5  <= r <= 100 - 5 and 80 + 5 <= g <= 100 - 5 and 60 + 5 <= b <= 80 - 5 and 25  <= h <= 35 and 55 <= s <= 65 and 85 <= v <= 95:
#             #     if 80 + 5  <= r1 <= 100 - 5 and 80 + 5 <= g1 <= 100 - 5 and 60 + 5 <= b1 <= 80 - 5 and 25  <= h1 <= 35 and 55 <= s1 <= 65 and 85 <= v1 <= 95:
#             #         if 80 + 5  <= r2 <= 100 - 5 and 80 + 5 <= g2 <= 100 - 5 and 60 + 5 <= b2 <= 80 - 5 and 25  <= h2 <= 35 and 55 <= s2 <= 65 and 85 <= v2 <= 95:
                        
#             #             return x-6,y-6
            
#             if 110 + 5  <= r <= 120 + 5  and 110 + 8 <= g <= 123 + 5 and 102 + 5 <= b <= 117 and 33 <= h <= 43 and 18 <= s <= 30 and 115 <= v <= 128:
#                 if 110 + 5  <= r1 <= 120 + 5  and 110 + 8 <= g1 <= 123 + 5 and 102 + 5 <= b1 <= 117 and 33 <= h1 <= 43 and 18 <= s1 <= 30 and 115 <= v1 <= 128:
#                     if 110 + 5  <= r2 <= 120 + 5  and 110 + 8 <= g2 <= 123 + 5 and 102 + 5 <= b2 <= 117 and 33 <= h2 <= 43 and 18 <= s2 <= 30 and 115 <= v2 <= 128:
                        
#                         return x-6,y-6

#     # Save or display the modified image
#     # img.show()  # You can use img.save('output_image.jpg') to save the image

# # Replace 'image_path' with the actual path to your image file

# import glob,os,shutil
# path = 'C:/Users/CCSX009/Pictures/Camera Roll/New folder'
# images_path = path + '*.jpg'
# try :
#     os.makedirs(path + 'TEMP', exist_ok=True)
# except :
#     pass 
# out_dir = path + 'TEMP/'
# for image_path in glob.glob(images_path):
#     img = Image.open(image_path)
#     width, height = img.size
#     draw = ImageDraw.Draw(img)
#     try:
#         x, y = draw_points(image_path)
#         print(x/1600,y/1200)
#     except:
#         x,y =0,0
# #     w = 0.181875 
# #     h = 0.142500
# #     x1 = x/1600 + w/2
# #     y1 = y/1200 + h/2
# #     tenf = os.path.basename(image_path)
# #     print(out_dir + tenf[:-3]+'txt')
# #     out = open(out_dir + tenf[:-3]+'txt', 'w')
# #     with open(image_path[:-3]+'txt', 'r') as f:
# #         # while True:
# #         #     line = f.readline()
# #         #     if not line:
# #         #         break
# #         #     tmp = line.split()    
# #         #     if int(tmp[0])== 0:                
# #         #         line = '0' + ' ' + str(x1)+ ' ' + str(y1)+ ' 0.181875 0.142500/n'
# #         try:
# #             out.writelines('0' + ' ' + str(x1)+ ' ' + str(y1)+ ' 0.181875 0.142500/n')  
# #         except:
# #             pass  
# #     out.close()
# #     # os.replace(out_dir + tenf[:-3]+'txt', image_path[:3]+'txt') 
# # print('compelted')
# # # shutil.rmtree(out_dir)
#     print(x/1600,y/1200)
#     draw.point((x, y), fill=(255, 0, 0))  # Change fill color as needed
#     img2 = cv2.imread(image_path)

#     cv2.circle(img2, (x, y), 3, (0, 0, 255), -1)
#     cv2.imshow(image_path, img2)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     # img.show()
    # draw_points(image_path)

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import colorsys
import cv2
# def on_click(event):
#     if event.xdata is not None and event.ydata is not None:
#         x = int(event.xdata)
#         y = int(event.ydata)
#         # rgb = (image[y, x] * 255).astype(int)

#         img = Image.open(image_path)
#         # Convert image to HSV color space
#         img2 = cv2.imread(image_path)
#         hsv_img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
#         h, s, v = hsv_img[y, x]

#         # img = Image.open(image_path).convert("RGBA")
#         r, g, b = img.getpixel((x, y))
#         # h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
#         # print(f"Selected point (x, y): ({x}, {y})")
#         print(f"RGB value: {r ,g ,b, h,s,v}")

# image_path = '1.jpg'  # Thay thế bằng đường dẫn thực tế đến bức ảnh
# image = plt.imread(image_path)

# fig, ax = plt.subplots()
# ax.imshow(image)
# ax.set_title('Click a point to get RGB value')

# cid = fig.canvas.mpl_connect('button_press_event', on_click)
# plt.show()


# R: 80 100
# G: 80 100 
# B: 60 80


# from PIL import Image

# def scan_image(image_path):
#     # Load the image
#     img = Image.open(image_path)
#     img2 = cv2.imread(image_path)
#     # img2 = img2[:,0:int(width/2)]
#     hsv_img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

#     width, height = img.size
#     draw = ImageDraw.Draw(img)
#     # Loop through all pixels
#     for y in range(int(height*3/4),int(height)):
#       for x in range(int(width*2/4),int(width*3/4)):
#             r, g, b = img.getpixel((x, y))
#             h, s, v = hsv_img[y, x]
#             # Check if RGB values are within the specified range
#             if 70 <= r <= 75 and 65 <= g <= 75 and 60 <= b <= 70 and 10 <= h <= 25 and 15 <= s <= 20 and 70 <= v <= 80:
#                 print(f"Found pixel at ({x}, {y}) with RGB values: ({r}, {g}, {b})")
#                 draw.point((x, y), fill=(255, 0, 0)) 
#     img.show()

# image_path = 'C:/Users/CCSX009/Pictures/Camera Roll/New folderTEMP/2023-08-19_10-14-16-835878.jpg'
# scan_image(image_path)


# R: 80 100
# G: 80 100 
# B: 60 80
# 25 35
# 55 65
# 85 95
# 25  <= h <= 35 and 55 <= s <= 65 and 85 <= v <= 95
from PIL import Image, ImageDraw

def draw_points(image_path):
    # Load the image
    img = Image.open(image_path)
    width, height = img.size

    # img = img[:,0:int(width/2)]
    img2 = cv2.imread(image_path)
    # img2 = img2[:,0:int(width/2)]
    hsv_img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    
    # Create a new image to draw the points on
    draw = ImageDraw.Draw(img)
    
    # # Loop through all pixels
    # for y in range(int(height/4),int(height/3)):
    #     for x in range(int(width/5),int(width/4)):
    for y in range(int(height*3/4),int(height-1)):
      for x in range(int(width*2/4),int(width*3/4)):
            r, g, b = img.getpixel((x, y))
            h, s, v = hsv_img[y, x]
                
            r1, g1, b1 = img.getpixel((x+1, y))
            h1, s1, v1 = hsv_img[y, x+1]

            r2, g2, b2 = img.getpixel((x, y+1))
            h2, s2, v2 = hsv_img[y+1, x]
                
            # Check if RGB values are within the specified range
            if 70 <= r <= 75 and 65 <= g <= 75 and 60 <= b <= 70 and 10 <= h <= 25 and 15 <= s <= 20 and 70 <= v <= 80:
                if 70 <= r1 <= 75 and 65 <= g1 <= 75 and 60 <= b1 <= 70 and 10 <= h1 <= 25 and 15 <= s1 <= 20 and 70 <= v1 <= 80:
                    if 70 <= r2 <= 75 and 65 <= g2 <= 75 and 60 <= b2 <= 70 and 10 <= h2 <= 25 and 15 <= s2 <= 20 and 70 <= v2 <= 80:
                        # draw.point((x, y), fill=(255, 0, 0)) 
                        return x,y
                        
            # if 205 <= r <= 220 and 210 <= g <= 240+ 5 and 230 + 5 <= b <= 255 and 95 <= h <= 110 and 36 <= s <= 40 and 230 <= v <= 250:
            #     if 205 <= r1 <= 220 and 210 <= g1 <= 240+ 5 and 230 + 5 <= b1 <= 255 and 95 <= h1 <= 110 and 36 <= s1 <= 40 and 230 <= v1 <= 250:
            #         if 205 <= r2 <= 220 and 210 <= g2 <= 240+ 5 and 230 + 5 <= b2 <= 255 and 95 <= h2 <= 110 and 36 <= s2 <= 40 and 230 <= v2 <= 250:
            #             draw.point((x, y), fill=(255, 0, 0))  # Change fill color as needed
            #             return x-25,y
    # img.show()
          
images_path = "C:/Users/CCSX009/Pictures/Camera Roll/New folderTEMP/*.jpg"
import glob
for image_path in glob.glob(images_path):
    img = Image.open(image_path)
    width, height = img.size
    draw = ImageDraw.Draw(img)
    try:
        x, y = draw_points(image_path)
    except:
        x,y =(0,0)
    print(x/1600,y/1200)
    draw.point((x, y), fill=(255, 0, 0))  # Change fill color as needed
    img2 = cv2.imread(image_path)


    cv2.circle(img2, (x, y), 5, (0, 0, 255), -1)
    img2 = cv2.resize(img2,(800,600))
    cv2.imshow(image_path, img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    draw_points(image_path)

