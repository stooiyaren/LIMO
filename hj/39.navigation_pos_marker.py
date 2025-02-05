#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped, Twist
from actionlib_msgs.msg import GoalStatusArray 
from ar_track_alvar_msgs.msg import AlvarMarkers
from tf.transformations import *
from math import *

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        self.goal_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)
        self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

        rospy.Subscriber("ar_pose_marker", AlvarMarkers, self.marker_cb)
        rospy.Subscriber("move_base/status", GoalStatusArray, self.goal_status_cb)
        
        self.goal_msg = PoseStamped()
        self.status_msg = GoalStatusArray()
        self.cmd_msg = Twist()

        self.goal_msg.header.frame_id = 'map'
        self.rate = rospy.Rate(0.3)
        self.pos_x = 0
        self.goal_status = 3
        self.marker_id = 0
        self.past_marker_id = -1
        

    def marker_cb(self,msg):
        self.marker_msg = msg

        if len(self.marker_msg.markers) == 0:
            self.marker_id = -1
        else:
            self.marker_id = self.marker_msg.markers[0].id
            self.past_marker_id = self.marker_id
        
    def goal_status_cb(self,msg):
        self.status_msg = msg
        if len(self.goal_status_msg.status_list) == 0:
            self.goal_status = 3
        else:
            self.goal_status = self.goal_status_msg.status_list[0].status

    def run(self):
        self.pos_x +=0.1
        self.goal_msg.pose.position.x = self.pos_x
        self.goal_msg.pose.position.y = 0.0

        yaw_degree = 60
        yaw = yaw_degree/180*pi
        x,y,z,w = quaternion_from_euler(0,0,yaw)

        self.goal_msg.pose.orientation.x = x
        self.goal_msg.pose.orientation.y = y
        self.goal_msg.pose.orientation.z = z
        self.goal_msg.pose.orientation.w = w

        # print(self.goal_msg)
        if self.past_marker_id == 0:
            try:
                x = self.marker_msg.marker[0].pose.pose.position.x
                y = self.marker_msg.marker[0].pose.pose.position.y
                z = self.marker_msg.marker[0].pose.pose.position.z
                w = self.marker_msg.marker[0].pose.pose.position.w

                self.cmd_msg.linear.x = x
                self.cmd_msg.angular.z = y*10

                self.cmd_pub.publish(self.cmd_msg)
            except:
                pass
        
        else:
            if self.goal_status == 3 and self.past_marker_id != -1:
                print(f"goal_setting:{self.past_marker_id}")
                if self.past_marker_id == 0:
                    self.pos_x = 0
                elif self.past_marker_id == 1:
                    self.pos_x = -2

                self.pos_y = 0.4
                self.goal_msg.pose.position.x = self.pos_x
                self.goal_msg.pose.position.y = self.pos_y

                self.goal_pub.publish(self.goal_msg)
                self.rate.sleep()

class_sub = Class_sub()
while not rospy.is_shutdown():
    class_sub.run()