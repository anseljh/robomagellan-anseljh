"""
Blink test on QT PY RP2040.
Blink on-board LED and an external LED on pin 8 (RX).
https://learn.adafruit.com/adafruit-qt-py-2040/built-in-neopixel-led
"""

import board
import digitalio
import time
import neopixel

# Pin setup
EXT_LED_PIN = board.GP5
NEOPIXEL_BRIGHTNESS = 0.5

pixel = neopixel.NeoPixel(board.LED, 1)
ext_led = digitalio.DigitalInOut(EXT_LED_PIN)
ext_led.direction = digitalio.Direction.OUTPUT

count = 0
while True:
    count += 1
    ext_led.value = True
    pixel.brightness = 0.0
    print("Blinking on-board LED")
    time.sleep(0.5)

    ext_led.value = False
    # mod = count % 3
    # if mod == 0:
    #     pixel.fill((255, 0, 0))  # Set external LED to red
    # elif mod == 1:
    #     pixel.fill((0, 255, 0))  # Set external LED to geen
    # elif mod == 2:
    #     pixel.fill((0, 0, 255))  # Set external LED to blue
    # else:
    #     print("impossible math is impossible")
    # pixel.fill((255, 0, 0))
    # pixel.brightness = NEOPIXEL_BRIGHTNESS
    # print("Blinking external LED")
    time.sleep(0.5)
