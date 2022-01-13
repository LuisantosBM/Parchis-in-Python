#usr/bin/python
#coding:utf-8
#Parchis.py
from tablero import *
from dado import *
from random import *
from jugador import *
from celda import *
from meta import *
from ficha import *

def elegir_ficha(n,jugador,m,tablero,ficha1,ficha2,ficha3,ficha4):
		
		if n ==1 :
			if ficha1.esta_en.tipo == "casa":
				print "No puede mover la ficha, esta en casa"
				return False
				
			elif ficha1.esta_en.tipo == "meta":
				print "No puede mover la ficha, esta en meta"
				return False
			
			elif jugador.evaluar_resultado(ficha1,m,tablero) == False:
				print "No se puede mover la ficha"
				return False
			else:
				return True
					 
		elif n ==2:
			if ficha2.esta_en.tipo == "casa":
				print "No puede mover la ficha, esta en casa"
				return False
				
			elif ficha2.esta_en.tipo == "meta":
				print "No puede mover la ficha, esta en meta"
				return False
				
			elif jugador.evaluar_resultado(ficha2,m,tablero) == False:
				print "No se puede mover la ficha"
				return False
				
			else:
				return True
					
		elif n ==3:
			if ficha3.esta_en.tipo == "casa":
				print "No puede mover la ficha, esta en casa"
				return False
				
			elif ficha3.esta_en.tipo == "meta":
				print "No puede mover la ficha, esta en meta"
				return False
				
			elif jugador.evaluar_resultado(ficha3,m,tablero) == False:
				print "No se puede mover la ficha"
				return False
				
			else:
				return True
					
		elif n==4:
			if ficha4.esta_en.tipo == "casa":
				print "No puede mover la ficha, esta en casa"
				return False
				
			elif ficha4.esta_en.tipo == "meta":
				print "No puede mover la ficha, esta en meta"
				return False
				
			elif jugador.evaluar_resultado(ficha4,m,tablero) == False:
				print "No se puede mover la ficha"
				return False
				
			else:
				return True
					
		else:
			print "Numero de ficha incorrecta, elija entre 1,2,3,4"
			return False


