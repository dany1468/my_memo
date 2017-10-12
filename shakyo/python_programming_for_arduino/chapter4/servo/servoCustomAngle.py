#!/usr/bin/env python
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import random

board = PyMata3()
SERVO_PIN = 13

def setup():
    board.servo_config(SERVO_PIN)

def setServoAngle(angle):
    board.analog_write(SERVO_PIN, angle)
    board.sleep(0.015)

def loop():
    while True:
        for i in range(0, 180):
            setServoAngle(i)
        for i in range(180, 1, -1):
            setServoAngle(i)

        i = input("Enter 'y' to continue or Enter to quit): ")
        if i == 'y':
            pass
        else:
            print('shutdown...')
            board.shutdown()
            break

if __name__ == "__main__":
    setup()
    loop()

