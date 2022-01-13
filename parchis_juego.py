#usr/bin/python
#coding: utf-8
#parchis.py

from Tkinter import *
import random 
import time
from tablero import *
from dado import *
from jugador import *
from celda import *
from meta import *
from ficha import *
from funcion_auxiliar import *
import tkMessageBox

##########################################################################
def mostrar(vv21):
	return vv21.deiconify

def ocultar(ventan):
	return ventan.withdraw()

def mostrar_ocultar(vv20,vv21):
	return vv20.deiconify, vv21.withdraw()
	
def ejecutar(f):
	vv1.after(100,f)
	
def cerrar_splashcreen():
	ejecutar(ocultar(vv1))
	ejecutar(mostrar(can_jug))

def imprimir(texto):
	print texto

def cerrar_ven():
	ejecutar(ocultar(vv1))
	ejecutar(mostrar(vv2))
	

#Splash Screen
vv1=Tk()
vv1.geometry("500x500+400+150")
vv1.title("Espere un momento...")
imagen2=PhotoImage(file="par1.gif")
label2 = Label(vv1,image=imagen2)
label2.grid(row=1,column=1)
vv1.config(bg="black")
vv1.protocol("WM_DELETE_WINDOW","onexit")
vv1.resizable(0,0)

vv1.after(2000,cerrar_splashcreen)

can_jug =Toplevel(vv1)
can_jug.geometry("500x400+400+150")
can_jug.title("Cantidad de jugadores")
can_jug.config(bg="lightblue")
textito = Label(can_jug, text= "Elija cantidad de Jugadores", font= ("Times New Roman", 15),fg = "blue", bg= "lightblue").place(x = 130, y = 50)
can_jug.withdraw()

####################################################################################

vv2=Toplevel(vv1)
vv2.geometry("1000x700+200+10")
vv2.config(bg="white")
vv2.title("PARCHIS")
imagen3 = PhotoImage(file="parchi.gif")
etiqueta = Label(vv2, text= "PARCHIS", fg = "purple", font = ("Times New Roman", 15))
etiqueta.pack()
##########################################################################

#Ventana Emergentes
def Hay_barrera():
	tkMessageBox.showinfo("", "¡HAY BARRERA!")
	
def captura_ficha():
	tkMessageBox.showinfo("", "¡CAPTURÓ FICHA!")
	
def ganador():
	tkMessageBox.showinfo("", "¡HA GANADO! Felicidades!!")
	
def no_mover():
	tkMessageBox.showinfo("", "¡NO PUEDE MOVER FICHA, ELIJA OTRA!")
	

#boton = Button(vv2, text="HI", command = ganador).place(x= 100, y = 100)
#####################################################################################
#Creando las entradas de los nombres y guardándolos en una lista.


def cantidad():
	
	nj = selec.get()
	
	def hola():
		tkMessageBox.showinfo("Error", "Olvidó elegir cantidad de jugadores")
		
	def aceptar_ven():
		if nj== 2:
			listajugadores2()
			if jugadores[0].nom=="" or jugadores[1].nom=="":
				hola()
			else:
				ejecutar(ocultar(vv2_entrada))
				vv2.deiconify()
		elif nj == 3:
			listajugadores3()
			if jugadores[0].nom=="" or jugadores[1].nom=="" or jugadores[2].nom=="":
				hola()
			else:
				ejecutar(ocultar(vv2_entrada))
				vv2.deiconify()
		elif nj == 4:
			listajugadores4()
			if jugadores[0].nom=="" or jugadores[1].nom=="" or jugadores[2].nom=="" or jugadores[3].nom=="":
				hola()
			else:
				ejecutar(ocultar(vv2_entrada))
				vv2.deiconify()
		
		
			 
		
		
	if nj == 2:
		ejecutar(ocultar(can_jug))
		vv2_entrada = Toplevel(vv1)
		vv2_entrada.title("Jugadores")
		vv2_entrada.geometry("300x200+500+250")
		vv2_entrada.config(bg = "pink")
		nombre = Label( vv2_entrada, bg= "pink", text = "Ingrese el nombre de los jugadores:").pack()
	
		def listajugadores2():
			Lj= [ ]
			Lj.append(jug1.get())
			Lj.append(jug2.get())
			
			lista_jugadores[0].nom = Lj[0]
			lista_jugadores[1].nom = Lj[1]
			jugadores.append(lista_jugadores[0])
			jugadores.append(lista_jugadores[1])
			jugadores[0].turno = True
			
			return len(Lj)

		jug1 = StringVar()
		jug2 = StringVar()

		jugador1 = Label(vv2_entrada, bg = "pink", text = "Jugador_1:").place(x = 35, y = 30 )
		nombre_caja1 = Entry(vv2_entrada, textvariable= jug1).place(x = 100, y = 30)
		jugador2 = Label(vv2_entrada, bg = "pink", text = "Jugador_2:").place(x = 35, y = 60 )
		nombre_caja2 = Entry(vv2_entrada,textvariable= jug2).place(x = 100, y = 60)

		botoncito = Button(vv2_entrada, text="Aceptar", command = aceptar_ven).place(x = 120, y = 150)

		
		Listita = listajugadores2()
		return Listita
	
	elif nj == 3:
		ejecutar(ocultar(can_jug))
		vv2_entrada = Toplevel(vv1)
		vv2_entrada.title("Jugadores")
		vv2_entrada.geometry("300x200+500+250")
		vv2_entrada.config(bg = "pink")
		nombre = Label(vv2_entrada, bg= "pink", text = "Ingrese el nombre de los jugadores:").pack()
	
		def listajugadores3():
			Lj= [ ]
			Lj.append(jug1.get())
			Lj.append(jug2.get())
			Lj.append(jug3.get())
			
			lista_jugadores[0].nom = Lj[0]
			lista_jugadores[1].nom = Lj[1]
			lista_jugadores[2].nom = Lj[2]
			jugadores.append(lista_jugadores[0])
			jugadores.append(lista_jugadores[1])
			jugadores.append(lista_jugadores[2])
			jugadores[0].turno = True
			return len(Lj)

		jug1 = StringVar()
		jug2 = StringVar()
		jug3 = StringVar()

		jugador1 = Label(vv2_entrada, bg = "pink", text = "Jugador_1:").place(x = 35, y = 30 )
		nombre_caja1 = Entry(vv2_entrada, textvariable= jug1).place(x = 100, y = 30)
		jugador2 = Label(vv2_entrada, bg = "pink", text = "Jugador_2:").place(x = 35, y = 60 )
		nombre_caja2 = Entry(vv2_entrada,textvariable= jug2).place(x = 100, y = 60)
		jugador3 = Label(vv2_entrada, bg = "pink", text = "Jugador_3:").place(x = 35, y = 90 )
		nombre_caja3 = Entry(vv2_entrada,textvariable= jug3).place(x = 100, y = 90)

		botoncito = Button(vv2_entrada, text="Aceptar", command = aceptar_ven).place(x = 120, y = 150)
		
		Listita = listajugadores3()
		return Listita

	elif nj == 4:
		ejecutar(ocultar(can_jug))
		vv2_entrada = Toplevel(vv1)
		vv2_entrada.title("Jugadores")
		vv2_entrada.geometry("300x200+500+250")
		vv2_entrada.config(bg = "pink")
		nombre = Label(vv2_entrada , bg= "pink", text = "Ingrese el nombre de los jugadores:").pack()

		def listajugadores4():
			Lj= [ ]
			Lj.append(jug1.get())
			Lj.append(jug2.get())
			Lj.append(jug3.get())
			Lj.append(jug4.get())
			
			lista_jugadores[0].nom = Lj[0]
			lista_jugadores[1].nom = Lj[1]
			lista_jugadores[2].nom = Lj[2]
			lista_jugadores[3].nom = Lj[3]
			jugadores.append(lista_jugadores[0])
			jugadores.append(lista_jugadores[1])
			jugadores.append(lista_jugadores[2])
			jugadores.append(lista_jugadores[3])
			jugadores[0].turno = True
			return len(Lj)

		jug1 = StringVar()
		jug2 = StringVar()
		jug3 = StringVar()
		jug4 = StringVar()

		jugador1 = Label(vv2_entrada, bg = "pink", text = "Jugador_1:").place(x = 35, y = 30 )
		nombre_caja1 = Entry(vv2_entrada, textvariable= jug1).place(x = 100, y = 30)
		jugador2 = Label(vv2_entrada, bg = "pink", text = "Jugador_2:").place(x = 35, y = 60 )
		nombre_caja2 = Entry(vv2_entrada,textvariable= jug2).place(x = 100, y = 60)
		jugador3 = Label(vv2_entrada, bg = "pink", text = "Jugador_3:").place(x = 35, y = 90 )
		nombre_caja3 = Entry(vv2_entrada,textvariable= jug3).place(x = 100, y = 90)
		jugador4 = Label(vv2_entrada, bg = "pink", text = "Jugador_4:").place(x = 35, y = 120 )
		nombre_caja4 = Entry(vv2_entrada,textvariable= jug4).place(x = 100, y = 120)

		botoncito = Button(vv2_entrada, text="Aceptar", command = aceptar_ven).place(x = 120, y = 150)

		Listita = listajugadores4()
		return Listita
	else:
		hola()

#####################################################################################

#Elijiendo cantidad de jugadores

selec = IntVar()
radio2 = Radiobutton(can_jug, text = "2 jugadores", fg = "blue", value = 2, var = selec).place(x=200,y= 120)
radio3 = Radiobutton(can_jug, text = "3 jugadores", fg = "blue", value = 3, var = selec).place(x=200,y= 170)
radio4 = Radiobutton(can_jug, text = "4 jugadores", fg = "blue",value = 4, var = selec).place(x=200,y= 220)

boton_salir= Button(can_jug, text="SALIR" ,command = lambda: exit()).place(x = 100, y = 300)
boton_continuar= Button(can_jug, text="CONTINUAR", command = cantidad).place(x = 350, y = 300)

