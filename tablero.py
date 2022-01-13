#usr/bin/python
#coding: utf-8
#tablero.py

from celda import *
from meta import *

class Tablero(object):
	def __init__(self, casas, casillas, pasillo_amarillo, pasillo_azul, pasillo_rojo, pasillo_verde):
		self.casas = casas
		self.casillas = casillas
		self.pasillo_amarillo = pasillo_amarillo
		self.pasillo_azul = pasillo_azul
		self.pasillo_rojo = pasillo_rojo
		self.pasillo_verde = pasillo_verde

#Creando el tablero

#Listas Necesarias Para Crear Las Celdas
colores=["amarillo","azul","rojo","verde"]

casas=[]
for i in range(1,5):
	casas.append(i)
casillas=[]
for i in range(1,69):
	casillas.append(i)
pasillo_amarillo=[]
for i in range(1,9):
	pasillo_amarillo.append(i)
pasillo_azul=[]
for i in range(1,9):
	pasillo_azul.append(i)
pasillo_rojo=[]
for i in range(1,9):
	pasillo_rojo.append(i)
pasillo_verde=[]
for i in range(1,9):
	pasillo_verde.append(i)

#Creando las celdas
celdas_casas=[]
for i in casas:
	celda=Celda(i,colores[i-1],"casa",[])
	celdas_casas.append(celda)
celdas_casillas=[]
for i in casillas:
	celda=Celda(i,"blanco","casilla",[])
	celdas_casillas.append(celda)
celdas_pasillo_amarillo=[]
for i in pasillo_amarillo:
	celda=Celda(i,"amarillo","pasillo",[])
	celdas_pasillo_amarillo.append(celda)
celdas_pasillo_azul=[]
for i in pasillo_azul:
	celda=Celda(i,"azul","pasillo",[])
	celdas_pasillo_azul.append(celda)
celdas_pasillo_rojo=[]
for i in pasillo_rojo:
	celda=Celda(i,"rojo","pasillo",[])
	celdas_pasillo_rojo.append(celda)
celdas_pasillo_verde=[]
for i in pasillo_verde:
	celda=Celda(i,"verde","pasillo",[])
	celdas_pasillo_verde.append(celda)


#Se crea el tablero
tablero1=Tablero(celdas_casas,celdas_casillas,celdas_pasillo_amarillo,celdas_pasillo_azul,celdas_pasillo_rojo,celdas_pasillo_verde)

#Modificando el atributo a las casillas seguras
seguras=[5,12,17,22,29,34,39,46,51,56,63,68]

for i in range(len(tablero1.casillas)):
	for j in seguras:
		if tablero1.casillas[i].numero==j:
			tablero1.casillas[i].tipo="segura"
			
#Creando las celdas de tipo meta
tablero1.pasillo_amarillo[7]=Meta(8,"amarillo","meta",[])
tablero1.pasillo_azul[7]=Meta(8,"azul","meta",[])
tablero1.pasillo_rojo[7]=Meta(8,"rojo","meta",[])
tablero1.pasillo_verde[7]=Meta(8,"verde","meta",[])


