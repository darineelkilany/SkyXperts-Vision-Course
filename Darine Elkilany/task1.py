import cv2 as cv 
path = './D:\Darine Elkilany\4.2.07.tiff/'
img = cv.imread('4.2.07.tiff')
cv.__version__
print(type(img.shape))
assert img is not None , "Cant read image"
cv.imshow("papper image ", img)
k = cv.waitKey(0)
cv.destroyAllWindows()