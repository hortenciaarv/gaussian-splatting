import cv2
import numpy as np

def edge_sharpness_score(image):
    # Detectar bordes con Sobel
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)
    return np.mean(gradient_magnitude)

# Leer imágenes en escala de grises
img_original = cv2.imread('original.jpg', cv2.IMREAD_GRAYSCALE)
img_gs = cv2.imread('gs.png', cv2.IMREAD_GRAYSCALE)
img_gs_bg = cv2.imread('gs_improve.png', cv2.IMREAD_GRAYSCALE)

# Redimensionar si es necesario
img_gs = cv2.resize(img_gs, (img_original.shape[1], img_original.shape[0]))
img_gs_bg = cv2.resize(img_gs_bg, (img_original.shape[1], img_original.shape[0]))

# Calcular nitidez de bordes
score_gs = edge_sharpness_score(img_gs)
score_bg = edge_sharpness_score(img_gs_bg)

print(f"Sharpness GS: {score_gs:.2f}")
print(f"Sharpness GS + BG: {score_bg:.2f}")
