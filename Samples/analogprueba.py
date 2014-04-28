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
		
		while True: # El bucle que se ejecuta para que continuamente se esten revisando el contenido de los archivos
			lock.acquire()
			#print("Se esta ejecutando el While Analogas")
			time.sleep(.3)  # El tiempo entre revision y revision
			file = open('/proc/adc3','r')
			valor = file.read()
			self.voltaje.config(text=valor)
			self.valv=valor
			file.close()
			file2 = open ('/proc/adc4','r')
			valor2= file2.read()
			self.valc = valor2
			self.corriente.config(text = valor2)
			file2.close()
			valor = ""
			valor2 =""
			 # de ahi en adelante lee el valor
			lock.release()

	def dar_valv(self):
		numero = self.valv
		return numero
	
	def dar_valc(self):
		numero = self.valc
		return numero
		
v0 = Tk()
v0.config(bg = "white")
v0.title('Alarmas del Transformador')
v0.geometry('700x500+290+150')



ola = alarmas_analogas(v0)



thread.start_new_thread(ola.checando_analog, ())

v0.mainloop()
#"""