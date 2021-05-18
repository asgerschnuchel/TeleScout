import serialcom
import re
import time

port = serialcom.comdetect()


def sendmessage(number, message): #sends message with provided number and message
    port = serialcom.comdetect()
    #checks if the message is more than 150 characters long, and splits the message if it is. 
    serialcom.clearmem(port)
    
    if len(message) >= 150:
        x=149
        res=[message[y-x:y] for y in range(x, len(message)+x,x)]
        
        inr = res
        #send the split message in individual messages
        #this part is kinda cursed, but it works really damn well....
        for y in range(len(res)-1):
            serialcom.clearmem(port)
            sendmessage(number, inr[0])
            serialcom.readline(port)
            time.sleep(5)
            inr.pop(0)
            if len(inr) == 1:
                sendmessage(number, inr[0])
                return

    print("message = " + message)
    serialcom.sendcommand("CMGF=1", port, "AT+")
    serialcom.readline(port)
    time.sleep(2)
    serialcom.sendcommand('CMGW="' + str(number) + '"', port, "AT+")
    serialcom.readline(port)
    time.sleep(2)
    serialcom.sendcommand(message, port, "")
    serialcom.readline(port)
    time.sleep(5)
    serialcom.sendcommand("CMSS=" + serialcom.cmereturn(port) + "\r\n", port, "AT+")
    return