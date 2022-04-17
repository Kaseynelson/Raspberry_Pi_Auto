#!/usr/bin/env python3
import gpiozero
from gpiozero import LineSensor
import time

#line_sensor1 = gpiozero.DigitalInputDevice(5)
#line_sensor2 = gpiozero.DigitalInputDevice(6)
#line_sensor3 = gpiozero.DigitalInputDevice(13)
#line_sensor4 = gpiozero.DigitalInputDevice(19)
#line_sensor5 = gpiozero.DigitalInputDevice(26)
line_sensor1 = LineSensor(5, queue_len = 50, sample_rate = 1000, threshold = 0.2)
line_sensor2 = LineSensor(6, queue_len = 50, sample_rate = 1000, threshold = 0.2)
line_sensor3 = LineSensor(13, queue_len = 50, sample_rate = 1000, threshold = 0.2)
line_sensor4 = LineSensor(19, queue_len = 50, sample_rate = 1000, threshold = 0.2)
line_sensor5 = LineSensor(26, queue_len = 50, sample_rate = 1000, threshold = 0.2)

while True:
    #line_sensor4.when_line = lambda: print('Line detected right')
    #line_sensor4.when_no_line = lambda: print('No line detected right')
    #line_sensor2.when_line = lambda: print('Line detected left')
    #line_sensor2.when_no_line = lambda: print('No line detected left')
    #line_sensor1.when_line = lambda: print('Line detected far left')
    #line_sensor1.when_no_line = lambda: print('No line detected far left')
    #line_sensor5.when_line = lambda: print('Line detected far right')
    #line_sensor5.when_no_line = lambda: print('No line detected far right')

#     if line_sensor1.is_active == False and line_sensor5.is_active == False:
#         print('undetermined')
    if line_sensor2.is_active == False:
        print("Line detected left")
    elif line_sensor4.is_active == False:
        print("Line detected right")
#    elif line_sensor5.is_active == True:
#        print("Line detected far right")
#    elif line_sensor1.is_active == True:
#        print("Line detected far left")
    else:
        print("Going forward")
        
    time.sleep(0.05)
