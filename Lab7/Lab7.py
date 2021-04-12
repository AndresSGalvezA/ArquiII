from datetime import datetime
import RPi.GPIO as GPIO
import sys
import signal
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
from os import system

tiempo = datetime.now()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.OUT) 
GPIO.setup(20, GPIO.IN)
PAHT_CRED = '/home/pi/Desktop/cred.json'
URL_DB = 'https://arqui2-2021-default-rtdb.firebaseio.com/'
cred = credentials.Certificate(PAHT_CRED)
firebase_admin.initialize_app(cred, {'databaseURL': URL_DB})
REF = db.reference("/")
REF.set({'Estado': {}})
REF = db.reference("/Estado")

def insertar(estado):
    tiempo = datetime.now()
    
    if(estado == 1):
        REF.push({ 
        "Fecha y hora": str(tiempo),
        "Accion": "Continuidad", 
        })
 
    else:
        REF.push({ 
        "Fecha y hora": str(tiempo),
        "Accion": "Interrupcion", 
        })
        
while True:
    tiempo = datetime.now()
    
    if GPIO.input(20): 
        GPIO.output(21, False)
        print("Se ha detectado una continuidad de sensor a las " + str(tiempo))
        insertar(1)
        
        while GPIO.input(20):
            tiempo = datetime.now()
    else:
        GPIO.output(21, True)
        print("Se ha detectado una interrupcion de sensor a las " + str(tiempo))
        insertar(0)
        
        while not GPIO.input(20):
            tiempo = datetime.now()
 
GPIO.cleanup()