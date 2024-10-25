import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from random import *
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Imu
from math import *

class Class_sub:
	def __init__(self):
		rospy.init_node("wego_sub_node") # 1. node 이름 설정
		self.pub = rospy.Publisher("/cmd_vel", Twist,queue_size=1)
		rospy.Subscriber("/scan", LaserScan, self.callback) #2. 노드역할
		self.scan_msg = LaserScan()
		self.cmd_msg = Twist()
		
		
	def callback(self,msg): #3. subscriber - callback
		self.pub.publish(self.cmd_msg)
		angle_min = msg.angle_min / pi * 180
		angle_max = msg.angle_max / pi * 180
		angle_increment = msg.angle_increment / pi * 180

		# degrees = []
		# idx = len(msg.ranges)
		# for i in range(0, idx):
			# degrees.append(angle_min + angle_increment*i)

		degrees = [angle_min + angle_increment * idx for idx, value in enumerate(msg.ranges)]

		for idx, value in enumerate(msg.ranges):
			if abs(degrees[idx]) < 30 and 0 < value < 0.5:
				print(f"obstacle : {degrees[idx]}, distance : {value}")
	
	def run(self):
		while not rospy.is_shutdown():
			self.msg.angular.z = 1
			self.msg.linear.x = 1
			self.pub.publish(self.msg)
			self.rate.sleep()
			print(self.msg)



class_sub = Class_sub()
rospy.spin()