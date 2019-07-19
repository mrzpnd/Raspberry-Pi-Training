import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
f='f'
r='r'
def forward():
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(5,GPIO.LOW)
def reverse():
    GPIO.output(4,GPIO.LOW)
    GPIO.output(5,GPIO.HIGH)
def stops():
    GPIO.output(4,GPIO.LOW)
    GPIO.output(5,GPIO.LOW)
    

while True:
    command=input("enter command"))
    if command=='f':
        forward()
    elif command=='r':
        reverse()
    else:
        stops()