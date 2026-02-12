"""
Test out a relay
"""

import board
import digitalio
import time

print("Relay test")

relay_pin = board.GP16
relay = digitalio.DigitalInOut(relay_pin)
relay.switch_to_output()

val = False
while True:
    val = not val
    print(val)
    relay.value = val
    time.sleep(1.0)
