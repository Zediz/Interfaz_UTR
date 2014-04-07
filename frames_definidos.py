#! /usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import cambio_alarmas
import alarmas_digitales

v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')
olas = alarmas_digitales.alarmas_digitales(v0)
change = cambio_alarmas.cambio_alarmas(v0)



# FRAME DE ALARMAS ANALOGAS *********************
alarmas_analogas = Frame(height=150,width=400, bg="black")
alarmas_analogas.place(x = 1 , y = 282)
#***************************************************************

#***************************************************************


def obtener():
	olas.cambio(change.imprimir_texto(),change.num_lista())



# FRAME DE LOS PINES *********************
pines =Frame(height = 260, width= 297, bg="black")
pines.place(x = 402, y = 172)
#***************************************************************

# FRAME DE Instrucciones *********************
instrucciones = Frame(height=66, width = 698, bg="black")
instrucciones.place(x=1,y= 433)

change.mainloop()
olas.mainloop()

mainloop()