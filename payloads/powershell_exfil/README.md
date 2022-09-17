# PowerShell Wireless Data Exfiltration
Instead of a payload, this provides a completely new code.py file for your project due to the complexity of the code. 

# What Does It Do
Upon insertion, the Pico sets up an unprotected wireless access point 'Exfil AP'. It then downloads and executes a PowerShell script. The Pico registers two serial ports - The standard CircuitPython REPL and a data port. The PowerShell identifies the data port and establishes a connection. At the same time, the Pico connects to the same data port, allowing for the two-way flow of information. 

The Pico also sets up a web server, which servers two endpoints - '/' and '/cmd'. 
When a GET request is sent to '/', the output of an executed command is returned (the initial demo command is ipconfig). 
When a GET request is sent to '/cmd', with the query string '?cmd=<command>', that command is sent over the serial port to the PowerShell listener, which executes the command and sends the output back over the serial port to the Pico. 
Whenever a '/cmd' request is executed, '/' updates to return the output of the transmitted command. 
Sending the command 'terminate' will shutdown the Powershell listener.

# Setup
## Boot.py
This payload requires that you update boot.py, you'll find the correct file under /src/optional/enable_data_channel-boot.

## Code.py
Update code.py to point to to your download location.

## Libaries
This payload requires a number of additional libraries:
* adafruit_bus_device [Folder]
* adafruit_esp32spi [Folder]
* asyncio [Folder]
* adafruit_requests.mpy [File]
* adafruit_ticks.mpy [File]

## Hardware
This project is implemented with the now discontinued Pimoroni Pico Wireless Pack. Once CircuitPython has has implemented full support for the Pico W, the code will be updated to use that hardware.  
