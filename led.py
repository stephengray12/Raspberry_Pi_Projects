LED_PIN = 17

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    try:
        
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(10)  

        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(10) 

    except KeyboardInterrupt:
      
        GPIO.cleanup()
        break




