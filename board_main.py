"""
CircuitPython code for the main robot MCU.

Devices:
- Serial to main board (hardware UART)
- Serial to RPi 4 (PIO UART)
- Serial to GPS module (PIO UART)
- Serial to Neato lidar (PIO UART)
- Motor controller (4 GPIO pins)
- Some status LEDs TBD (1 GPIO each)
- Mode selector switch (1 GPIO pin)

Pinout diagram: https://picow.pinout.xyz/
"""

import time
import board
import pwmio
import digitalio

from utils import init_hw_uart, init_pio_uart
from robot import RoboMagellanBot

# Pin setup
MODE_SELECTOR_PIN = None # mode-selector switch (manual / autonomous)
AUTONOMOUS_LAMP_PIN = None # bright yellow light or strobe to indicate autonomous mode is active
VISION_TX_PIN = None
VISION_RX_PIN = None
GPS_TX_PIN = None
GPS_RX_PIN = None
LIDAR_TX_PIN = None
LIDAR_RX_PIN = None
M1_PWM_PIN = None
M1_DIR_PIN = None
M2_PWM_PIN = None
M2_DIR_PIN = None

class Motor:
    FORWARD = 1
    BACKWARD = -1
    
    def __init__(self, pwm_pin, dir_pin, motor_dir=FORWARD):
        self.pwm = pwmio.PWMOut(pwm_pin, frequency=1000, duty_cycle=0)
        self.dir = digitalio.DigitalInOut(dir_pin)
        self.dir.direction = digitalio.Direction.OUTPUT

    def set_speed(self, speed):
        if speed < 0:
            self.dir.value = True
            self.speed = -speed
        else:
            self.dir.value = False
            self.speed = speed
        
        # Flip direction if motor is facing opposite
        if self.motor_dir == Motor.BACKWARD:
            self.dir.value = not self.dir.value
        
        self.pwm.duty_cycle = int(self.speed * 65535)
    
    def stop(self):
        self.pwm.duty_cycle = 0

class Drivetrain:
    def __init__(self, M1_PWM_PIN, M1_DIR_PIN, M2_PWM_PIN, M2_DIR_PIN):
        self.motor_left = Motor(M1_PWM_PIN, M1_DIR_PIN, Motor.FORWARD)
        self.motor_right = Motor(M2_PWM_PIN, M2_DIR_PIN, Motor.BACKWARD)
        self.stop()
        print("Drivetrain reporting for duty!")

    def stop(self):
        self.motor_left.stop()
        self.motor_right.stop()
    
    def turn_left(self, speed):
        self.motor_left.set_speed(-speed)
        self.motor_right.set_speed(speed)

    def turn_right(self, speed):
        self.motor_left.set_speed(speed)
        self.motor_right.set_speed(-speed)
    
    def forward(self, speed):
        self.motor_left.set_speed(speed)
        self.motor_right.set_speed(speed)

    def backward(self, speed):
        self.motor_left.set_speed(-speed)
        self.motor_right.set_speed(-speed)
    
    def test_partern(self):
        self.stop()
        
        # TODO: Honk
        time.sleep(1)
        
        self.turn_right(0.25)
        time.sleep(1)
        self.stop()
        time.sleep(1)
        
        self.turn_left(0.25)
        time.sleep(1)
        self.stop()
        time.sleep(1)
        
        self.forward(0.25)
        time.sleep(1)
        self.stop()
        time.sleep(1)
        
        self.backward(0.25)
        time.sleep(1)
        self.stop()
        
        # TODO: Honk

class MainBoard:

    def __init__(self):
        # UART from safety MCU for conveying non-safety commands from remote
        self.uart_safety = init_hw_uart(board.TX, board.RX)

        # UART for cone prediction from RPi 4
        self.uart_vision = init_pio_uart(VISION_TX_PIN, VISION_RX_PIN)

        # UART for GPS module
        self.uart_GPS = init_pio_uart(GPS_TX_PIN, GPS_RX_PIN)
        
        # UART for Neato lidar
        # self.uart_lidar = None # TODO: setup a PIO UART for the Neato lidar
        self.uart_lidar = init_pio_uart(LIDAR_TX_PIN, LIDAR_RX_PIN)

        # Initialize drivetrain
        self.drivetrain = Drivetrain()

        # Init mode selector switch
        # TODO

        self.bot = RoboMagellanBot()

    def main_loop():
        pass
