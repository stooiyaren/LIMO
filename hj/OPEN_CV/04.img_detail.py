import cv2

img = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('i', cv2.WINDOW_NORMAL)
print(img[100,200])
print(img.shape)

b,g,r = cv2.split(img)
rgb_img = cv2.merge([g,b,r])

cv2.imshow('i',img)
cv2.waitKey(0)