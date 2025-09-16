import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np
import sys
import skimage.util 
from skimage.util  import random_noise
path = '4.2.07.tiff'
img= cv.imread("4.2.07.tiff", cv.IMREAD_GRAYSCALE)

plt.figure()
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title('Original Image')
plt.show()


noisyImg = random_noise(img, mode="s&p",amount=0.05)
noisyImg = np.array(255*noisyImg, dtype="uint8")
plt.figure() 
plt.imshow(noisyImg, cmap="gray", vmin=0, vmax=255)
plt.title('Noisy Image')
plt.axis('off')
plt.show()
