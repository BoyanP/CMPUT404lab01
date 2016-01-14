#!/usr/bin/env python

# Copyright (c) Boyan Peychoff


import socket 

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect(("www.google.com", 80))

httpRequest = """GET / HTTP/1.0 \r\n\r\n"""

clientSocket.sendall(httpRequest)

response = bytearray()

while 1:

    part = clientSocket.recv(1024)
    if(part):    
        response.extend(part)
    else:
        break

print response



    
