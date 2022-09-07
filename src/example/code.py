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

# Windows Key + R
payload1 = [usb.RUN]
# Command: calc + <enter>
payload2 = usb.get_sequence('calc')
payload2.append(usb.ENTER)
# Input
payload3 = usb.get_sequence('31337')
# Close Command: ALT+F4
payload4 = [usb.CLOSE]

# Command: notepad + <enter>
payload5 = usb.get_sequence('notepad')
payload5.append(usb.ENTER)
# Input: Tyler was here!
payload6 = usb.get_sequence('Tyler was here!')

def send(this_input, sleep=0.25):
    for item in this_input:
        if type(item) is list:
            kbd.send(*item)
        else:
            kbd.send(item)
    time.sleep(sleep)

time.sleep(2)
# Close the Explorer Window that opens.
send([usb.CLOSE])
send(payload1)
send(payload2, 1)
send(payload3, 2)
send(payload4)
send(payload1)
send(payload5)
send(payload6)
