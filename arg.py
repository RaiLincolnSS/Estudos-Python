#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

if len(sys.argv) <= 2:
	print "Modo de uso: script.py 192.168.0 80"
else:
	print ""
	print "Varrendo o host:",sys.argv[1],"na porta",sys.argv[2]
	print ""
	print "Iniciando Descoberta de hosts: "
	for ip in range(1,10):
		print "Varrendo hosts: 192.168.0.%s" %ip
