import cv2 as cv 
import numpy as np
import sys
img= cv.imread("4.2.07.tiff")
scale_up_x = 1.2
scale_up_y = 1.2
scale_down = 0.6
 
scaled_f_down = cv.resize(img, None, fx= scale_down, fy= scale_down, interpolation= cv.INTER_LINEAR)
scaled_f_up = cv.resize(img, None, fx= scale_up_x, fy= scale_up_y, interpolation= cv.INTER_LINEAR)
cv.imshow("Orignal", img)
cv.waitKey(0)
cv.imshow("scale up ", scaled_f_up)
cv.waitKey(0)
cv.imshow("scale down ", scaled_f_down)
cv.waitKey(0)
cv.destroyAllWindows()