import cv2 as cv 
import numpy as np
import sys
img= cv.imread("4.2.07.tiff")
Cropped_img = img [20:200 , 50:200]
cv.imshow("Orignal", img)
cv.waitKey(0)
cv.imshow("Cropped img ", Cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()