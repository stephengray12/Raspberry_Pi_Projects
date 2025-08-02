import RPi.GPIO as GPIO
import time

# === GPIO Setup ===
GPIO.setmode(GPIO.BCM)

# LED Pins
RED_LED = 22
GREEN_LED = 27
BLUE_LED = 17  # You can keep or remove this if unused

# Switch Pin (only one now)
SWITCH_ON = 23

# Servo Pin
SERVO_PIN = 18

# === Pin Configuration ===
GPIO.setup([RED_LED, GREEN_LED, BLUE_LED], GPIO.OUT)
GPIO.setup(SWITCH_ON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# PWM Setup for Servo (50Hz)
servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)  # Start with 0% duty cycle

# === Helper Function ===
def set_servo_position(duty):
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)  # Give servo time to move
    servo.ChangeDutyCycle(0)  # Prevent jitter

# === Main Program ===
try:
    while True:
        on_state = GPIO.input(SWITCH_ON)

        if on_state:
            # Switch ON → Green LED on, Red LED off
            GPIO.output(RED_LED, GPIO.LOW)
            GPIO.output(GREEN_LED, GPIO.HIGH)
            GPIO.output(BLUE_LED, GPIO.LOW)  # Optional, can remove if unused

            set_servo_position(7.5)  # Move servo to ON position

        else:
            # Switch OFF → Red LED on, Green LED off
            GPIO.output(RED_LED, GPIO.HIGH)
            GPIO.output(GREEN_LED, GPIO.LOW)
            GPIO.output(BLUE_LED, GPIO.LOW)  # Optional

            set_servo_position(2.5)  # Move servo to OFF position

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    print("Cleaning up GPIO and stopping servo...")
    servo.stop()
    GPIO.cleanup()
