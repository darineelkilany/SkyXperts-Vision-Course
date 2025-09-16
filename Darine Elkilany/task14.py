import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np
import sys
import skimage.util 
from skimage.util  import random_noise
path = '4.2.07.tiff'
img= cv.imread("4.2.07.tiff", cv.IMREAD_GRAYSCALE)

# i didn't know how to do it