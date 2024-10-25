import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu



class Class_pub:
    def __init__(self):
        rospy.init_node("wego_pub_node")
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        rospy.Subscriber("/imu", Imu, self.callback)
        self.rate = rospy.Rate(2)
        self.msg = Twist()
        self.imu_msg = Imu()
        # self.msg.angular.z
    
    def callback(self,msg):
        self.imu_msg = msg