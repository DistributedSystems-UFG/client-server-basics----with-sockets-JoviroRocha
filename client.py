from asyncio import constants
from socket  import *
from constCS import *

def initialize(controler, s):
    controler = "start"
    s.send(str.encode(controler))
    recieveData(controler, s)

def sendData(controler, s):
    controler = input()
    controler = controler.lower()
    if(controler == ""): 
        controler = "Error"
    s.send(str.encode(controler))
    return controler

def recieveData(controler, s):
    data = s.recv(1024)
    data = bytes.decode(data)
    
    if (data == "Error"):
        print("Sorry but an error ocurred with your request! \nIf you are sendind a math expression, maybe there is one missing bracket, or maybe you are dividing for zero! \nTry again!\n")
    elif (controler == "end" or controler == "man" or controler == "start"):
        print (data)
    else:
        print("\n\nThe answear is: ", data, "\n\n")
    print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:\n")    

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) 
controler = ""
initialize(controler, s)

while True:
    
    controler = sendData(controler, s)
    recieveData(controler, s)
    if(controler == "end"): 
        s.close()
        break

s.close()
