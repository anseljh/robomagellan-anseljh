"""
CircuitPython code for the remote MCU.
Board: Adafruit QT PY RP2040
    https://circuitpython.org/board/adafruit_qtpy_rp2040/

Devices:
- RFM69 radio (SPI)
- Nunchuk adapter (I2C)
- Dead-man's switch button (1 GPIO)
- Autonomous/manual selector switch (1 GPIO)
- Autonomous-mode LED (1 GPIO)

Sparkfun: How to Build a Remote Kill Switch
    https://learn.sparkfun.com/tutorials/how-to-build-a-remote-kill-switch
"""

import time
import board
import digitalio
import busio

from wiichuck.nunchuk import Nunchuk

from utils import init_radio

# Pin setup
PIN_MOSI = board.GP3
PIN_MISO = board.GP4
PIN_SCK = board.GP6
PIN_CS = board.GP5
PIN_RESET = board.GP20
QWIIC_SCL = board.GP23
QWIIC_SDA = board.GP22


class RemoteBoard:
    def __init__(self):
        # Init RFM69 radio
        self.radio = init_radio(
            mosi_pin=PIN_MOSI,
            miso_pin=PIN_MISO,
            clock_pin=PIN_SCK,
            cs_pin=PIN_CS,
            reset_pin=PIN_RESET,
        )
        print("RFM69 radio initialized!")
        print(self.radio)
        print(f"Temperature: {self.radio.temperature}C")
        print(f"Frequency: {self.radio.frequency_mhz} MHz")
        print(f"Bit rate: {self.radio.bitrate / 1000} kbit/s")
        print(f"Frequency deviation: {self.radio.frequency_deviation} Hz")

        # Instantiate Nunchuck
        i2c1 = busio.I2C(QWIIC_SCL, QWIIC_SDA)
        self.nunchuck = Nunchuk(i2c1)
        print("Nunchuk initialized!")
        print(self.nunchuck)

        # Init enabling switch
        # TODO

    def main_loop():
        pass
