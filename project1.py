from gpiozero import LED, Button, Servo
from time import sleep

red = LED(22)
green = LED(27)
blue = LED(17)  # Optional
switch = Button(23, pull_up=True)
servo = Servo(18)

def activate_servo_on():
    servo.value = 1  # Full forward speed (adjust as needed for your servo)

def deactivate_servo():
    servo.value = None  # Turn off servo (no signal sent = motor off)

def update_state():
    if switch.is_pressed:
        print("Switch ON: green LED ON, red LED OFF, servo spinning")
        red.off()
        green.on()
        activate_servo_on()
    else:
        print("Switch OFF: green LED OFF, red LED ON, servo off")
        green.off()
        deactivate_servo()
        red.on()

# Initial state
red.on()
green.off()
deactivate_servo()

try:
    while True:
        update_state()
        sleep(0.2)
except KeyboardInterrupt:
    print("\nExiting gracefully, turning off all outputs.")
    red.off()
    green.off()
    blue.off()
    deactivate_servo()
