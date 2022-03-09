#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " distance: %.3f", data.data)

def ultrasonic_listener():
    rospy.init_node('ultrasonic_listener', anonymous=True)
    rospy.Subscriber('ultrasonic_topic', Float32, callback)
    rospy.spin()

if __name__== '__main__':
    ultrasonic_listener()
