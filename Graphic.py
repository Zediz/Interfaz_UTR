#! /usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk




v1= tk.Tk()
v1.config(bg = "black")
v1.title('Agregar Una Alarma')
v1.geometry('350x200+580+300')
v1.withdraw()

campo_texto = tk.Entry(v1)
campo_texto.pack()

Aceptar_button =tk.Button(v1, text= "Aceptar", command= lambda : crea_label(texto,funcion))
Aceptar_button.pack()

labels =[]
texto=" "

def crea_label(alarma_name, funcion):
	v1.withdraw()
	labels.append(alarma_name)
	funcion
	print (alarma_name)
	
def obtener_texto():
	campo_texto.get()
	




def Agregar_Alarma (funcion):
	v1.deiconify()
	
	
	print (texto)
	






