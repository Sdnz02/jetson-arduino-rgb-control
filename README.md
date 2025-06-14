# RGB LED Control with Jetson Nano & Arduino

This is a hybrid embedded project developed for **EEE 313 - Introduction to Embedded Systems** course. It demonstrates how to use an **Arduino Uno** for analog input processing and an **NVIDIA Jetson Nano Developer Kit** for digital output control.

## Project Purpose

Due to the lack of native analog input support on Jetson Nano, we used Arduino to read values from a 10k potentiometer and determine color codes. Then, we transmitted this information via digital GPIO lines to Jetson Nano, which changes the color of an **RGB LED** accordingly.

- 🔴 Red: (0, 0)
- 🟢 Green: (1, 1)
- 🔵 Blue: (others)

---

## Hardware Components

| Component     | Description                                 |
|---------------|---------------------------------------------|
| Controller  | Jetson Nano Dev Kit + Arduino Uno           |
| Sensor      | 10k Potentiometer                           |
| Output      | Common Cathode RGB LED                     |
| Connection  | Digital GPIO (Jetson) + Analog Input (Uno) |

---

## Software Environment

- Python on Jetson Nano (manual GPIO control)
- Arduino IDE for analog reading
- Jetson GPIO library (`RPi.GPIO` ported for Jetson)

---

## Code Structure

### `Ardunio_Uno_Analog_Code.ino`  
Reads analog voltage from potentiometer  
Sends digital HIGH/LOW signals to Jetson Nano GPIOs

### `Nvidia Jetson Nano Code.py`

```python
import RPi.GPIO as GPIO

# Define GPIO pins for RGB LED
RED_PIN = 5
GREEN_PIN = 6
BLUE_PIN = 13

# Define GPIO pins for communication from Arduino
POT_PIN1 = 19
POT_PIN2 = 11

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
    print("(", pot_value1, ",", pot_value2, ")")

    if pot_value1 == 0 and pot_value2 == 0:
        set_color((1, 0, 0))  # Red
    elif pot_value1 == 1 and pot_value2 == 1:
        set_color((0, 1, 0))  # Green
    else:
        set_color((0, 0, 1))  # Blue

GPIO.cleanup()

```

## Circuit Diagram

The full circuit is designed in Fritzing. See jetson_finder_schmetics.fzz in this repository.

## Demo Video

https://youtu.be/QDzVxSBcgCM?feature=shared

## Team
  Ata Güneş
  Suat Deniz

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this project for personal, academic, or commercial purposes — just make sure to include proper attribution.

