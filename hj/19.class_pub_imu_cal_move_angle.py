import rospy
from sensor_msgs.msg import Imu
from tf.transformations import *
from geometry_msgs.msg import Twist
from math import *

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        rospy.Subscriber("/imu", Imu, self.callback)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
        self.imu_msgs = Imu()
        self.cmd_msg = Twist()
        self.imu_msgs.orientation
        self.goal_degrees = [-135,-45,45,135]
        self.num = 0

    def run(self):
        x = self.imu_msgs.orientation.x
        y = self.imu_msgs.orientation.y
        z = self.imu_msgs.orientation.z
        w = self.imu_msgs.orientation.w

        roll, pitch, yaw = euler_from_quaternion([x,y,z,w])
        # print(f'roll : {roll} pitch : {pitch} yaw : {yaw}')

        state_degree = yaw*180/pi
        # goal_degree = 90
        # self.cmd_msg.angular.z = (goal_degree - state_degree) * 0.1
        # self.pub.publish(self.cmd_msg)

        goal_degrees = self.goal_degrees[self.num]

        if self.goal_degrees[self.num] -0.5 < state_degree < self.goal_degrees[self.num] + 0.5:
            self.num=(self.num+1)%4
        # self.goal_degrees[self.num] = -90
        self.cmd_msg.angular.z = (self.goal_degrees[self.num]-state_degree)*0.05
        self.pub.publish(self.cmd_msg)
        # self.rate.sleep()

    def callback(self, msg):
        # print(msg.orientation)
        self.imu_msgs = msg
        print(msg)

class_sub = Class_sub()
while not rospy.is_shutdown():
    class_sub.run()