def premio_meta(jugador,ficha,tablero):
	
	if ficha.esta_en.tipo == "meta" and len(ficha.esta_en.fichas)!=4:
		
		print "Gano diez pasos por llevar una ficha a la meta."
		ficha_a_mover = 0
		for i in range(4):
			n = input("elegir ficha para mover:")
			if elegir_ficha(n,jugador,r1,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
				ficha_a_mover = n
				break
		if ficha_a_mover == 0:
			print "perdio turno, no puede mover ninguna ficha"
		else:
			jugador.mover_ficha(jugador.fichas[n-1],10,tablero)
			###capturando
			capturar(jugador,n,tablero)
			
						
def capturar(jugador,n,tablero):
	
	if len(jugador.fichas[n-1].esta_en.fichas)==2 and jugador.fichas[n-1].esta_en.fichas[0].col!=jugador.fichas[n-1].col and jugador.fichas[n-1].esta_en.tipo!="segura":
		for w in tablero.casas:
			if w.color == jugador.fichas[n-1].esta_en.fichas[0].col:
				break
		premio = jugador.fichas[n-1].capturar_ficha(jugador.fichas[n-1].esta_en.fichas[0],w)
		jugador.mover_ficha(jugador.fichas[n-1],premio,tablero)
		premio_meta(jugador,jugador.fichas[n-1],tablero)
		capturar(jugador,n,tablero)
	
		
	
def nuevo_recorrido(jugador,r1,r2,tablero,indice):
	if r2 == 5 and r1 != 5:
		bandera = False
		for j in jugador.fichas:
			#verificando si hay una ficha en casa
			if j.esta_en.tipo == "casa":
				if jugador.color == "verde":
					if len(tablero1.casillas[55].fichas) == 2 or len(jugador.casa.fichas)==0:
						pass
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[55])
						bandera = True
				elif jugador.color == "rojo":
					if len(tablero1.casillas[38].fichas) == 2 or len(jugador.casa.fichas)==0:
						pass
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[38])
						bandera = True
				elif jugador.color == "azul":
					if len(tablero1.casillas[21].fichas) == 2 or len(jugador.casa.fichas)==0:
						pass
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[21])
						bandera = True
				elif jugador.color == "amarillo":
					if len(tablero1.casillas[4].fichas) == 2 or len(jugador.casa.fichas)==0:
						pass
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[4])
						bandera = True
				break
		if bandera == True:
			#resultado de r1
			ficha_a_mover = 0
			
			for i in range(4):
				n = input("elegir ficha para mover:")
				if elegir_ficha(n,jugador,r1,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
					ficha_a_mover = n
					break
			if ficha_a_mover == 0:
				print "perdio su turno, no puede mover ninguna ficha"
			else:
				jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
				##Verficando si llego a la meta
				premio_meta(jugador,jugador.fichas[n-1],tablero)
				###capturando
				capturar(jugador,n,tablero)
					
					
				
		else:
			#resultado de r1
			ficha_a_mover = 0
			
			for i in range(4):
				n = input("elegir ficha para mover:")
				if elegir_ficha(n,jugador,r1,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
					ficha_a_mover = n
					break
			if ficha_a_mover == 0:
				print "perdio su turno, no puede mover ninguna ficha"
			else:
				jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
				##verificando si llego a la meta
				premio_meta(jugador,jugador.fichas[n-1],tablero)
				###capturando
				capturar(jugador,n,tablero)
			
			#resultado de r2
			ficha_a_mover = 0
			for i in range(4):
				n = input("elegir ficha para mover:")
				if elegir_ficha(n,jugador,r2,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
					ficha_a_mover = n
					break
			if ficha_a_mover == 0:
				print "perdio su turno, no puede mover ninguna ficha"
			else:
				jugador.mover_ficha(jugador.fichas[n-1],r2,tablero)
				##verficiando si llego a la meta
				premio_meta(jugador,jugador.fichas[n-1],tablero)
				###capturando
				capturar(jugador,n,tablero)
			
	elif r1 == 5 and r2 != 5:
		bandera = False
		for j in jugador.fichas:
			#verficando si hay ficha en casa
			if j.esta_en.tipo == "casa":
				if jugador.color == "verde":
					if len(tablero1.casillas[55].fichas) == 2 or len(jugador.casa.fichas)==0:
						pass
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[55])
						bandera = True
				elif jugador.color == "rojo":
					if len(tablero1.casillas[38].fichas) == 2 or len(jugador.casa.fichas)==0:
						pass
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[38])
						bandera = True
				elif jugador.color == "azul":
					if len(tablero1.casillas[21].fichas) == 2 or len(jugador.casa.fichas)==0:
						pass
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[21])
						bandera = True
				elif jugador.color == "amarillo":
					if len(tablero1.casillas[4].fichas) == 2 or len(jugador.casa.fichas)==0:
						pass
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[4])
						bandera = True
				break
		if bandera == True:
			#resultado de r2
			ficha_a_mover = 0
			
			for i in range(4):
				n = input("elegir ficha para mover:")
				if elegir_ficha(n,jugador,r2,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
					ficha_a_mover = n
					break
			if ficha_a_mover == 0:
				print "perdio su turno, no puede mover ninguna ficha"
			else:
				jugador.mover_ficha(jugador.fichas[n-1],r2,tablero)
				##verficiando si llego a la meta
				premio_meta(jugador,jugador.fichas[n-1],tablero)
				###capturando
				capturar(jugador,n,tablero)
			
			
		else:
			
			#resultado de r1
			ficha_a_mover = 0
			
			for i in range(4):
				n = input("elegir ficha para mover:")
				if elegir_ficha(n,jugador,r1,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
					ficha_a_mover = n
					break
			if ficha_a_mover == 0:
				print "perdio su turno, no puede mover ninguna ficha"
			else:
				jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
				##verficiando si llego a la meta
				premio_meta(jugador,jugador.fichas[n-1],tablero)
				###capturando
				capturar(jugador,n,tablero)
				
			ficha_a_mover = 0
			
			#resultado de r2
			
			for i in range(4):
				n = input("elegir ficha para mover:")
				if elegir_ficha(n,jugador,r2,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
					ficha_a_mover = n
					break
			if ficha_a_mover == 0:
				print "perdio su turno, no puede mover ninguna ficha"
			else:
				jugador.mover_ficha(jugador.fichas[n-1],r2,tablero)
				##verficiando si llego a la meta
				premio_meta(jugador,jugador.fichas[n-1],tablero)
				###capturando
				capturar(jugador,n,tablero)

	
	elif r1 == 5 and r2 == 5:
			band = False
			for j in range(len(tablero1.casas)):
				if tablero1.casas[j].color==jugador.color and len(tablero1.casas[j].fichas)!=0:
					indice = j
					band = True
			if band == True:
		
				if jugador.color == "verde":
					if len(tablero1.casillas[55].fichas) == 2 or len(jugador.casa.fichas)==0:
						#aqui se elige nueva ficha si no se puede sacar
						#resultado de r1
						
						ficha_a_mover = 0
						
						for i in range(4):
							n = input("elegir ficha para mover:")
							if elegir_ficha(n,jugador,r1,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
								ficha_a_mover = n
								break
						if ficha_a_mover == 0:
							print "perdio su turno, no puede mover ninguna ficha"
						else:
							jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
							##verficiando si llego a la meta
							premio_meta(jugador,jugador.fichas[n-1],tablero)
							###capturando
							capturar(jugador,n,tablero)
							
						ficha_a_mover = 0
						
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[55])
				elif jugador.color == "rojo":
					if len(tablero1.casillas[38].fichas) == 2 or len(jugador.casa.fichas)==0:
						#resultado de r1
						
						ficha_a_mover = 0
						
						for i in range(4):
							n = input("elegir ficha para mover:")
							if elegir_ficha(n,jugador,r1,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
								ficha_a_mover = n
								break
						if ficha_a_mover == 0:
							print "perdio su turno, no puede mover ninguna ficha"
						else:
							jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
							##verficiando si llego a la meta
							premio_meta(jugador,jugador.fichas[n-1],tablero)
							###capturando
							capturar(jugador,n,tablero)
							
						ficha_a_mover = 0
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[38])
				elif jugador.color == "azul":
					if len(tablero1.casillas[21].fichas) == 2 or len(jugador.casa.fichas)==0:
						#resultado de r1
						
						ficha_a_mover = 0
						
						for i in range(4):
							n = input("elegir ficha para mover:")
							if elegir_ficha(n,jugador,r1,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
								ficha_a_mover = n
								break
						if ficha_a_mover == 0:
							print "perdio su turno, no puede mover ninguna ficha"
						else:
							jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
							##verficiando si llego a la meta
							premio_meta(jugador,jugador.fichas[n-1],tablero)
							###capturando
							capturar(jugador,n,tablero)
							
						ficha_a_mover = 0
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[21])
				elif jugador.color == "amarillo":
					if len(tablero1.casillas[4].fichas) == 2 or len(jugador.casa.fichas)==0:
						#resultado de r1
						
						ficha_a_mover = 0
						
						for i in range(4):
							n = input("elegir ficha para mover:")
							if elegir_ficha(n,jugador,r1,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
								ficha_a_mover = n
								break
						if ficha_a_mover == 0:
							print "perdio su turno, no puede mover ninguna ficha"
						else:
							jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
							##verficiando si llego a la meta
							premio_meta(jugador,jugador.fichas[n-1],tablero)
							###capturando
							capturar(jugador,n,tablero)
							
						ficha_a_mover = 0
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[4])
			else:
				#resultado de r1
						
				ficha_a_mover = 0
				
				for i in range(4):
					n = input("elegir ficha para mover:")
					if elegir_ficha(n,jugador,r1,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
						ficha_a_mover = n
						break
				if ficha_a_mover == 0:
					print "perdio su turno, no puede mover ninguna ficha"
				else:
					jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
					##verficiando si llego a la meta
					premio_meta(jugador,jugador.fichas[n-1],tablero)
					###capturando
					capturar(jugador,n,tablero)
					
					
				ficha_a_mover = 0
				
			#### segundo resultado
			band = False
			for j in range(len(tablero1.casas)):
				if tablero1.casas[j].color==jugador.color and len(tablero1.casas[j].fichas)!=0:
					indice = j
					band = True
			if band == True:
				
				if jugador.color == "verde":
					if len(tablero1.casillas[55].fichas) == 2 or len(jugador.casa.fichas)==0:
						#resultado de r2
						
						ficha_a_mover = 0
						
						for i in range(4):
							n = input("elegir ficha para mover:")
							if elegir_ficha(n,jugador,r2,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
								ficha_a_mover = n
								break
						if ficha_a_mover == 0:
							print "perdio su turno, no puede mover ninguna ficha"
						else:
							jugador.mover_ficha(jugador.fichas[n-1],r2,tablero)
							##verficiando si llego a la meta
							premio_meta(jugador,jugador.fichas[n-1],tablero)
							###capturando
							capturar(jugador,n,tablero)
				
						ficha_a_mover = 0
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[55])
				elif jugador.color == "rojo":
					if len(tablero1.casillas[38].fichas) == 2 or len(jugador.casa.fichas)==0:
						#resultado de r2
						
						ficha_a_mover = 0
						
						for i in range(4):
							n = input("elegir ficha para mover:")
							if elegir_ficha(n,jugador,r2,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
								ficha_a_mover = n
								break
						if ficha_a_mover == 0:
							print "perdio su turno, no puede mover ninguna ficha"
						else:
							jugador.mover_ficha(jugador.fichas[n-1],r2,tablero)
							##verficiando si llego a la meta
							premio_meta(jugador,jugador.fichas[n-1],tablero)
							###capturando
							capturar(jugador,n,tablero)
							
					
						ficha_a_mover = 0
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[38])
				elif jugador.color == "azul":
					if len(tablero1.casillas[21].fichas) == 2 or len(jugador.casa.fichas)==0:
						#resultado de r2
						
						ficha_a_mover = 0
						
						for i in range(4):
							n = input("elegir ficha para mover:")
							if elegir_ficha(n,jugador,r2,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
								ficha_a_mover = n
								break
						if ficha_a_mover == 0:
							print "perdio su turno, no puede mover ninguna ficha"
						else:
							jugador.mover_ficha(jugador.fichas[n-1],r2,tablero)
							##verficiando si llego a la meta
							premio_meta(jugador,jugador.fichas[n-1],tablero)
							###capturando
							capturar(jugador,n,tablero)
							
							
						ficha_a_mover = 0
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[21])
				elif jugador.color == "amarillo":
					if len(tablero1.casillas[4].fichas) == 2 or len(jugador.casa.fichas)==0:
						#resultado de r2
						
						ficha_a_mover = 0
						
						for i in range(4):
							n = input("elegir ficha para mover:")
							if elegir_ficha(n,jugador,r2,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
								ficha_a_mover = n
								break
						if ficha_a_mover == 0:
							print "perdio su turno, no puede mover ninguna ficha"
						else:
							jugador.mover_ficha(jugador.fichas[n-1],r2,tablero)
							##verficiando si llego a la meta
							premio_meta(jugador,jugador.fichas[n-1],tablero)
							###capturando
							capturar(jugador,n,tablero)
							
						ficha_a_mover = 0
					else:
						print "Se esta sacando una ficha de casa"
						tablero1.casas[indice].fichas[0].cambiar_posicion(tablero1.casillas[4])
			else:
				#resultado de r2
						
				ficha_a_mover = 0
				
				for i in range(4):
					n = input("elegir ficha para mover:")
					if elegir_ficha(n,jugador,r2,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
						ficha_a_mover = n
						break
				if ficha_a_mover == 0:
					print "perdio su turno, no puede mover ninguna ficha"
				else:
					jugador.mover_ficha(jugador.fichas[n-1],r2,tablero)
					##verficiando si llego a la meta
					premio_meta(jugador,jugador.fichas[n-1],tablero)
					###capturando
					capturar(jugador,n,tablero)
					
					
				ficha_a_mover = 0
				
	else:
		
		#resultado de r1
		ficha_a_mover = 0
		
		for i in range(4):
			n = input("elegir ficha para mover:")
			if elegir_ficha(n,jugador,r1,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
				ficha_a_mover = n
				break
		if ficha_a_mover == 0:
			print "perdio su turno, no puede mover ninguna ficha"
		else:
			jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
			##verficiando si llego a la meta
			premio_meta(jugador,jugador.fichas[n-1],tablero)
			###capturando
			capturar(jugador,n,tablero)
			
		ficha_a_mover = 0
		
		#resultado de r2
		
		for i in range(4):
			n = input("elegir ficha para mover:")
			if elegir_ficha(n,jugador,r2,tablero,jugador.fichas[0],jugador.fichas[1],jugador.fichas[2],jugador.fichas[3])==True:
				ficha_a_mover = n
				break
		if ficha_a_mover == 0:
			print "perdio su turno, no puede mover ninguna ficha"
		else:
			jugador.mover_ficha(jugador.fichas[n-1],r2,tablero)
			##verficiando si llego a la meta
			premio_meta(jugador,jugador.fichas[n-1],tablero)
			###capturando
			capturar(jugador,n,tablero)
		

#Programa Principal Juego Parchis
inicio = "  BIENVENIDOS A PARCHIS  "
print inicio.center(40,"*")
num_jugadores = input("\nIngrese el numero de jugadores: ")

if num_jugadores > 4 or num_jugadores <= 1 or type(num_jugadores)!= int:
	print "numero de jugadores invalido"

else:
	nombres = []
	
	colores = ["amarillo","azul","rojo","verde"]
	
	fichas_iniciales = [tablero1.casillas[4],tablero1.casillas[21],tablero1.casillas[38],tablero1.casillas[55]]
	Lista_Jugadores=[]
	for i in range(num_jugadores):
		nombres.append(raw_input("Ingrese el nombre del jugador: "))
	
	#Creamos una lista auxiliar en la que ordenaremos los nombres
	ordenados=[]
	for i in range(num_jugadores):
		ordenados.append(nombres[i])
		print ordenados[i]
	
	#Lista en la que guardamos el resultado del lanzamiento para cada jugador
	turnos = []
	for i in range(num_jugadores):
		print nombres[i],", lanza el dado para ver que turno obtienes en el juego (presiona Enter): "
		raw_input()
		resultado=randint(1,6)
		print "Obtuviste",resultado,"\n"
		turnos.append(resultado)

	#Ordenando a los jugadores en orden ascendente con respecto a los resultados
	for i in range(0, len(turnos)-1) : 
			indiceMenor=i
			for j in range(i+1, len(turnos)):
				if turnos[j]>turnos[indiceMenor] : 
					indiceMenor=j 
			if i!=indiceMenor : 
				turnos[i],turnos[indiceMenor]=turnos[indiceMenor],turnos[i]
				ordenados[i],ordenados[indiceMenor]=ordenados[indiceMenor],ordenados[i]

	#Creamos la una lista con los objetos tipo jugador
	lista_jugadores=[]
	for j in range(len(ordenados)):
		lista_jugadores.append(Jugador(ordenados[j],colores[j],[Ficha(fichas_iniciales[j],1,colores[j]),Ficha(tablero1.casas[j],2,colores[j]),Ficha(tablero1.casas[j],3,colores[j]),Ficha(tablero1.casas[j],4,colores[j])],tablero1.casas[j]))

	#sacando ficha para jugar

	for r in range(len(ordenados)):
		fichas_iniciales[r].fichas.append(lista_jugadores[r].fichas[0])	

	#llenando las casas
	for r in range(len(ordenados)):
		tablero1.casas[r].fichas.append(lista_jugadores[r].fichas[1])
		tablero1.casas[r].fichas.append(lista_jugadores[r].fichas[2])
		tablero1.casas[r].fichas.append(lista_jugadores[r].fichas[3])	

	#############################################################################
	#demostraciones
	#primera demostracion (prueba de barrera):
	#lista_jugadores[1].fichas[2].cambiar_posicion(tablero1.casillas[6])
	#lista_jugadores[1].fichas[3].cambiar_posicion(tablero1.casillas[6])
	
	#segunda demostracion(captura):
	#lista_jugadores[1].fichas[1].cambiar_posicion(tablero1.casillas[5])
	
	#tercera prueba (llega a la meta):
	#lista_jugadores[1].fichas[0].cambiar_posicion(tablero1.pasillo_azul[6])
	
	#cuarta prueba (final del juego):
	#lista_jugadores[1].fichas[2].cambiar_posicion(tablero1.pasillo_azul[7])
	#lista_jugadores[1].fichas[3].cambiar_posicion(tablero1.pasillo_azul[7])
	#lista_jugadores[1].fichas[1].cambiar_posicion(tablero1.pasillo_azul[7])
	#lista_jugadores[1].fichas[0].cambiar_posicion(tablero1.pasillo_azul[5])


	print num_jugadores, "numero jugadores"
	for i in range(1,num_jugadores+1):
		print i,"juega:", lista_jugadores[i-1].nom
		print lista_jugadores[i-1].casa.color
				


	while tablero1.pasillo_amarillo[7].definir_ganador()!=True and tablero1.pasillo_rojo[7].definir_ganador()!=True and tablero1.pasillo_verde[7].definir_ganador()!=True and tablero1.pasillo_azul[7].definir_ganador()!=True:
		contador = 0
		for i in lista_jugadores:
			contador = contador + 1 
			indice = 0
			#r1 = 20
			#r2 = 25
			
			#r1 = 1
			#r2 = 5
			
			#r1 = 1
			#r2 = 1
			print "\n"
			print "Turno de:",i.nom
			r1 = i.lanzar_dado(dado1)
			print "primer dado:",r1
			r2 = i.lanzar_dado(dado2)
			print "segundo dado:",r2
			
			#print "numero de fichas en casa:",len(i.casa.fichas)
			
			if len(i.casa.fichas)==4 and r1 != 5 and r2 != 5:
				print "pierde turno, no tiene fichas para jugar"
			
			elif r1 == 6 or r2 == 6:
				
				for j in range(len(tablero1.casas)):
					if tablero1.casas[j].color==i.color and len(tablero1.casas[j].fichas)!=0:
						indice = j
						break
				
				nuevo_recorrido(i,r1,r2,tablero1,indice)
				
				
				r1 = i.lanzar_dado(dado1)
				print "primer dado:",r1
				r2 = i.lanzar_dado(dado2)
				print "segundo dado:",r2
				
				for j in range(len(tablero1.casas)):
					if tablero1.casas[j].color==i.color and len(tablero1.casas[j].fichas)!=0:
						indice = j
						break
						
				nuevo_recorrido(i,r1,r2,tablero1,indice)		
					
			else:
				for j in range(len(tablero1.casas)):
					if tablero1.casas[j].color==i.color and len(tablero1.casas[j].fichas)!=0:
						indice = j
						break
				nuevo_recorrido(i,r1,r2,tablero1,indice)
				
			if tablero1.pasillo_amarillo[7].definir_ganador()!=True and tablero1.pasillo_rojo[7].definir_ganador()!=True and tablero1.pasillo_verde[7].definir_ganador()!=True and tablero1.pasillo_azul[7].definir_ganador()!=True:
				pass
			else:
				break 
			
					
	if tablero1.pasillo_amarillo[7].definir_ganador()==True:
		print "\n ¡¡¡¡¡¡Gana",lista_jugadores[0].nom,"!!!!" 
	elif tablero1.pasillo_rojo[7].definir_ganador()==True:
		print "\n ¡¡¡¡¡¡Gana",lista_jugadores[2].nom,"!!!!"
	elif tablero1.pasillo_verde[7].definir_ganador() ==True:
		print "\n¡¡¡¡¡¡Gana",lista_jugadores[3].nom,"!!!!"
	elif tablero1.pasillo_azul[7].definir_ganador()==True:
		print "\n ¡¡¡¡¡¡Gana",lista_jugadores[1].nom,"!!!!"
