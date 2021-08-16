#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket,sys

ip=int(sys.argv[1])
porta=(sys.argv[2])

if len(sys.argv) == "" :
	print "Modo de uso: python portscan.py IPALVO"
for porta in range(1,65535):
	meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if meusocket.connect_ex((ip,porta)) == 0:
	print "Porta",porta,"[ABERTA]"
	meusocket.close()
