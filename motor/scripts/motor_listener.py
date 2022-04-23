#!/usr/bin/env python3
import math
from board import SCL,SDA
import busio
from adafruit_pca9685 import PCA9685
import time
from datetime import datetime, timedelta
import adafruit_motor.servo
import rospy
from std_msgs.msg import Float32, Int16, String

def delta_time(waitTime):
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds = waitTime)
    while startTime < endTime:
        startTime = datetime.now()

def Servo_Motor_Initialization():
    #setting up ic2
    i2c_bus = busio.I2C(SCL,SDA)
    # Start Communicating with Driver
    pca =PCA9685(i2c_bus)
    # Set Frequency
    pca.frequency =  100
    #kit = ServoKit(channels=16)
    return pca

pca = Servo_Motor_Initialization()

def Steering(pca,angle):
    # Limiting
    if angle >180:
        angle = 180
    if angle < 0:
        angle = 0
    # Converts to 16-bit duty between 10% and 20%
    duty = ((angle/180)*6553)+6553
    pca.channels[0].duty_cycle= math.floor(duty)

def Motor_StartUp(pca):
    print('Starting Motor Start UP Sequence')
    for i in range(10):
        Motor_Speed(pca, i*0.001+0.155, 11)
        time.sleep(0.5)
    Motor_Speed(pca, 0.161, 11)
    time.sleep(1)
    print('Start Up Complete')

def Motor_Speed(pca, percent, channel = 11):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)
    print(percent)

def ultrasonic_callback(data):
    rospy.loginfo(rospy.get_caller_id() + " distance: %.3f", data.data)
    if (data.data < 40):
        Steering(pca, 0)
        #delta_time(0.5)
        #Steering(pca,60)

def linetracker_callback(data):
    rospy.loginfo(rospy.get_caller_id() + " line tracker value: %i", data.data)
    if (data.data == -1):
        Steering(pca, 70)
        #delta_time(0.5)
        #Steering(pca, 60)
    elif (data.data == 1):
        Steering(pca, 50)
        #delta_time(0.5)
        #Steering(pca, 60)

Motor_StartUp(pca)
Motor_Speed(pca, 0.165, 11)
time.sleep(0.5)
Steering(pca, 60)

if __name__== '__main__':
    try:
        rospy.init_node('listener_nodes', anonymous=True)
        rospy.Subscriber('ultrasonic_topic', Float32, ultrasonic_callback)
        rospy.Subscriber('linetracker_topic', Int16, linetracker_callback)
        rospy.spin()
    
    # Reset by pressing CTRL + C
    except rospy.ROSInterruptException:
        pass
