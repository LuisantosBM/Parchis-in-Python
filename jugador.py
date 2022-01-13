#usr/bin/python
#coding: utf-8

from ficha import *
from tablero import *
from celda import *
from dado import *

class Jugador(object):
	
	def __init__(self,nombre,color, fichas,casa):
		self.nom = nombre
		self.color = color
		self.fichas = fichas #lista de las fichas del jugador
		self.turno = False
		self.casa = casa
		self.extra = False
		self.dado1_usado = False
		self.dado2_usado = False
		self.tiro = 1
		self.botones = 0
	
	def lanzar_dado(self,dado):
		r = dado.dar_resultado()
		return r

	def mover_ficha(self,ficha,m,tablero):
		
		celda = ficha.mostrar_posicion()
		
		if celda.tipo == "pasillo":
			
			if celda.numero + m <=8:
				tem = True
				if celda.color == "amarillo":
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.pasillo_amarillo[i].fichas) == 2 and tablero.pasillo_amarillo[i].tipo !="meta":
							 tem = False
							 
					if tem==True:
						ficha.cambiar_posicion(tablero.pasillo_amarillo[celda.numero+m-1])

						#return tem
					else:
						pass
						#return False
				elif celda.color == "azul":
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.pasillo_azul[i].fichas) == 2 and tablero.pasillo_amarillo[i].tipo !="meta":
							 tem = False
							 
					if tem==True:
						ficha.cambiar_posicion(tablero.pasillo_azul[celda.numero+m-1])
						
						#return tem
					else:
						pass
						#return False
				elif celda.color == "verde":
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.pasillo_verde[i].fichas) == 2 and tablero.pasillo_amarillo[i].tipo !="meta":
							 tem = False
							 
					if tem==True:
						ficha.cambiar_posicion(tablero.pasillo_verde[celda.numero+m-1])
				
						#return tem
					else:
						pass
						#return False
				elif celda.color == "rojo":
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.pasillo_rojo[i].fichas) == 2 and tablero.pasillo_amarillo[i].tipo !="meta":
							 tem = False
							 
					if tem==True:
						ficha.cambiar_posicion(tablero.pasillo_rojo[celda.numero+m-1])
		
						#return tem
					else:
						pass
						#return False
			else:
				pass
				#return False
								
		else:
			#ficha verde
			if ficha.col=="verde":
				if celda.numero + m <= 68 and ficha.memoria == 1:
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2:
							 tem = False
						elif i == 67:
							ficha.memoria = 2
							 
					if tem==True:
						ficha.cambiar_posicion(tablero.casillas[celda.numero+m-1])
									#return tem
					else:
						pass
						#return False
				else:
					
					if celda.numero + m <= 51 and ficha.memoria ==3:
						tem = True
						for i in range(celda.numero, celda.numero + m):
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
								 
						if tem==True:
							ficha.cambiar_posicion(tablero.casillas[celda.numero+m-1])
										
										#return tem
						else:
							pass
							#return False
					
					elif celda.numero + m-68 <= 51 and ficha.memoria !=3:
						tem = True
						for i in range(celda.numero,68):
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
							elif i == 67:
								ficha.memoria = 3
								 
						for i in range(celda.numero+m-68):
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
								 
						if tem==True:
							ficha.cambiar_posicion(tablero.casillas[celda.numero+m-68-1])
							#return tem
						else:
							pass
							#return False	
					else:
					
						falt = celda.numero + m - 51 
						
						tem = True
						for i in range(celda.numero,51):
							if len(tablero.casillas[i].fichas) != 2:
								 tem = False
						
								 
						if tem == True:
							if len(tablero.pasillo_verde[0].fichas)==2:
								ficha.cambiar_posicion(tablero.pasillo_verde[0])
								
								self.mover_ficha(ficha,falt-1,tablero)
								#return tem
							else:
								pass
								#return False	
							
						else:
							pass
							#return False
			
			#ficha roja			
			elif ficha.col=="rojo":
				print ficha.memoria
				if celda.numero + m <= 68 and ficha.memoria == 1:
				
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2:
						
							tem = False
						elif i == 67:
							ficha.memoria = 2
							 
					if tem==True:
					
						ficha.cambiar_posicion(tablero.casillas[celda.numero+m-1])
									
									#return tem
					else:
						pass
						#return False
				else:
					
					if celda.numero + m <= 34 and ficha.memoria == 3:
						tem = True
						for i in range(celda.numero,celda.numero + m):
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
								
								 
						if tem==True:
							ficha.cambiar_posicion(tablero.casillas[celda.numero+m-1])
										
										#return tem
						else:
							pass
							#return False
					
					elif celda.numero + m-68 <= 34 and ficha.memoria!=3 :
						tem = True
						for i in range(celda.numero,68):
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
							elif i == 67:
								ficha.memoria = 3
								 
						for i in range(celda.numero+m-68):
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
								 
						if tem==True:
							ficha.cambiar_posicion(tablero.casillas[celda.numero+m-68-1])
										
										#return tem
						else:
							pass
							#return False
					else:
						
						falt = celda.numero + m - 34
						
						tem = True
						for i in range(celda.numero,34):
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
								 
						if tem == True:
							if len(tablero.pasillo_rojo[0].fichas)!=2:
								ficha.cambiar_posicion(tablero.pasillo_rojo[0])
								
								self.mover_ficha(ficha,falt-1,tablero)
								#return tem
							else:
								pass
								#return False	
							
						else:
							pass
							#return False		
									
			#ficha amarilla			
			elif ficha.col=="amarillo":
				if celda.numero + m <= 68 :
					#print "aqui estoy"
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2:
							tem = False
							break
							 
					if tem==True:
						ficha.cambiar_posicion(tablero.casillas[celda.numero+m-1])
									
									#return tem
					else:
						pass
						#return False
				else:
					print "Entrando al pasillo"
					falt = celda.numero + m - 68
					
					tem = True
					for i in range(celda.numero,68):
						if len(tablero.casillas[i].fichas) == 2:
							 tem = False
							 
					if tem == True:
						if len(tablero.pasillo_amarillo[0].fichas)!=2:
							ficha.cambiar_posicion(tablero.pasillo_amarillo[0])
							
							self.mover_ficha(ficha,falt-1,tablero)
							#return tem
						else:
							pass
							#return False	
						
					else:
						pass
						#return False							
							
			#ficha azul			
			elif ficha.col=="azul":
				
				if celda.numero + m <= 68 and ficha.memoria == 1:
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2 and i!=67:
							 tem = False
							
						elif i == 67:
							
							ficha.memoria = 2
							 
					if tem==True:
						ficha.cambiar_posicion(tablero.casillas[celda.numero+m-1])
									
									#return tem
					else:
						pass
						#return False
				else:
					
					if celda.numero + m <= 17 and ficha.memoria == 3:
						tem = True
						for i in range(celda.numero,celda.numero + m):
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
								
						if tem==True:
							ficha.cambiar_posicion(tablero.casillas[celda.numero+m-1])
										
										#return tem
						else:
							pass
							#return False
								
					elif celda.numero + m-68 <= 17 and ficha.memoria != 3:
						
						tem = True
						for i in range(celda.numero,68):
							
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
							elif i == 67:
								
								ficha.memoria = 3
									
								 
						for i in range(celda.numero+m-68):
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
								 
						 
						if tem==True:
							
							 ficha.cambiar_posicion(tablero.casillas[celda.numero+m-68-1])
										
										#return tem
										
						else:
							pass
							#return False
										
					else:
						print "Entrando al pasillo"
						falt = celda.numero + m - 17
						#print falt
						
						tem = True
						for i in range(celda.numero,17):
							if len(tablero.casillas[i].fichas) == 2:
								 tem = False
								 
						if tem == True:
							
							if len(tablero.pasillo_azul[0].fichas)!=2:
							
								ficha.cambiar_posicion(tablero.pasillo_azul[0])
																
								self.mover_ficha(ficha,falt-1,tablero)
								#return tem
							else:
								pass
								#return False	
						
						else:
							pass
							#return False
										
											
	def evaluar_resultado(self,ficha,m,tablero):
		celda = ficha.mostrar_posicion()
		
		if celda.tipo == "pasillo":
			
			if celda.numero + m <=8:
				
				tem = True
				if celda.color == "amarillo":
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.pasillo_amarillo[i].fichas) == 2 and tablero.pasillo_amarillo[i].tipo !="meta":
							 print "Hay barerra"
							 tem = False
							 break
							 
					if tem==True:
						

						return tem
					else:
						
						return False
				elif celda.color == "azul":
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.pasillo_azul[i].fichas) == 2 and tablero.pasillo_amarillo[i].tipo !="meta":
							 print "Hay barerra"
							 tem = False
							 break
							 
					if tem==True:
						
						return tem
					else:
						
						return False
				elif celda.color == "verde":
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.pasillo_verde[i].fichas) == 2 and tablero.pasillo_amarillo[i].tipo !="meta":
							 print "Hay barerra"
							 tem = False
							 break
							 
					if tem==True:
						
						return tem
					else:
						
						return False
				elif celda.color == "rojo":
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.pasillo_rojo[i].fichas) == 2 and tablero.pasillo_amarillo[i].tipo !="meta":
							 print "Hay barerra"
							 tem = False
							 break
							 
					if tem==True:
						
						return tem
					else:
						
						return False
			else:
				
				return False
								
		else:
			#ficha verde
			if ficha.col=="verde":
				if celda.numero + m <= 68 and ficha.memoria2 == 1:
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2:
							print "Hay barerra"
							tem = False
							
						elif i == 67:
							ficha.memoria2 = 2
							 
					return tem 
					
				else:
					
					if celda.numero + m <= 51 and ficha.memoria2 ==3:
						tem = True
						for i in range(celda.numero, celda.numero + m):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								break
								 
						return tem
					
					elif celda.numero + m-68 <= 51 and ficha.memoria2 !=3:
						tem = True
						for i in range(celda.numero,68):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								
							elif i == 67:
								ficha.memoria2 = 3
								 
						for i in range(celda.numero+m-68):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								break
								 
						return tem
							
					else:
					
						falt = celda.numero + m - 51 
						
						tem = True
						for i in range(celda.numero,51):
							if len(tablero.casillas[i].fichas) != 2:
								print "Hay barerra"
								tem = False
								break
						
								 
						if tem == True:
							bandera = True
							for i in range(falt):
								if len(tablero.pasillo_verde[i].fichas)==2:
									print "Hay barerra"
									bandera = False
									break
															
							return bandera
							
						else:
							
							return False
			
			#ficha roja			
			elif ficha.col=="rojo":
				if celda.numero + m <= 68 and ficha.memoria2 == 1:
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2:
							print "Hay barerra"
							tem = False
							
						elif i == 67:
							ficha.memoria2 = 2
							 
					return tem
					
				else:
					
					if celda.numero + m <= 34 and ficha.memoria2 == 3:
						tem = True
						for i in range(celda.numero,celda.numero + m):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								break
								
								 
						return tem
					
					elif celda.numero + m-68 <= 34  and ficha.memoria2 !=3:
						tem = True
						for i in range(celda.numero,68):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								
							elif i == 67:
								ficha.memoria2 = 3
								 
						for i in range(celda.numero+m-68):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								break
								 
						return tem
						
					else:
						
						falt = celda.numero + m - 34
						if falt <=8:
							tem = True
							for i in range(celda.numero,34):
								if len(tablero.casillas[i].fichas) == 2:
									print "Hay barerra"
									tem = False
									break
									 
							if tem == True:
								bandera = True
								for i in range(falt):
									if len(tablero.pasillo_rojo[i].fichas)==2:
										print "Hay barerra"
										bandera = False
										break
																
								return bandera	
								
							else:
								
								return False	
						else:
							return False	
									
			#ficha amarilla			
			elif ficha.col=="amarillo":
				if celda.numero + m <= 68 :
					
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2:
							print "Hay barerra"
							tem = False
							break
							 
					return tem
					
				else:
					
					falt = celda.numero + m - 68
					
					tem = True
					for i in range(celda.numero,68):
						if len(tablero.casillas[i].fichas) == 2:
							print "Hay barerra"
							tem = False
							break
							 
					if tem == True:
						bandera = True
						for i in range(falt):
							if len(tablero.pasillo_amarillo[i].fichas)==2:
								print "Hay barerra"
								bandera = False
								break
															
						return bandera	
						
					else:
						
						return False							
							
			#ficha azul			
			elif ficha.col=="azul":
				
				if celda.numero + m <= 68 and ficha.memoria2 == 1:
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2 and i!=67:
							print "Hay barerra"
							tem = False
							
						elif i == 67:
							
							ficha.memoria2 = 2
							 
					return tem
					
				else:
					
					if celda.numero + m <= 17 and ficha.memoria2 == 3:
						tem = True
						for i in range(celda.numero,celda.numero + m):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								break
								
						return tem
							
					elif celda.numero + m-68 <= 17 and ficha.memoria2 != 3:
						tem = True
						for i in range(celda.numero,68):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
							elif i == 67:
								ficha.memoria2 = 3
								
							
								 
						for i in range(celda.numero+m-68):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								 
						return tem
										
					else:
						
						falt = celda.numero + m - 17
						#print falt
						
						tem = True
						for i in range(celda.numero,17):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								 
						if tem == True:
							bandera = True
							for i in range(falt):
								if len(tablero.pasillo_azul[i].fichas)==2:
									print "Hay barerra"
									bandera = False
									break
															
							return bandera	
						
						else:
							
							return False

#Creamos la una lista con los objetos tipo jugador
colores = ["amarillo","azul","rojo","verde"]
lista_jugadores=[]
for j in range(4):
	lista_jugadores.append(Jugador("",colores[j],[],0))
	
Aa = []
Bb = []

for i in range(9,26):
	Aa.append(i)


for i in range(43,60):
	Bb.append(i)

lista = Jugador("",colores[j],[],0)
