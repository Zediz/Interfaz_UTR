#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from Tkinter import *
from time import sleep
from random import randint
import interfaz
#
# correct password is: password
#
def check(Event = None):
    if str(var.get()) != "Sh0ck123":  # hash for password
        o = root.geometry()
        l['text'] = 'Password Equivocada\nSi introduces otra password incorrecta puedes ser reportado'
        l.config(font=('eurostile', 14), fg='red', bg = "black")
        for times in range(50): 
                 root.geometry("+%d+%d" %(int(root.geometry().split("+")[1])+randint(-69, 69), int(root.geometry().split("+")[2])+randint(-69, 69)))
                 root.update()
                 sleep(.05)
                 root.geometry(o)
        root.geometry(o)        
        root.update()
    else:
        l['text'] = 'OK: Entrando al sistema de alarmas'
        print ('\nEstas conectado al sistema de alarmas\n')
        l.config(fg='black')
        sleep(.25)
        root.deiconify()
        root.geometry()
        root.destroy()
        interfaz.shido()
    var.set("")
#        
root = Tk()
root.config(bg = "black", cursor = "hand2")
root.title("IDU-UM v1.0")
root.geometry("413x260+430+230")             
root.wm_attributes("-topmost", 1)
root.focus()

fit = Canvas (root,height = 240, width =273, bg="black", bd = 0 ,highlightthickness=0, relief = 'ridge')
fit.place(x=141, y=0)
file2 = PhotoImage(file="fit.gif")
fit.create_image(150,100, image =file2)

cfe = Canvas (root,height = 100, width =140, bg="black", bd = 0 ,highlightthickness=0, relief = 'ridge')
cfe.place(x=1, y=1)
file1 = PhotoImage(file="cfelogo.gif")
cfe.create_image(50,30, image =file1)


um = Canvas (root,height = 75, width =413, bg="black", bd = 0 ,highlightthickness=0, relief = 'ridge')
um.place(x=1, y=185)
file = PhotoImage(file="umlogo.gif")
um.create_image(205,40, image =file)

var = StringVar()
l = Label(root, font=('eurostile', 15), text = "Bienvenido Hiram... \n Introduce tu Password", bg="black", fg = "gray", bd=0, relief='flat', cursor='hand2')
l.place(x=5, y=103)
a = Entry(root, font=('eurostile', 15), show = '●', bg='#D7DAED', bd=0, relief='flat', cursor='xterm', highlightcolor='red', textvariable = var)  # show = '*'
a.place(x=5, y =150)
a.bind("<Return>", check)
a.focus()
root.mainloop()