#####################################################################################

#Creando la vv2 de dibujo dentro de "vv2"
canvas = Canvas(vv2, width =650, height= 650)

#Agregando nuestra foto a la vv2 de dibujo.
foto = PhotoImage(file = "parchis.gif")
canvas.create_image(320,325,image= foto)
canvas.pack()

ocultar(vv2)

## ficha de prueba, ficha blanca
u = canvas.create_oval(380, 599, 403, 622, width="0.01c", fill='white', outline='black')
	
##############################################################################
#### funciones #####################
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
		dado2.resultado = 10
		jugador.dado2_usado = False
			
			
						
def capturar(jugador,n,tablero):
	
	if len(jugador.fichas[n-1].esta_en.fichas)==2 and jugador.fichas[n-1].esta_en.fichas[0].col!=jugador.fichas[n-1].col and jugador.fichas[n-1].esta_en.tipo!="segura":
		for w in tablero.casas:
			if w.color == jugador.fichas[n-1].esta_en.fichas[0].col:
				break
		nn = jugador.fichas[n-1].esta_en.fichas[0].num
		if nn == 3:
			nn = 4
		elif nn == 4:
			nn = 6
		else:
			nn = 0
		canvas.move(jugador.fichas[n-1].esta_en.fichas[0].imagen,w.coor3[nn]-jugador.fichas[n-1].esta_en.coor1,w.coor3[nn+1]-jugador.fichas[n-1].esta_en.coor2)
		vv2.update()
		
		premio = jugador.fichas[n-1].capturar_ficha(jugador.fichas[n-1].esta_en.fichas[0],w)
		
		mover0(premio,jugador.fichas[n-1].imagen,jugador.fichas[n-1],jugador.fichas[n-1].esta_en.numero)
		
		jugador.mover_ficha(jugador.fichas[n-1],premio,tablero)
		
		premio_meta(jugador,jugador.fichas[n-1],tablero)
		capturar(jugador,n,tablero)
	
		
def sacar_ficha(jugador):
	bandera = False
	for j in jugador.fichas:
		#verficando si hay ficha en casa
		if j.esta_en.tipo == "casa":
			if jugador.color == "verde":
				if len(tablero1.casillas[55].fichas) == 2 or len(jugador.casa.fichas)==0:
					pass
				else:
					print "Se esta sacando una ficha de casa"
					
					uu = jugador.casa.fichas[0].imagen
					nn = jugador.casa.fichas[0].num
					if nn == 3:
						nn = 4
					elif nn == 4:
						nn = 6
					else:
						nn = 0
					canvas.coords(uu,130, 384, 153, 407)
					vv2.update()
					jugador.casa.fichas[0].mover = True
					jugador.casa.fichas[0].cambiar_posicion(tablero1.casillas[55])
					if len(tablero1.casillas[55].fichas) == 2:
						barrera(uu,tablero1.casillas[55].fichas[1],-15)
					else:
						barrera(uu,tablero1.casillas[55].fichas[0],-15)
					bandera = True
			elif jugador.color == "rojo":
				if len(tablero1.casillas[38].fichas) == 2 or len(jugador.casa.fichas)==0:
					pass
				else:
					print "Se esta sacando una ficha de casa"
					
					uu = jugador.casa.fichas[0].imagen
					nn = jugador.casa.fichas[0].num
					if nn == 3:
						nn = 4
					elif nn == 4:
						nn = 6
					else:
						nn = 0
					canvas.coords(uu,235, 135, 258, 158)
					vv2.update()
					jugador.casa.fichas[0].mover = True
					jugador.casa.fichas[0].cambiar_posicion(tablero1.casillas[38])
					if len(tablero1.casillas[38].fichas) == 2:
						barrera(uu,tablero1.casillas[38].fichas[1],-15)
					else:
						barrera(uu,tablero1.casillas[38].fichas[0],-15)
					bandera = True
			elif jugador.color == "azul":
				if len(tablero1.casillas[21].fichas) == 2 or len(jugador.casa.fichas)==0:
					pass
				else:
					print "Se esta sacando una ficha de casa"
					
					uu = jugador.casa.fichas[0].imagen
					nn = jugador.casa.fichas[0].num
					print nn
					if nn == 3:
						nn = 4
					elif nn == 4:
						nn = 6
					else:
						nn = 0
					canvas.coords(uu,486, 243, 509, 266)
					vv2.update()
					jugador.casa.fichas[0].mover = True
					jugador.casa.fichas[0].cambiar_posicion(tablero1.casillas[21])
					if len(tablero1.casillas[21].fichas) == 2:
						barrera(uu,tablero1.casillas[21].fichas[1],-15)
					else:
						barrera(uu,tablero1.casillas[21].fichas[0],-15)
					bandera = True
			elif jugador.color == "amarillo":
				if len(tablero1.casillas[4].fichas) == 2 or len(jugador.casa.fichas)==0:
					pass
				else:
					print "Se esta sacando una ficha de casa"
					
					uu = jugador.casa.fichas[0].imagen
					nn = jugador.casa.fichas[0].num
					if nn == 3:
						nn = 4
					elif nn == 4:
						nn = 6
					else:
						nn = 0
					canvas.coords(uu,381, 491, 404, 514)
					vv2.update()
					jugador.casa.fichas[0].mover = True
					jugador.casa.fichas[0].cambiar_posicion(tablero1.casillas[4])
					if len(tablero1.casillas[4].fichas) == 2:
						barrera(uu,tablero1.casillas[4].fichas[1],-15)
					else:
						barrera(uu,tablero1.casillas[4].fichas[0],-15)
					bandera = True
			break
	return bandera
def nuevo_recorrido(jugador,r1,tablero,n):
	if r1 == 5:
		bandera = False
		
		if bandera != True:
			
			jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
			##verficiando si llego a la meta
			premio_meta(jugador,jugador.fichas[n-1],tablero)
			###capturando
			capturar(jugador,n,tablero)
				
			ficha_a_mover = 0
	else:
		
		
		jugador.mover_ficha(jugador.fichas[n-1],r1,tablero)
		##verficiando si llego a la meta
		premio_meta(jugador,jugador.fichas[n-1],tablero)
		###capturando
		capturar(jugador,n,tablero)
			
		ficha_a_mover = 0

##############################################################################
### lista de jugadores####
jugadores = []


lista_jugadores[0].fichas = lista_fichas_amarillas
lista_jugadores[1].fichas = lista_fichas_azul
lista_jugadores[2].fichas = lista_fichas_rojo
lista_jugadores[3].fichas = lista_fichas_verde

lista_jugadores[0].casa = tablero1.casas[0]
lista_jugadores[1].casa = tablero1.casas[1]
lista_jugadores[2].casa = tablero1.casas[2]
lista_jugadores[3].casa = tablero1.casas[3]

### ficha inicial en el tablero
fichas_iniciales = [tablero1.casillas[4],tablero1.casillas[21],tablero1.casillas[38],tablero1.casillas[55]]
for r in range(4):
	fichas_iniciales[r].fichas.append(lista_jugadores[r].fichas[0])	
	lista_jugadores[r].fichas[0].esta_en = fichas_iniciales[r]


#### llenando las casas #####
for r in range(4):
		tablero1.casas[r].fichas.append(lista_jugadores[r].fichas[1])
		tablero1.casas[r].fichas.append(lista_jugadores[r].fichas[2])
		tablero1.casas[r].fichas.append(lista_jugadores[r].fichas[3])
		lista_jugadores[r].fichas[1].esta_en = tablero1.casas[r]
		lista_jugadores[r].fichas[2].esta_en = tablero1.casas[r]
		lista_jugadores[r].fichas[3].esta_en = tablero1.casas[r]
	
#########################################################################
######funciones de los botones############################################
## funcion rojo es para poder mover las fichas en la imagen considerando el pasillo
 
def rojo(m,imagen,R,esta_en,tipo,r10,memoria2,dato):
		
		if m + esta_en > dato and  tipo!="meta" and esta_en<=dato:
			
			if esta_en < dato and tipo != "pasillo":
				mover0(dato-esta_en,imagen,R,esta_en)
				m0 = m + esta_en - dato
				if m0 <=8:
					if R.col == "amarillo":
						m0 = -1*m0
						x = 0
						y = 9*m0
					elif R.col == "rojo":
						x = 0
						y = 9*m0
					elif R.col == "azul":
						m0 = -1*m0
						x = 9*m0
						y = 0
					elif R.col == "verde":
						x = 9*m0
						y = 0
					for i in range(3):
						time.sleep(0.1)
						#vv2.update()
						canvas.move(r10,x,y)
						vv2.update()
			elif esta_en == dato :
				
				m0 = m
				if R.col == "amarillo":
					m0 = -1*m0
					x = 0
					y = 9*m0
				elif R.col == "rojo":
					x = 0
					y = 9*m0
				elif R.col == "azul":
					m0 = -1*m0
					x = 9*m0
					y = 0
				elif R.col == "verde":
					x = 9*m0
					y = 0
				
				for i in range(3):
					time.sleep(0.1)
					#vv2.update()
					canvas.move(r10,x,y)
					vv2.update()
		
		elif tipo == "meta":
			pass

		else:
			if tipo == "pasillo":
				if R.esta_en.numero + m <= 7:
					
					m0 = m
					if R.col == "amarillo":
						m0 = -1*m0
						x = 0
						y = 9*m0
					elif R.col == "rojo":
						x = 0
						y = 9*m0
					elif R.col == "azul":
						m0 = -1*m0
						x = 9*m0
						y = 0
					elif R.col == "verde":
						x = 9*m0
						y = 0
					for i in range(3):
						time.sleep(0.1)
						#vv2.update()
						canvas.move(imagen,x,y)
						vv2.update()
				elif m == 1:
					m0 = 1
					
					if R.col == "amarillo":
						m0 = -1*m0
						x = 0
						y = 9*m0
					elif R.col == "rojo":
						x = 0
						y = 9*m0
					elif R.col == "azul":
						m0 = -1*m0
						x = 9*m0
						y = 0
					elif R.col == "verde":
						x = 9*m0
						y = 0
					for i in range(3):
						time.sleep(0.1)
						#vv2.update()
						canvas.move(imagen,x,y)
						vv2.update()
			else:
				mover0(m,imagen,R,esta_en)
	
				
