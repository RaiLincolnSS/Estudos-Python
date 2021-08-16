#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket,sys,re

if len(sys.argv) !=2:
	print "Modo de uso: python smtpbrute.py IP usuario"
	sys.exit(0)
else:

file = open("listasmtp.txt")
for linha in file:
	print linha
	if re.search("252",user):
		print "Usuario encontrado: "+user.strip("252 2.0.0")
	tcp = socket.sock(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect((sys.argv[1],587))
	banner = tcp.recv(1024)
	tcp.send("VRFY"+linha)
	user = tcp.recv(1024)
	print user
