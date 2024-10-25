import rospy
from sensor_msgs.msg import Imu, LaserScan
from tf.transformations import *
from geometry_msgs.msg import Twist
from math import *

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        rospy.Subscriber("/imu", Imu, self.imu_cb)
        rospy.Subscriber("/scan", LaserScan, self.lidar_cb)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
        self.imu_msg = Imu()
        self.cmd_msg = Twist()
        self.lidar_msg = LaserScan()
        self.goal_degrees = [-180,90,90,180]
        self.num = 0
        self.goal_degree = 0
        self.rate = rospy.Rate(10)


    def lidar_cb(self, msg):
        self.lidar_msg = msg


    def imu_cb(self, msg):
        self.imu_msg = msg

        
    def e_stop(self):
        degree_min = self.lidar_msg.angle_min*180/pi
        degree_max = self.lidar_msg.angle_max*180/pi
        degree_increment = self.lidar_msg.angle_increment*180/pi
        degrees = [degree_min + degree_increment *idx for idx,value in enumerate(self.lidar_msg.ranges)]
        self.obstacle = 0
        for idx,value in enumerate(self.lidar_msg.ranges):
            if 0<value<0.5 and abs(degrees[idx])<30:
                print(f'obstacle : {degrees[idx]}')
                self.obstacle = self.obstacle+1
        

    
    def cal_angle(self):
        x = self.imu_msg.orientation.x
        y = self.imu_msg.orientation.y
        z = self.imu_msg.orientation.z
        w = self.imu_msg.orientation.w
        roll, pitch, yaw = euler_from_quaternion([x,y,z,w])
        self.state_degree = yaw*180/pi
        self.goal_degree = self.goal_degrees[self.num]


    def run(self):
        if self.obstacle > 0:
            self.cmd_msg.angular.z = 0
        else:
            self.cmd_msg.angular.z = (self.goal_degrees[self.num]-self.state_degree)*0.05
            self.pub.publish(self.cmd_msg)
            self.rate.sleep()
            if self.goal_degree -0.5 < self.state_degree < self.goal_degree:
                self.num=(self.num+1)%4
        self.pub.publish(self.cmd_msg)
        self.rate.sleep()

class_sub = Class_sub()
while not rospy.is_shutdown():
    class_sub.e_stop()
    class_sub.cal_angle()
    class_sub.run()