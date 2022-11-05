from socket  import *
from constCS import *

def calculate(data, conn):

    try:
      data = eval(data)
    except:
      data = "Error"
    
    conn.send(str.encode(str(data)))

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  
s.listen(1)           
(conn, addr) = s.accept()   
while True:                

  data = conn.recv(1024) 
  if not data: conn.close()       
  else: data = data.decode('utf-8')

  if (data == "end"): 
    data = """
Oookay!
See you next time!
Have an excelent day!
"""
    conn.send(str.encode(data))
    break
  
  elif (data == "man"):

    data = """
Enter your math equation.
Operations:
% ==> Modulus
** ==> Exponentiation
// ==> Floor division
/ ==> Division
* ==> Multiplication
+ ==> Addition
- ==> Subtraction
Or type \"end\" to end the program.
"""
    conn.send(str.encode(data))

  elif (data == "start"):
    data = """    
       _________
      / ======= \\
     / __________\\
    | ___________ |
    | | -       | |
    | |         | | Hello! Welcome to Distributed Computing System.                                
    | |_________| |_________________________________________________
    \=____________/         
    / \"\"\"\"\"\"\"\"\"\"\" \                       
   / ::::::::::::: \\       
  (_________________) 
              
Enter your equation!

Or type \"end\" to end the program.

You can also type \"man\" if you can't recall the operations.
"""
    conn.send(str.encode(data)) 

  else:  
      calculate(data, conn) 

conn.close()              
