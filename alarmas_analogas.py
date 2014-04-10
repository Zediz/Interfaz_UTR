#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
import time, os
import thread

lock = thread.allocate_lock()

class alarmas_analogas(Frame):
	def __init__(self, master):
		Frame.__init__(self, master,height=217,width=400, bg="black")
		self.place(x = 1 , y = 282)

		title_analog = Label(self,text="Alarmas Analogas", fg ="green", bg = "black")
		title_analog.place(x= 130, y =1)

		analog1 = Label (self, text =" Alarma Analoga 1", fg = "green", bg = "black")
		analog1.place(x= 15, y= 30) 
		analog2 = Label (self, text =" Alarma Analoga 2", fg = "green", bg = "black")
		analog2.place(x= 15, y= 60)

		self.voltaje = Label(self,text="10 v")
		self.voltaje.place(x=200, y=30)

		self.corriente= Label(self,text="10 mA")
		self.corriente.place(x=200, y=60)

	


	def checando_analog(self):
		global lock

		ADC_PATH = os.path.normpath('/proc/')
		ADC_FILENAME = "adc"

		adcFiles=[]
		conta = 0
		x=0
		punto = 0

		for i in range(0,6):
		    adcFiles.append(os.path.join(ADC_PATH, ADC_FILENAME+ str(i)))
		
		while True:
			lock.acquire()
			print("Se esta ejecutando el While Analogas")
			time.sleep(1) #.3
			for file in adcFiles:

				fd = open(file,'r')
				fd.seek(0)
				valor = fd.read()
				
				if conta == 3:
					self.voltaje = Label(self,text=valor+" V")
					self.voltaje.place(x=200, y=30)
				elif conta ==4:
					self.corriente = Label(self, text=valor+" mA")
					self.corriente.place(x=200, y=60)
				conta += 1
				fd.close()
			conta = 0
			lock.release()

		
"""v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

ola = alarmas_analogas(v0)


thread.start_new_thread(ola.checando_analog, ())

v0.mainloop()"""