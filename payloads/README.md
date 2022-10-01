# Unless otherwise noted, all payloads are Windows based. 

All text files are for insertion into code.py in the payload section. You will also need to add send lines in the send section for each payload. Payloads are numbered in order of execution. 

Some of the more complex playloads are included in their own folders, this is because they require additional steps or content.

| Name                        | Platform | Description                                                                               |
|-----------------------------|----------|-------------------------------------------------------------------------------------------|
| powershell_exfil            | Windows  | See README in folder                                                                      |
| screenshot-and-upload       | Windows  | See README in folder                                                                      |
| mac_imessage.txt            | macOS    | Send command output via iMessage.                                                         |
| mac_sms.txt                 | macOS    | Send command output via SMS (requires Text Message Forwarding be enabled for the device). |
| rickroll.txt                | Windows  | Load 'Never Gonna Give You Up' in the default browser.                                    |
| setoolkit-reverse-shell.txt | Windows  | Download and run the Social Engineering Toolkit Reverse Shell PowerShell Payload.         |
| swap-mouse.txt              | Windows  | Swap the Right and Left mouse buttons and log the user out.                               |

# macOS Setup
For the 'mac_' payloads, there are a few additional steps that need to be taken make these work. The biggest one is building a custom firmware to install on your Pico.

## Why Custom Firmware?

When you plug an unrecognized device into a Mac, you are prompted with the Keyboard Setup Assistant. Your Pico will not operate as an HID until you get past this, which involves using the mouse and keyboard. This isn't really possible in this situation, so we need to force macOS to recognize the "keyboard" immediately. We do this by adjusting the USB VID and PID that are built into the firmware.

## Building a Custom uf2 File
(Performed on a Ubuntu 22.04 LTS system)

Building the firmware can be done primarily by following the [instructions provided by Adafruit](https://learn.adafruit.com/building-circuitpython/build-circuitpython). There are a few additional steps that need to be taken. 

1. Before you begin, install build-essential and gettext via apt. 
2. Install the GNU Arm Embedded Toolchain using the [instructions provided on Lindevs](https://lindevs.com/install-gnu-arm-embedded-toolchain-on-ubuntu).
3. Ignore the Adafruit 'Build CircuitPython' section (see Build CircuitPython below)

## Build CircuitPython

1. cd ports/raspberrypi
2. Edit boards/raspberry_pi_pico/mpconfiguboard.mk
3. Update the file with the following:
```
  USB_VID = 0x05AC
  USB_PID = 0x0220
  USB_PRODUCT = "Aluminum Keyboard (ANSI)"
  USB_MANUFACTURER = "Apple, Inc."
```
4. make BOARD=raspberry_pi_pico
5. After the build is complete, take the firmware.uf2 file in board-raspberry_pi_pico folder and use it to flash your Pico

