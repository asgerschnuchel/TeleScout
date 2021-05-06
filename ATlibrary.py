import serialcom
import re
import time

port = serialcom.comdetect()


def sendmessage(number, message): #sends message with provided number and message
    
    #checks if the message is more than 160 characters long, and splits the message if it is. 
    if len(message) >= 159:
        x=159 
        res=[message[y-x:y] for y in range(x, len(message)+x,x)]
        print(len(res))

        #send the split message in individual messages
        for x in range(len(res)-1):
            print("x=" + str(x))
            print(res)
            print(res[x])
            sendmessage(number, res[x])
            serialcom.readline(port)
            time.sleep(2)      

    serialcom.sendcommand("CMGF=1", port, "AT+")
    serialcom.readline(port)
    serialcom.sendcommand('CMGW="' + str(number) + '"', port, "AT+")
    serialcom.readline(port)
    serialcom.sendcommand(message, port, "")
    serialcom.readline(port)
    serialcom.sendcommand("CMSS=" + serialcom.cmereturn(port) + "\r\n", port, "AT+")

sendmessage(21329977, "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")