#!/usr/bin/env python

import socket
import time

protocolo = "TCP"
PORT = 5005
IP = '127.0.0.1'

if protocolo == "TCP":
    print("TCP selecionado")    
    TCP_IP = IP
    TCP_PORT = PORT
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print ("received data:", data)
        conn.send(data)
    conn.close()


elif protocolo == "UDP":
    print("UDP selecionado")
    BUFFER_SIZE = 20
    msgFromServer = "Hello"
    bytesToSend = str.encode(msgFromServer)
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
    # Bind to address and ip
    UDPServerSocket.bind((IP, PORT))  
    print("UDP server up and listening")  
    # Listen for incoming datagrams
    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(BUFFER_SIZE)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        print(clientMsg)
        print(clientIP)
        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)