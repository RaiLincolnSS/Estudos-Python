#!/usr/bin/python
# -*- coding: utf-8 -*-

#import hashlib,sys

#if len(sys.argv) <= 2:
#	print "Modo de uso: python genhashsimple.py 12345678 md5"
#else: 	texto = sys.argv[1]
#type = sys.argv[2]
#md5 = hashlib.md5(texto).hexdigest()
#sha1 = hashlib.sha1(texto).hexdigest()
#
#if type == md5 :
#	print md5
#else:
#	exit(0)
#if type == sha1:
#	print sha1
#else:
#	exit
import hashlib,sys,base64

print
print "         Modo de uso: python genhashsimple.py 12345678 md5"
print

md5 = hashlib.md5()
md5.update(sys.argv[2])

sha1 = hashlib.sha1()
sha1.update(sys.argv[2])

sha256 = hashlib.sha256()
sha256.update(sys.argv[2])

sha512 = hashlib.sha512()
sha512.update(sys.argv[2])

if len(sys.argv) < 2 :
       print
       print "         Hash para sys.argv[2] :"
       print
else:
	if (sys.argv[2]) == "md5" :
		print md5.hexdigest()
		exit(0)
	elif (sys.argv[2]) == "sha1" :
		print sha1.hexdigest()
		exit(0)
	if (sys.argv[2]) == "sha256" :
		print sha256.hexdigest()
		exit(0)
	elif (sys.argv[2]) == "sha512" :
		print sha512.hexdigest()
		exit(0)
	else:
		print "         Argumentos diferem dos dispiniveis"
