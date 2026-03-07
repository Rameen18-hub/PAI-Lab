import cv2
import numpy as np

img = cv2.imread('blur1.webp')


if img is None:
    print("Error: Image not found. Please check the file path and name.")
    exit()

img = img.astype(np.float32) 
c = 255 / (np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)


log_transformed = np.uint8(log_transformed)

cv2.imwrite('log_transformed.jpg', log_transformed)

print("Log transformed image saved successfully!")

import cv2
import numpy as np

# Open the image.
img = cv2.imread('blur1.webp')

# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2]:
    
    # Apply gamma correction.
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')

    # Save edited images.
    cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)


    import cv2
import numpy as np

# Function to map each intensity level to output intensity level.
def pixelVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2

# Open the image.
img = cv2.imread('blur1.webp')

# Define parameters.
r1 = 70
s1 = 0
r2 = 140
s2 = 255

# Vectorize the function to apply it to each value in the Numpy array.
pixelVal_vec = np.vectorize(pixelVal)

# Apply contrast stretching.
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

# Save edited image.
cv2.imwrite('contrast_stretch.jpg', contrast_stretched)