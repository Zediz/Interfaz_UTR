#! /usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import thread
import cambio_alarmas
import alarmas_digitales
import alarmas_analogas


v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

digi = alarmas_digitales.alarmas_digitales(v0)
change = cambio_alarmas.cambio_alarmas(v0)
analog = alarmas_analogas.alarmas_analogas(v0)

def cambio_de_ala (): # Este es el metodo que se ejectua al presionar el boton para cambiar la alarma
	num = int(change.num_lista()) # Aqui obtengo el valor de la alarma que esta seleccionada
	texto = change.gettext() # Aqui obtengo el texto que esta en el campo de texto

	digi.cambio(num,texto) # Ejecuto el metodo cambio, que es el que cambia la alarma del frame de alarmas digitales 
	change.vaciar() # Vacio el campo para que escriban otra alarma.

# FRAME DE LOS PINES *********************
pines =Frame(height = 260, width= 297, bg="black")
pines.place(x = 402, y = 172)
#***************************************************************

boton = Button(change, text="Aceptar" ,command = lambda : cambio_de_ala() ) # El boton que lo situo en el frame de cambio de alarma y ejecuta 
boton.place(x=210,y=140) # el metodo de cambio de la alarma

thread.start_new_thread(digi.checando, ()) # Un metodo que se ejecuta al mismo tiempo que el de abajo 
thread.start_new_thread(analog.checando_analog, ()) # El otro metdo que se ejecuta con el de arriba 

v0.mainloop()