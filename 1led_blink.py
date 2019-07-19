import RPi.GPIO as x
import time
x.setmode(x.BCM)
x.setup(4,x.OUT)
while True:
    x.output(4,x.HIGH)
    time.sleep(1)
    x.output(4,x.LOW)
    time.sleep(1)
    
