import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pins = [17, 27, 22]

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


try:
    for i in range(3):

        for pin in led_pins:
            GPIO.output(pin,GPIO.HIGH)
            time.sleep(.5)

        for pin in led_pins:
            GPIO.output(pin,GPIO.LOW)
            time.sleep(.5)

    GPIO.cleanup()
    print("Finished blinking. All LEDs should now be OFF.")
except KeyboardInterrupt:
    print("Interrupted.")
finally:
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)  # Make sure all LEDs are off
    GPIO.cleanup()
    print("GPIO cleanup done.")


