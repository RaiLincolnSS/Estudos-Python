#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket,sys

ip=sys.argv[1]
porta=int(sys.argv[2])

lista=["A"]
contador=100

while len(lista) <= 50:
	lista.append("A"*contador)
	contador = contador + 100

for dados in lista:
	print "Fuzzing com SEND %s bytes"%len(dados)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip,porta))
	s.recv(1024)
	s.send("USER "+dados+"\r\n")
