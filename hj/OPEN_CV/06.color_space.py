import cv2
import numpy as np

blank = np.zeros((480,640,3),np.uint8)
blank[:,0:640//3] = (255,0,0)
blank[:,640//3:640*2//3] = (0,255,0)
blank[:,640*2//3:] = (0,0,255)

bgr_img = cv2.cvtColor(blank,cv2.COLOR_BGR2HSV)

cv2.imshow("blank", blank)
cv2.imshow("bgr_img",bgr_img)
cv2.waitKey(0)