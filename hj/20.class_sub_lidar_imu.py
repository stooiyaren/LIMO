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
		rospy.Subscriber("/scan", LaserScan, self.lidar_cb) # lidar = 10hz?
		rospy.Subscriber("/imu", Imu, self.imu_cb) # imu = 100 hz
		self.Lidar_msg = LaserScan()
		self.imu_msg = Imu()
		self.cmd_msg = Twist()
		
		
	def lidar_cb(self, msg):
		print(msg)
		self.cmd_msg.linear.x = 0
		self.pub.publish(self.cmd_msg)


	def imu_cb(self,msg): #3. subscriber - callback
		print(msg)
		self.cmd_msg.linear.x = 1
		self.pub.publish(self.cmd_msg)

	def e_stop(self):
		degree_min = self.lidar_msg.angle_min*180/pi
		degree_max = self.lidar_msg.angle_max*180/pi
		degree_increment = self.Lidar_msg.angle_increment*180/pi
		degrees = [degree_min + degree_increment *idx for idx,value in enumerate(self.Lidar_msg.ranges)]
		self.obstacle = 0
		for idx,value in enumerate(self.Lidar_msg.ranges):
			if 0<value<0.5 and abs(degrees[idx])<30:
				print(f'obstacle : {degrees[idx]}')
				self.obstacle = self.obstacle+1
	
	def cal_angle(self):
		passs




class_sub = Class_sub()
rospy.spin()