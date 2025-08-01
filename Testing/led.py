import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    for _ in range(5):  # Blink 5 times
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(2)
    print("Finished blinking. LED should now be OFF.")
except KeyboardInterrupt:
    print("Interrupted.")
finally:
    GPIO.output(LED_PIN, GPIO.LOW)  # Make sure LED is off
    GPIO.cleanup()
