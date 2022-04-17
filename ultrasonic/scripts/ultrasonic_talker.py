#!/usr/bin/env python3
#Libraries
import RPi.GPIO as GPIO
import time
import rospy
import numpy
from std_msgs.msg import Float32
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def ultrasonic_talker():
    publisher = rospy.Publisher('ultrasonic_topic', Float32)
    rospy.init_node('ultrasonic', anonymous=True)
    rate = rospy.Rate(30) #30Hz
    size = 3
    distArray = numpy.empty(size, dtype=float)
    i = 0
    while True:
        distArray[i] = distance()
        i += 1
        if i == size:
            i = 0
            avgDist = numpy.mean(distArray)
            publisher.publish(avgDist)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        ultrasonic_talker()
 
    # Reset by pressing CTRL + C
    except rospy.ROSInterruptException:
        GPIO.cleanup()
        pass
