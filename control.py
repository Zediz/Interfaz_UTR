#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
import time, os



class control(Frame):

	def __init__(self, master):
		Frame.__init__(self, master,height=100, width=400, bg= "black")
		self.place(x=1,y=399)

		self.l1 = Label (self, text = "", bg="black", fg = "green")
		self.l1.place (x=15, y=40)

		self.b1 = Button(self, text= "Switch", command = lambda: self.switch())
		self.b1.place(x=300, y =37)

		self.foco= Label(self, text = "          ", bg = "red")
		self.foco.place(x=200, y = 40)
		self.start()

	def cambio_modo (self):
		file = open('/sys/devices/virtual/misc/gpio/mode/gpio6', 'r+' )
		file.write("1")
		file.close()

	def start(self):
		file = open('/sys/devices/virtual/misc/gpio/pin/gpio6','r+')
		valor = int(file.read())

		if valor== 1:
			self.l1.config(text = "El switch esta cerrado")
			self.foco.config(bg = "green")
			self.b1.config(text = "Abrir")
			file.close()
		elif valor == 0:
			self.l1.config(text = "El switch esta abierto")
			self.foco.config(bg = "red")
			self.b1.config(text = "Cerrar")
			file.close()
			

	def switch(self):
		print ("Si funciona el boton")
		file = open('/sys/devices/virtual/misc/gpio/pin/gpio6','r+')
		valor = int(file.read())
		file.seek(0)
		print(valor)

		if valor == 1:
			self.l1.config(text = "El switch esta abierto")
			self.foco.config(bg = "red")
			self.b1.config(text = "Cerrar")
			file.write("0")
			file.close()

		elif valor == 0:
			self.l1.config(text = "El switch esta cerrado")
			self.foco.config(bg = "green")
			self.b1.config(text = "Abrir")
			file.write("1")
			file.close()

	


"""v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

ola = control(v0)
ola.cambio_modo()


v0.mainloop()

#"""