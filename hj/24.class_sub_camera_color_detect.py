import rospy
import cv2
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import numpy as np

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        rospy.Subscriber("/camera/rgb/image_raw/compressed", CompressedImage, self.camera_cb)
        self.bridge = CvBridge()

    def camera_cb(self, msg):
        # print(msg)
        cv_img = self.bridge.compressed_imgmsg_to_cv2(msg)
        hsv_img = cv2.cvtColor(cv_img,cv2.COLOR_BGR2HSV)
        lower = np.array([0,0,240])
        upper = np.array([179,15,255])
        mask = cv2.inRange(hsv_img, lower, upper)
        # msk = cv2.merge([mask,mask,mask])
        # and_img = cv2.bitwise_and(cv_img, mask)

        cv2.imshow("cv_img", cv_img)
        # cv2.imshow("hsv_img", hsv_img)
        # cv2.imshow('and', and_img)
        # cv2.imshow("mask", mask)
        # cv2.imshow('msk', msk)
        cv2.waitKey(1)
    
class_sub = Class_sub()
rospy.spin()