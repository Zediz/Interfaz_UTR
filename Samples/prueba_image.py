#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
import time, os

v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

imagen = Canvas (v0,height = 300, width =300, bg="blue")
imagen.place(x=10,y=10)

file = PhotoImage(file="termometro.gif")
imagen.create_image(150,75, image =file)



v0.mainloop()