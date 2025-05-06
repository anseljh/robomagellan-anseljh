"""
CircuitPython code for the remote MCU.

Devices:
- RFM69 radio (SPI)
- Nunchuck (I2C)
- Dead-man's switch button (1 GPIO)
- Some other buttons TBD (1 GPIO each)
- Some status LEDs TBD (1 GPIO each)

Pinout diagram: https://pico.pinout.xyz/

Sparkfun: How to Build a Remote Kill Switch 
    https://learn.sparkfun.com/tutorials/how-to-build-a-remote-kill-switch
"""

import time
import board
import digitalio

from wiichuck.nunchuk import Nunchuk

from utils import init_radio

# Pin setup
PIN_RADIO_CS = board.D5
PIN_RADIO_RESET = board.D6

class RemoteBoard:
    def __init__(self):
        # Init RFM69 radio
        self.radio = init_radio(PIN_RADIO_CS, PIN_RADIO_RESET)
        
        # Instantiate Nunchuck
        self.nunchuck = Nunchuk(board.I2C())

        # Init enabling switch
        # TODO
       
    def main_loop():
        pass
