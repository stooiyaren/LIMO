import cv2
import numpy as np

img = cv2.imread('forest.jpg', cv2.IMREAD_COLOR)
blank = np.zeros_like(img, np.uint8)
bi = blank+255

cv2.putText(blank, "Thumbnail",(80, 260),cv2.FONT_HERSHEY_COMPLEX,6,(255,255,255),15)
cv2.putText(bi, "Thumbnail",(80, 260),cv2.FONT_HERSHEY_COMPLEX,6,(0,0,0),15)
add_img = cv2.add(img, blank)
ai = cv2.add(img, bi)

subtract_img = cv2.subtract(img,blank)
si = cv2.subtract(img, bi)

alpha = 0.8
aa = cv2.addWeighted(img, alpha, blank, )

cv2.namedWindow('i', cv2.WINDOW_NORMAL)
cv2.imshow('i',img)
cv2.imshow('blank', blank)
cv2.imshow('add_img', add_img)
cv2.imshow('sub', subtract_img)
cv2.imshow('b',bi)
cv2.imshow('a',ai)
cv2.imshow('s',si)
cv2.waitKey(0)