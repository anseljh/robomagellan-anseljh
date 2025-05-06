"""
Utility functions common to all the Pico boards
"""

import time
import board
import busio
import digitalio

RADIO_FREQ_MHZ = 915.0


def init_hw_uart(tx_pin, rx_pin):
    uart = busio.UART(tx_pin, rx_pin, baudrate=9600)
    return uart

def init_pio_uart(rx_pin, tx_pin):
    pass

# Initialize RFM69 radio
def init_radio(cs_pin, reset_pin, freq_mhz):
    """
    Initialize the RFM69 radio module.
    CircuitPython library: https://docs.circuitpython.org/projects/rfm69/en/latest/index.html
    """
    import adafruit_rfm69
    CS = digitalio.DigitalInOut(cs_pin)
    RESET = digitalio.DigitalInOut(reset_pin)
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, RADIO_FREQ_MHZ)
    rfm69.encryption_key = (
        b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
    )
    # Print out some chip state:
    print("RFM69 radio initialized!")
    print("Temperature: {0}C".format(rfm69.temperature))
    print("Frequency: {0}mhz".format(rfm69.frequency_mhz))
    print("Bit rate: {0}kbit/s".format(rfm69.bitrate / 1000))
    print("Frequency deviation: {0}hz".format(rfm69.frequency_deviation))
    return rfm69
