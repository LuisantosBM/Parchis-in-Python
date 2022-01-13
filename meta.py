#usr/bin/python
#coding: utf-8
#meta.py

#from tablero import *
from celda import *

class Meta(Celda):
	def definir_ganador(self):
		if len(self.fichas)==4:
			return True
		else:
			return False
