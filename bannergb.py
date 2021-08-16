#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

ip = raw_input("Digite o ip: ")
porta = input("Digite a porta: ")

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect_ex((ip,porta))
banner = meusocket.recv(1024)
print banner
