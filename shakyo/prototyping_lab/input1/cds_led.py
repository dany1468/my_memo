#!/usr/bin/env python
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import signal

board = PyMata3()
LED_PIN = 9 
ANALOG_PIN = 0

value = 0

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.  
    return rightMin + (valueScaled * rightSpan)

def my_callback(data):
    global value
    value = translate(data[1], 0, 1023, 0, 255)

def setup():
    board.set_pin_mode(LED_PIN, Constants.PWM)
    board.set_pin_mode(ANALOG_PIN, Constants.ANALOG, my_callback)

def signal_handler(signal, frame):
    board.shutdown()

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    setup()

    while True:
        print('loop... ' + str(int(value)))

        # update LED
        board.analog_write(LED_PIN, int(value))

        board.sleep(2)

