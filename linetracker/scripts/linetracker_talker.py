#!/usr/bin/env python3
from gpiozero import LineSensor
import time
import rospy
from std_msgs.msg import Int16, String
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

threshold = 32000

def linetracker_talker():
    publisher = rospy.Publisher('linetracker_topic', Int16)
    rospy.init_node('linetracker', anonymous=True)
    rate = rospy.Rate(150) #100Hz
    while True:
        # create an analog input channel on pin 0
        chan0 = AnalogIn(mcp, MCP.P0)
        #chan1 = AnalogIn(mcp, MCP.P1)
        #chan2 = AnalogIn(mcp, MCP.P2)
        #chan3 = AnalogIn(mcp, MCP.P3)
        chan4 = AnalogIn(mcp, MCP.P4)
       
        if chan4.value < threshold:
            publisher.publish(1)
        elif chan0.value < threshold:
            publisher.publish(-1)
        else:
            publisher.publish(0)
        rate.sleep()

#line_sensor1 = LineSensor(5, queue_len = 10, sample_rate = 100, threshold = 0.2)
#line_sensor2 = LineSensor(6, queue_len = 10, sample_rate = 100, threshold = 0.2)
#line_sensor3 = LineSensor(13, queue_len = 10, sample_rate = 100, threshold = 0.2)
#line_sensor4 = LineSensor(19, queue_len = 10, sample_rate = 100, threshold = 0.2)
#line_sensor5 = LineSensor(26, queue_len = 10, sample_rate = 100, threshold = 0.2)
    
#def linetracker_talker():
#    publisher = rospy.Publisher('linetracker_topic', Int16)
#    rospy.init_node('linetracker', anonymous=True)
#    rate = rospy.Rate(25) #100Hz
#    while True:
#        if line_sensor2.is_active == False:
#            publisher.publish(-1)
#        elif line_sensor4.is_active == False:
#            publisher.publish(1)
#        else:
#            publisher.publish(0)
#        rate.sleep()
        

if __name__ == '__main__':
    try:
        linetracker_talker()
 
    # Reset by pressing CTRL + C
    except rospy.ROSInterruptException:
        GPIO.cleanup()
        pass
