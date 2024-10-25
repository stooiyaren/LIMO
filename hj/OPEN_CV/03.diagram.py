import cv2
import numpy as np

black =(0,0,0)
red = (0,0,255)
yellow = (0,255,255)
green = (0,255,0)
cyan = (255,255,0)
blue = (255,0,0)
purple = (255,0,255)
white = (255,255,255)

blank = np.zeros((480,680,3), np.uint8) #(y,x)
cv2.circle(blank, (340,240), 60, black, 1) #(center(x,y),radius,color,thick)
cv2.rectangle(blank, (100,200), (200,400), white, 10)
cv2.line(blank, (400,200), (500,300), blue, 5)
pt1=(100,100)
pt2=(100,300)
pt3=(200,400)
pt4=(400,200)
pt5=(300,100)
pts =np.array((pt1,pt2,pt3,pt4,pt5))
# cv2.polylines(blank,[pts],True,red,5)
cv2.fillPoly(blank,[pts],red)
cv2.putText(blank, "wego",(100, 200),cv2.FONT_HERSHEY_COMPLEX,3,white,5)

cv2.imshow("blank",blank)
cv2.waitKey(1)