###Asignando coordenadas#######
tablero1.casillas[0].coor1 = 392
tablero1.casillas[1].coor1 = 392
tablero1.casillas[2].coor1 = 392
tablero1.casillas[3].coor1 = 392
tablero1.casillas[4].coor1 = 392
tablero1.casillas[5].coor1 = 392
tablero1.casillas[6].coor1 = 392
tablero1.casillas[7].coor1 = 392
tablero1.casillas[8].coor1 = 417
tablero1.casillas[9].coor1 = 444
tablero1.casillas[10].coor1 = 471
tablero1.casillas[11].coor1 = 498
tablero1.casillas[12].coor1 = 525
tablero1.casillas[13].coor1 = 552
tablero1.casillas[14].coor1 = 579
tablero1.casillas[15].coor1 = 606
tablero1.casillas[16].coor1 = 606
tablero1.casillas[17].coor1 = 606
tablero1.casillas[18].coor1 = 579
tablero1.casillas[19].coor1 = 552
tablero1.casillas[20].coor1 = 525
tablero1.casillas[21].coor1 = 498
tablero1.casillas[22].coor1 = 471
tablero1.casillas[23].coor1 = 444
tablero1.casillas[24].coor1 = 417
tablero1.casillas[25].coor1 = 392
tablero1.casillas[26].coor1 = 392
tablero1.casillas[27].coor1 = 392
tablero1.casillas[28].coor1 = 392
tablero1.casillas[29].coor1 = 392
tablero1.casillas[30].coor1 = 392
tablero1.casillas[31].coor1 = 392
tablero1.casillas[32].coor1 = 392
tablero1.casillas[33].coor1 = 320
tablero1.casillas[34].coor1 = 246
tablero1.casillas[35].coor1 = 246
tablero1.casillas[36].coor1 = 246
tablero1.casillas[37].coor1 = 246
tablero1.casillas[38].coor1 = 246
tablero1.casillas[39].coor1 = 246
tablero1.casillas[40].coor1 = 246
tablero1.casillas[41].coor1 = 246
tablero1.casillas[42].coor1 = 222
tablero1.casillas[43].coor1 = 195
tablero1.casillas[44].coor1 = 168
tablero1.casillas[45].coor1 = 141
tablero1.casillas[46].coor1 = 114
tablero1.casillas[47].coor1 = 87
tablero1.casillas[48].coor1 = 60
tablero1.casillas[49].coor1 = 33
tablero1.casillas[50].coor1 = 33
tablero1.casillas[51].coor1 = 33
tablero1.casillas[52].coor1 = 60
tablero1.casillas[53].coor1 = 87
tablero1.casillas[54].coor1 = 114
tablero1.casillas[55].coor1 = 141
tablero1.casillas[56].coor1 = 168
tablero1.casillas[57].coor1 = 195
tablero1.casillas[58].coor1 = 222
tablero1.casillas[59].coor1 = 246
tablero1.casillas[60].coor1 = 246
tablero1.casillas[61].coor1 = 246
tablero1.casillas[62].coor1 = 246
tablero1.casillas[63].coor1 = 246
tablero1.casillas[64].coor1 = 246
tablero1.casillas[65].coor1 = 246
tablero1.casillas[66].coor1 = 246
tablero1.casillas[67].coor1 = 320
#############################################################
tablero1.casillas[0].coor2 = 610
tablero1.casillas[1].coor2 = 583
tablero1.casillas[2].coor2 = 556
tablero1.casillas[3].coor2 = 529
tablero1.casillas[4].coor2 = 502
tablero1.casillas[5].coor2 = 475
tablero1.casillas[6].coor2 = 448
tablero1.casillas[7].coor2 = 421
tablero1.casillas[8].coor2 = 398
tablero1.casillas[9].coor2 = 398
tablero1.casillas[10].coor2 = 398
tablero1.casillas[11].coor2 = 398
tablero1.casillas[12].coor2 = 398
tablero1.casillas[13].coor2 = 398
tablero1.casillas[14].coor2 = 398
tablero1.casillas[15].coor2 = 398
tablero1.casillas[16].coor2 = 326
tablero1.casillas[17].coor2 = 251
tablero1.casillas[18].coor2 = 251
tablero1.casillas[19].coor2 = 251
tablero1.casillas[20].coor2 = 251
tablero1.casillas[21].coor2 = 251
tablero1.casillas[22].coor2 = 251
tablero1.casillas[23].coor2 = 251
tablero1.casillas[24].coor2 = 251
tablero1.casillas[25].coor2 = 227
tablero1.casillas[26].coor2 = 200
tablero1.casillas[27].coor2 = 173
tablero1.casillas[28].coor2 = 146
tablero1.casillas[29].coor2 = 119
tablero1.casillas[30].coor2 = 92
tablero1.casillas[31].coor2 = 65
tablero1.casillas[32].coor2 = 38
tablero1.casillas[33].coor2 = 38
tablero1.casillas[34].coor2 = 38
tablero1.casillas[35].coor2 = 65
tablero1.casillas[36].coor2 = 92
tablero1.casillas[37].coor2 = 119
tablero1.casillas[38].coor2 = 146
tablero1.casillas[39].coor2 = 173
tablero1.casillas[40].coor2 = 200
tablero1.casillas[41].coor2 = 227
tablero1.casillas[42].coor2 = 251
tablero1.casillas[43].coor2 = 251
tablero1.casillas[44].coor2 = 251
tablero1.casillas[45].coor2 = 251
tablero1.casillas[46].coor2 = 251
tablero1.casillas[47].coor2 = 251
tablero1.casillas[48].coor2 = 251
tablero1.casillas[49].coor2 = 251
tablero1.casillas[50].coor2 = 326
tablero1.casillas[51].coor2 = 398
tablero1.casillas[52].coor2 = 398
tablero1.casillas[53].coor2 = 398
tablero1.casillas[54].coor2 = 398
tablero1.casillas[55].coor2 = 398
tablero1.casillas[56].coor2 = 398
tablero1.casillas[57].coor2 = 398
tablero1.casillas[58].coor2 = 398
tablero1.casillas[59].coor2 = 421
tablero1.casillas[60].coor2 = 448
tablero1.casillas[61].coor2 = 475
tablero1.casillas[62].coor2 = 502
tablero1.casillas[63].coor2 = 529
tablero1.casillas[64].coor2 = 556
tablero1.casillas[65].coor2 = 583
tablero1.casillas[66].coor2 = 610
tablero1.casillas[67].coor2 = 610


