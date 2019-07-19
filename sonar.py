import RPi.GPIO as GPIO
import time
from time import sleep
TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance
 
while True:
    dist = distance()
    print(dist)
    sleep(0.1)