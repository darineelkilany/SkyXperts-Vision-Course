import cv2 as cv 
import numpy as np
import sys
img= cv.imread("4.2.07.tiff")
height, width , _= img.shape
center = (width/2, height/2)  
rotate_matrix = cv.getRotationMatrix2D(center=center, angle=45, scale=1)
rotate_matrix_90 = cv.getRotationMatrix2D(center=center, angle = 90, scale=1)
rotate_matrix_180 = cv.getRotationMatrix2D(center=center, angle = 180, scale=1)
rotated_image = cv.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))
rotated_image_90 = cv.warpAffine(src=img, M=rotate_matrix_90, dsize=(width, height))
rotated_image_180 = cv.warpAffine(src=img, M=rotate_matrix_180, dsize=(width, height))
cv.imshow("Orignal", img)
cv.waitKey(0)
cv.imshow("Rotated image 45 ", rotated_image)
cv.waitKey(0)
cv.imshow("Rotated image 90 ", rotated_image_90)
cv.waitKey(0)
cv.imshow("Rotated image 180 ", rotated_image_180)
cv.waitKey(0)
cv.destroyAllWindows()