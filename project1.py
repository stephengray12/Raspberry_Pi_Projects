from gpiozero import LED, Button, Servo
from time import sleep
import time
from LCD import LCD

red = LED(22)
green = LED(27)
blue = LED(17) 
switch = Button(23, pull_up=True)
servo = Servo(18)

def activate_servo_on():
    servo.value = 1  

def deactivate_servo():
    servo.value = None  

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




# Code to mess with i2c display library stored in directory in repo.
# 
# lcd = LCD(2, 0x27, True)  
# 
# lcd.message("Alysa is", 1)        
# lcd.message("awesome!!!!!!", 2)    
# 
# time.sleep(5)
# 
# 
# lcd.clear()