import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)

try:
    while True:
        GPIO.output(17, GPIO.HIGH)  # Turn LED on
        time.sleep(1)               # Wait for 1 second
        GPIO.output(17, GPIO.LOW)   # Turn LED off
        time.sleep(1)               # Wait for 1 second
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup() 