def rojo1(m,imagen,R,esta_en,tipo,r10,memoria2,dato):
	
		if m + esta_en > dato and  tipo!="meta" :
			if esta_en < dato and tipo != "pasillo":
				
				mover0(dato-esta_en,imagen,R,esta_en)
				m0 = m + esta_en - dato
				if m0 <=8:
					if R.col == "amarillo":
						m0 = -1*m0
						x = 0
						y = 9*m0
					elif R.col == "rojo":
						x = 0
						y = 9*m0
					elif R.col == "azul":
						m0 = -1*m0
						x = 9*m0
						y = 0
					elif R.col == "verde":
						x = 9*m0
						y = 0
					for i in range(3):
						time.sleep(0.1)
						#vv2.update()
						canvas.move(r10,x,y)
						vv2.update()
			elif esta_en == dato :
				
				m0 = m
				if R.col == "amarillo":
					m0 = -1*m0
					x = 0
					y = 9*m0
				elif R.col == "rojo":
					x = 0
					y = 9*m0
				elif R.col == "azul":
					m0 = -1*m0
					x = 9*m0
					y = 0
				elif R.col == "verde":
					x = 9*m0
					y = 0
				
				for i in range(3):
					time.sleep(0.1)
					#vv2.update()
					canvas.move(r10,x,y)
					vv2.update()
		
		elif tipo == "meta":
			pass

		else:
			if tipo == "pasillo":
				if R.esta_en.numero + m <= 7:
					
					m0 = m
					if R.col == "amarillo":
						m0 = -1*m0
						x = 0
						y = 9*m0
					elif R.col == "rojo":
						x = 0
						y = 9*m0
					elif R.col == "azul":
						m0 = -1*m0
						x = 9*m0
						y = 0
					elif R.col == "verde":
						x = 9*m0
						y = 0
					for i in range(3):
						time.sleep(0.1)
						#vv2.update()
						canvas.move(imagen,x,y)
						vv2.update()
				elif m == 1:
					m0 = 1
					
					if R.col == "amarillo":
						m0 = -1*m0
						x = 0
						y = 9*m0
					elif R.col == "rojo":
						x = 0
						y = 9*m0
					elif R.col == "azul":
						m0 = -1*m0
						x = 9*m0
						y = 0
					elif R.col == "verde":
						x = 9*m0
						y = 0
					for i in range(3):
						time.sleep(0.1)
						#vv2.update()
						canvas.move(imagen,x,y)
						vv2.update()
			else:
				
				mover0(m,imagen,R,esta_en)
				
#### funciones de los botones lanzar dado ####

#### funciones para imagen ###
#Creamos las variables conteniendo los archivos de imagenes para los resultados del dado
resultado6 = PhotoImage(file = "seis_m.gif")
resultado5 = PhotoImage(file = "cinco_m.gif")
resultado4 = PhotoImage(file = "cuatro_m.gif")
resultado3 = PhotoImage(file = "siete_m.gif")
resultado2 = PhotoImage(file = "dos_m.gif")
resultado1 = PhotoImage(file = "uno_m.gif")

def VentanaDado(dad1,dad2):
	#Funcion auxiliar
	def ocultar(ventana):
		return ventana.withdraw()
	
	#Ventana para el dado	
	#Creando ventana hija de "ventana"
	ventana_dado= Toplevel(vv2)

	#Creando la ventana de dibujo dentro de "ventana_dado"
	canvas2 = Canvas(ventana_dado, width=350, height=200)
	
	
	#Creando el botton de OK para cerrar la ventana con los resultados
	boton_ok= Button(ventana_dado, text="OK", height = 1, width = 1,command=lambda:(ocultar(ventana_dado))).place(x = 175, y = 175)
	
	#Verifica los resultados para asignar al lienzo las imagenes correspondientes
	
	def verifica_resultado(dad1,dad2,canvas2):
		#Agregando nuestra imagen al lienzo.
		if dad1==1:
			canvas2.create_image(100,100,image= resultado1)
		if dad1==2:
			canvas2.create_image(100,100,image= resultado2)
		if dad1==3:
			canvas2.create_image(100,100,image= resultado3)
		if dad1==4:
			canvas2.create_image(100,100,image= resultado4)
		if dad1==5:
			canvas2.create_image(100,100,image= resultado5)
		if dad1==6:
			canvas2.create_image(100,100,image= resultado6)
		if dad2==1:
			canvas2.create_image(250,100,image= resultado1)
		if dad2==2:
			canvas2.create_image(250,100,image= resultado2)
		if dad2==3:
			canvas2.create_image(250,100,image= resultado3)
		if dad2==4:
			canvas2.create_image(250,100,image= resultado4)
		if dad2==5:
			canvas2.create_image(250,100,image= resultado5)
		if dad2==6:
			canvas2.create_image(250,100,image= resultado6)
		canvas2.pack()
	verifica_resultado(dad1,dad2,canvas2)

#################


def tirar_dado1():
	#rojo
	if len(jugadores)>=3:
		if jugadores[2].turno == True or jugadores[2].extra == True :
			
			f1 = jugadores[2].fichas[0]
			f2 = jugadores[2].fichas[1]
			f3 = jugadores[2].fichas[2]
			f4 = jugadores[2].fichas[3]
			
			w1 = f1.memoria3
			w2 = f2.memoria3
			w3 = f3.memoria3
			w4 = f4.memoria3
			
			tengo1 = dado1.dar_resultado()
			tengo2 = dado2.dar_resultado()
			m1 = tengo1
			m2 = tengo2
			if tengo1 == 5 or tengo2 == 5:
				if tengo1 == 5:
					temp = sacar_ficha(jugadores[2])
					if temp == True:
						jugadores[2].dado1_usado = True
				elif tengo2 == 5:
					temp = sacar_ficha(jugadores[2])
					if temp == True:
						jugadores[2].dado2_usado = True
				else:
					temp1 = sacar_ficha(jugadores[2])
					temp2 = sacar_ficha(jugadores[2])
					if temp1 == True:
						jugadores[2].dado1_usado = True
					if temp2 == True:
						jugadores[2].dado2_usado = True
			
			if evaluar_resultado(f1,m1,tablero1) == False and evaluar_resultado(f2,m1,tablero1) == False and evaluar_resultado(f3,m1,tablero1) == False and evaluar_resultado(f4,m1,tablero1) == False and evaluar_resultado(f1,m2,tablero1) == False and evaluar_resultado(f2,m2,tablero1) == False and evaluar_resultado(f3,m2,tablero1) == False and evaluar_resultado(f4,m2,tablero1) == False:
				if len(jugadores)==3:
					jugadores[0].turno = True
					jugadores[2].turno = False
				else:
					jugadores[3].turno = True
					jugadores[2].turno = False

				
				f1.mover = False
				f2.mover = False
				f3.mover = False
				f4.mover = False
				
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f2,m1,tablero1) == False:
				f2.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f3,m1,tablero1) == False:
				f3.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f4,m1,tablero1) == False:
				f4.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			else:
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			jugadores[2].extra = False
			jugadores[2].tiro = 1
			VentanaDado(tengo1,tengo2)
def tirar_dado2():
	#azul
	if len(jugadores)>=2:
		if jugadores[1].turno == True or jugadores[1].extra == True :
			
			f1 = jugadores[1].fichas[0]
			f2 = jugadores[1].fichas[1]
			f3 = jugadores[1].fichas[2]
			f4 = jugadores[1].fichas[3]
			
			w1 = f1.memoria3
			w2 = f2.memoria3
			w3 = f3.memoria3
			w4 = f4.memoria3
			
			tengo1 = dado1.dar_resultado()
			tengo2 = dado2.dar_resultado()
			m1 = tengo1
			m2 = tengo2
			if tengo1 == 5 or tengo2 == 5:
				if tengo1 == 5:
					temp = sacar_ficha(jugadores[1])
					if temp == True:
						jugadores[1].dado1_usado = True
				elif tengo2 == 5:
					temp = sacar_ficha(jugadores[1])
					if temp == True:
						jugadores[1].dado2_usado = True
				else:
					temp1 = sacar_ficha(jugadores[1])
					temp2 = sacar_ficha(jugadores[1])
					if temp1 == True:
						jugadores[1].dado1_usado = True
					if temp2 == True:
						jugadores[1].dado2_usado = True
			
			if evaluar_resultado(f1,m1,tablero1) == False and evaluar_resultado(f2,m1,tablero1) == False and evaluar_resultado(f3,m1,tablero1) == False and evaluar_resultado(f4,m1,tablero1) == False and evaluar_resultado(f1,m2,tablero1) == False and evaluar_resultado(f2,m2,tablero1) == False and evaluar_resultado(f3,m2,tablero1) == False and evaluar_resultado(f4,m2,tablero1) == False:
				if len(jugadores)==2:
					jugadores[0].turno = True
					jugadores[1].turno = False
				else:
					jugadores[2].turno = True
					jugadores[1].turno = False

				
				f1.mover = False
				f2.mover = False
				f3.mover = False
				f4.mover = False
				
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f2,m1,tablero1) == False:
				f2.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f3,m1,tablero1) == False:
				f3.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f4,m1,tablero1) == False:
				f4.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			else:
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			jugadores[1].extra = False
			jugadores[1].tiro = 1
			VentanaDado(tengo1,tengo2)
	
