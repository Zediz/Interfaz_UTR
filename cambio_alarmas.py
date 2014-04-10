#! /usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

class cambio_alarmas(Frame):

	def __init__(self, master):
		Frame.__init__(self, master,height=170, width=297, bg= "black")
		self.place(x=402,y=1)

		titulo = Label(self, text="Cambio de Nombre de las alarmas", fg= "green", bg ="black")
		titulo.place(x=40, y=1)

		paso1 = Label(self, text="1.- Seleccione una alarma -->", fg ="green", bg= "black")
		paso1.place(x=1, y=50)

		paso2 = Label(self, text ="2.- Escriba el texto y de click en aceptar", fg="green", bg="black")
		paso2.place(x=1,y=115)

		self.lista = Listbox(self, height=5, width=9)
		self.lista.insert(1, "  Alarma 1")
		self.lista.insert(2, "  Alarma 2")
		self.lista.insert(3, "  Alarma 3")
		self.lista.insert(4, "  Alarma 4")
		self.lista.insert(5, "  Alarma 5")
		self.lista.place(x=210, y=30)

		self.entrythingy = Entry(self,width=24)
		self.entrythingy.place(x=1, y=140)

		self.boton = Button(self, text="Aceptar", bg = "black" ,command = self.imprimir_texto)
		self.boton.place(x=210,y=140)

		self.contenido = StringVar()
		self.entrythingy.config(textvariable = self.contenido)



	def num_lista(self):
		num = self.lista.curselection()[0]
		print (num)
		return num
	
	def imprimir_texto (self):

		"""print ("Esto es lo que se escribio en el cuadro ----- > " + self.contenido.get())
		self.etiqueta = Label(master,text= self.contenido.get(), fg="green",bg = "black")
		self.etiqueta.pack()"""

		texto = self.contenido.get()
		print (texto)
		return texto

ola = cambio_alarmas(v0)
ola.mainloop()

v0.mainloop()

