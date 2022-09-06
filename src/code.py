# type: ignore
# code.py template for Raspberry Pi Pico 
# Tested using Circuit Python 7.0.0
# Requires adafruit_hid library

import usb_hid
import time
import usb_hid_map as usb

from adafruit_hid.keyboard import Keyboard

# Disable autoreload
import supervisor
supervisor.disable_autoreload()

kbd = Keyboard(usb_hid.devices)

# Payloads Go Here

def send(this_input, sleep=0.25):
    for item in this_input:
        if type(item) is list:
            kbd.send(*item)
        else:
            kbd.send(item)
    time.sleep(sleep)

time.sleep(2)
# SEND PAYLOADS HERE