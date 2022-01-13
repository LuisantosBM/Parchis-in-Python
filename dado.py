#usr/bin/python
#coding: utf-8
#dado.py

import random
#importar random completamente
#from random import *

class Dado(object):
	def __init__(self, numero):
		self.numero=numero
		self.resultado = 0
		self.bandera = False
	def dar_resultado(self):
		resultado = random.randint(1,6)
		if resultado == 6:
			self.bandera = True
		self.resultado = resultado
		return resultado

dado1=Dado(1)
dado2=Dado(2)


if __name__== "__main__":
	print (dado1.dar_resultado())
	print (dado2.dar_resultado())
	print type(dado1.dar_resultado())
