from gpiozero import LED, Button, Servo
from signal import pause
from time import sleep

red = LED(22)
green = LED(27)
blue = LED(17)
switch = Button(23)
servo = Servo(18)

def set_servo_position(pos):
    servo.value = pos  # -1 to 1
    sleep(0.5)

while True:
    if switch.is_pressed:
        red.off()
        green.on()
        blue.off()
        set_servo_position(0)  # middle
    else:
        red.on()
        green.off()
        blue.off()
        set_servo_position(-1)  # leftmost
    sleep(0.5)
