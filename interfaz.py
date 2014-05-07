#! /usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import thread
import cambio_alarmas
import alarmas_digitales
import control
import Hora_archivos

lock = thread.allocate_lock()

def cambio_de_ala (): # Este es el metodo que se ejectua al presionar el boton para cambiar la alarma
	global control, digi, change, archivos
	lock.acquire()
	num = int(change.num_lista()) # Aqui obtengo el valor de la alarma que esta seleccionada
	texto = change.gettext() # Aqui obtengo el texto que esta en el campo de texto

	digi.cambio(num,texto) # Ejecuto el metodo cambio, que es el que cambia la alarma del frame de alarmas digitales 
	change.vaciar() # Vacio el campo para que escriban otra alarma.
	lock.release()

# FRAME DE LOS PINES *********************
def shido ():
	global control, digi, change, archivos

	v0 = Tk()
	v0.config(bg = "white")
	v0.title('IDU-UM v1.20')
	v0.geometry('700x500+290+150')

	lock = thread.allocate_lock()

	digi = alarmas_digitales.alarmas_digitales(v0)
	change = cambio_alarmas.cambio_alarmas(v0)
	control = control.control(v0)
	archivos = Hora_archivos.win_archivos(v0)

	pines =Frame(height = 260, width= 297, bg="black")
	pines.place(x = 402, y = 172)

	analogas = Frame(height=100, width=297, bg= "black")
	analogas.place (x=402,y=399)
	#***************************************************************

	boton = Button(change, font=('eurostile', 14), text="Aceptar" ,command = lambda : cambio_de_ala() ) # El boton que lo situo en el frame de cambio de alarma y ejecuta 
	boton.place(x=210,y=140) # el metodo de cambio de la alarma

	bguardar = Button(archivos, font=('eurostile', 14), text = "Guardar", command = lambda : archivos.salida())
	bguardar.place(x=300, y = 35)
	archivos.tick ()

	thread.start_new_thread(digi.checando, ()) # Un metodo que se ejecuta al mismo tiempo que el de abajo  # El otro metdo que se ejecuta con el de arriba 
	thread.start_new_thread(archivos.guardando, (digi.dar_val1, digi.dar_val2, digi.dar_val3, digi.dar_val4, digi.dar_val5, control.dar_estado))

	print control.dar_estado()

	v0.mainloop()