#usr/bin/python
#coding: utf-8

class Celda(object):
	def __init__(self, numero, color, tipo,fichas):
		self.numero = numero
		self.color =color
		self.tipo = tipo
		self.fichas = fichas
		self.coor1 = 0
		self.coor2 = 0
		self.coor3 = 0
