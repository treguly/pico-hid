# pico-hid
This code will allow the Raspberry Pi Pico to be detected as an HID device and send payloads to a system when plugged in. 

# Installation Steps

## Step 1
Plug in a Raspberry Pi Pico to your computer, it will mount as 'RPI-RP2'. 

## Step 2
[Download CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) as a 'uf2' file. Drag and drop the downloaded file on the mounted 'RPI-RP2' folder. After the copy completes, the Pico will restart and mount as 'CIRCUITPY'.

## Step 3
[Download the CircuitPython Libraries](https://circuitpython.org/libraries) and extract them. Place the extracted adafruit_hid folder from within the extracted file contents within CIRCUITPY/lib/

## Step 4
Download this repo and place src/lib/usb_hid_map.py in CIRCUITPY/lib/ and src/code.py (or src/example/code.py) in CIRCUITPY/, replacing the existing code.py file. The Pico will restart and launch your payload. 
