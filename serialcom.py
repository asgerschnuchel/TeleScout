import os
import sys
import time
import serial
import serial.tools.list_ports
import re
import io

def comdetect(): #Searches for avalible ports on system and returns highest port number, which works most of the time :D If this does not work, resolve by to hardcode COM port in ATlibrary
    print('Searching avalible ports on system...')
    ports = serial.tools.list_ports.comports(include_links=False)
    for port in ports :
        time.sleep(0.2)
        print('Found port '+ port.device)
        

    ser = serial.Serial(port.device)
    if ser.isOpen():
        ser.close()

    ser = serial.Serial(port.device, 9600, timeout=1)
    ser.flushInput()
    ser.flushOutput()
    time.sleep(0.4)
    print('Connected ' + ser.name)
    return(ser.name)


def modemready(port): #issues AT command and looks for right echo back. Returns True og false. Port argument obtained from comdetect
    #initialize serial connection
    s = serial.Serial(port, timeout=1)
    #issue command and compare answer to expected outcome
    s.write("AT\r\n".encode())
    response = s.read(64).decode()
    print(response)
    s.close()
    if ("OK") in response:
        return(True)
    else:
        return(False)

def sendtermination(port): #issues equivilant of ctrl+z on serial connection
    s = serial.Serial(port, timeout=1)
    command_variable = chr(26)
    s.write(command_variable.encode('utf-8'))

def sendcommand(command, port, prefix): #send commmand to serial port. Prefix parameter is applied before the command and is executed as one combined command
    s = serial.Serial(port, timeout=1)
    print(str(prefix + command + "\r\n"))
    s.write(str(prefix + command + "\r\n").encode())

def readline(port): #read content on serial port. Returns the last 64 bytes recieved from target in readable text
    s = serial.Serial(port, timeout=1)
    message = ""
    byte = ""
    message = s.read(64).decode()
    return message

def cmereturn(port): #used to recieve cme number/index of message in buffer when sending SMS. Returns buffer location of last created sms if used correctly 
    #open serial connection with target
    s = serial.Serial(port, timeout=1)
    #send termination(ctrl+z) function sendtermination() dosn't work here for unknows reasons....
    command_variable = chr(26)
    s.write(command_variable.encode('utf-8'))
    #read response and put all numbers into list. the last element in the list should always be cme index of the last created message
    response = s.read(128)
    print(response.decode())
    numbers = re.findall('[0-9]+', str(response).strip())
    print(numbers)
    return(numbers[len(numbers)-1])

def cme(port): #Clears SMS atoreage on the module. This is required as more than 2 consequtive long messages might not be able so send ue to lack of SMS buffer.
    s = serial.Serial(prot, timeout = 1)
    sendcommand("CMGD=4", port, "AT+")
    readline(port)
