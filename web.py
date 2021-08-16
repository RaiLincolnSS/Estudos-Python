#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

objeto = raw_input("Digite o site: ")
site = requests.get(objeto)
status = site.status_code

if (status == 200):
	print "Pagina Existe"
else:
	print "Pagina Inexistente"
