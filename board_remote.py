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
import busio
from digitalio import DigitalInOut, Direction, Pull

from adafruit_nunchuk import Nunchuk

from utils import init_radio

# Pin setup
PIN_MOSI = board.GP3
PIN_MISO = board.GP4
PIN_SCK = board.GP6
PIN_CS = board.GP5
PIN_RESET = board.GP20
QWIIC_SCL = board.GP23
QWIIC_SDA = board.GP22
SWITCH_DEAD_MAN = board.A0  # A0 for enabling/dead-man's switch
SWITCH_MODE = board.A1  # A1 for autonomous/manual mode switch
# nothing on A2 yet
LED_MODE = board.A3  # A3 for autonomous/manual mode LED


class RemoteBoard:
    def __init__(self):
        # Init mode LED
        self.led_mode = DigitalInOut(LED_MODE)
        self.led_mode.direction = Direction.OUTPUT
        print("Mode LED initialized.")

        # Init mode switch
        self.switch_mode = DigitalInOut(SWITCH_MODE)
        self.switch_mode.direction = Direction.INPUT
        # self.switch_mode.pull = None  # Pull.UP  # Pull-up resistor for switch
        print("Mode switch initialized.")

        # Init dead-man's switch
        self.switch_enabling = DigitalInOut(SWITCH_DEAD_MAN)
        self.switch_enabling.direction = Direction.INPUT
        # self.switch_enabling.pull = Pull.UP
        print("Dead-man's switch initialized.")

        # Init RFM69 radio
        self.radio = init_radio(
            mosi_pin=PIN_MOSI,
            miso_pin=PIN_MISO,
            clock_pin=PIN_SCK,
            cs_pin=PIN_CS,
            reset_pin=PIN_RESET,
            freq_mhz=915.0,
        )
        print("RFM69 radio initialized.")
        print(self.radio)
        print(f"Temperature: {self.radio.temperature}C")
        print(f"Frequency: {self.radio.frequency_mhz} MHz")
        print(f"Bit rate: {self.radio.bitrate / 1000} kbit/s")
        print(f"Frequency deviation: {self.radio.frequency_deviation} Hz")

        # Instantiate Nunchuck
        i2c1 = busio.I2C(QWIIC_SCL, QWIIC_SDA)
        try:
            self.nunchuck = Nunchuk(i2c1)
            print("Nunchuk initialized.")
            print(self.nunchuck)
        except ValueError as e:
            print(f"Failed to initialize Nunchuk: {e}")
            self.nunchuck = None
        
        print("** Remote board initialized **")

    def main_loop(self):
        print("Remote main loop beginning...")
        while True:
            if self.switch_mode.value:
                print("Mode switch is HIGH")
                self.led_mode.value = True
                print("Autonomous mode active.")
            else:
                print("Mode switch is LOW")
                self.led_mode.value = False
                print("Manual mode active.")

            print(f"Enabling switch: {self.switch_enabling.value}")

            # Read the Nunchuk state
            if self.nunchuck:
                print(f"Nunchuk state: stick {self.nunchuck.joystick} / buttons {self.nunchuck.buttons} / accel {self.nunchuck.acceleration}")

            time.sleep(0.5)


if __name__ == "__main__":
    board = RemoteBoard()
    for _ in range(3):
        board.led_mode.value = True
        time.sleep(0.5)
        print("Blinking")
        board.led_mode.value = False
        time.sleep(0.5)
    board.main_loop()
