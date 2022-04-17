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


def Motor_Start(pca, channel = 11):
    pca.channels[channel].duty_cycle = 9830
    
#def Motor_Speed(pca, percent, channel = 11):
 #   speed = (percent*3276) + 65535 * 0.15
  #  pca.channels[channel].duty_cycle = math.floor(speed)
   # print(percent)
    
def Motor_StartUp(pca):
    print('Starting Motor Start Up Sequence')
    pca.channels[11].duty_cycle = math.floor(.15*65535)
    time.sleep(5)
    pca.channels[11].duty_cycle = math.floor(.2*65535)
    time.sleep(3)
    pca.channels[11].duty_cycle = math.floor(.15*65535)
    time.sleep(3)
    pca.channels[11].duty_cycle = math.floor(.1*65535)
    time.sleep(3)
    pca.channels[11].duty_cycle = math.floor(.15*65535)
    time.sleep(3)
    print('Start Up Complete')

def Motor_Speed(pca, percent, channel = 11):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)
    print(percent)

pca = Servo_Initialize()
Motor_StartUp(pca)

print('')
print('Changing Speeds:')
Motor_Speed(pca, 0.15, 11)
time.sleep(5)
Motor_Speed(pca, 0.1, 11)#pca.channels[11].duty_cycle = math.floor(.17*65535)
time.sleep(5)
Motor_Speed(pca, 0.15, 11)
