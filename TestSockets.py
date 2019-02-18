import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b = s.connect(("127.0.0.1", 39397))

if b==True :
     print("Successfully connected to server {}".format(s.getsockname()))
     
else :
         print("Error connecting to {}".format(s.getsockname()))
