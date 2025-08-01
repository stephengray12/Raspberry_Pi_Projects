import RPi.GPIO as GPIO
import time

# Use BCM numbering (GPIO numbers)
GPIO.setmode(GPIO.BCM)
button_pin = 17

# Setup pin 17 as input with internal pull-down resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Waiting for button press. Press CTRL+C to exit.")
try:
    while True:
        if GPIO.input(button_pin) == GPIO.HIGH:
            print("Button was pressed!")
            time.sleep(0.2)  # debounce delay
except KeyboardInterrupt:
    print("Exiting.")
finally:
    GPIO.cleanup()
