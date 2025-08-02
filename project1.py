import RPi.GPIO as GPIO
import time
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# GPIO Setup
GPIO.setmode(GPIO.BCM)

RED_LED = 22
GREEN_LED = 27
BLUE_LED = 17
SWITCH_ON = 23
SERVO_PIN = 18

GPIO.setup([RED_LED, GREEN_LED, BLUE_LED], GPIO.OUT)
GPIO.setup(SWITCH_ON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Initialize Servo
try:
    servo = GPIO.PWM(SERVO_PIN, 50)
    servo.start(0)
except Exception as e:
    print(f"Error initializing servo PWM: {e}")
    GPIO.cleanup()
    exit(1)

# Initialize I2C Display
i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.show()

# Create blank image for drawing
image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

def display_text(line1="", line2=""):
    draw.rectangle((0, 0, display.width, display.height), outline=0, fill=0)
    draw.text((0, 0), line1, font=font, fill=255)
    draw.text((0, 16), line2, font=font, fill=255)
    display.image(image)
    display.show()

def set_servo_position(duty):
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

try:
    while True:
        on_state = GPIO.input(SWITCH_ON)
        print(f"Current Motor State: {on_state}")  # Still useful for debugging
        display_text("Motor State:", str(on_state))

        if on_state:
            GPIO.output(RED_LED, GPIO.LOW)
            GPIO.output(GREEN_LED, GPIO.HIGH)
            GPIO.output(BLUE_LED, GPIO.LOW)
            set_servo_position(7.5)
        else:
            GPIO.output(RED_LED, GPIO.HIGH)
            GPIO.output(GREEN_LED, GPIO.LOW)
            GPIO.output(BLUE_LED, GPIO.LOW)
            set_servo_position(0)

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting program...")

finally:
    print("Cleaning up GPIO and turning everything OFF...")
    display_text("Shutting down", "Cleaning GPIO")

    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(BLUE_LED, GPIO.LOW)

    try:
        servo.stop()
    except Exception as e:
        print(f"Error stopping servo: {e}")

    GPIO.cleanup()
    time.sleep(2)
    display.fill(0)
    display.show()
