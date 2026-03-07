

import cv2

print(cv2.__version__)

img = cv2.imread("blur1.webp")

if img is None:
    print("Image not found. Check file name or path.")
    exit()

resized_image = cv2.resize(img, (300, 300))

# Original
cv2.imshow("Original Image", resized_image)
cv2.waitKey(0)

# Gaussian Blur
gaussian = cv2.GaussianBlur(resized_image, (15, 15), 0)
cv2.imshow("Gaussian Blur", gaussian)
cv2.waitKey(0)

# Median Blur
median = cv2.medianBlur(resized_image, 11)
cv2.imshow("Median Blur", median)
cv2.waitKey(0)

# Bilateral Filter
bilateral = cv2.bilateralFilter(resized_image, 15, 150, 150)
cv2.imshow("Bilateral Filter", bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()


