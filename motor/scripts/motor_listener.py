#!/usr/bin/env python3
import math
from board import SCL,SDA
import busio
from adafruit_pca9685 import PCA9685
import time
import adafruit_motor.servo
import rospy
from std_msgs.msg import Float32

def Sero_Motor_Initialization():
    #setting up ic2
    i2c_bus = busio.I2C(SCL,SDA)
    # Start Communicating with Driver
    pca =PCA9685(i2c_bus)
    # Set Frequency
    pca.frequency =  100
    #kit = ServoKit(channels=16)
    return pca

def Steering(pca,angle):
    # Limiting
    if angle >180:
        angle = 180
    if angle < 0:
        angle = 0
    # Converts to 16-bit duty between 10% and 20%
    duty = ((angle/180)*6553)+6553
    pca.channels[0].duty_cycle= math.floor(duty)
       
def Motor_Speed(pca, percent, channel = 11):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)
    print(percent)

def ultrasonic_callback(data):
    rospy.loginfo(rospy.get_caller_id() + " distance: %.3f", data.data)
    print(data.data)
    if (data.data < 20):
      Motor_Speed(pca, 0.0, 11)

def ultrasonic_listener(pca):
    rospy.init_node('ultrasonic_listener', anonymous=True)
    rospy.Subscriber('ultrasonic_topic', Float32, ultrasonic_callback)
    rospy.spin()

pca=Sero_Motor_Initialization
Motor_Speed(pca, 0.1, 11)

if __name__== '__main__':
    ultrasonic_listener()
    #rospy.spin()