"""
Blink test on Raspberry Pi Pico.
Blink on-board LED and an external LED on pin 20 (GP15).
"""

import board
import digitalio
import time

# Pin setup
ONBOARD_LED_PIN = board.LED
EXT_LED_PIN = board.GP15

onboard_led = digitalio.DigitalInOut(ONBOARD_LED_PIN)
onboard_led.direction = digitalio.Direction.OUTPUT
ext_led = digitalio.DigitalInOut(EXT_LED_PIN)
ext_led.direction = digitalio.Direction.OUTPUT

while True:
    onboard_led.value = True
    ext_led.value = False
    print("Blinking on-board LED")
    time.sleep(0.5)
    onboard_led.value = False
    ext_led.value = True
    print("Blinking external LED")
    time.sleep(0.5)