#########################################################################
#####coordenadas de la casa##################################################

tablero1.casas[0].coor3 = []
tablero1.casas[1].coor3 = []
tablero1.casas[2].coor3 = []
tablero1.casas[3].coor3 = []
#### amarillo############

tablero1.casas[0].coor3.append(446)
tablero1.casas[0].coor3.append(575)

tablero1.casas[0].coor3.append(446)
tablero1.casas[0].coor3.append(606)

tablero1.casas[0].coor3.append(476)
tablero1.casas[0].coor3.append(606)

tablero1.casas[0].coor3.append(506)
tablero1.casas[0].coor3.append(606)

#### azul ####
tablero1.casas[1].coor3.append(446)
tablero1.casas[1].coor3.append(155)

tablero1.casas[1].coor3.append(446)
tablero1.casas[1].coor3.append(186)

tablero1.casas[1].coor3.append(476)
tablero1.casas[1].coor3.append(186)

tablero1.casas[1].coor3.append(506)
tablero1.casas[1].coor3.append(186)


##### rojo ##################


tablero1.casas[2].coor3.append(131)
tablero1.casas[2].coor3.append(140)

tablero1.casas[2].coor3.append(131)
tablero1.casas[2].coor3.append(186)

tablero1.casas[2].coor3.append(161)
tablero1.casas[2].coor3.append(186)

tablero1.casas[2].coor3.append(191)
tablero1.casas[2].coor3.append(186)



##### verde ##################


tablero1.casas[3].coor3.append(131)
tablero1.casas[3].coor3.append(575)

tablero1.casas[3].coor3.append(131)
tablero1.casas[3].coor3.append(606)

tablero1.casas[3].coor3.append(161)
tablero1.casas[3].coor3.append(606)

tablero1.casas[3].coor3.append(191)
tablero1.casas[3].coor3.append(606)



if __name__=="__main__":
	#Pruebas
	print "Lista de casas"
	for i in range(len(tablero1.casas)):
		print tablero1.casas[i].numero,
	
	print "\nLista de casillas"
	for i in range(len(tablero1.casillas)):
		print tablero1.casillas[i].numero,
	
	print "\nLista de pasillo amarillo"
	for i in range(len(tablero1.pasillo_amarillo)):
		print tablero1.pasillo_amarillo[i].numero,
	
	print "\nLista de pasillo azul"
	for i in range(len(tablero1.pasillo_azul)):
		print tablero1.pasillo_azul[i].numero,
	
	print "\nLista de pasillo rojo"
	for i in range(len(tablero1.pasillo_rojo)):
		print tablero1.pasillo_rojo[i].numero,
	
	print "\nLista de pasillo verde"
	for i in range(len(tablero1.pasillo_verde)):
		print tablero1.pasillo_verde[i].numero,
	
	print "\nLista de casillas seguras"
	for i in range(len(tablero1.casillas)):
		if tablero1.casillas[i].tipo=="segura":
			print tablero1.casillas[i].numero,
	print "\nLista de metas"
	for i in range(len(tablero1.pasillo_amarillo)):
		if tablero1.pasillo_amarillo[i].tipo=="meta":
			print tablero1.pasillo_amarillo[i].numero,
		if tablero1.pasillo_azul[i].tipo=="meta":
			print tablero1.pasillo_azul[i].numero,
		if tablero1.pasillo_rojo[i].tipo=="meta":
			print tablero1.pasillo_rojo[i].numero,
		if tablero1.pasillo_verde[i].tipo=="meta":
			print tablero1.pasillo_verde[i].numero,