def tirar_dado3():
	#verde
	if len(jugadores)>=4:
		if jugadores[3].turno == True or jugadores[3].extra == True :
			
			f1 = jugadores[3].fichas[0]
			f2 = jugadores[3].fichas[1]
			f3 = jugadores[3].fichas[2]
			f4 = jugadores[3].fichas[3]
			
			w1 = f1.memoria3
			w2 = f2.memoria3
			w3 = f3.memoria3
			w4 = f4.memoria3
			
			tengo1 = dado1.dar_resultado()
			tengo2 = dado2.dar_resultado()
			m1 = tengo1
			m2 = tengo2
			if tengo1 == 5 or tengo2 == 5:
				if tengo1 == 5:
					temp = sacar_ficha(jugadores[3])
					if temp == True:
						jugadores[3].dado1_usado = True
				elif tengo2 == 5:
					temp = sacar_ficha(jugadores[0])
					if temp == True:
						jugadores[3].dado2_usado = True
				else:
					temp1 = sacar_ficha(jugadores[3])
					temp2 = sacar_ficha(jugadores[3])
					if temp1 == True:
						jugadores[3].dado1_usado = True
					if temp2 == True:
						jugadores[3].dado2_usado = True
			
			if evaluar_resultado(f1,m1,tablero1) == False and evaluar_resultado(f2,m1,tablero1) == False and evaluar_resultado(f3,m1,tablero1) == False and evaluar_resultado(f4,m1,tablero1) == False and evaluar_resultado(f1,m2,tablero1) == False and evaluar_resultado(f2,m2,tablero1) == False and evaluar_resultado(f3,m2,tablero1) == False and evaluar_resultado(f4,m2,tablero1) == False:
				jugadores[0].turno = True
				jugadores[3].turno = False
				
				f1.mover = False
				f2.mover = False
				f3.mover = False
				f4.mover = False
				
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f2,m1,tablero1) == False:
				f2.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f3,m1,tablero1) == False:
				f3.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f4,m1,tablero1) == False:
				f4.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			else:
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			jugadores[3].extra = False
			jugadores[3].tiro = 1
			VentanaDado(tengo1,tengo2)
	
def tirar_dado4():
	#amarillo
	if len(jugadores)>=1:
		if jugadores[0].turno == True or jugadores[0].extra == True :
			
			f1 = jugadores[0].fichas[0]
			f2 = jugadores[0].fichas[1]
			f3 = jugadores[0].fichas[2]
			f4 = jugadores[0].fichas[3]
			
			w1 = f1.memoria3
			w2 = f2.memoria3
			w3 = f3.memoria3
			w4 = f4.memoria3
			
			tengo1 = dado1.dar_resultado()
			tengo2 = dado2.dar_resultado()
			m1 = tengo1
			m2 = tengo2
			if tengo1 == 5 or tengo2 == 5:
				if tengo1 == 5:
					temp = sacar_ficha(jugadores[0])
					if temp == True:
						jugadores[0].dado1_usado = True
				elif tengo2 == 5:
					temp = sacar_ficha(jugadores[0])
					if temp == True:
						jugadores[0].dado2_usado = True
				else:
					temp1 = sacar_ficha(jugadores[0])
					temp2 = sacar_ficha(jugadores[0])
					if temp1 == True:
						jugadores[0].dado1_usado = True
					if temp2 == True:
						jugadores[0].dado2_usado = True
			
			if evaluar_resultado(f1,m1,tablero1) == False and evaluar_resultado(f2,m1,tablero1) == False and evaluar_resultado(f3,m1,tablero1) == False and evaluar_resultado(f4,m1,tablero1) == False and evaluar_resultado(f1,m2,tablero1) == False and evaluar_resultado(f2,m2,tablero1) == False and evaluar_resultado(f3,m2,tablero1) == False and evaluar_resultado(f4,m2,tablero1) == False:
				jugadores[1].turno = True
				jugadores[0].turno = False
				
				f1.mover = False
				f2.mover = False
				f3.mover = False
				f4.mover = False
				
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f2,m1,tablero1) == False:
				f2.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f3,m1,tablero1) == False:
				f3.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			elif evaluar_resultado(f4,m1,tablero1) == False:
				f4.mover = False
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			else:
				f1.memoria3 = w1
				f2.memoria3 = w2
				f3.memoria3 = w3
				f4.memoria3 = w4
			jugadores[0].extra = False
			jugadores[0].tiro = 1
			VentanaDado(tengo1,tengo2)
		
############## Rojo######################
def mover_rojo1():
	
	if len(jugadores) >= 3:
		
		turno = jugadores[2].turno
		R = lista_fichas_rojo[0]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m = 0
		if turno == True and R.mover == True:
			
			#distincion entre dados
			if jugadores[2].dado1_usado == False:
				jugadores[2].dado1_usado = True
				
				m = dado1.resultado
			elif jugadores[2].dado2_usado == False:
				
				jugadores[2].dado2_usado = True
				m = dado2.resultado
			
			bandera = evaluar_resultado(lista_fichas_rojo[0],m,tablero1)
			
			if bandera == True:
				if m + esta_en -34 <= 8 and esta_en <= 34:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,34)
						
					nuevo_recorrido(jugadores[2],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,34)
						
					nuevo_recorrido(jugadores[2],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
					
				
				
				print jugadores[2].extra, jugadores[2].dado1_usado, jugadores[2].dado2_usado 
				print len(jugadores)
				# verficando si tiene tiro extra
				if m == 6 and jugadores[2].extra == False and jugadores[2].tiro <2:
					jugadores[2].extra = True
					jugadores[2].tiro = jugadores[2].tiro +1
				if jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True and jugadores[2].extra == False:
					jugadores[2].turno = False
					if len(jugadores) <= 3:
						jugadores[0].turno = True

					elif len(jugadores)>= 4:
						jugadores[3].turno = True
						
				if jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True and jugadores[2].extra == True:
					jugadores[2].dado1_usado = False
					jugadores[2].dado2_usado = False
					
					
				elif jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True:
					
					jugadores[2].dado1_usado = False
					jugadores[2].dado2_usado = False
				
	if len(tablero1.pasillo_rojo[7].fichas)==4:
		ganador()
		if len(jugadores) <= 3:
			jugadores[0].turno = False
		elif len(jugadores)>= 4:
		
			jugadores[3].turno = False
def mover_rojo2():
	if len(jugadores) >= 3:
		turno = jugadores[2].turno
		
		R = lista_fichas_rojo[1]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m= 0
			
		if turno == True and R.mover == True:
			#distincion entre dados
			if jugadores[2].dado1_usado == False:
				jugadores[2].dado1_usado = True
				m = dado1.resultado
				
			elif jugadores[2].dado2_usado == False:
				jugadores[2].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_rojo[1],m,tablero1)
			if bandera == True:
				if m + esta_en -34 <= 8 and esta_en <= 34:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,34)
						
					nuevo_recorrido(jugadores[2],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,34)
						
					nuevo_recorrido(jugadores[2],m,tablero1,2)
						
					barrera(R.imagen,R,-15)
					
				
				# verficando si tiene tiro extra
				if m == 6 and jugadores[2].extra == False and jugadores[2].tiro <2:
					jugadores[2].extra = True
					jugadores[2].tiro = jugadores[2].tiro +1
				elif jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True and jugadores[2].extra == False:
					jugadores[2].turno = False
					if len(jugadores) <= 3:
						jugadores[0].turno = True
					elif len(jugadores)>= 4:
						jugadores[3].turno = True
				if jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True and jugadores[2].extra == True:
					jugadores[2].dado1_usado = False
					jugadores[2].dado2_usado = False
					
				elif jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True:
					
					jugadores[2].dado1_usado = False
					jugadores[2].dado2_usado = False
	if len(tablero1.pasillo_rojo[7].fichas)==4:
		ganador()
		if len(jugadores) <= 3:
			jugadores[0].turno = False
		elif len(jugadores)>= 4:
		
			jugadores[3].turno = False

def mover_rojo3():
	if len(jugadores) >= 3:
		turno = jugadores[2].turno
		m = 0
		R = lista_fichas_rojo[2]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
			
		if turno == True and R.mover == True:
			#distincion entre dados
			if jugadores[2].dado1_usado == False:
				jugadores[2].dado1_usado = True
				m = dado1.resultado
				
			elif jugadores[2].dado2_usado == False:
				jugadores[2].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_rojo[2],m,tablero1)
			
			if bandera == True:
				if m + esta_en -34 <= 8 and esta_en <= 34:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,34)
						
					nuevo_recorrido(jugadores[2],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,34)
						
					nuevo_recorrido(jugadores[2],m,tablero1,3)
						
					barrera(R.imagen,R,-15)
					
				
				# verficando si tiene tiro extra
				if m == 6 and jugadores[2].extra == False and jugadores[2].tiro <2:
					jugadores[2].extra = True
					jugadores[2].tiro = jugadores[2].tiro +1
				elif jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True and jugadores[2].extra == False:
					jugadores[2].turno = False
					if len(jugadores) <= 3:
						jugadores[0].turno = True
					elif len(jugadores)>= 4:
						jugadores[3].turno = True
				if jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True and jugadores[2].extra == True:
					jugadores[2].dado1_usado = False
					jugadores[2].dado2_usado = False
					
				elif jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True:
					
					jugadores[2].dado1_usado = False
					jugadores[2].dado2_usado = False
	if len(tablero1.pasillo_rojo[7].fichas)==4:
		ganador()
		if len(jugadores) <= 3:
			jugadores[0].turno = False
		elif len(jugadores)>= 4:
		
			jugadores[3].turno = False

