#! /usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import thread
import cambio_alarmas
import alarmas_digitales
import instrucciones
import alarmas_analogas


v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

digi = alarmas_digitales.alarmas_digitales(v0)
change = cambio_alarmas.cambio_alarmas(v0)
analog = alarmas_analogas.alarmas_analogas(v0)

def cambio_de_ala ():
	num = int(change.num_lista())
	texto = change.gettext()

	digi.cambio(num,texto)
	change.vaciar()



# FRAME DE LOS PINES *********************
pines =Frame(height = 260, width= 297, bg="black")
pines.place(x = 402, y = 172)
#***************************************************************

boton = Button(change, text="Aceptar" ,command = lambda : cambio_de_ala() )
boton.place(x=210,y=140)

thread.start_new_thread(digi.checando, ())
thread.start_new_thread(analog.checando_analog, ())

v0.mainloop()