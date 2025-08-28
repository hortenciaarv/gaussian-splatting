from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('/root/gaussian-splatting/ssim/original.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('/root/gaussian-splatting/ssim/gs.png', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('/root/gaussian-splatting/ssim/gs_improve.png', cv2.IMREAD_GRAYSCALE)

# image size
print(f"original: {img1.shape}")
print(f"gs: {img2.shape}")
print(f"gs_improve: {img3.shape}")

#resize image
if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
if img1.shape != img3.shape:
    img3 = cv2.resize(img3, (img1.shape[1], img1.shape[0]))


# SSIM
score, diff = ssim(img1, img2, full=True)
score2, diff2 = ssim(img1, img3, full=True)
print(f"SSIM gs: {score}")
print(f"SSIM gs improve: {score2}")


# DSSIM
diff_map = (1 - diff)  # cuanto más alto, más diferencia

plt.imshow(diff_map, cmap='hot')
plt.title("Original and GS")
plt.colorbar()
plt.savefig("diff_map_gs.png")


diff_map2 = (1 - diff2)  # cuanto más alto, más diferencia

plt.imshow(diff_map2, cmap='hot')
plt.title("Original and GS with BG")
plt.savefig("diff_map_gs_bg.png")