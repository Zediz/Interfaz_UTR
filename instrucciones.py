#! /usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

"""v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')"""

class instrucciones (Frame):

	def __init__ (self,master):
		Frame.__init__(self, master,height=66, width = 698, bg="black")
		self.place(x=1,y= 433)

		instrucciones = Label (self, text="En el recuadro de Alarmas digitales vera las alarmas conectadas a los pines X - X. \n En el Recuadro Cambio de nombre podemos seleccionar una alarma y cambiar el nombre de esta. \n En el recuadro de Pines, encontramos la informacion referente a los pines para utilizar en esta interfaz", fg ="green" , bg = "black")
		instrucciones.place(x=1,y=1)

"""ola = instrucciones(v0)
ola.mainloop()

v0.mainloop()"""