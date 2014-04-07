#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *


class alarmas_digitales(Frame):
	def __init__(self, master):
		Frame.__init__(self, master,height=280, width=400 ,bg="black")
		self.place(x=1, y=1)

		titulo = Label (self,text= "Alarmas Digitales", fg ="green", bg= "black")
		titulo.place(x= 130, y= 1)

		alarma1 = Label (self, text =" Alarma 1", fg = "green", bg = "black")
		alarma1.place(x= 15, y= 50)
		alarma2 = Label (self, text =" Alarma 2", fg = "green", bg = "black")
		alarma2.place(x= 15, y= 90)
		alarma3 = Label (self, text =" Alarma 3", fg = "green", bg = "black")
		alarma3.place(x= 15, y= 130)
		alarma4 = Label (self, text ="Alarma 4", fg = "green", bg = "black")
		alarma4.place(x= 15, y= 170)
		alarma5 = Label (self, text =" Alarma 5", fg = "green", bg = "black")
		alarma5.place(x= 15, y= 210)

		flecha1 = Label (self, text =" >>>>", fg = "green", bg = "black")
		flecha1.place(x= 280, y= 50)
		flecha2 = Label (self, text =" >>>>", fg = "green", bg = "black")
		flecha2.place(x= 280, y= 90)
		flecha3 = Label (self, text =" >>>>", fg = "green", bg = "black")
		flecha3.place(x= 280, y= 130)
		flecha4 = Label (self, text =" >>>>", fg = "green", bg = "black")
		flecha4.place(x= 280, y= 170)
		flecha5 = Label (self, text =" >>>>", fg = "green", bg = "black")
		flecha5.place(x= 280, y= 210)

		foco1 = Label (self, text ="          ", fg = "green", bg = "red")
		foco1.place(x= 340, y= 52)
		foco2 = Label (self, text ="          ", fg = "green", bg = "red")
		foco2.place(x= 340, y= 92)
		foco3 = Label (self, text ="          ", fg = "green", bg = "red")
		foco3.place(x= 340, y= 132)
		foco4 = Label (self, text ="          ", fg = "green", bg = "red")
		foco4.place(x= 340, y= 172)
		foco5 = Label (self, text ="          ", fg = "green", bg = "red")
		foco5.place(x= 340, y= 212)

	def cambio (self,texto, num):

		if num == 1:
			alarma1= Label (self, text =texto, fg = "green", bg = "black")
			alarma1.place(x= 15, y= 50)
		elif num == 2:
			alarma2 = Label (self, text =texto, fg = "green", bg = "black")
			alarma2.place(x= 15, y= 90)
		elif num == 3:
			alarma3 = Label (self, text =texto, fg = "green", bg = "black")
			alarma3.place(x= 15, y= 130)	
		elif num == 4:
			alarma4 = Label (self, text =texto, fg = "green", bg = "black")
			alarma4.place(x= 15, y= 170)
		elif num == 5:
			alarma5 = Label (self, text =texto, fg = "green", bg = "black")
			alarma5.place(x= 15, y= 210)


