#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
import time, os

class alarmas_analogas(Frame):
	def __init__(self, master):
		Frame.__init__(self, master,height=150,width=400, bg="black")
		self.place(x = 1 , y = 282)

		title_analog = Label(self,text="Alarmas Analogas", fg ="green", bg = "black")
		title_analog.place(x= 130, y =1)

		analog1 = Label (self, text =" Alarma Analoga 1", fg = "green", bg = "black")
		analog1.place(x= 15, y= 50) 
		analog2 = Label (self, text =" Alarma Analoga 2", fg = "green", bg = "black")
		analog2.place(x= 15, y= 90)

		self.entrythingy = Entry(self,width=5,text=" Hola")
		self.entrythingy.place(x=100, y=50)
		