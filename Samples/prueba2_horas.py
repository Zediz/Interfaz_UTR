#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
import time, os
import threading
from datetime import datetime
import thread
from multiprocessing import Process

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

		self.l1 = Label (self, text= "Guarda un nuevo archivo", fg = "green", bg= "black")
		self.l1.place(x=1, y = 35)

	def tick(self):  
	    self.time2 = time.strftime('%H:%M:%S') 
	    if self.time2 != self.time1: 
	        self.time1 = self.time2 
	        self.clock.config(text=self.time2) 
	    self.clock.after(200, self.tick)

class archivo (threading.Thread):
	def __init__(self):
 		threading.Thread.__init__(self)
 		self.fecha = datetime.today()
 		self.name_file= 'Dia_' + str(self.fecha.strftime("%x")).replace('/','-') + '_Start_time_' + str(self.fecha.strftime("%X")).replace(':','-') + '_log.txt'
 		self.f = open(self.name_file, 'a')
 		self.f.write("Lectura de las alarmas\n")
 		self.f.write("-------------------------------------------\n")
 		self.f.write("Leitura\t" + "Hora\t" + "Celsius\t" + "Fahrenheit\n") # escreve esta linha no arquivo
		self.f.write("-------------------------------------------\n")
		self.f.close()

 	def archoo (self):
 		#@Esto es lo que se va a correr
 		global ala1, ala2,ala3,salir,lock

 		time.sleep(1)
 		while salir == 0:
 			print "entre al While"
 			lock.acquire()
	 		self.f = open(self.name_file, 'a')
	 		self.f.write(ala1 + ala2 + ala3)
	 		self.f.close()
	 		lock.release()
	 		print salir
	 		

	def salida(self):
	 	global salir
	 	salir = 1




v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

ola = alarmas_digitales(v0)
#ola.tick()

salir = 0

ala1 ="1"
ala2 ="2"
ala3="3"

b1 = Button(ola, text = "Guardar", command = lambda : archi.salida())
b1.place(x=200, y = 35)


archi = archivo()
t = Process(target = archi.archoo, ())
t.start()
t.join()

lock.acquire()
lock.release()

v0.mainloop()
#****************************************"""