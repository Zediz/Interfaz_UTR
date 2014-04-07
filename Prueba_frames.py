#! /usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

alarmas_digitales = Frame(height=280, width=400 ,bg="black")
alarmas_digitales.place(x=1, y=1)



alarmas_analogas = Frame(height=150,width=400, bg="black")
alarmas_analogas.place(x = 1 , y = 282)

change_name = Frame(height=170, width=297, bg= "black")
change_name.place(x=402,y=1)

entrythingy = Entry(change_name)
entrythingy.place(x =1, y =1)

pines =Frame(height = 260, width= 297, bg="black")
pines.place(x = 402, y = 172)

instrucciones = Frame(height=66, width = 698, bg="black")
instrucciones.place(x=1,y= 433)





mainloop()