def mover_rojo4():
	if len(jugadores) >= 3:
		turno = jugadores[2].turno
		
		R = lista_fichas_rojo[3]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m = 0
		if turno == True and R.mover==True:
			#distincion entre dados
			if jugadores[2].dado1_usado == False:
				jugadores[2].dado1_usado = True
				m = dado1.resultado
				
			elif jugadores[2].dado2_usado == False:
				jugadores[2].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_rojo[3],m,tablero1)
			if bandera == True:
				if m + esta_en -34 <= 8 and esta_en <= 34:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,34)
						
					nuevo_recorrido(jugadores[2],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,34)
						
					nuevo_recorrido(jugadores[2],m,tablero1,4)
						
					barrera(R.imagen,R,-15)
					
				
				# verficando si tiene tiro extra
				if m == 6 and jugadores[2].extra == False and jugadores[2].tiro <2:
					jugadores[2].extra = True
					jugadores[2].tiro = jugadores[2].tiro +1
				if jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True and jugadores[2].extra == False:
					jugadores[2].turno = False
					if len(jugadores) <= 3:
						jugadores[0].turno = True
					elif len(jugadores)>= 4:
						
						jugadores[3].turno = True
				if jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True and jugadores[2].extra == True:
					jugadores[2].dado1_usado = False
					jugadores[2].dado2_usado = False
					
				elif jugadores[2].dado1_usado == True and jugadores[2].dado2_usado == True:
					
					jugadores[2].dado1_usado = False
					jugadores[2].dado2_usado = False
	if len(tablero1.pasillo_rojo[7].fichas)==4:
		ganador()
		if len(jugadores) <= 3:
			jugadores[0].turno = False
		elif len(jugadores)>= 4:
		
			jugadores[3].turno = False

####### verde #####################3

def mover_verde1():
	
	if len(jugadores) >= 4:
		turno = jugadores[3].turno
		R = lista_fichas_verde[0]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m = 0
			
		if turno == True and R.mover == True :
			#distincion entre dados
			if jugadores[3].dado1_usado == False:
				jugadores[3].dado1_usado = True
				m = dado1.resultado
			elif jugadores[3].dado2_usado == False:
				jugadores[3].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_verde[0],m,tablero1)
			if bandera == True:
				if m + esta_en -51 <= 8 and esta_en<=51:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,51)
						
					nuevo_recorrido(jugadores[3],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,51)
						
					nuevo_recorrido(jugadores[3],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
					
				
				
				# verficando si tiene tiro extra
				if m == 6 and jugadores[3].extra == False and jugadores[3].tiro <2:
					jugadores[3].extra = True
					jugadores[3].tiro = jugadores[3].tiro +1
				elif jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True and jugadores[3].extra == False:
					jugadores[3].turno = False
					
					jugadores[0].turno = True
					
				if jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True and jugadores[3].extra == True:
					jugadores[3].dado1_usado = False
					jugadores[3].dado2_usado = False
					
				elif jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True:
					
					jugadores[3].dado1_usado = False
					jugadores[3].dado2_usado = False

	if len(tablero1.pasillo_verde[7].fichas)==4:
		ganador()
		jugadores[0].turno = False

def mover_verde2():
	
	if len(jugadores) >= 4:
		turno = jugadores[3].turno
		
		R = lista_fichas_verde[1]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m = 0
			
		if turno == True and R.mover == True :
			#distincion entre dados
			if jugadores[3].dado1_usado == False:
				jugadores[3].dado1_usado = True
				m = dado1.resultado
			elif jugadores[3].dado2_usado == False:
				jugadores[3].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_verde[1],m,tablero1)
			if bandera == True:
				if m + esta_en -51 <= 8 and esta_en<=51:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,51)
						
					nuevo_recorrido(jugadores[3],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,51)
						
					nuevo_recorrido(jugadores[3],m,tablero1,2)
						
					barrera(R.imagen,R,-15)
					
				
				# verficando si tiene tiro extra
				if m == 6 and jugadores[3].extra == False and jugadores[3].tiro <2:
					jugadores[3].extra = True
					jugadores[3].tiro = jugadores[3].tiro +1
				elif jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True and jugadores[3].extra == False:
					jugadores[3].turno = False
					
					jugadores[0].turno = True
					
				if jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True and jugadores[3].extra == True:
					jugadores[3].dado1_usado = False
					jugadores[3].dado2_usado = False
					
				elif jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True:
					
					jugadores[3].dado1_usado = False
					jugadores[3].dado2_usado = False
	if len(tablero1.pasillo_verde[7].fichas)==4:
		ganador()
		jugadores[0].turno = False
def mover_verde3():
	if len(jugadores) >= 4:
		turno = jugadores[3].turno
		m = 0
		R = lista_fichas_verde[2]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
			
		if turno == True and R.mover == True:
			#distincion entre dados
			if jugadores[3].dado1_usado == False:
				jugadores[3].dado1_usado = True
				m = dado1.resultado
			elif jugadores[3].dado2_usado == False:
				jugadores[3].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_verde[2],m,tablero1)
			if bandera == True:
				if m + esta_en -51 <= 8 and esta_en<=51:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,51)
						
					nuevo_recorrido(jugadores[3],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,51)
						
					nuevo_recorrido(jugadores[3],m,tablero1,3)
						
					barrera(R.imagen,R,-15)
					
				
				# verficando si tiene tiro extra
				if m == 6 and jugadores[3].extra == False and jugadores[3].tiro <2:
					jugadores[3].extra = True
					jugadores[3].tiro = jugadores[3].tiro +1
				elif jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True and jugadores[3].extra == False:
					jugadores[3].turno = False
					
					jugadores[0].turno = True
					
				if jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True and jugadores[3].extra == True:
					jugadores[3].dado1_usado = False
					jugadores[3].dado2_usado = False
					
				elif jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True:
					
					jugadores[3].dado1_usado = False
					jugadores[3].dado2_usado = False
	if len(tablero1.pasillo_verde[7].fichas)==4:
		ganador()
		jugadores[0].turno = False
def mover_verde4():
	if len(jugadores) >= 4:
		turno = jugadores[3].turno
		
		R = lista_fichas_verde[3]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m = 0
			
		if turno == True and R.mover == True:
			#distincion entre dados
			if jugadores[3].dado1_usado == False:
				jugadores[3].dado1_usado = True
				m = dado1.resultado
			elif jugadores[3].dado2_usado == False:
				jugadores[3].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_verde[3],m,tablero1)
			if bandera == True:
				if m + esta_en -51 <= 8 and esta_en<=51:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,51)
						
					nuevo_recorrido(jugadores[3],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,51)
						
					nuevo_recorrido(jugadores[3],m,tablero1,4)
						
					barrera(R.imagen,R,-15)
					
				
				# verficando si tiene tiro extra
				if m == 6 and jugadores[3].extra == False and jugadores[3].tiro <2:
					jugadores[3].extra = True
					jugadores[3].tiro = jugadores[3].tiro +1
				elif jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True and jugadores[3].extra == False:
					jugadores[3].turno = False
					
					jugadores[0].turno = True
					
				if jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True and jugadores[3].extra == True:
					jugadores[3].dado1_usado = False
					jugadores[3].dado2_usado = False
					
				elif jugadores[3].dado1_usado == True and jugadores[3].dado2_usado == True:
					
					jugadores[3].dado1_usado = False
					jugadores[3].dado2_usado = False
	if len(tablero1.pasillo_verde[7].fichas)==4:
		ganador()
		jugadores[0].turno = False
############ azul###########################

def mover_azul1():
	if len(jugadores) >=2 :
		turno = jugadores[1].turno
		
		R = lista_fichas_azul[0]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria
		tipo = R.esta_en.tipo
		m = 0
		
		if turno == True and R.mover == True:
			#distincion entre dados
			if jugadores[1].dado1_usado == False:
				jugadores[1].dado1_usado = True
				m = dado1.resultado
			elif jugadores[1].dado2_usado == False:
				jugadores[1].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_azul[0],m,tablero1)
			if bandera == True:
				if m + esta_en -17 <= 8 and esta_en <= 17:
					
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,17)
						
					nuevo_recorrido(jugadores[1],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
				
				
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,17)
						
					nuevo_recorrido(jugadores[1],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
					
				
				
				# verficando si tiene tiro extra
				if m == 6 and jugadores[1].extra == False and jugadores[1].tiro <2:
					jugadores[1].extra = True
					jugadores[1].tiro = jugadores[1].tiro +1
				elif jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True and jugadores[1].extra == False:
					jugadores[1].turno = False
					if len(jugadores) <= 2:
						jugadores[0].turno = True
					elif len(jugadores)>=3:
						jugadores[2].turno = True
				if jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True and jugadores[1].extra == True:
					jugadores[1].dado1_usado = False
					jugadores[1].dado2_usado = False
					
				elif jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True:
					
					jugadores[1].dado1_usado = False
					jugadores[1].dado2_usado = False
	if len(tablero1.pasillo_azul[7].fichas)==4:
		ganador()
		if len(jugadores) <= 2:
			jugadores[0].turno = False
		elif len(jugadores)>=3:
			jugadores[2].turno = False

def mover_azul2():
	if len(jugadores) >=2 :
		turno = jugadores[1].turno
		R = lista_fichas_azul[1]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m = 0
			
		if turno == True and R.mover == True:
			#distincion entre dados
			if jugadores[1].dado1_usado == False:
				jugadores[1].dado1_usado = True
				m = dado1.resultado
			elif jugadores[1].dado2_usado == False:
				jugadores[1].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_azul[1],m,tablero1)
			if bandera == True:
				if m + esta_en -17 <= 8 and esta_en<=17:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,17)
						
					nuevo_recorrido(jugadores[1],m,tablero1,2)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,17)
						
					nuevo_recorrido(jugadores[1],m,tablero1,2)
						
					barrera(R.imagen,R,-15)
					
				
						
					barrera(R.imagen,R,-15)
				# verficando si tiene tiro extra
				if m == 6 and jugadores[1].extra == False and jugadores[1].tiro <2:
					jugadores[1].extra = True
					jugadores[1].tiro = jugadores[1].tiro +1
				elif jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True and jugadores[1].extra == False:
					jugadores[1].turno = False
					if len(jugadores) <= 2:
						jugadores[0].turno = True
					elif len(jugadores)>=3:
						jugadores[2].turno = True
				if jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True and jugadores[1].extra == True:
					jugadores[1].dado1_usado = False
					jugadores[1].dado2_usado = False
					
				elif jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True:
					
					jugadores[1].dado1_usado = False
					jugadores[1].dado2_usado = False
	if len(tablero1.pasillo_azul[7].fichas)==4:
		ganador()
		if len(jugadores) <= 2:
			jugadores[0].turno = False
		elif len(jugadores)>=3:
			jugadores[2].turno = False
