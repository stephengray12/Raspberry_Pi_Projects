LED_PIN = 17

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, GPIO.HIGH)

time.sleep(10)

GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
# This code turns on an LED connected to GPIO pin 17 for 10 seconds and then turns it off.