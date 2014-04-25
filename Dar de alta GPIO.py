import wiringpi2

OUTPUT = 1
pin = 2
HIGH = 1 
LOW = 0 

wiringpi2.wiringPiSetupPhys() 
wiringpi2.pinMode(pin,OUTPUT) # se asignaba el pin 2 como salida

while 1:
    wiringpi2.digitalWrite(pin,HIGH) # Escribe 1 en el pin 2
    wiringpi2.delay(1000) # Se espera 1 segundo
    wiringpi2.digitalWrite(pin,LOW)  # Escribe 0 en el pin 2
    wiringpi2.delay(1000) # Se espera 1 segundo




    