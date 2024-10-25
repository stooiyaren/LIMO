import cv2

img = cv2.imread('forest.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('i', cv2.WINDOW_NORMAL)
cv2.imshow('i', img)
cv2.waitKey(0)
# cv2.imwrite("i_gray.jpg",img)