#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
import time, os
import thread

lock = thread.allocate_lock()

class alarmas_analogas(Frame):
	def __init__(self, master):
		Frame.__init__(self, master,height=116,width=400, bg="black")
		self.place(x = 1 , y = 282)

		title_analog = Label(self,text="Alarmas Analogas", fg ="green", bg = "black")
		title_analog.place(x= 130, y =1)

		analog1 = Label (self, text =" Alarma Analoga 1", fg = "green", bg = "black")
		analog1.place(x= 15, y= 30) 
		analog2 = Label (self, text =" Alarma Analoga 2", fg = "green", bg = "black")
		analog2.place(x= 15, y= 60)

		self.voltaje = Label(self,text="")
		self.voltaje.place(x=200, y=30)

		self.corriente= Label(self,text="")
		self.corriente.place(x=200, y=60)

		self.valv = ""
		self.valc = ""


	def checando_analog(self): # Metodo que checa los archivos adc para ver los valores que estos tienen
		global lock

		ADC_PATH = os.path.normpath('/proc/')
		ADC_FILENAME = "adc"

		adcFiles=[]
		conta = 0
		x=0
		punto = 0

		for i in range(0,6): # Guardamos las direcciones de los archivos en un arreglo
		    adcFiles.append(os.path.join(ADC_PATH, ADC_FILENAME+ str(i)))
		
		while True: # El bucle que se ejecuta para que continuamente se esten revisando el contenido de los archivos
			lock.acquire()
			#print("Se esta ejecutando el While Analogas")
			time.sleep(.3)  # El tiempo entre revision y revision
			for file in adcFiles: #Este abre los 6 archivos de los pines

				fd = open(file,'r') # se abre el archivo
				fd.seek(0) # Se situa en el character 5 del archivo
				valor = fd.read() # de ahi en adelante lee el valor
				

				if conta == 3:
					self.voltaje.config(text=valor+" V") # si esta en el pin 3 asigna el valor en la alarma analoga 1
					self.valv = valor
					#print self.valv
				elif conta ==4: # si esta en el pin 4 asigna el valor a la label de la alarma analoga 2
					self.corriente.config(text=valor+" mA")
					self.valc = valor
					#print self.valc
				conta += 1 # aumenta conta para saber en que momento entra en el pin 3  y 4
				fd.close() # Cierra el archivo cada vez que se termina de leer
			conta = 0 # la variable conta la ponemos en 0 nuevamente apra que empiece a contar de nuevo
			lock.release()

	def dar_valv(self):
		numero = self.valv
		return numero
	
	def dar_valc(self):
		numero = self.valc
		return numero
		
"""v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

ola = alarmas_analogas(v0)



thread.start_new_thread(ola.checando_analog, ())

v0.mainloop()
#"""