def mover_azul3():
	if len(jugadores) >=2 :
		turno = jugadores[1].turno
		R = lista_fichas_azul[2]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m = 0
			
		if turno == True and R.mover == True :
			#distincion entre dados
			if jugadores[1].dado1_usado == False:
				jugadores[1].dado1_usado = True
				m = dado1.resultado
			elif jugadores[1].dado2_usado == False:
				jugadores[1].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_azul[2],m,tablero1)
			if bandera == True:
				if m + esta_en -17 <= 8 and esta_en<=17:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,17)
						
					nuevo_recorrido(jugadores[1],m,tablero1,2)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,17)
						
					nuevo_recorrido(jugadores[1],m,tablero1,3)
						
					barrera(R.imagen,R,-15)
					
				
				# verficando si tiene tiro extra
				if m == 6 and jugadores[1].extra == False and jugadores[1].tiro <2:
					jugadores[1].extra = True
					jugadores[1].tiro = jugadores[1].tiro +1
				elif jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True and jugadores[1].extra == False:
					jugadores[1].turno = False
					if len(jugadores) <= 2:
						jugadores[0].turno = True
					elif len(jugadores)>=3:
						jugadores[2].turno = True
				if jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True and jugadores[1].extra == True:
					jugadores[1].dado1_usado = False
					jugadores[1].dado2_usado = False
					
				elif jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True:
					
					jugadores[1].dado1_usado = False
					jugadores[1].dado2_usado = False
	if len(tablero1.pasillo_azul[7].fichas)==4:
		ganador()
		if len(jugadores) <= 2:
			jugadores[0].turno = False
		elif len(jugadores)>=3:
			jugadores[2].turno = False
def mover_azul4():
	if len(jugadores) >=2 :
		turno = jugadores[1].turno
		m = 0
		R = lista_fichas_azul[3]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
			
		if turno == True and R.mover == True:
			#distincion entre dados
			if jugadores[1].dado1_usado == False:
				jugadores[1].dado1_usado = True
				m = dado1.resultado
			elif jugadores[1].dado2_usado == False:
				jugadores[1].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_azul[3],m,tablero1)
			if bandera == True:
				if m + esta_en -17 <= 8 and esta_en<=17:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,17)
						
					nuevo_recorrido(jugadores[1],m,tablero1,2)
				if memoria2 != 3:
					barrera(R.imagen,R,15)
						
					rojo(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,17)
						
					nuevo_recorrido(jugadores[1],m,tablero1,4)
						
					barrera(R.imagen,R,-15)
					
				
						
					barrera(R.imagen,R,-15)
				# verficando si tiene tiro extra
				if m == 6 and jugadores[1].extra == False and jugadores[1].tiro <2:
					jugadores[1].extra = True
					jugadores[1].tiro = jugadores[1].tiro +1
				elif jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True and jugadores[1].extra == False:
					jugadores[1].turno = False
					if len(jugadores) <= 2:
						jugadores[0].turno = True
					elif len(jugadores)>=3:
						jugadores[2].turno = True
				if jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True and jugadores[1].extra == True:
					jugadores[1].dado1_usado = False
					jugadores[1].dado2_usado = False
					
				elif jugadores[1].dado1_usado == True and jugadores[1].dado2_usado == True:
					
					jugadores[1].dado1_usado = False
					jugadores[1].dado2_usado = False
	if len(tablero1.pasillo_azul[7].fichas)==4:
		ganador()
		if len(jugadores) <= 2:
			jugadores[0].turno = False
		elif len(jugadores)>=3:
			jugadores[2].turno = False
######## amarillo ##########################################

def mover_amarillo1():
	if len(jugadores) >=1 :
		
		turno = jugadores[0].turno
		R = lista_fichas_amarillas[0]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m = 0
		
		if turno == True and R.mover == True:
			
			#distincion entre dados
			if jugadores[0].dado1_usado == False:
				jugadores[0].dado1_usado = True
				m = dado1.resultado
			elif jugadores[0].dado2_usado == False:
				jugadores[0].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_amarillas[0],m,tablero1)
			if bandera == True:
				if memoria2 != 3:
					
					barrera(R.imagen,R,15)
					
						
					rojo1(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,68)
						
					nuevo_recorrido(jugadores[0],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
					
				if m + esta_en -68 <= 8 and memoria2 != 1:
					
					if esta_en1.fichas.index(R)==1:
						barrera(R.imagen,R,15)
					else:
						barrera(esta_en1.fichas[0].imagen,esta_en1.fichas[0],15)
						
					rojo1(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,68)
						
					nuevo_recorrido(jugadores[0],m,tablero1,1)
						
					barrera(R.imagen,R,-15)
				
				# verficando si tiene tiro extra
				if m == 6 and jugadores[0].extra == False and jugadores[0].tiro <2:
					jugadores[0].extra = True
					jugadores[0].tiro = jugadores[0].tiro +1
				elif jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True and jugadores[0].extra == False:
					jugadores[0].turno = False
					
					if len(jugadores)>=2:
						jugadores[1].turno = True
				if jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True and jugadores[0].extra == True:
					jugadores[0].dado1_usado = False
					jugadores[0].dado2_usado = False
					
				elif jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True:
					
					jugadores[0].dado1_usado = False
					jugadores[0].dado2_usado = False
	if len(tablero1.pasillo_amarillo[7].fichas)==4:
		ganador()
		jugadores[1].turno = False

def mover_amarillo2():
	if len(jugadores) >=1 :
		turno = jugadores[0].turno
		m =0
		R = lista_fichas_amarillas[1]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
			
		if turno == True and R.mover == True:
			#distincion entre dados
			if jugadores[0].dado1_usado == False:
				jugadores[0].dado1_usado = True
				m = dado1.resultado
			elif jugadores[0].dado2_usado == False:
				jugadores[0].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_amarillas[1],m,tablero1)
			if bandera == True:
				if memoria2 != 3:
					barrera(R.imagen,R,15)
					
						
					rojo1(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,68)
						
					nuevo_recorrido(jugadores[0],m,tablero1,2)
						
					barrera(R.imagen,R,-15)
					
				if m + esta_en -68 <= 8 and memoria2 != 1:
					barrera(R.imagen,R,15)
					
						
					rojo1(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,68)
						
					nuevo_recorrido(jugadores[0],m,tablero1,2)
						
					barrera(R.imagen,R,-15)
				# verficando si tiene tiro extra
				if m == 6 and jugadores[0].extra == False and jugadores[0].tiro <2:
					jugadores[0].extra = True
					jugadores[0].tiro = jugadores[0].tiro +1
				elif jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True and jugadores[0].extra == False:
					jugadores[0].turno = False
					
					if len(jugadores)>=2:
						jugadores[1].turno = True
				if jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True and jugadores[0].extra == True:
					jugadores[0].dado1_usado = False
					jugadores[0].dado2_usado = False
					
				elif jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True:
					
					jugadores[0].dado1_usado = False
					jugadores[0].dado2_usado = False
	if len(tablero1.pasillo_amarillo[7].fichas)==4:
		ganador()
		jugadores[1].turno = False
def mover_amarillo3():
	if len(jugadores) >=1 :
		turno = jugadores[0].turno
		R = lista_fichas_amarillas[2]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m = 0
			
		if turno == True and R.mover == True:
			#distincion entre dados
			if jugadores[0].dado1_usado == False:
				jugadores[0].dado1_usado = True
				m = dado1.resultado
			elif jugadores[0].dado2_usado == False:
				jugadores[0].dado2_usado = True
				m = dado2.resultado
			
			
			bandera = evaluar_resultado(lista_fichas_amarillas[2],m,tablero1)
			if bandera == True:
				if memoria2 != 3:
					barrera(R.imagen,R,15)
					
						
						
					rojo1(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,68)
						
					nuevo_recorrido(jugadores[0],m,tablero1,3)
						
					barrera(R.imagen,R,-15)
					
				if m + esta_en -68 <= 8 and memoria2 != 1:
					barrera(R.imagen,R,15)
					
					
						
					rojo1(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,68)
						
					nuevo_recorrido(jugadores[0],m,tablero1,3)
						
					barrera(R.imagen,R,-15)
				# verficando si tiene tiro extra
				if m == 6 and jugadores[0].extra == False and jugadores[0].tiro <2:
					jugadores[0].extra = True
					jugadores[0].tiro = jugadores[0].tiro +1
				elif jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True and jugadores[0].extra == False:
					jugadores[0].turno = False
					
					if len(jugadores)>=2:
						jugadores[1].turno = True
				if jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True and jugadores[0].extra == True:
					jugadores[0].dado1_usado = False
					jugadores[0].dado2_usado = False
					
				elif jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True:
					
					jugadores[0].dado1_usado = False
					jugadores[0].dado2_usado = False
	if len(tablero1.pasillo_amarillo[7].fichas)==4:
		ganador()
		jugadores[1].turno = False
