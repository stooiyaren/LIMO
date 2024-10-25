import rospy
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        rospy.Subscriber("/camera/rgb/image_raw/compressed", CompressedImage, self.camera_cb)
        self.pub = rospy.Publisher('/cmd_msg', Twist, queue_size=1)

        self.bridge = CvBridge()

    def camera_cb(self, msg):
        cv_img = self.bridge.compressed_imgmsg_to_cv2(msg)
        hsv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv_img)

        red = 0
        yellow = 30
        green = 60
        cyan = 90
        blue = 120
        magenta = 150
        color = yellow

        if color == red:
            red1_lower = np.array([red,128,128])
            red1_upper = np.array([red + 15,255,255])
            red1_filter = cv2.inRange(hsv_img, red1_lower, red1_upper)

            red2_lower = np.array([180 - red,128,128])
            red2_upper = np.array([180, 255,255])
            red2_filter = cv2.inRange(hsv_img,red2_lower,red2_upper)

            filter = cv2.bitwise_or(red1_filter,red2_filter)
        else:
            lower = np.array([color -20, 140,60])
            upper = np.array([color +20, 255,255])
            filter = cv2.inRange(hsv_img,lower, upper)

        and_msg = cv2.bitwise_and(cv_img,cv_img,mask = close_filter)
        gray_img = cv2.cvtColor(and_msg, cv2.COLOR_BGR2GRAY)

        thresh_h = cv2.threshold(gray_img, 40, 255, cv2.THRESH_BINARY)
        struct = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        close_filter = cv2.morphologyEx(thresh_h,cv2.MORPH_CLOSE, struct)


        bin_img = np.zeros_like(filter)
        bin_img = gray_img
        bin_img[gray_img<30] = 0
        hist_x = np.sum(bin_img, axis = 0)
        hist_y = np.sum(bin_img, axis = 1)

        try:
            cnt = contour[0]
            x,y,w,h = cv2.

        

        center_index = x//2
        self.cmd_msg.angular.z = (center_x - center_index)
        cv2.imshow("filter", filter)
        cv2.imshow("cv_img",cv_img)
        cv2.waitKey(1)


class_sub = Class_sub()
rospy.spin()