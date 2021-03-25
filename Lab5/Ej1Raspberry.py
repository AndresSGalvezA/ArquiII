#Hacer parpadear un LED.
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) #Para que la consola no tire warnings.
GPIO.setmode(GPIO.BCM) #Configuración de los pines para cambiar estados de entrada y salida.
GPIO.setup(18, GPIO.OUT) #El pin 18 es una salida.

def blink(pin):
    GPIO.output(pin, True) #Esto hace positiva la salida de ese pin.
    time.sleep(1)
    GPIO.output(pin, False) #Esto hace negativa la salida de ese pin.
    time.sleep(1)
    return
   
for i in range(0, 50):
    blink(18)

GPIO.cleanup() #Limpia todo el programa.