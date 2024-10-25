import rospy
from sensor_msgs.msg import Imu

class Class_sub:
    def __init__(self):
        rospy.init_node("wego_sub_node")
        rospy.Subscriber("/imu", Imu, self.callback)
        self.sensor_msgs = Imu()


    def callback(self, msg):
        print(msg)
        print('----')
        print(self.sensor_msgs)
        print('////')

class_sub = Class_sub()
rospy.spin()