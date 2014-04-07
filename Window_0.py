#! /usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter
import Graphic
import time


#Creacion de Ventana Principal


presionado = 0
	

	

def presionar():
	presionado = 1

def wait_write(ventana):
	alarma = Graphic.labeles()
	print (presionado)
	while presionado == 0:
		print ("Waiting for the Button")
		time.sleep(10)

	alarma.set_name()
	alarma.creation(ventana)
	alarma.mostrar_en_pantalla()


def get_texto():
	texto = campo_de_texto.get()
	return (texto)

