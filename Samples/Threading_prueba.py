#! /usr/bin/python
# -*- coding: utf-8 -*

import time, os
import threading

class MiThread(threading.Thread):
	def __init__(self, num):
		threading.Thread.__init__(self)
		self.num = num

		def run(self):
			print "Soy un Hilo", self.num


print "Soy el hilo principal"

for	i in range (0,10):
	t=MiThread(i)
	t.start()
	t.join
	