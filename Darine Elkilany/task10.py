import cv2
import matplotlib.pyplot as plt 
import numpy as np
import sys
img= cv2.imread("4.2.07.tiff")
blurimag = cv2.blur(img ,ksize = (5,5))
kernel = np.array([[-1,5,-1],[0,-1,0]])

sharpImg = cv2.filter2D(img, -1, kernel)
avg_image = cv2.filter2D(img , ddepth = -1 , kernel = kernel)
cv2.imshow('Original image',img)
cv2.waitKey(0)
cv2.imshow('BLURRED',blurimag)
cv2.waitKey(0)
cv2.destroyAllWindows()


