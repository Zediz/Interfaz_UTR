#! /usr/bin/python
# -*- coding: utf-8 -*-

import time, os

GPIO_MODE_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/mode')
GPIO_PIN_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/pin')
GPIO_FILENAME = "gpio"

HIGH = "1"
LOW ="0"
INPUT = "0"
OUTPUT = "1"
INPUT_PU = "8"

pinMode = []
pinData = []

for i in range(0,18):
	pinMode.append(os.path.join(GPIO_MODE_PºATH, 'gpio' + str(i)))
	pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+ str(i)))


def Change_Mode(pin,mode):
	file  = open(GPIO_MODE_PATH+"/"+GPIO_FILENAME+str(pin), 'r+')
	file.write(mode)
	file.close()

def HIGH(pin):
	file = open(GPIO_PIN_PATH + "/"+GPIO_FILENAME+str(pin), 'r+')
	file.write("1")
	file.close()

def LOW (pin):
	file = open(GPIO_PIN_PATH + "/"+GPIO_FILENAME+str(pin), 'r+')
	file.write("0")
	file.close()


print ("Programa terminado Todos los Archivos Cambiados")	


