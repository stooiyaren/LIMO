import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from tf.transformations import *
from math import *

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        self.pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)
        rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, self.amcl_cb)
        self.goal_msg = PoseStamped()
        self.amcl_msg = PoseWithCovarianceStamped()
        self.goal_msg.header.frame_id = 'base_link'
        self.rate = rospy.Rate(0.3)
        self.goal_pos_x = -6
        self.msg_flag = False

    def run(self):
        if self.msg_flag == True:
            self.goal_pos_x -= 0.5
            self.goal_pos_y = -1
            self.goal_msg.pose.position.x = self.goal_pos_x
            self.goal_msg.pose.position.y = self.goal_pos_y

            yaw_degree = 60
            yaw = yaw_degree/180*pi
            x,y,z,w = quaternion_from_euler(0,0,yaw)

            self.goal_msg.pose.orientation.x = x
            self.goal_msg.pose.orientation.y = y
            self.goal_msg.pose.orientation.z = z
            self.goal_msg.pose.orientation.w = w
            self.pub.publish(self.goal_msg)
            self.rate.sleep()
    
    def amcl_cb(self, msg):
        if msg != None:
            self.amcl_msg = msg
            self.pos_x = self.amcl_msg.pose.pose.position.x
            self.pos_y = self.amcl_msg.pose.pose.position.y
            x = self.amcl_msg.pose.pose.orientation.x
            y = self.amcl_msg.pose.pose.orientation.y
            z = self.amcl_msg.pose.pose.orientation.z
            w = self.amcl_msg.pose.pose.orientation.w
            roll,pitch,yaw = euler_from_quaternion([x,y,z,w])
            self.yaw = yaw
            self.msg_flag = True
        else:
            pass


class_sub = Class_sub()
while not rospy.is_shutdown():
    class_sub.run()