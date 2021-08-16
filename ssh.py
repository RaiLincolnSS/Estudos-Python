#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:

	ssh.connect('192.168.15.3', username='root', password='toor')

except paramiko.ssh_exception.AuthenticationException:
	print "Acesso Falhou"
else:
	print "Conectado"

	stdin, stdout, stderr = ssh.exec_command('id')

	for linha in stdout.readlines():

		print linha.strip()

ssh.close()
