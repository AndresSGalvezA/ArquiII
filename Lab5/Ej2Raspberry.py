#Apagar un LED al cambiar la entrada del pin 20.
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN) #Este pin es una entrada.

while True:
    #Si hay un 1 en el pin 20
    if GPIO.input(20):
        GPIO.output(21, False)
    else:
        GPIO.output(21, True)