def mover_amarillo4():
	if len(jugadores) >=1 :
		turno = jugadores[0].turno
		R = lista_fichas_amarillas[3]
		esta_en = R.esta_en.numero
		esta_en1 = R.esta_en
		memoria2 = R.memoria2
		tipo = R.esta_en.tipo
		m = 0
			
		if turno == True and R.mover == True:
			#distincion entre dados
			if jugadores[0].dado1_usado == False:
				jugadores[0].dado1_usado = True
				m = dado1.resultado
			elif jugadores[0].dado2_usado == False:
				jugadores[0].dado2_usado = True
				m = dado2.resultado
			
			
			
			bandera = evaluar_resultado(lista_fichas_amarillas[3],m,tablero1)
			if  bandera == True:
				if memoria2 != 3:
					barrera(R.imagen,R,15)
					
						
					rojo1(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,68)
						
					nuevo_recorrido(jugadores[0],m,tablero1,4)
						
					barrera(R.imagen,R,-15)
					
				if m + esta_en -68 <= 8 and memoria2 != 1:
					barrera(R.imagen,R,15)
						
					rojo1(m,R.imagen,R,esta_en,tipo,R.imagen,R.memoria2,68)
						
					nuevo_recorrido(jugadores[0],m,tablero1,4)
						
					barrera(R.imagen,R,-15)
				# verficando si tiene tiro extra
				if m == 6 and jugadores[0].extra == False and jugadores[0].tiro <2:
					jugadores[0].extra = True
					jugadores[0].tiro = jugadores[0].tiro +1
				elif jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True and jugadores[0].extra == False:
					jugadores[0].turno = False
					
					if len(jugadores)>=2:
						jugadores[1].turno = True
				if jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True and jugadores[0].extra == True:
					jugadores[0].dado1_usado = False
					jugadores[0].dado2_usado = False
					
				elif jugadores[0].dado1_usado == True and jugadores[0].dado2_usado == True:
					
					jugadores[0].dado1_usado = False
					jugadores[0].dado2_usado = False
	if len(tablero1.pasillo_amarillo[7].fichas)==4:
		ganador()
		jugadores[1].turno = False
		
############################################################
################################################################################	
		
