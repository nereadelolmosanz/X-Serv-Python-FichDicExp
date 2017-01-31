#!/usr/bin/python

"""
	Nerea Del Olmo Sanz - GITT
	Ejercico 13.5
	Uso de diccionarios y captura de excepciones
"""

pass_file = open ("/etc/passwd", "r") 		# No es necesario "r", modo read por defecto

file_lines = pass_file.readlines()
dicc = {}

for line in file_lines:
	conf = line.split(":") 		# Busca : en la cadena
	user = conf [0] 			# Se queda con el primer elemento
	shell = conf [-1]			# Se queda con el ultimo elemento
	dicc [user] = shell			# Almacena par clave:USER y valor:SHELL

try:
	print "root", dicc["root"]
	print "imaginario", dicc["imaginario"]
except KeyError:
	print (" ------> ERROR: Invalid key.")

#### Get the total number of users ####
users_number = len(file_lines)
print "\nThere are " + str(users_number) + " users.\n"

pass_file.close()
