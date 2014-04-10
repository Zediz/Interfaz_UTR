import time, os

ADC_PATH = os.path.normpath('/proc/')
ADC_FILENAME = "adc"

adcFiles=[]
conta = 0

for i in range(0,6):
    adcFiles.append(os.path.join(ADC_PATH, ADC_FILENAME+ str(i)))

for file in adcFiles:
    fd = open(file,'r')
    fd.seek(0)
    if conta == 3:
		print ("ADC Channel : " + str(adcFiles.index(file))+ " Result: " + fd.read())
    elif conta ==4:
    	print ("ADC Channel : " + str(adcFiles.index(file))+ " Result: " + fd.read())
    
    conta += 1 
    fd.close()

conta = 0
