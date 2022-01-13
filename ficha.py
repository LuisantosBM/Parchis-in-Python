#usr/bin/python
#coding:utf-8
#ficha.py

#Creando la Clase FICHA.
class Ficha(object):
	def __init__(self,esta_en,numero,color,memoria = 1,memoria2 =1):
		self.esta_en = esta_en
		self.num = numero
		self.col = color
		self.memoria = memoria
		self.memoria2 = memoria2
		self.memoria3 = 1
		self.imagen = ""
		self.mover = True
		#self.mover2 = True

	def cambiar_posicion(self,pos):
	
		self.esta_en.fichas.remove(self)
		self.esta_en = pos
		pos.fichas.append(self)
		if self.esta_en.tipo == "meta":
			print "la ficha esta en meta",self.col
		else:
			print "la ficha esta en:",self.esta_en.numero,"y la ficha es de color:",self.col,"y la celda donde esta es de tipo:",self.esta_en.tipo

		
	def capturar_ficha(self,ficha,casa):
		ficha.esta_en.fichas.remove(ficha)
		ficha.esta_en = casa
		casa.fichas.append(ficha)
		print "capturo a una ficha de color:",ficha.col,"y la envia a la casa de color:",ficha.esta_en.color
		return 10
		
	def mostrar_posicion(self):
		dev_pos = self.esta_en
		return dev_pos

#Creamos la una lista con los objetos tipo jugador
colores = ["amarillo","azul","rojo","verde"]

lista_fichas_amarillas=[]
for j in range(4):
	lista_fichas_amarillas.append(Ficha(0,j+1,colores[0]))

lista_fichas_azul=[]
for j in range(4):
	lista_fichas_azul.append(Ficha(0,j+1,colores[1]))
	
lista_fichas_rojo=[]
for j in range(4):
	lista_fichas_rojo.append(Ficha(0,j+1,colores[2]))
	
lista_fichas_verde=[]
for j in range(4):
	lista_fichas_verde.append(Ficha(0,j+1,colores[3]))
