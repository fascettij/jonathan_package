#!/user/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
	print(data.data)

def listener():

	# In ROS, nodes are uniquely named. If two nodes with
	# the same name are launched, the previous one is
	# kicked off. The anonymous=True flag menas that rospy
	# will choose a unique name for our listener' node so
	# that multiple listeners can run simultaneously.

	rospy.init_node('receiver', anonymous=True)
	rospy.Subscriber("catter", String, callback)

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	listener()


