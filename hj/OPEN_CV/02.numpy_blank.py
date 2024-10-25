import cv2
import numpy as np

blank = np.zeros((480,640,3),np.uint8)+128
# blank[300:400] = 255 # insert garo
blank[230:250,320:340] = (120,125,0) # insert sero
cv2. imshow("blank", blank)
cv2.waitKey(0)