import cv2 as cv 
import numpy as np
import sys
img= cv.imread("4.2.07.tiff")
h,w , _ = img.shape
h = h
w = 100
dim = (h,w)

Width_img = cv.resize(img, dim , interpolation = cv.INTER_AREA)
h,w , _ = img.shape
h = 200
w = w
Height_img = cv.resize(img, dim , interpolation = cv.INTER_AREA)
dim = (h,w)
h,w , _ = img.shape
h = 300
w = 300
dim = (h,w)

HW_img = cv.resize(img, dim , interpolation = cv.INTER_AREA)

cv.imshow("Orignal", img)
cv.waitKey(0)
cv.imshow("Width image ", Width_img)
cv.waitKey(0)
cv.imshow("Height image ", Height_img)
cv.waitKey(0)
cv.imshow("Height and Width image ", HW_img)
cv.waitKey(0)
cv.destroyAllWindows()