#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
import time, os
import thread
from datetime import datetime
import threading

lock = thread.allocate_lock()

class alarmas_digitales(Frame):
	def __init__(self, master):
		Frame.__init__(self, master,height=100, width=297 ,bg="black")
		self.place(x=402, y=399)

		self.fecha = datetime.today()
		self.time1 = '' 
		self.clock = Label(self, font=('ubuntu', 10, 'bold'), bg='black', fg='green', bd=0) 
		self.clock.place(x=200, y=85)

		self.date = Label (self, bg = "black", fg ="green", text= self.fecha.strftime("%d %b %Y ") )
		self.date.place(x=1, y=80)

		self.l1 = Label (self, text= "Guarda un nuevo archivo", fg = "green", bg= "black")
		self.l1.place(x=1, y = 35)

		self.salir = 0

	def tick(self):  
	    self.time2 = time.strftime('%H:%M:%S') 
	    if self.time2 != self.time1: 
	        self.time1 = self.time2 
	        self.clock.config(text=self.time2) 
	    self.clock.after(200, self.tick)

	#Aqui iba cambio del nombre de la alarma	

	def guardando(self, val1,val2,val3,val4,val5,valanalog1,valanalog2,valswitch):
		global lock, salir 
		
	
		num = 0
		
		while True:
			
			archi = self.archivo()
			nombre = archi.get_name()
			print "entre al While1"
			while self.salir == 0:
				print "entre al while 2"
	 			lock.acquire()
		 		archi = open(nombre, 'a')
		 		archi.write(str(self.fecha.strftime("%H:%M:%S "))+ "\t\t" +  val1() +"\t\t" + val2() + "\t\t" + val3() + "\t\t" + val4() + "\t\t" + val5() + "\t\t   "+ valanalog1() + "\t\t\t   " + valanalog2()+ "\t\t  "+ valswitch() + "\n")
		 		archi.close()
		 		lock.release()
		 		print(num)
				num +=1
		 		time.sleep(1)
		 	self.salir = 0



			
	def salida(self):
		global salir
		self.salir = 1

		
			

	class archivo (threading.Thread):
		def __init__(self):
	 		threading.Thread.__init__(self)
	 		self.fecha = datetime.today()
	 		self.name_file= 'Dia_' + str(self.fecha.strftime("%x")).replace('/','-') + '_Start_time_' + str(self.fecha.strftime("%X")).replace(':','-') + '_log.txt'
	 		self.f = open(self.name_file, 'a')
	 		self.f.write("Lectura de alarmas\n")
	 		self.f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
	 		self.f.write("Hora\t\t"+ "|" + "   Alarma 1\t" + "|" + "   Alarma 2\t" + "|" + "   Alarma 3\t" + "|" + "   Alarma 4\t" + "|" + "   Alarma 5\t" + "|" + "   Alarma Analoga 1\t" + "|" + "   Alarma Analoga 2\t" + "|" + "  Switch\n") # escreve esta linha no arquivo
			self.f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
			self.f.close()

		def get_name (self):
			name = self.name_file
			return name
			


v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')

ola = alarmas_digitales(v0)

b1 = Button(ola, text = "Guardar", command = lambda : ola.salida())
b1.place(x=200, y = 35)


def dar_val1():
	return "1"

def dar_val2():
	return "2"

def dar_val3():
	return "3"

def dar_val4():
	return "4"

def dar_val5():
	return "5"

def dar_val6():
	return "6"

def dar_val7():
	return "7"

def dar_val8():
	return "8"


thread.start_new_thread(ola.guardando, (dar_val1,dar_val2,dar_val3,dar_val4,dar_val5,dar_val6,dar_val7,dar_val8))


v0.mainloop()
#****************************************"""
