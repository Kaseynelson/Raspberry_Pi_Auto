#!/usr/bin/env python
import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BOARD)

#define pin, frequency and duty cycle
PWN_pin = 36
frequency = 100*pow(10, 3)
dutyCycle = 10

#configure pin for output
GPIO.setup(PWN_pin, GPIO.OUT)

#create PWM instance for pin w frequency
pwm = GPIO.PWM(PWN_pin, frequency)

#start the PWM object
pwm.start(dutyCycle)
time.sleep(5)

#stop the output for the PWM pin
pwm.stop()
GPIO.cleanup()
