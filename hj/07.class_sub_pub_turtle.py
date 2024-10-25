import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from random import *

class Class_sub:
	def __init__(self):
		rospy.init_node("wego_sub_node") # 1. node 이름 설정
		self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist,queue_size=1)
		rospy.Subscriber("/turtle1/pose",Pose,self.callback) #2. 노드역할
		self.rate = rospy.Rate(2)
		self.pose_msg = Pose()
		# self.pose_msg.linear_velocity
		self.cmd_msg = Twist()
		self.num = 0
		
		
	def run(self):
		while not rospy.is_shutdown():
			self.num=self.num+1
			# self.cmd_msg.linear.x = self.num
			self.pub.publish(self.cmd_msg)
			self.rate.sleep()
			print(self.cmd_msg)
	
	def callback(self,msg):
		# print(msg)
		self.pose_msg = msg
		
class_sub = Class_sub()
rospy.spin()