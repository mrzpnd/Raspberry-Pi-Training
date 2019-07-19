import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
f='f'
r='r'
def forward():
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(5,GPIO.LOW)
    m.ChangeDutyCycle(speed)
def reverse():
    GPIO.output(4,GPIO.LOW)
    GPIO.output(5,GPIO.HIGH)
    m.ChangeDutyCycle(speed)
def stops():
    GPIO.output(4,GPIO.LOW)
    GPIO.output(5,GPIO.LOW)
    

while True:
    command=input("enter command"))
    speed=int(input("enter speed"))
    if command=='f':
        forward()
    elif command=='r':
        reverse()
    else:
        stops()
    

