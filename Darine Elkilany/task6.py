 
import cv2 as cv
import numpy as np
import sys
path = '4.2.01.tiff'
img = cv.imread("4.2.01.tiff")
h ,w ,c = img.shape
mid_h,mid_w = h//2 , w//2
top_left = img[0:mid_h, 0:mid_w]
top_right = img[0:mid_h, mid_w:w]

bottom_left = img[mid_h:h, 0:mid_w]
bottom_right = img[mid_h:h, mid_w:w]

top = np.hstack((top_left, top_right))
bottom = np.hstack((bottom_left, bottom_right))
img = np.vstack((top, bottom))

cv.imshow('top_left', top_left)
cv.waitKey(0)

cv.imshow('top_right', top_right)
cv.waitKey(0)

cv.imshow('bottom_left', bottom_left)
cv.waitKey(0)

cv.imshow('bottom_right', bottom_right)
cv.waitKey(0)

cv.imshow('stitched', img)
cv.waitKey(0)
cv.destroyAllWindows()