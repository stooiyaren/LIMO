import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import *
from math import *

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, self.callback)
        self.amcl_msg = PoseWithCovarianceStamped()
    
    def callback(self, msg):
        self.amcl_msg = msg
        pos_x = self.amcl_msg.pose.pose.position.x
        pos_y = self.amcl_msg.pose.pose.position.y
        x = self.amcl_msg.pose.pose.orientation.x
        y = self.amcl_msg.pose.pose.orientation.y
        z = self.amcl_msg.pose.pose.orientation.z
        w = self.amcl_msg.pose.pose.orientation.w
        roll,pitch,yaw = euler_from_quaternion([x,y,z,w])
        print(f'x:{pos_x} y:{pos_y} degree:{yaw*180/pi}')

class_sub = Class_sub()
rospy.spin()