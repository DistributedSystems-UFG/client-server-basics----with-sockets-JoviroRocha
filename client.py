from asyncio import constants
from socket  import *
from constCS import * 

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
controler = "start"
while True:
    s.send(str.encode(controler))
    data = s.recv(1024)
    print (bytes.decode(data))
    controler = input()
    if (controler == "end"): break
s.close()