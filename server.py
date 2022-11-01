from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  data = bytes.decode(data)
  if not data: break       # stop if client stopped
  if (data == "end"): 
    data = "\n \nOookay! \nSee you next time! \nHave an excelent day! \n \n"
    conn.send(str.encode(data))
    break
  elif (data == "start"):
    data = "\n \nHello! \n \nWelcome to Distributed Computing System. \nType \"calculator\" to use the calculator. \nType \"end\" to end the program.\n\n"
    conn.send(str.encode(data)) # return sent data plus an "*"
conn.close()               # close the connection
