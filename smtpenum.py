#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket,sys

if len(sys.argv) !=3:
	print "Modo de uso: python smtp enumenum.py IP usuario"
	sys.exit(0)

tcp = socket.sock(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],587))

banner = tcp.recv(1024)
print banner

#tcp.send("VRFY"+sys.argv[2]+"\r\n")
#user = tcp.recv(1024)
#print user
