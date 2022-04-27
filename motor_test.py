#!/usr/bin/env python
import math
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import time


def Servo_Initialize():
   i2c = busio.I2C(SCL, SDA)
   pca = PCA9685(i2c)
   pca.frequency = 100
   return pca


def Motor_StartUp(pca):
    print('Starting Motor Start Up Sequence')
    for i in range(10):
        Motor_Speed(pca, i*0.001+0.155, 11)
        time.sleep(0.5)
    Motor_Speed(pca, 0.161, 11)
    time.sleep(1)
    print('Start Up Complete')

def Motor_Speed(pca, percent, channel = 11):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)
    print(percent)

pca = Servo_Initialize()
Motor_StartUp(pca)
Motor_Speed(pca, 0.161, 11)
time.sleep(2)
#Motor_Speed(pca, 0.160, 11)
