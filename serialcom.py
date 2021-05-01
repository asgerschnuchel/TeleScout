import os
import sys
import time
import serial
import serial.tools.list_ports

def comdetect():
    print('Searching avalible ports on system...')
    ports = serial.tools.list_ports.comports(include_links=False)
    for port in ports :
        time.sleep(0.4)
        print('Found port '+ port.device)
        

    ser = serial.Serial(port.device)
    if ser.isOpen():
        ser.close()

    ser = serial.Serial(port.device, 9600, timeout=1)
    ser.flushInput()
    ser.flushOutput()
    time.sleep(0.8)
    print('Connected ' + ser.name)
    return(ser.name)

