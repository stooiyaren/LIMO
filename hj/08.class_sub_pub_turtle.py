#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from random import *

class Class_sub:
	def __init__(self):
		rospy.init_node("wego_sub_node") # 1. node 이름 설정
		self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist,queue_size=1)
		rospy.Subscriber("/turtle1/pose",Pose,self.callback) #2. 노드역할
		# self.pose_msg = Pose()
		# self.pose_msg.linear_velocity
		self.cmd_msg = Twist()
		
		
	def callback(self,msg): #3. subscriber - callback
		if msg.x >= 9 or msg.x <= 2 or msg.y >= 9 or msg.y <= 2:
			self.cmd_msg.linear.x = 1
			self.cmd_msg.angular.z = random()*5
		elif msg.x >= 10 or msg.x <= 1 or msg.y >= 10 or msg.y <=1:
			self.cmd_msg.linear.x = 0
			self.cmd_msg.angular.z = random()*5
		else:
			self.cmd_msg.linear.x = 2
			self.cmd_msg.angular.z = 0

		self.pub.publish(self.cmd_msg)
		
class_sub = Class_sub()
rospy.spin()