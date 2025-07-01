"""
CircuitPython code for the safety mechanism MCU.
Board: Raspberry Pi Pico 1

Devices:
- RFM69 radio (SPI)
- Motor-enable relay (1 GPIO)
- Cytron motor driver (4 GPIO)
- Serial to main board (UART)
- Autonomous-mode strobe via relay (1 GPIO)
- Some status LEDs TBD (1 GPIO each)

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
