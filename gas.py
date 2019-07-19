from time import sleep 
import RPi.GPIO as GPIO
SENSOR = 10
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SENSOR, GPIO.IN)
while True:
    state = GPIO.input(SENSOR)
    if state == False:
        print("Gas Detected")
    else:
        print("No Gas Detected")
    sleep(0.5)