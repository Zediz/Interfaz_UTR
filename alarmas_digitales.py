#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
import time, os
import thread

lock = thread.allocate_lock()

class alarmas_digitales(Frame):
	def __init__(self, master):
		Frame.__init__(self, master,height=280, width=400 ,bg="black")
		self.place(x=1, y=1)

		titulo = Label (self,text= "Alarmas Digitales", fg ="green", bg= "black")
		titulo.place(x= 130, y= 1)

		alarma1 = Label (self, text =" Alarma 1", fg = "green", bg = "black")
		alarma1.place(x= 15, y= 50)
		alarma2 = Label (self, text =" Alarma 2", fg = "green", bg = "black")
		alarma2.place(x= 15, y= 90)
		alarma3 = Label (self, text =" Alarma 3", fg = "green", bg = "black")
		alarma3.place(x= 15, y= 130)
		alarma4 = Label (self, text =" Alarma 4", fg = "green", bg = "black")
		alarma4.place(x= 15, y= 170)
		alarma5 = Label (self, text =" Alarma 5", fg = "green", bg = "black")
		alarma5.place(x= 15, y= 210)

		flecha1 = Label (self, text =" >>>>", fg = "green", bg = "black")
		flecha1.place(x= 280, y= 50)
		flecha2 = Label (self, text =" >>>>", fg = "green", bg = "black")
		flecha2.place(x= 280, y= 90)
		flecha3 = Label (self, text =" >>>>", fg = "green", bg = "black")
		flecha3.place(x= 280, y= 130)
		flecha4 = Label (self, text =" >>>>", fg = "green", bg = "black")
		flecha4.place(x= 280, y= 170)
		flecha5 = Label (self, text =" >>>>", fg = "green", bg = "black")
		flecha5.place(x= 280, y= 210)

		foco1 = Label (self, text ="          ", fg = "green", bg = "red")
		foco1.place(x= 340, y= 52)
		foco2 = Label (self, text ="          ", fg = "green", bg = "red")
		foco2.place(x= 340, y= 92)
		foco3 = Label (self, text ="          ", fg = "green", bg = "red")
		foco3.place(x= 340, y= 132)
		foco4 = Label (self, text ="          ", fg = "green", bg = "red")
		foco4.place(x= 340, y= 172)
		foco5 = Label (self, text ="          ", fg = "green", bg = "red")
		foco5.place(x= 340, y= 212)

	def cambio (self,texto, num): # Cambio del nombre de la alarma 

		if num == 1:
			alarma1= Label (self, text =texto, fg = "green", bg = "black")
			alarma1.place(x= 15, y= 50)
		elif num == 2:
			alarma2 = Label (self, text =texto, fg = "green", bg = "black")
			alarma2.place(x= 15, y= 90)
		elif num == 3:
			alarma3 = Label (self, text =texto, fg = "green", bg = "black")
			alarma3.place(x= 15, y= 130)	
		elif num == 4:
			alarma4 = Label (self, text =texto, fg = "green", bg = "black")
			alarma4.place(x= 15, y= 170)
		elif num == 5:
			alarma5 = Label (self, text =texto, fg = "green", bg = "black")
			alarma5.place(x= 15, y= 210)

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
			time.sleep(.5)
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
			self.foco1 = Label (self, text ="          ",  bg = "red")
			self.foco1.place(x= 340, y= 52)
		elif num == 1:
			self.foco2 = Label (self, text ="          ",  bg = "red")
			self.foco2.place(x= 340, y= 92)
		elif num == 2:
			self.foco3 = Label (self, text ="          ",  bg = "red")
			self.foco3.place(x= 340, y= 132)	
		elif num == 3:
			self.foco4 = Label (self, text ="          ",  bg = "red")
			self.foco4.place(x= 340, y= 172)
		elif num == 4:
			self.foco5 = Label (self, text ="          ",  bg = "red")
			self.foco5.place(x= 340, y= 212)

	def set_color_green(self, num):
		if num == 0:
			self.foco1 = Label (self, text ="          ",  bg = "green")
			self.foco1.place(x= 340, y= 52)
		elif num == 1:
			self.foco2 = Label (self, text ="          ",  bg = "green")
			self.foco2.place(x= 340, y= 92)
		elif num == 2:
			self.foco3 = Label (self, text ="          ",  bg = "green")
			self.foco3.place(x= 340, y= 132)	
		elif num == 3:
			self.foco4 = Label (self, text ="          ",  bg = "green")
			self.foco4.place(x= 340, y= 172)
		elif num == 4:
			self.foco5 = Label (self, text ="          ",  bg = "green")
			self.foco5.place(x= 340, y= 212)
"""v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

ola = alarmas_digitales(v0)

thread.start_new_thread(ola.checando, ())


v0.mainloop()
#****************************************"""














