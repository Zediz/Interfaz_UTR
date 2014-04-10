import time, os

ADC_PATH = os.path.normpath('/proc/')
ADC_FILENAME = "adc"

adcFiles=[]

for i in range(0,6):
    adcFiles.append(os.path.join(ADC_PATH, ADC_FILENAME+ str(i)))

for file in adcFiles:
    fd = open(file,'r')
    fd.seek(0)
    print ("ADC Channel : " + str(adcFiles.index(file))+ " Result: " + fd.read(16))
    fd.close()
