#! /usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk


alarm1 = 0
alarm2 = 0
alarm3 = 0
alarm4 = 0
alarm5 = 0 


# VENTANA DONDE SE INTRODUCE NOMBRE DE LA ALARMA#########
v1= tk.Tk()
v1.config(bg = "black")
v1.title('Agregar Una Alarma')
v1.geometry('350x200+580+300')
campo_texto = tk.Entry(v1)
campo_texto.pack()
aceptar_button = tk.Button(v1, text="Aceptar", command=lambda : Oprimir_Boton())
aceptar_button.pack()
v1.withdraw()
Boton = 0


# ---------*---------------*---------------*--------------------
def Oprimir_Boton ():
	Boton = 1

def Mostrar_Ventana(ventana):
	v1.deiconify()
		
	

	while Boton != 1:

		print ("Espera de Boton")
		txt = campo_texto.get()
	
	print (txt)


	alarm1 = tk.Label(ventana, text= txt , fg="green", bg="black")
	alarm1.pack()
	Boton = 0
	v1.mainloop()












	

	
	
	






