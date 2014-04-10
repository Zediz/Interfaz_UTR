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
olas = alarmas_digitales.alarmas_digitales(v0)
change = cambio_alarmas.cambio_alarmas(v0)
instrucc = instrucciones.instrucciones(v0)
analog = alarmas_analogas.alarmas_analogas(v0)


# FRAME DE ALARMAS ANALOGAS *********************
#***************************************************************

#***************************************************************


"""def obtener():
	olas.cambio(change.imprimir_texto(),change.num_lista())

"""

# FRAME DE LOS PINES *********************
pines =Frame(height = 260, width= 297, bg="black")
pines.place(x = 402, y = 172)
#***************************************************************


thread.start_new_thread(olas.checando, ())

v0.mainloop()