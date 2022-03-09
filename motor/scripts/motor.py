#!/usr/bin/env python
import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BOARD)

#define pin, frequency and duty cycle
PWM_pin = 7
frequency = 100*pow(10, 3)
dutyCycle = 4

#configure pin for output
GPIO.setup(PWM_pin, GPIO.OUT)

#create PWM instance for pin w frequency
pwm = GPIO.PWM(PWM_pin, frequency)
#start the PWM object
pwm.start(dutyCycle)
time.sleep(2)
pwm.ChangeDutyCycle(8)
time.sleep(2)

#stop the output for the PWM pin
pwm.stop()
GPIO.cleanup()
