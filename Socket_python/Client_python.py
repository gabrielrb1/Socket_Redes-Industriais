#!/usr/bin/env python

import socket
import timeit

protocolo = input("Indicar o protocolo de transporte desejado (UTP/TCP)")
tentativas = input("Indique a quantidade de tentativas")

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode("utf-8"))
start = timeit.timeit()
data = s.recv(BUFFER_SIZE)
s.close()
end = timeit.timeit()
elapsed = end-start

#print ("received data:", data)
print (elapsed)
print (protocolo)