import math
from board import SCL,SDA
import busio
from adafruit_pca9685 import PCA9685
import time
import adafruit_motor.servo

def Sero_Motor_Initialization():
    # Libaries provide by Adafruit
    # https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython
    # https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
    # Create busio i2C bus instance to communicate with driver.
    i2c_bus = busio.I2C(3,2)
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

pca=Sero_Motor_Initialization()
Steering(pca, 90)
