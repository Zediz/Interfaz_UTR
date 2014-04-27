#! /usr/bin/python
# -*- coding: utf-8 -*
from datetime import datetime
import time, os
import thread
from mtTkinter import *

lock = thread.allocate_lock()

def uno ():
	return "1"

def dos ():
	return "2"

def tres ():
	return "3"

def cuatro ():
	return "4"

def cinco ():
	return "5"

def seis ():
	return "5"

def siete ():
	return "5"

def ocho ():
	return "8"	

numeros = ["8","8","8","8","8","8","8",]
alarma1= uno()
alarma2 = dos()
alarma3 = tres()
alarma4= cuatro()
alarma5 = cinco()
alarma6 = seis()
alarma7 = siete()
alarma8 = ocho()

def creararchivo ():
	fecha = datetime.today()
	nome_file = 'Dia_' + str(fecha.strftime("%x")).replace('/','-') + '_Start_Time' + str(fecha.strftime("%X")).replace(':','-') + '_log.txt'
	f = open(nome_file, 'w'); # cria arquivo para armazenar as leituras recebidas pela serial port
	print ("Si se abre el archivo")
	f.write("Lectura de Alarmas\n"); # escreve esta linha no arquivo	
	f.write("------------------------------------------------------------------------------------------------------------------------------------------------------\n"); # escreve esta linha no arquivo
	f.write("Hora\t\t" + "|   Alarma 1\t" + "|   Alarma 2\t" + "|   Alarma 3\t" + "|   Alarma 4\t" + "|   Alarma 5\t" + "|   Alarma Analoga 1\t" + "|   Alarma Analoga 2\t" + "| Switch\n"); # escreve esta linha no arquivo	
	f.write("-----------\n")
	f.close()
	print ("El archivo se cerro")
	return nome_file

salir = 0

def salida():
	global salir
	salir = 1


def escribir (alarma1, alarma2,alarma3,alarma4,alarma5,alarmaanalog1,alarmaanalog2,switch):	
	global  salir
	while True:
		print ("Si entro al while 1")
		fecha = datetime.today()
		archivo = creararchivo()
		
		print ("El archivo se abrio nuevamente")
		print (salir)
		while salir == 0:
			print "Si entro al while 2"
			f = open(archivo, "a")
			f.write(str(fecha.strftime("%H" + ":" + "%M" + ":" + "%S" + "\t" +"|\t" + alarma1 +"\t" +"|\t"+ alarma2 +"\t" +"|\t" + alarma3+"\t"+"|\t" + alarma4+"\t"+"|\t" + alarma5+"\t" +"|\t"+ alarmaanalog1+"\t\t" +"|\t"+ alarmaanalog2+"\t\t" +"|"+ switch+"\n" )))
			time.sleep(1)
			f.close()

		

def iniciar ():
	print ("Se inicio el nuevo thread")
	thread.start_new_thread(escribir(alarma1,alarma2, alarma3, alarma4,alarma5,alarma6, alarma7,alarma8))
			

v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

b1 = Button(v0, text = "Guardar", command = lambda : salida())
b1.pack()

b2 = Button (v0, text = "Iniciar" , command = lambda : iniciar())
b2.pack()

v0.mainloop()



