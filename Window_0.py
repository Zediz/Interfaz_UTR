#! /usr/bin/python
# -*- coding: utf-8 -*-

import time, os
import Tkinter as tk
import Graphic

#VARIABLES ***************************




def set (valor) :
	alarma1 = valor


#************Ventana Principal *****************
def ventana_0 ():	
	v0=tk.Tk()
	v0.config(bg = "black")
	v0.title('Alarmas del Transformador')
	v0.geometry('700x500+290+150')

	#### #AGREGAR COMADO#### 
	b1 = tk.Button(v0, text="Agrear Alarma", command=lambda : Graphic.Mostrar_Ventana(v0))
	b1.pack()
	v0.mainloop()

#*********VENTANA DE ALARMA *********************



#************************************************








print ("Programa Terminado")




