import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from actionlib_msgs.msg import GoalStatusArray
from tf.transformations import *
from math import *

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        self.pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)
        rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, self.goal_status_cb)
        self.goal_msg = PoseStamped()
        self.amcl_msg = PoseWithCovarianceStamped()
        self.goal_status_msg = GoalStatusArray()
        self.goal_msg.header.frame_id = 'map'
        self.rate = rospy.Rate(0.5)
        self.goal_pos_x = -6
        self.msg_flag = False
        self.goal_flag = False

    def run(self):
        if self.msg_flag == True:
            if self.goal_status == 3:

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

                # self.pub.publish(self.goal_msg)
                self.rate.sleep()
            elif 
    
    def goal_status_cb(self, msg):
        if msg != None:
            self.goal_status_msg = msg
            print(self.goal_status_msg.status_list[0].status)
        else:
            pass


class_sub = Class_sub()
while not rospy.is_shutdown():
    class_sub.run()