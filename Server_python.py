#!/usr/bin/env python

import socket
import time

protocolo = input("Indicar o protocolo de transporte desejado (UTP/TCP) ")
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
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print ("received data:", data)
        conn.send(data)
    conn.close()


elif protocolo == "UDP":
    print("UDP selecionado")
    UDP_IP = IP
    UDP_PORT = PORT
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(20) # buffer size is 1024 bytes
        print ("received message:", data)
        print("Endereço",addr) 
        sock.sendto(data,(addr))# foi necessário mapear a porta usada pelo cliente para fazer o envio, pois a mesma é aleatória
    conn.close()