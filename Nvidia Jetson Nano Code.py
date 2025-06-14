import RPi.GPIO as GPIO

# Define GPIO pins for RGB LED
RED_PIN = 5
GREEN_PIN = 6
BLUE_PIN = 13

# Define GPIO pin for the potentiometer
POT_PIN1 = 19
POT_PIN2 = 11
# Set up GPIO mode and initial values
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(POT_PIN1, GPIO.IN)
GPIO.setup(POT_PIN2, GPIO.IN)
def set_color(color):
    GPIO.output(RED_PIN, color[0])
    GPIO.output(GREEN_PIN, color[1])
    GPIO.output(BLUE_PIN, color[2])


while True:
    pot_value1 = GPIO.input(POT_PIN1)
    pot_value2 = GPIO.input(POT_PIN2)
    print("(",pot_value1,",",pot_value2,")")
    if pot_value1 == 0 and pot_value2 ==0:
        set_color((1, 0, 0))  # Red
    elif  pot_value1 == 1 and pot_value2 ==1:
        set_color((0, 1, 0))  # Green
    else:
        set_color((0, 0, 1))  # Blue

GPIO.cleanup()