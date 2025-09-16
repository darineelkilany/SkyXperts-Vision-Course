import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np
import sys
img= cv.imread("4.2.07.tiff")

img_BGR = cv.cvtColor(img,cv.IMREAD_COLOR)
img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
img_LAB = cv.cvtColor(img,cv.COLOR_BGR2LAB)
img_grey= cv.imread("4.2.07.tiff", cv.IMREAD_GRAYSCALE)
print (type(img_BGR))
print (type(hsv_img))
print(type(img_RGB))
print(type(img_LAB))
print(type(img_grey))

cv.imshow('pepper image', img_BGR)
cv.waitKey(0)
cv.imshow('pepper image', img_grey)
cv.waitKey(0)

cv.imshow('pepper image', img_RGB)
cv.waitKey(0)

cv.imshow('pepper image', hsv_img)
cv.waitKey(0)

cv.imshow('pepper image', img_LAB)
cv.waitKey(0)
cv.destroyAllWindows()
