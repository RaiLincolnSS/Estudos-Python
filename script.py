#!/usr/bin/python
# -*- coding: utf-8 -*-

#Meu primeiro script
print "Visual"
ip = raw_input("Digite o IP: ") #string
porta = input("Digite a porta: ") #inteiro
ver = 1.2

print "Scan versao:",ver
print "Varrendo Host:",ip,"na porta",porta

print "IP - ",type(ip) #pode remover esses 3 types se quiser...
print "Porta - ",type(porta)
print "Ver - ",type(ver)

print "Visual versao: %.1f \n Varrendo Host: %s na porta %i" %(ver,ip,porta)
