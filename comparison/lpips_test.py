# LPIPS: Learned Perceptual Image Patch Similarity

import lpips
import torch
from PIL import Image
import torchvision.transforms as transforms

loss_fn = lpips.LPIPS(net='alex')  

transform = transforms.Compose([
    transforms.Resize((512, 512)),  
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5]*3, std=[0.5]*3)
])

img1 = Image.open('/root/gaussian-splatting/ssim/original.jpg').convert('RGB')
img2 = Image.open('/root/gaussian-splatting/ssim/gs.png').convert('RGB')
img3 = Image.open('/root/gaussian-splatting/ssim/gs_improve.png').convert('RGB')

t1 = transform(img1).unsqueeze(0)
t2 = transform(img2).unsqueeze(0)
t3 = transform(img3).unsqueeze(0)

# LPIPS
d1 = loss_fn(t1, t2)
d2 = loss_fn(t1, t3)

# low values, more like the original

print(f"LPIPS original vs gs: {d1.item():.4f}")
print(f"LPIPS original vs gs_improve: {d2.item():.4f}")
