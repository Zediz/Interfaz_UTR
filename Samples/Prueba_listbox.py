#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()

b1 = Button(top, text= "Imprime", command=lambda : imprimir())
b1.pack()

def imprimir():
	 print (Lb1.curselection()[0])
	 


top.mainloop()