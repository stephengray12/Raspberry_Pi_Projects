import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)

# LEDs
RED_LED = 22
GREEN_LED = 27
BLUE_LED = 17

# Switch inputs
SWITCH_ON = 23
SWITCH_OFF = 24

# Servo
SERVO_PIN = 18

# Setup pins
GPIO.setup([RED_LED, GREEN_LED, BLUE_LED], GPIO.OUT)
GPIO.setup([SWITCH_ON, SWITCH_OFF], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Setup PWM for servo
servo = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz
servo.start(0)

def set_servo_position(duty):
    servo.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo.ChangeDutyCycle(0)  # Prevent servo jitter

try:
    while True:
        on_state = GPIO.input(SWITCH_ON)
        off_state = GPIO.input(SWITCH_OFF)

        if on_state and not off_state:
            # Servo ON state
            GPIO.output(RED_LED, GPIO.LOW)
            GPIO.output(GREEN_LED, GPIO.HIGH)
            GPIO.output(BLUE_LED, GPIO.LOW)
            set_servo_position(7.5)  # Midpoint (adjust if needed)

        elif off_state and not on_state:
            # Servo OFF state
            GPIO.output(RED_LED, GPIO.HIGH)
            GPIO.output(GREEN_LED, GPIO.LOW)
            GPIO.output(BLUE_LED, GPIO.LOW)
            set_servo_position(2.5)  # Move to OFF position (adjust as needed)

        elif on_state and off_state:
            # ERROR: both directions triggered
            GPIO.output(RED_LED, GPIO.LOW)
            GPIO.output(GREEN_LED, GPIO.LOW)
            GPIO.output(BLUE_LED, GPIO.HIGH)
            set_servo_position(0)  # Stop servo

        else:
            # No switch pressed — maintain current state
            pass

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    servo.stop()
    GPIO.cleanup()
