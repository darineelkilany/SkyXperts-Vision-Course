import cv2 as cv 
import numpy as np
import sys
img= cv.imread("4.2.07.tiff")
Scale_percent = 60
h,w , _ = img.shape
h = int(Scale_percent *h / 100)
w = int(Scale_percent * w / 100 )
dim = (h,w)

down_img = cv.resize(img, dim , interpolation = cv.INTER_AREA)
Scale_percent = 200
h,w , _ = img.shape
h = int(Scale_percent *h / 100)
w = int(Scale_percent * w / 100 )
dim = (h,w)

UP_img = cv.resize(img, dim , interpolation = cv.INTER_AREA)
print(down_img.shape)
print(UP_img.shape)
print(img.shape)
cv.imshow("Orignal", img)
cv.waitKey(0)
cv.imshow("Down Scaled image ", down_img)
cv.waitKey(0)
cv.imshow("UP Scaled image ", UP_img)
cv.waitKey(0)
cv.destroyAllWindows()