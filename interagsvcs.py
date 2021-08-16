#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

print "Interagindo com FTP SERVER"

ip = raw_input("Digite o ip: ")
porta = 21

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect_ex((ip,porta))
banner = meusocket.recv(1024)
print banner

print "Enviando usuario"
meusocket.send("USER ftp\r\n")
banner = meusocket.recv(1024)
print banner

print "Enviando senha"
meusocket.send("PASS ftp\r\n")
banner = meusocket.recv(1024)
print banner
