from datetime import datetime 
import RPi.GPIO as GPIO

tiempo = datetime.now()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.OUT) 
GPIO.setup(20, GPIO.IN)

while True:
    tiempo = datetime.now()
    if GPIO.input(20): 
        GPIO.output(21, False)
        print("Se ha detectado una continuidad de sensor a las " + str(tiempo))
    
        while GPIO.input(20):
            tiempo = datetime.now()
    
    else:
        GPIO.output(21, True)
        print("Se ha detectado una interrupcion de sensor a las " + str(tiempo))
        
        while not GPIO.input(20):
            tiempo = datetime.now()
 
GPIO.cleanup()