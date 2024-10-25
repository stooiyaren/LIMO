import rospy
import cv2
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge


class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        rospy.Subscriber("/camera/rgb/image_raw/compressed", CompressedImage, self.camera_cb)
        self.bridge = CvBridge()

    def camera_cb(self, msg):
        print(msg)
        cv_img = self.bridge.compressed_imgmsg_to_cv2(msg)
        cv2.imshow("cv_img", cv_img)
        cv2.waitKey(1)
    
class_sub = Class_sub()
rospy.spin()