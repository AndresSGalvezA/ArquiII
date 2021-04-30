import RPi.GPIO as GPIO
import requests
import time

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN) #Boton
GPIO.setup(5, GPIO.OUT) #LED
GPIO.setup(6, GPIO.OUT) #a
GPIO.setup(13, GPIO.OUT) #b
GPIO.setup(19, GPIO.OUT) #c
GPIO.setup(26, GPIO.OUT) #d
GPIO.setup(16, GPIO.OUT) #e
GPIO.setup(20, GPIO.OUT) #f
GPIO.setup(21, GPIO.OUT) #g
GPIO.setup(12, GPIO.OUT) #Relayendpoint = 'https://clzkr8khla.execute-api.us-east-2.amazonaws.com/v1/?pulse='
GPIO.output(5, True) #Indica que el programa se inicia
time.sleep(2)

while True:
    entry = 'a'
    GPIO.output(5, False)
    GPIO.output(6, False)
    GPIO.output(13, False)
    GPIO.output(19, False)
    GPIO.output(26, False)
    GPIO.output(16, False)
    GPIO.output(20, False)
    GPIO.output(21, False)
    GPIO.output(12, False)
 
    if GPIO.input(15):
        clear = requests.get('https://clzkr8khla.execute-api.us-east2.amazonaws.com/v1/?pulse=c')
 
        if GPIO.input(2):
            entry = entry + '1'
        else:
            entry = entry + '0'
 
        if GPIO.input(3):
            entry = entry + '1'
        else:
            entry = entry + '0'
     
        if GPIO.input(4):
            entry = entry + '1'
        else:
            entry = entry + '0' 
            
        if GPIO.input(14):
            entry = entry + '1'
        else:
            entry = entry + '0'
     
        url = endpoint + entry
        response = requests.get(url)
        show = requests.get(endpoint + 's')
        
        # Esperar el resultado de la resta
        while show.text == '"0000000000"':
            time.sleep(1)
            show = requests.get(endpoint + 's')
 
        if show.text[1] == '1':
            GPIO.output(6, True)
        else:
            GPIO.output(6, False)
 
        if show.text[2] == '1':
            GPIO.output(13, True)
        else:
            GPIO.output(13, False)
 
        if show.text[3] == '1':
            GPIO.output(19, True)
        else:
            GPIO.output(19, False)
 
        if show.text[4] == '1':
            GPIO.output(26, True)
        else:
            GPIO.output(26, False) 
        
        if show.text[5] == '1':
            GPIO.output(16, True)
        else:
            GPIO.output(16, False)
 
        if show.text[6] == '1':
            GPIO.output(20, True)
        else:
            GPIO.output(20, False)
 
        if show.text[7] == '1':
            GPIO.output(21, True)
        else:
            GPIO.output(21, False)
 
        if show.text[8] == '1':
            GPIO.output(5, True)
        else:
            GPIO.output(5, False)
           
        # Encender y apagar el foco
        for i in range(int(show.text[9] + show.text[10])):
            GPIO.output(12, True)
            time.sleep(1)
            GPIO.output(12, False)
            time.sleep(1)
        
        # Esperar una nueva entrada
        while not GPIO.input(15):
            entry = ''

GPIO.cleanup()