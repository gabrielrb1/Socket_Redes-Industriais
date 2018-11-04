#!/usr/bin/env python

import socket
import time

protocolo = input("Indicar o protocolo de transporte desejado (UTP/TCP) ")
tentativas = int (input("Indique a quantidade de tentativas "))
IP = '127.0.0.1'
PORT = 5005
MESSAGE = "a"
media = 0
maximum = 0
minimum = 1
n = 0
acerto = 0

if protocolo == "TCP":
    print ("TCP selecionado")
    TCP_IP = IP
    TCP_PORT = PORT
    BUFFER_SIZE = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    while (tentativas>0):
        start = time.clock()
        s.send(MESSAGE.encode("utf-8"))
        data = s.recv(BUFFER_SIZE)
        data = data.decode("utf-8")
        end = time.clock()
        elapsed = end-start
        if data == MESSAGE:
            print (elapsed)
            print (data)
            tentativas = tentativas - 1
            n = n + 1
            if elapsed > maximum:
                maximum = elapsed
            elif elapsed < minimum:
                minimum = elapsed
            media = media + elapsed
            acerto = acerto + 1
        else:
            elapsed = 0
    s.close()
    end = time.clock()
    elapsed = end - start
    media = media/n
    assertividade = acerto/n*100
    print ("Tempo médio de resposta: ",elapsed)
    print ("Resposta mais lenta: ",maximum)
    print ("Resposta mais rápida: ",minimum)
    print ("Assertividade [ % ]",assertividade)
    print ("Quantidade de mensagens enviadas: ",n)


elif protocolo == "UDP":
    print("UDP selecionado")
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while (tentativas>0):
        UDP_IP = IP
        UDP_PORT = PORT        
        start = time.clock()
        sock.sendto(MESSAGE.encode("utf-8"), (UDP_IP, UDP_PORT))
        data, addr = sock.recvfrom(20)
        end = time.clock()
        elapsed = end-start
        print (elapsed)
        tentativas = tentativas - 1
        n = n + 1
        media = media + elapsed
        if elapsed > maximum:
            maximum = elapsed
        elif elapsed < minimum:
           minimum = elapsed
        media = media + elapsed
    media = (media)/n
    print ("Tempo médio de resposta: ",media)
    print ("Resposta mais lenta: ",maximum)
    print ("Resposta mais rápida: ",minimum)
    print ("Quantidade de mensagens enviadas: ",n)

else:
    print ("Selecione um protocolo válido")