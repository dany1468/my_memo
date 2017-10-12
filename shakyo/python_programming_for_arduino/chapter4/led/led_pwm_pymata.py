#!/usr/bin/env python
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import random

board = PyMata3()
pin = 11

def setup():
    board.set_pin_mode(pin, Constants.PWM)

def random_blink():
    for i in range(0, 99):
        r = random.randint(1, 100)
        board.analog_write(pin, r)
        board.sleep(0.1)

if __name__ == "__main__":
    setup()
    random_blink()
    board.analog_write(pin, 0)

