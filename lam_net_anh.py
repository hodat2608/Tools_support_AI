import torch,cv2
from basicsr.archs.rrdbnet_arch import RRDBNet

import torch
from basicsr.archs.rrdbnet_arch import RRDBNet

device = torch.device('cpu')
model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32)
# model.load_state_dict(torch.load('realesr-general-wdn-x4v3.pth'), strict=True)
model.load_state_dict(torch.load('realesr-general-wdn-x4v3.pth', map_location=torch.device('cpu')), strict=True)
model.eval()
model = model.to(device)

def enhance_image(img):
    img = torch.from_numpy(img.transpose((2, 0, 1))).float().unsqueeze(0) / 255.0
    img = img.to(device)
    with torch.no_grad():
        output = model(img)
    output = output.squeeze().cpu().numpy().transpose((1, 2, 0))
    output = (output * 255.0).clip(0, 255).astype('uint8')
    return output

img = cv2.imread('C:/Users/CCSX009/Desktop/New folder/2023-04-21_03-03-18-142806-1TC.jpg')
enhanced_img = enhance_image(img)
cv2.imshow(enhanced_img)
cv2.imwrite('enhanced_image.jpg', enhanced_img)