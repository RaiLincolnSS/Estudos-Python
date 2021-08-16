#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.3",5800))
banner = recv(1024)
print banner
s.send("HELP\r\n")
r = s.recv(1024)
print r
