#!/usr/bin/env python3
import gpiozero
import time

line_sensor1 = gpiozero.DigitalInputDevice(5)
line_sensor2 = gpiozero.DigitalInputDevice(6)
line_sensor3 = gpiozero.DigitalInputDevice(13)
line_sensor4 = gpiozero.DigitalInputDevice(19)
line_sensor5 = gpiozero.DigitalInputDevice(26)

while True:
    if line_sensor2.is_active == False:
        print("Line detected left")
    elif line_sensor4.is_active == False:
        print("Line detected right")
    else:
        print("Going forward")
        
    time.sleep(0.01)
