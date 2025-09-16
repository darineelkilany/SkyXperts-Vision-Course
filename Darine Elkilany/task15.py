import cv2 
import matplotlib.pyplot as plt 
import numpy as np
import sys
import skimage.util 
from skimage.util  import random_noise
camera_id = 0
delay = 400
window_name = 'frame'

cap = cv2.VideoCapture(camera_id)

if not cap.isOpened():
    sys.exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
 gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
 
 
cv2.imshow(window_name, frame)
if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

   
cap.release()
cv2.destroyWindow(window_name)


 