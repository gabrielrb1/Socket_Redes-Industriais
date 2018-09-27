#!/usr/bin/env python

import socket
import timeit

protocolo = input("Indicar o protocolo de transporte desejado (UTP/TCP) ")
tentativas = int (input("Indique a quantidade de tentativas "))
IP = '127.0.0.1'
PORT = 5005
MESSAGE = "a"
media = 0
maximum = 0
minimum = 0
n = 0


if protocolo == "TCP":
    print ("TCP selecionado")
    TCP_IP = IP
    TCP_PORT = PORT
    BUFFER_SIZE = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    while (tentativas>0):
        s.send(MESSAGE.encode("utf-8"))
        start = timeit.timeit()
        data = s.recv(BUFFER_SIZE)
        end = timeit.timeit()
        elapsed = end-start
        print (elapsed)
        tentativas = tentativas - 1
        n = n + 1
        if elapsed > maximum:
            maximum = elapsed
        elif elapsed < minimum:
            minimum = elapsed
        media = media + elapsed
    s.close()
    media = media/n
    print ("Tempo médio de resposta: ",media)
    print ("Resposta mais lenta: ",maximum)
    print ("Resposta mais rápida: ",minimum)


elif protocolo == "UDP":
    print("UDP selecionado")
    while (tentativas>0):
        UDP_IP = IP
        UDP_PORT = PORT
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(MESSAGE.encode("utf-8"), (UDP_IP, UDP_PORT))
        start = timeit.timeit()
        end = timeit.timeit()
        elapsed = end-start
        print (elapsed)
        tentativas = tentativas - 1
        n = n + 1
        media = (media + elapsed)/n
    print("Tempo médio de resposta: ",media)

else:
    print ("Selecione um protocolo válido")