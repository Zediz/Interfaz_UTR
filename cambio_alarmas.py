#! /usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

class cambio_alarmas(Frame):

	def __init__(self, master):
		Frame.__init__(self, master,height=170, width=297, bg= "black")
		self.place(x=402,y=1)

		titulo = Label(self,   text="Cambio de Nombre de las alarmas", fg= "green", bg ="black")
		titulo.place(x=40, y=1)

		paso1 = Label(self,  text="1.- Seleccione una alarma -->", fg ="green", bg= "black")
		paso1.place(x=1, y=50)

		paso2 = Label(self,  text ="2.- Escriba el texto y de click en aceptar", fg="green", bg="black")
		paso2.place(x=1,y=115)

		self.lista = Listbox(self,   height=5, width=9)
		self.lista.insert(1, "  Alarma 1")
		self.lista.insert(2, "  Alarma 2")
		self.lista.insert(3, "  Alarma 3")
		self.lista.insert(4, "  Alarma 4")
		self.lista.insert(5, "  Alarma 5")
		self.lista.place(x=210, y=30)
		self.lista.select_set(0)
		

		self.entrythingy = Entry(self,width=24)
		self.entrythingy.place(x=1, y=140)

		self.contenido = StringVar()
		self.entrythingy.config(textvariable = self.contenido)



	def num_lista(self): # Metodo que entrega el numero de la alarma que esta seleccionada en la lista
		
		num = self.lista.curselection()
		num2 = num[0]
		#print (num2)
		return num2
	

	def gettext (self): # Metodo que adquiere el texto que esta en el campo de texto y lo entrega.
		texto = self.contenido.get()
		#print ("Esto es lo que se escribio en el cuadro ----- > " + texto)
		return (texto)
		
	def vaciar (self): # Metodo que vacia el campo de texto despues de oprimir el boton
		self.entrythingy.delete (0, END )	

"""v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')
ola = cambio_alarmas(v0)



v0.mainloop()
#*********************"""
