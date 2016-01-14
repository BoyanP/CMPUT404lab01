#!/usr/bin/env python

# Copyright (c) Boyan Peychoff

import socket, os , sys , select 

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind(("0.0.0.0", 8000))
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

serverSocket.listen(5)

while 1:
    print "waiting for mum's spaghetti"

    (clientSocket , address) = serverSocket.accept()

    print "we got a connection from : %s" % {str(address)} 

    pid = os.fork()
    if(pid == 0 ):
        #this da child homie 
        outgoingSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        outgoingSocket.connect(("www.google.com", 80))


        request = bytearray()
        while True:
            clientSocket.setblocking(0)
            try:
                part = clientSocket.recv(1024)
            except socket.error as exception:
                if exception.errno == 11:
                    part = None
                else:
                    raise
            if(part):
                request.extend(part)
                outgoingSocket.sendall(part)

            outgoingSocket.setblocking(0)
            try:
                part = outgoingSocket.recv(1024)
            except socket.error as exception:
                if exception.errno == 11:
                    part = None
                else:
                    raise
                
            if(part):
                request.extend(part)
                clientSocket.sendall(part)

            select.select([clientSocket,outgoingSocket],
                          [],
                          [clientSocket,outgoingSocket],
                          1.0)
        print request
        sys.exit(0)



    else:
        #here's the parent 
        pass

