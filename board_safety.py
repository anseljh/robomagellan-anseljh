"""
CircuitPython code for the safety mechanism MCU.

Devices:
- RFM69 radio (SPI)
- Relay (1 GPIO)
- Serial to main board (UART)
- Some status LEDs TBD (1 GPIO each)
- Maybe a strobe light, TBD (1 GPIO)

Pinout diagram: https://pico.pinout.xyz/
"""

import time
import board
import busio
import digitalio

from utils import init_hw_uart, init_radio

# Pin setup
PIN_RADIO_CS = board.D5
PIN_RADIO_RESET = board.D6

class SafetyBoard:
    def __init__(self):
        # Init RFM69 radio
        self.radio = init_radio(PIN_RADIO_CS, PIN_RADIO_RESET)
        
        # UART to main board for conveying non-safety commands from remote
        self.uart_main = init_hw_uart(board.TX, board.RX)

    def main_loop():
        pass
