LED_PIN = 17

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)  # Set GPIO pin 17 as an output

GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
time.sleep(5)  # Keep the LED on for 5 seconds
GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED

GPIO.cleanup()  # Clean up GPIO settings