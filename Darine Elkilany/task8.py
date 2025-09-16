import cv2 as cv 
import numpy as np
import sys
img= cv.imread("4.2.07.tiff")

(h ,w)= img.shape[:2]
center =(w // 2, h//2)
angle=45
scale=0.5
M = cv.getRotationMatrix2D(center, angle, scale)
rotated_image = cv.warpAffine(img,M,(w,h))
print(img.shape)
print(rotated_image.shape)
cv.imshow("original",img)
cv.waitKey(0)
cv.imshow("Rotate and scale", rotated_image)
cv.waitKey(0)
cv.destroyAllWindows()