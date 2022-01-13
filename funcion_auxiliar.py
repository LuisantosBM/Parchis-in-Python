#usr/bin/python
#coding: utf-8

def evaluar_resultado(ficha,m,tablero):
		celda = ficha.esta_en
		
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
		elif celda.tipo == "meta":
			return False
		elif celda.tipo == "casa":
			return False
								
		else:
			#ficha verde
			if ficha.col=="verde":
				if celda.numero + m <= 68 and ficha.memoria3 == 1:
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2:
							print "Hay barerra"
							tem = False
							
						elif i == 67:
							ficha.memoria3 = 2
							 
					return tem 
					
				else:
					
					if celda.numero + m <= 51 and ficha.memoria3 ==3:
						tem = True
						for i in range(celda.numero, celda.numero + m):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								break
								 
						return tem
					
					elif celda.numero + m-68 <= 51 and ficha.memoria3 !=3:
						tem = True
						for i in range(celda.numero,68):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								
							elif i == 67:
								ficha.memoria3 = 3
								 
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
				if celda.numero + m <= 68 and ficha.memoria3 == 1:
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2:
							print "Hay barerra"
							tem = False
							
						elif i == 67:
							ficha.memoria3 = 2
							 
					return tem
					
				else:
					
					if celda.numero + m <= 34 and ficha.memoria3 == 3:
						tem = True
						for i in range(celda.numero,celda.numero + m):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								break
								
								 
						return tem
					
					elif celda.numero + m-68 <= 34  and ficha.memoria3 !=3:
						tem = True
						for i in range(celda.numero,68):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								
							elif i == 67:
								ficha.memoria3 = 3
								 
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
				
				if celda.numero + m <= 68 and ficha.memoria3 == 1:
					tem = True
					for i in range(celda.numero,celda.numero+m):
						if len(tablero.casillas[i].fichas) == 2 and i!=67:
							print "Hay barerra"
							tem = False
							
						elif i == 67:
							
							ficha.memoria3 = 2
							 
					return tem
					
				else:
					
					if celda.numero + m <= 17 and ficha.memoria3 == 3:
						tem = True
						for i in range(celda.numero,celda.numero + m):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
								break
								
						return tem
							
					elif celda.numero + m-68 <= 17 and ficha.memoria3 != 3:
						tem = True
						for i in range(celda.numero,68):
							if len(tablero.casillas[i].fichas) == 2:
								print "Hay barerra"
								tem = False
							elif i == 67:
								ficha.memoria3 = 3
								
							
								 
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
