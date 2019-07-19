from time import sleep
import RPi.GPIO as GPIO
SENSOR = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SENSOR,GPIO.IN)
while True:
    state = GPIO.input(SENSOR)
    if state == False:
        print("Moisture detected")
    else:
        print("Needs Watering")
    sleep(0.5)