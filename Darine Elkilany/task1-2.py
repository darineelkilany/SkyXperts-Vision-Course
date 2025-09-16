import cv2 as cv 

import numpy as np
import sys
img_BGR = cv.imread("4.2.07.tiff", cv.IMREAD_COLOR)
img_grey= cv.imread("4.2.07.tiff", cv.IMREAD_GRAYSCALE)
print (type(img_BGR))
print(type(img_grey))
cv.imshow('pepper image', img_BGR)
cv.imshow('pepper image', img_grey)
k=cv.waitkey(0)
cv.destroyAllWindow()