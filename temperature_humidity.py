import Adafruit_DHT
from time import sleep
import RPi.GPIO as GPIO
SENSOR_TYPE = Adafruit_DHT.DHT11
SENSOR = 17
GPIO.setmode GPIO>BCM
GPIO.setwarnings(False)
GPIO.setup(SENSOR,GPIO.OUT)
while True:
    temperature, humidity = Adafruit_DHT.read_retry(SENSOR_TYPE,SENSOR)
    print("Temperature: {}".format(temperature))
    print("Humidity: {}".format(humidity))
    sleep(1)