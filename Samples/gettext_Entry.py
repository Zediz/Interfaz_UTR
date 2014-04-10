#! /usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

class label_alarmas(Tk):

	def __init__(self,parent):
		Tk.__init__(self,parent)
		self.parent = parent

		self.entrythingy = Entry(self)
		self.entrythingy.pack()

		self.boton = Button(self, text="Aceptar", command = self.imprimir_texto)
		self.boton.pack()

		self.contenido = StringVar()
		self.entrythingy.config(textvariable = self.contenido)

		self.entrythingy.bind('<Key-Return>', self.imprimir_texto)
	
	def imprimir_texto (self):
		print ("Esto es lo que se escribio en el cuadro ----- > " + self.contenido.get())
		self.etiqueta = Label(self,text= self.contenido.get(), fg="green",bg = "black")
		self.etiqueta.pack()

root = label_alarmas(None)
root.mainloop()








	

	
	
	






