#!/usr/bin/python

lista=["A"]
contador=100

while len(lista) <= 50:
	lista.append("A"*contador)
	contador = contador + 100

for dados in lista:
	print "Fuzzing com SEND %s bytes"%len(dados)


#import socket
#
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("192.168.0.3",5800))
#banner = recv(1024)
#print banner
#s.send("HELP\r\n")
#r = s.recv(1024)
#print r
