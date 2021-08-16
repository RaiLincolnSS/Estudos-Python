#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket,sys

ip = raw_input("Digite o ip: ")
porta = input("Digite a porta: ")

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = meusocket.connect_ex((ip,porta))

if (res == 0):
	print("Porta Aberta")
else:
	print("Porta Fechada")
