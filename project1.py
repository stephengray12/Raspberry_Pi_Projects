from gpiozero import LED, Button
from signal import pause

green = LED(27)
red = LED(22)
blue = LED(17)
switch = Button(23)

def switch_toggled():
    if switch.is_pressed:
        green.on()
    else:
        green.off()
        red.off()
        blue.off()

# Attach handler to switch state changes
switch.when_pressed = switch_toggled
switch.when_released = switch_toggled

try:
    # Run indefinitely
    pause()
except KeyboardInterrupt:
    print("\nExiting, turning off all LEDs.")
    green.off()
    red.off()
    blue.off()
