import rospy
from geometry_msgs.msg import Twist

class Class_pub:
    def __init__(self):
        rospy.init_node("wego_pub_node")
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1)
        self.rate = rospy.Rate(2)
        self.msg = Twist()
        self.msg.angular.z
    
    def run(self):
        while not rospy.is_shutdown():
            self.msg.angular.z = 1
            self.pub.publish(self.msg)
            self.rate.sleep()
            print(self.msg)

class_pub = Class_pub()
class_pub.run()