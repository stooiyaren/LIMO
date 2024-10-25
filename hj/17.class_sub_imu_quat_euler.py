import rospy
from sensor_msgs.msg import Imu
from tf.transformations import *
from math import *

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        rospy.Subscriber("/imu", Imu, self.callback)
        self.imu_msgs = Imu()
        self.imu_msgs.orientation

    def callback(self, msg):
        # print(msg.orientation)
        x = msg.orientation.x
        y = msg.orientation.y
        z = msg.orientation.z
        w = msg.orientation.w

        # print(f'z: {z*180}')

        roll, pitch, yaw = euler_from_quaternion([x,y,z,w])
        # print(f'roll : {roll} pitch : {pitch} yaw : {yaw}')

        state_degree = yaw*180/pi
        goal_degree = 90
        self.cmd_msg.angularz = (goal_degree - state_degree) * 0.5
        self.pub.publish(self.cmd_msg)

class_sub = Class_sub()
rospy.spin()