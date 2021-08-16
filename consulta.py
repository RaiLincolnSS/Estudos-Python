#!/usr/share/python
# -*- coding: utf-8 -*-
import socket,sys
if len(sys.argv) <= 1:
	print "Use mode to search by hostnames: python consulta.py exemple.com \n"
	print "Use mode to search by ip address: python consulta.py 191.250.22.1 \n"
else:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("whois.iana.org",43))
	s.send(sys.argv[1]+"\r\n")
	resposta = s.recv(1024).split()
	whois = resposta[19]
	s.close()
	s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s1.connect((whois,43))
	s1.send(sys.argv[1]+"\r\n")
	resp = s1.recv(1024)
	print resp
