import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('blur1.webp')  # same folder mein image rakho

if img is None:
    print("Error: Image not found.")
    exit()

rows, cols = img.shape[:2]

M_left   = np.float32([[1, 0, -50], [0, 1, 0]])
M_right  = np.float32([[1, 0,  50], [0, 1, 0]])
M_top    = np.float32([[1, 0,  0],  [0, 1, -50]])
M_bottom = np.float32([[1, 0,  0],  [0, 1,  50]])

img_left   = cv2.warpAffine(img, M_left,   (cols, rows))
img_right  = cv2.warpAffine(img, M_right,  (cols, rows))
img_top    = cv2.warpAffine(img, M_top,    (cols, rows))
img_bottom = cv2.warpAffine(img, M_bottom, (cols, rows))

# Convert BGR to RGB for display
img_left   = cv2.cvtColor(img_left, cv2.COLOR_BGR2RGB)
img_right  = cv2.cvtColor(img_right, cv2.COLOR_BGR2RGB)
img_top    = cv2.cvtColor(img_top, cv2.COLOR_BGR2RGB)
img_bottom = cv2.cvtColor(img_bottom, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 8))
plt.subplot(221), plt.imshow(img_left), plt.title('Left')
plt.subplot(222), plt.imshow(img_right), plt.title('Right')
plt.subplot(223), plt.imshow(img_top), plt.title('Top')
plt.subplot(224), plt.imshow(img_bottom), plt.title('Bottom')
plt.axis('off')
plt.show()
