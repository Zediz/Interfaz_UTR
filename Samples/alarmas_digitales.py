#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
import time, os
from datetime import datetime
import thread

lock = thread.allocate_lock()

class alarmas_digitales(Frame):
	def __init__(self, master):
		Frame.__init__(self, master,height=100, width=297 ,bg="black")
		self.place(x=402, y=399)

		fecha = datetime.today()
		self.time1 = '' 
		self.clock = Label(self, font=('ubuntu', 10, 'bold'), bg='black', fg='green', bd=0) 
		self.clock.place(x=200, y=85)

		self.date = Label (self, bg = "black", fg ="green", text= fecha.strftime("%d %b %Y ") )
		self.date.place(x=1, y=80)

		self.b1 = Button(self, text = "Guardar", command = lambda : self.salida())
		self.b1.place(x=200, y = 35)

		self.l1 = Label (self, text= "Guarda un nuevo archivo", fg = "green", bg= "black")
		self.l1.place(x=1, y = 35)

	def tick(self):  
	    self.time2 = time.strftime('%H:%M:%S') 
	    if self.time2 != self.time1: 
	        self.time1 = self.time2 
	        self.clock.config(text=self.time2) 
	    self.clock.after(200, self.tick)
	    

	#Aqui iba cambio del nombre de la alarma
	def cambio (self,num,texto): # Cambio del nombre de la alarma 
			
			print ("Si tiene el valor " + str(num))
			print ("Si tiene el valor " + texto)
			global alarma1

			if num == 0:
				self.alarma1.config(text =texto)
			elif num == 1:
				self.alarma2.config(text =texto)
			elif num == 2:
				self.alarma3.config(text =texto)	
			elif num == 3:
				self.alarma4.config(text =texto)
			elif num == 4:
				self.alarma5.config(text =texto)
			



	def checando(self):
		global lock 

		GPIO_MODE_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
		GPIO_PIN_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
		GPIO_FILENAME = "gpio"

		HIGH = "1"
		LOW ="0"
		INPUT = "0"
		OUTPUT = "1"
		INPUT_PU = "8"

		pinMode = []
		pinData = []

		for i in range(0,5):
			pinMode.append(os.path.join(GPIO_MODE_PATH, 'gpio' + str(i)))
			pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+ str(i)))

		for pin in range (0,5):
			file = open(pinMode[pin], 'r+')
			file.write(INPUT_PU)
			file.close

		while True:
			print("Se esta ejecutando el While digitales")
			time.sleep(.55) #.5
			for pin in range (0,5):
				print ("Estoy checando el gpio" + str(pin))
				file = open(pinData[pin], 'r')
				lock.acquire()
				if int(file.read()) == 1:
					self.set_color_red(pin)
				else:
					self.set_color_green(pin)
				file.close()
				lock.release()


	def set_color_red(self, num):
		if num == 0:
			self.foco1.config(bg = "red")
		elif num == 1:
			self.foco2.config(bg = "red")
		elif num == 2:
			self.foco3.config(bg = "red")
		elif num == 3:
			self.foco4.config(bg = "red")
		elif num == 4:
			self.foco5.config(bg = "red")


	def set_color_green(self, num):
		if num == 0:
			self.foco1.config(bg = "green")
		elif num == 1:
			self.foco2.config(bg = "green")
		elif num == 2:
			self.foco3.config(bg = "green")
		elif num == 3:
			self.foco4.config(bg = "green")
		elif num == 4:
			self.foco5.config(bg = "green")

v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

ola = alarmas_digitales(v0)

thread.start_new_thread(ola.checando, ())


v0.mainloop()
#****************************************"""
