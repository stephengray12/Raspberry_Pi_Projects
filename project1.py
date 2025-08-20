from gpiozero import LED, Button, Servo
from time import sleep
from LCD import LCD  # Assuming LCD is a custom class/module

# Setup
red = LED(22)
green = LED(27)
servo = Servo(18)

lcd = LCD(2, 0x27, True)
lcd.message("Alysa is", 1)        
lcd.message("awesome!!!!!!", 2)    
sleep(.5)
lcd.clear()

def activate_servo_on():
    servo.value = 1  

def deactivate_servo():
    servo.value = None  # or use 0 if needed

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

# Main loop
try:
    while True:
        update_state()
        sleep(0.2)
except KeyboardInterrupt:
    print("\nExiting gracefully, turning off all outputs.")
    red.off()
    green.off()
    deactivate_servo()