def barrera(u,F,a):
	if len(F.esta_en.fichas)==2 and F.esta_en.fichas.index(F)==1:
		
		color = F.esta_en.fichas[0].col
		numero = F.esta_en.fichas[0].num
		if color == "rojo":
			if numero == 1:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(r1,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
					
				else:
					canvas.move(r1,a,0)
					canvas.move(u,-1*a,0)
					vv2.update()
			
			elif numero == 2:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(r2,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(r2,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
					
			elif numero == 3:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(r3,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(r3,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
					
			elif numero == 4:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(r4,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(r4,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
		
		elif color == "amarillo":
			if numero == 1:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(a1,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
					
				else:
					canvas.move(a1,a,0)
					canvas.move(u,-1*a,0)
					vv2.update()
			
			elif numero == 2:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(a2,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(a2,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
					
			elif numero == 3:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(a3,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(a3,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
					
			elif numero == 4:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(a4,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(a4,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
					
		elif color == "azul":
			if numero == 1:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(z1,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
					
				else:
					canvas.move(z1,a,0)
					canvas.move(u,-1*a,0)
					vv2.update()
			
			elif numero == 2:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(z2,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(z2,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
					
			elif numero == 3:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(z3,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(z3,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
					
			elif numero == 4:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(z4,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(z4,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
					
		elif color == "verde":
			if numero == 1:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(v1,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
					
				else:
					canvas.move(v1,a,0)
					canvas.move(u,-1*a,0)
					vv2.update()
			
			elif numero == 2:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(v2,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(v2,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
					
			elif numero == 3:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(v3,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(v3,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
					
			elif numero == 4:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(v4,0,a)
					canvas.move(u,0,-1*a)
					vv2.update()
				else:
					canvas.move(v4,a,0)
					canvas.move(u,-1*a,0) 
					vv2.update()
	elif len(F.esta_en.fichas)==2 and F.esta_en.fichas.index(F)==0:
		
		color = F.esta_en.fichas[1].col
		numero = F.esta_en.fichas[1].num
		if color == "rojo":
			if numero == 1:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(r1,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
					
				else:
					canvas.move(r1,-1*a,0)
					canvas.move(u,a,0)
					vv2.update()
			
			elif numero == 2:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(r2,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(r2,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
					
			elif numero == 3:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(r3,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(r3,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
					
			elif numero == 4:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(r4,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(r4,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
		
		elif color == "amarillo":
			if numero == 1:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(a1,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
					
				else:
					canvas.move(a1,-1*a,0)
					canvas.move(u,a,0)
					vv2.update()
			
			elif numero == 2:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(a2,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(a2,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
					
			elif numero == 3:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(a3,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(a3,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
					
			elif numero == 4:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(a4,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(a4,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
					
		elif color == "azul":
			if numero == 1:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(z1,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
					
				else:
					canvas.move(z1,-1*a,0)
					canvas.move(u,a,0)
					vv2.update()
			
			elif numero == 2:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(z2,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(z2,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
					
			elif numero == 3:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(z3,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(z3,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
					
			elif numero == 4:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(z4,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(z4,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
					
		elif color == "verde":
			if numero == 1:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(v1,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
					
				else:
					canvas.move(v1,-1*a,0)
					canvas.move(u,a,0)
					vv2.update()
			
			elif numero == 2:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(v2,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(v2,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
					
			elif numero == 3:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(v3,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(v3,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()
					
			elif numero == 4:
				if F.esta_en.numero in Aa or F.esta_en.numero in Bb:
					canvas.move(v4,0,-1*a)
					canvas.move(u,0,a)
					vv2.update()
				else:
					canvas.move(v4,-1*a,0)
					canvas.move(u,a,0) 
					vv2.update()

def mover0(m,u,F,numero):
	#numero = F.esta_en.numero
	
	if m + numero <=8:
		#F.cambiar_posicion(tablero1.casillas[m+numero-1])
		x = 0
		y = -9*m
		for i in range(3):
			time.sleep(0.1)
			#vv2.update()
			canvas.move(u,x,y)
			vv2.update()
			
	elif m + numero == 9:
		if numero < 8:
			temp = 8 - numero
			#F.cambiar_posicion(tablero1.casillas[temp+numero-1])
			mover0(temp,u,F,numero)
			mover0(m-temp,u,F,8)
		else:
			
			x1 = 392
			y1 = 421
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			x = 417-x1
			y = 398-y1
			canvas.move(u,x,y)
			vv2.update()
		
	elif m + numero <=16:
		if numero < 9:
			mover0(8-numero,u,F,numero)
			mover0(1,u,F,8)
			mover0(m+numero-9,u,F,9)
		else:
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			y = 0
			x = 9*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
			
	elif m + numero <= 18:
		if numero <16:
			temp = 16 - numero
			#F.cambiar_posicion(tablero1.casillas[temp+numero-1])
			mover0(temp,u,F,numero)
			mover0(m-temp,u,F,16)
		else:
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			x = 0
			y = -24*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
	
	elif m + numero <=25:
		if numero < 18:
			temp = 18 - numero
			mover0(temp,u,F,numero)
			mover0(m+numero-18,u,F,18)
		else:
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			y = 0
			x = -9*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
			
	elif m + numero == 26:
		if numero < 25:
			mover0(25-numero,u,F,numero)
			mover0(1,u,F,25)
		else:
			x1 = 417
			y1 = 251
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			x = 392-x1
			y = 227-y1-3
			canvas.move(u,x,y)
			vv2.update()
		
	elif m + numero <=33:
		if numero < 26:
			mover0(26-numero,u,F,numero)
			mover0(m+numero-26,u,F,26)
		else:
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			x = 0
			y = -9*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
			
	elif m + numero <= 35:
		if numero < 33:
			mover0(33-numero,u,F,numero)
			mover0(m+numero-33,u,F,33)
		else:
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			y = 0
			x = -24*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
		
	elif m + numero <=42:
		if numero < 35:
			mover0(35-numero,u,F,numero)
			mover0(m+numero-35,u,F,35)
		else:
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			x = 0
			y = 9*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
			
	elif m + numero == 43:
		if numero < 42:
			mover0(42-numero,u,F,numero)
			mover0(1,u,F,42)
		else:
			x1 = 246
			y1 = 227
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			x =  222-x1
			y = 251-y1
			canvas.move(u,x,y)
			vv2.update()
		
	elif m + numero <=50:
		if numero < 43:
			mover0(43-numero,u,F,numero)
			mover0(m+numero-43,u,F,43)
		else:
			
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			y = 0
			x = -9*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
			
	elif m + numero <= 52:
		if numero < 50:
			mover0(50-numero,u,F,numero)
			mover0(m+numero-50,u,F,50)
		else:
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			x = 0
			y = 24*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
			
	elif m + numero <=59:
		if numero < 52:
			mover0(52-numero,u,F,numero)
			mover0(m+numero-52,u,F,52)
		else:
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			y = 0
			x = 9*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
			
	elif m + numero == 60:
		if numero < 59:
			mover0(59-numero,u,F,numero)
			mover0(1,u,F,59)
		else:
			x1 = 222
			y1 = 398
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			x = 246-x1
			y = 421-y1+3
			canvas.move(u,x,y)
			vv2.update()
		
	elif m + numero <=67:
		if numero < 60:
			mover0(60-numero,u,F,numero)
			mover0(m+numero-60,u,F,60)
		else:
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			x = 0
			y = 9*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
			
	elif m + numero <= 68:
		if numero < 67:
			mover0(67-numero,u,F,numero)
			mover0(m+numero-67,u,F,67)
		else:
			#F.cambiar_posicion(tablero1.casillas[m+numero-1])
			y = 0
			x = 24*m
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
	elif m + numero > 68:
		
		if numero < 68:
			mover0(68-numero,u,F,numero)
			#F.cambiar_posicion(tablero1.casillas[0])
			y = 0
			x = 24
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
			mover0(m+numero-69,u,F,1)
		elif numero == 68:
			#F.cambiar_posicion(tablero1.casillas[0])
			y = 0
			x = 24
			for i in range(3):
				time.sleep(0.1)
				#vv2.update()
				canvas.move(u,x,y)
				vv2.update()
			mover0(m+numero-69,u,F,1)
		

################################################################################################

#Creando ventana hija de "ventana" y botones
def normasdeljuego():
	reglas= Toplevel(vv2)
	reglas.geometry("600x500+400+40")
	reglas.title("Reglas del Juego")
	usuario = Label(reglas, text = "Instrucciones : ", font=("URW Chancery L", 20)).place(x = 50, y = 5)
	usuario1 = Label(reglas, text = "1.	Para poder sacar una ficha de la casa se debe obtener un 5 de cualquiera de los", font=("URW Chancery L", 12)).place(x = 10, y = 40)
	usuario1 = Label(reglas, text = "	 dos dados (que se arrojaran al azar). De hecho mientras dentro de su casa tenga", font=("URW Chancery L", 12)).place(x = 5, y = 60)
	usuario1 = Label(reglas, text = "	fichas y el resultado de al menos uno de los dados sea 5, se está obligado a", font=("URW Chancery L", 12)).place(x = 5, y = 80)
	usuario1 = Label(reglas, text = "	  sacar una ficha.De no poder hacerlo porque hay dos fichas en la casilla  de salida", font=("URW Chancery L", 12)).place(x = 5, y = 100)
	usuario1 = Label(reglas, text = "	   o porque ya no quedan fichas por sacar, se deberá mover cualquier otra ficha", font=("URW Chancery L", 12)).place(x = 5, y = 120)
	usuario1 = Label(reglas, text = "	 el total de espacios indicados por los dados. ", font=("URW Chancery L", 12)).place(x = 5, y = 140)
	usuario1 = Label(reglas, text = "2.	Las fichas se mueven en el tablero en sentido contrario a las manecillas del reloj.", font=("URW Chancery L", 12)).place(x = 10, y =170 )
	usuario1 = Label(reglas, text = "3.	Si se obtiene un 6 se gana un turno adicional. Si se obtiene un segundo 6 no.", font=("URW Chancery L", 12)).place(x = 10, y = 200)
	usuario1 = Label(reglas, text = "4.	Si al mover una de las fichas se llega a una casilla  no segura ocupada por otra ", font=("URW Chancery L", 12)).place(x = 10, y = 230)
	usuario1 = Label(reglas, text = "	  ficha, esta última puede ser capturada.La ficha capturada regresa a su casa y la ficha  ", font=("URW Chancery L", 12)).place(x = 5, y = 250)
	usuario1 = Label(reglas, text = "	vencedora se moverá diez espacios.", font=("URW Chancery L", 12)).place(x = 5, y = 270)
	usuario1 = Label(reglas, text = "5.	No se puede capturar fichas cuando éstas se encuentren en casillas seguras.", font=("URW Chancery L", 12)).place(x = 5, y = 300)
	usuario1 = Label(reglas, text = "6.	En la zona final del tablero solo puede lanzarse un dado.", font=("URW Chancery L", 12)).place(x = 5, y = 320)
	usuario1 = Label(reglas, text = "7.	El juego se termina cuando un jugador ha llevado todas sus fichas hasta la meta. ", font=("URW Chancery L", 12)).place(x = 5, y = 360)
	usuario1 = Label(reglas, text = "	  Para esto deberá obtenerse el número exacto  al lanzar el dado. Si no es exacto deberá ", font=("URW Chancery L", 12)).place(x = 5, y = 380)
	usuario1 = Label(reglas, text = "	 mover la ficha. Al llevar una ficha a la meta se puede mover otra ficha 10 espacios.",font=("URW Chancery L", 12)).place(x = 5, y = 400)
	salir_reglas = Button(reglas, text="Salir", command= reglas.destroy).pack(side= BOTTOM)

########Fichas de cada jugador################################################

#Fichas del rojo
r1 = canvas.create_oval(235, 135, 258, 158, width="0.01c", fill='red', outline='black')
r2 = canvas.create_oval(120, 175, 143, 198, width="0.01c", fill='red', outline='black')
r3 = canvas.create_oval(150, 175, 173, 198, width="0.01c", fill='red', outline='black')
r4 = canvas.create_oval(180, 175, 203, 198, width="0.01c", fill='red', outline='black')
lista_fichas_rojo[0].imagen = r1
lista_fichas_rojo[1].imagen = r2
lista_fichas_rojo[2].imagen = r3
lista_fichas_rojo[3].imagen = r4
#Fichas del azul
z1 = canvas.create_oval(486, 243, 509, 266, width="0.01c", fill='blue', outline='black')
z2 = canvas.create_oval(435, 175, 458, 198, width="0.01c", fill='blue', outline='black')
z3 = canvas.create_oval(465, 175, 488, 198, width="0.01c", fill='blue', outline='black')
z4 = canvas.create_oval(495, 175, 518, 198, width="0.01c", fill='blue', outline='black')
lista_fichas_azul[0].imagen = z1
lista_fichas_azul[1].imagen = z2
lista_fichas_azul[2].imagen = z3
lista_fichas_azul[3].imagen = z4
#Fichas del verde
v1 = canvas.create_oval(130, 384, 153, 407, width="0.01c", fill='green', outline='black')
v2 = canvas.create_oval(120, 595, 143, 618, width="0.01c", fill='green', outline='black')
v3 = canvas.create_oval(150, 595, 173, 618, width="0.01c", fill='green', outline='black')
v4 = canvas.create_oval(180, 595, 203, 618, width="0.01c", fill='green', outline='black')
lista_fichas_verde[0].imagen = v1
lista_fichas_verde[1].imagen = v2
lista_fichas_verde[2].imagen = v3
lista_fichas_verde[3].imagen = v4
#Fichas del amarillo
a1 = canvas.create_oval(381, 491, 404, 514, width="0.01c", fill='yellow', outline='black')
a2 = canvas.create_oval(435, 595, 458, 618, width="0.01c", fill='yellow', outline='black')
a3 = canvas.create_oval(465, 595, 488, 618, width="0.01c", fill='yellow', outline='black')
a4 = canvas.create_oval(495, 595, 518, 618, width="0.01c", fill='yellow', outline='black')
lista_fichas_amarillas[0].imagen = a1
lista_fichas_amarillas[1].imagen = a2
lista_fichas_amarillas[2].imagen = a3
lista_fichas_amarillas[3].imagen = a4

################################################################################################
######## Botones de las fichas para cada jugador #############################

#Botones de las fichas rojos:
boton1_rojo= Button(canvas, text="ficha 1", fg = "red", height = 1, width = 5,command = mover_rojo1).place(x = 35, y = 35)
boton2_rojo= Button(canvas, text="ficha 2", fg = "red", height = 1, width = 5,command = mover_rojo2).place(x = 35, y = 75)
boton3_rojo= Button(canvas, text="ficha 3", fg = "red", height = 1, width = 5,command = mover_rojo3).place(x = 35, y = 135)
boton4_rojo= Button(canvas, text="ficha 4", fg = "red", height = 1, width = 5,command = mover_rojo4).place(x = 35, y = 175)
boton5_rojo= Button(canvas, text="*", fg = "red",height = 1, width = 5,command = tirar_dado1).place(x = 130, y = 35)

#Botones de las fichas azules:
boton1_azul= Button(canvas, text="ficha 1", fg = "blue",height = 1, width = 5,command = mover_azul1).place(x = 540, y = 35)
boton2_azul= Button(canvas, text="ficha 2", fg = "blue",height = 1, width = 5,command = mover_azul2).place(x = 540, y = 75)
boton3_azul= Button(canvas, text="ficha 3", fg = "blue",height = 1, width = 5,command = mover_azul3).place(x = 540, y = 135)
boton4_azul= Button(canvas, text="ficha 4", fg = "blue",height = 1, width = 5,command = mover_azul4).place(x = 540, y = 175)
boton5_azul= Button(canvas, text="*", fg = "blue",height = 1, width = 5,command = tirar_dado2).place(x = 440, y = 35)

#Botones de las fichas verdes:
boton1_verde= Button(canvas, text="ficha 1", height = 1, width = 5,command = mover_verde1).place(x = 35, y = 450)
boton2_verde= Button(canvas, text="ficha 2", height = 1, width = 5,command = mover_verde2).place(x = 35, y = 490)
boton3_verde= Button(canvas, text="ficha 3", height = 1, width = 5,command = mover_verde3).place(x = 35, y = 545)
boton4_verde= Button(canvas, text="ficha 4", height = 1, width = 5,command = mover_verde4).place(x = 35, y = 585)
boton5_verde= Button(canvas, text="*", height = 1, width = 5,command = tirar_dado3).place(x = 130, y = 450)

#Botones de las fichas amarillos:
boton1_amarillo= Button(canvas, text="ficha 1", fg = "brown", height = 1, width = 5,command = mover_amarillo1).place(x = 540, y = 450)
boton2_amarillo= Button(canvas, text="ficha 2", fg = "brown", height = 1, width = 5,command = mover_amarillo2).place(x = 540, y = 490)
boton3_amarillo= Button(canvas, text="ficha 3", fg = "brown", height = 1, width = 5,command = mover_amarillo3).place(x = 540, y = 545)
boton4_amarillo= Button(canvas, text="ficha 4", fg = "brown", height = 1, width = 5,command = mover_amarillo4).place(x = 540, y = 585)
boton5_amarillo= Button(canvas, text="*", fg = "brown", height = 1, width = 5,command = tirar_dado4).place(x = 440, y = 450)

####################################################################################################









######################################################################################################
#Cargar una barra de Menú
barraMenu = Menu(vv2)

#Creando un menú
menuArchivo = Menu(barraMenu)
menuAyuda = Menu(barraMenu)

#Opciones del Menú
menuArchivo.add_command(label= "Salir", command = lambda: exit())
menuAyuda.add_command(label="Juego_Ayuda", command = normasdeljuego)

barraMenu.add_cascade(label= "Archivo", menu = menuArchivo)
barraMenu.add_cascade(label="Ayuda", menu = menuAyuda)

vv2.config(menu = barraMenu)


vv1.mainloop()

