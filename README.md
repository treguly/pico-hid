# pico-hid
This code will allow the Raspberry Pi Pico to be detected as an HID and send payloads to a system when plugged in. This project is intended to be educational, demonstrating how to emulate an HID and the risks of BadUSB attacks.

# Installation Steps

## Step 1
Plug in a Raspberry Pi Pico to your computer, it will mount as 'RPI-RP2'. 

## Step 2
[Download CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) as a 'uf2' file. Drag and drop the downloaded file on the mounted 'RPI-RP2' folder. After the copy completes, the Pico will restart and mount as 'CIRCUITPY'.

## Step 3
[Download the CircuitPython Libraries](https://circuitpython.org/libraries) and extract them. Place the extracted adafruit_hid folder from within the extracted file contents within CIRCUITPY/lib/

## Step 4
Download this repo and place src/lib/usb_hid_map.py in CIRCUITPY/lib/ and src/code.py (or src/example/code.py) in CIRCUITPY/, replacing the existing code.py file. The Pico will restart and launch your payload. 

# Optional Steps

## boot.py
Under src/optional, you'll find a boot.py file with two lines of code. When this file is placed on your Pico, it will prevent it from popping up as a USB storage device. Add this after you are happy with your payload and have loaded all of your files. To reset the device, you can access CircuitPython via the serial interface and use the following commands to reset the device to a clean CircuitPython image (it will wipe out boot.py, code.py, and your libraries). 
```
import storage
storage.erase_filesystem()
```
