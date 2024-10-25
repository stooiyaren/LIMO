#!/usr/bin/env python3

import rospy
from ar_track_alvar_msgs.msg import AlvarMarkers
from geometry_msgs.msg import Twist

class Class_sub():
    def __init__(self):
        rospy.init_node("wego_sub_node")
        rospy.Subscriber("ar_pose_marker", AlvarMarkers, self.callback)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.marker_msg = AlvarMarkers()
        self.cmd_msg = Twist()
        self.marker_id = 1

    def callback(self, msg):
        self.marker_msg = msg
        if len(self.marker_msg.markers) == 0:
            self.marker_id = -1
        else:
            self.marker_id = self.marker_msg.markers[0].id
        
        if self.marker_id == 0:
            self.cmd_msg.linear.x = 0.5
        elif self.marker_id == 3:
            self.cmd_msg.linear.x = 1
        elif self.marker_id == 6:
            self.cmd_msg.linear.x = 0.25
        else:
            pass

        self.pub.publish(self.cmd_msg)
    

class_sub = Class_sub()
rospy.spin()