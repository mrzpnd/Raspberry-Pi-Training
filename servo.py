import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(10,GPIO.OUT)
m=GPIO.PWM(10,50)
m.start(0)
def set_angle(angle):
    dutycycle=angle/18+2
    m.ChangeDutyCycle(dutycycle)
    time.sleep(2)
    m.ChangeDutyCycle(0)
while True:
    angle=int(input("enter angle"))
    if angle<=180 and angle>0:
        set_angle(angle)
    else:
        print("angle out of range")