from socket  import *
from constCS import *

global add
add = float(1)
global subtract
subtract = float(2)
global multiply
multiply = float(3)
global divide
divide = float(4)

def isNotANumber (data):
  for item in data:
    try:
      float(item)
    except ValueError:
      return True
  return False

def calculate(data, conn):

    data[0] = float(data[0])
    data[1] = float(data[1])
    data[2] = float(data[2])

    if (data[0] == add):
      data = str(data[1] + data[2])
      conn.send(str.encode(data))
    
    elif (data[0] == subtract):      
      data = str(data[1] - data[2])
      conn.send(str.encode(data))  

    elif (data[0] == multiply):     
      data = str(data[1] * data[2])
      conn.send(str.encode(data))  

    elif (data[0] == divide):
      if (data[2] == 0):
        data = "DivisionError"      
      else:
        data = str(data[1] / data[2])
      conn.send(str.encode(data))
    
    else:
      conn.send(str.encode("Error"))

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
Choose one of the following operations and then choose the numbers that you want to apply the operation.
1 - Addition.
2 - Subtraction.
3 - Multiplication.
4 - Division 
As the following example: (100 + 50) => 1 100 50.

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
              
Choose one of the following operations and then choose the numbers that you want to apply the operation.
1 - Addition.
2 - Subtraction.
3 - Multiplication.
4 - Division 
As the following example: (100 + 50) => 1 100 50.

Or type \"end\" to end the program.

You can also type \"man\" if you can't recall the operations.
"""
    conn.send(str.encode(data)) 

  else:  

    data = data.split()
    if( len(data) != 3 or isNotANumber(data)):
      conn.send(str.encode("Error"))
    else:
      calculate(data, conn) 

conn.close()              
