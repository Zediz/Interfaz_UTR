#! /usr/bin/python
# -*- coding: utf-8 -*-

import time, os
import Tkinter as tk
import Graphic as graf

v0=tk.Tk()
v0.config(bg = "black")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

label = " "

def insert_label ():
	graf.v1.withdraw()
	graf.crea_label()
	label =tk.Label(v0,text= graf.labels[0], fg="green",bg = "black")
	label.place(x=100,y=100)


b1 = tk.Button(v0, text="Agregar Alarma",command=lambda : graf.Agregar_Alarma(insert_label))
b1.pack()




print ("Programa Terminado")




v0.mainloop()