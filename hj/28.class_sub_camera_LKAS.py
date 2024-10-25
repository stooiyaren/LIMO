import rospy
import cv2
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import numpy as np

black =(0,0,0)
red = (0,0,255)
yellow = (0,255,255)
green = (0,255,0)
cyan = (255,255,0)
blue = (255,0,0)
purple = (255,0,255)
white = (255,255,255)

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        rospy.Subscriber("/camera/rgb/image_raw/compressed", CompressedImage, self.camera_cb)
        self.pub = rospy.Publisher("/cmd_vel",Twist, queue_size= 1)
        self.cmd_msg = Twist()
        self.bridge = CvBridge()

    def camera_cb(self, msg):
        cv_img = self.bridge.compressed_imgmsg_to_cv2(msg)
        
        y, x, channel = cv_img.shape

        hsv_img = cv2.cvtColor(cv_img,cv2.COLOR_BGR2HSV)


        white_lower = np.array([0,0,150])
        white_upper = np.array([179,20,255])
        white_filter = cv2.inRange(hsv_img, white_lower, white_upper)

        yellow_lower = np.array([15, 60, 60])
        yellow_upper = np.array([45, 255, 255])
        yellow_filter = cv2.inRange(hsv_img, yellow_lower,yellow_upper)

        combine_filter = cv2.bitwise_or(white_filter, yellow_filter)

        and_img = cv2.bitwise_and(cv_img,cv_img,mask=yellow_filter)

        margin_x = 250
        margin_y = 300
        src_pt1 = (0,y)
        src_pt2 = (margin_x,margin_y)
        src_pt3 = (x-margin_x,margin_y)
        src_pt4 = (x,y)
        src_pts = np.float32([src_pt1,src_pt2,src_pt3,src_pt4])

        dst_margin_x = 120
        dst_pt1 = (dst_margin_x,y)
        dst_pt2 = (dst_margin_x,0)
        dst_pt3 = (x - dst_margin_x,0)
        dst_pt4 = (x-dst_margin_x,y)
        dst_pts = np.float32([dst_pt1,dst_pt2,dst_pt3,dst_pt4])
        
        matrix = cv2.getPerspectiveTransform(src_pts,dst_pts)
        warp_img = cv2.warpPerspective(and_img, matrix, (x,y))
        gray_img = cv2.cvtColor(warp_img, cv2.COLOR_BGR2GRAY)
        bin_img = np.zeros_like(gray_img)
        bin_img[gray_img != 0] = 1

        histogram = np.sum(bin_img, axis= 0)
        center_index = x//2
        left_side = histogram[:center_index]
        right_side = histogram[center_index:]
        max_left_side = np.argmax(left_side)
        max_right_side = np.argmax(right_side)+center_index
        avg_index = (max_left_side + max_right_side)//2

        error_index = (avg_index - center_index)
        self.cmd_msg.linear.x = 0.1
        self.cmd_msg.angular.z = error_index*0.01
        self.pub.publish(self.cmd_msg)

        cv2.line(warp_img,(max_left_side,0),(max_left_side,y),red,3)
        cv2.line(warp_img,(max_right_side,0),(max_right_side,y),blue,3)
        cv2.line(warp_img,(avg_index,0),(avg_index,y),yellow,3)
        cv2.line(warp_img,(center_index,0),(center_index,y), green, 3)

        cv2.circle(cv_img, src_pt1,20, blue, -1)
        cv2.circle(cv_img, src_pt2,20, green, -1)
        cv2.circle(cv_img, src_pt3,20, red, -1)
        cv2.circle(cv_img, src_pt4,20, yellow, -1)



        cv2.imshow("cv_img", cv_img)
        # cv2.imshow("and_img", and_img)
        cv2.imshow('warp_img', warp_img)
        # cv2.imshow("gray_img", gray_img)
        # cv2.imshow('bin_img', bin_img)
        cv2.waitKey(1)
    
class_sub = Class_sub()
rospy.spin()