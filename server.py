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
  
  elif (data == "end"): 
    data = "\n \nOookay! \nSee you next time! \nHave an excelent day! \n \n"
    conn.send(str.encode(data))
    break
  
  elif (data == "start"):
    data = "\n \nHello! \n \nWelcome to Distributed Computing System. \nType \"calculator\" to use the calculator. \nType \"end\" to end the program.\n\n"
    conn.send(str.encode(data)) # return sent data plus an "*"
  
  elif (data == "calculator"):
    data = "\nGot it! Now choose one of the following operations and then choose the numbers that you want to apply the operation. \n1 - Addition. \n2 - Subtraction.\nAs the following example: (100 + 50) => 1 100 50.\n" 
    conn.send(str.encode(data))
    data = conn.recv(1024)   
    data = bytes.decode(data)
    print(data[0],data[1],data[2])


  else:
    data = "Oops, I could not understando your text. \nPlease try again.\n"
    conn.send(str.encode(data))
conn.close()               # close the connection
