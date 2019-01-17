#!/usr/bin/env python
import rospy
from jonathan_package.msg import Num

def callback(data):
    rospy.loginfo("%s is age: %d" % (data.firstInt, data.secondInt))

def listener():
    rospy.init_node('message_listener', anonymous=True)
    rospy.Subscriber("message_receiver", Num, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
