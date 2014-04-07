#! /usr/bin/python
# -*- coding: utf-8 -*-

import Window_0 as win
import Tkinter as tk 
import time

v0 = tk.Tk()
v0.config(bg = "black")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')


b0 = tk.Button(v0, text="Agregar Alarma",bg = "black", command=lambda : ventana_peque())
b0.pack()

print ("ola")

v1 = tk.Toplevel(v0)
v1.config(bg="black")
v1.title('Agregando alarma')
v1.geometry('300x200')



def ventana_peque():
	v1.deiconify()
	win.wait_write(v0)


v1.withdraw()
v0.mainloop()

