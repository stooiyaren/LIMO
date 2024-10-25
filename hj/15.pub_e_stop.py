import rospy
from geometry_msgs.msg import Twist
from random import *
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Imu
from math import *

class Class_sub:
	def __init__(self):
		rospy.init_node("wego_sub_node") # 1. node 이름 설정
		self.pub = rospy.Publisher("/cmd_vel", Twist,queue_size=1)
		rospy.Subscriber("/scan", LaserScan, self.callback)
		self.lidar_msg = LaserScan()
		self.cmd_msg = Twist()
		
	def ctrl(self):
		angle_min = self.lidar_msg.angle_min / pi * 180
		# angle_max = self.lidar_msg.angle_max / pi * 180
		angle_increment = self.lidar_msg.angle_increment / pi * 180
		degrees = [angle_min + angle_increment * idx for idx, value in enumerate(self.lidar_msg.ranges)]
		self.obstacle = 0
		for idx, value in enumerate(self.lidar_msg.ranges):
			if abs(degrees[idx]) < 30 and 0 < value < 0.5:
				print(f"obstacle : {degrees[idx]} | distance : {value}")
				self.obstacle = self.obstacle +1
		else:
			pass
		if self.obstacle > 0:
			self.cmd_msg.linear.x = 0
		else:
			self.cmd_msg.linear.x = 1

		self.pub.publish(self.cmd_msg)

	def callback(self,msg): #3. subscriber - callback
		self.lidar_msg = msg



class_sub = Class_sub()
while not rospy.is_shutdown():
	class_sub.ctrl()