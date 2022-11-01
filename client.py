from asyncio import constants
from socket  import *
from constCS import * 

def initialize(controler, s):
    controler = "start"
    s.send(str.encode(controler))
    recieveData(s)

def sendData(s):
    controler = input()
    s.send(str.encode(controler))
    return controler

def recieveData(s):
    data = s.recv(1024)
    print (bytes.decode(data))

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
controler = ""
initialize(controler, s)

while True:
    
    if (sendData(s) == "end"): break
    recieveData(s)
    
s.close()
