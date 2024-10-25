import cv2
import numpy as np

img = cv2.imread("forest.jpg", cv2.IMREAD_COLOR)
b,g,r = cv2.split(img)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower = np.array([105,0,0])
upper = np.array([135,255,255])
mask = cv2.inRange(hsv_img,lower,upper)
cv2.imshow("mask",mask)
cv2.imshow('img',img)

cv2.waitKey(0)