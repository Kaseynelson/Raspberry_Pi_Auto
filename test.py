import RPi.GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
TRIG = 13
ECHO = 22
# Setup of the input and output 
GPIO.setup(TRIG, GPIO.OUT)
GPIO.OUTPUT(TRIG, False)
GPIO.setup(ECHO, GPIO.IN)
time.sleep(.5)
time_start = time.time()

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

whule GPIO.input(ECHO) == 0:
	start_time = time.time()
whule GPIO.input(ECHO) == 1:
	end_time = time.time()
time_end = time.time()

total_distance = (end_time - start_time) *34300
print(total_distance/2)
priint(time_end - time_start)
GPIO.cleanup()