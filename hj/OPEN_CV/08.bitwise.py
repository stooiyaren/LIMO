import cv2
import numpy as np

blank1 = np.zeros((480,640), np.uint8)
blank2 = np.zeros((480,640), np.uint8)
blank1[:,320:] = 255
cv2.circle(blank2,(320,240), 135,255,-1)
img = cv2.bitwise_or(blank1,blank2)
img2 = cv2.bitwise_and(blank1,blank2)
img3 = cv2.bitwise_xor(blank1,blank2)
img4 = cv2.bitwise_not(blank1,blank2)

cv2.imshow('blank1', blank1)
cv2.imshow('blank2', blank2)
cv2.imshow('mask', img)
cv2.imshow('mask', img2)
cv2.imshow('mask', img3)
cv2.imshow('mask', img4)
cv2.waitKey(0)