#!/usr/bin/env python

from pymata_aio.pymata_core import PymataCore
from pymata_aio.constants import Constants
from time import sleep
import asyncio
import signal
import functools

board = PymataCore()
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

async def my_async_callback(data):
    await board.analog_write(LED_PIN, int(translate(data[1], 0, 1023, 255, 0)))

async def setup():
    await board.set_pin_mode(LED_PIN, Constants.PWM)
    await board.set_pin_mode(ANALOG_PIN, Constants.ANALOG, my_async_callback, Constants.CB_TYPE_ASYNCIO)

class GracefulExit(SystemExit):
    code = 1

def raise_graceful_exit():
    raise GracefulExit()

if __name__ == "__main__":
    board.start()

    loop = asyncio.get_event_loop()
    #asyncio.ensure_future(setup())
    loop.run_until_complete(setup())
    loop.add_signal_handler(signal.SIGINT, raise_graceful_exit)

    try:
        loop.run_forever()
    except (GracefulExit):
        # see https://github.com/aio-libs/aiohttp/blob/master/aiohttp/web.py#L460
        pass
    finally:
        if board is not None:
            print('board shutting down...')
            loop.run_until_complete(board.shutdown())

    print('loop closing...')
    loop.close()

