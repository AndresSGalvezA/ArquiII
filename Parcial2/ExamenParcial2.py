from datetime import datetime
import RPi.GPIO as GPIO
import sys
import signal
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
from os import system

finalProcess = datetime.now()
entryTime = datetime.now()
sizeTime = datetime.now()
carSize = ""
cost1 = 0.0
cost2 = 0.0
cost3 = 0.0
cost4 = 0.0
cost5 = 0.0
cost6 = 0.0
time1 = datetime.now()
endTime1 = datetime.now()
time2 = datetime.now()
endTime2 = datetime.now()
time3 = datetime.now()
endTime3 = datetime.now()
time4 = datetime.now()
endTime4 = datetime.now()
time5 = datetime.now()
endTime5 = datetime.now()
time6 = datetime.now()
endTime6 = datetime.now()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN) #Entrada de un carro.
GPIO.setup(21, GPIO.OUT) #Indicador entrada.
GPIO.setup(20, GPIO.OUT) #Indicador servicio 1.
GPIO.setup(26, GPIO.OUT) #Indicador servicio 2.
GPIO.setup(16, GPIO.OUT) #Indicador servicio 3.
GPIO.setup(19, GPIO.OUT) #Indicador servicio 4.
GPIO.setup(13, GPIO.OUT) #Indicador servicio 5.
GPIO.setup(12, GPIO.OUT) #Indicador servicio 6.
GPIO.setup(6, GPIO.OUT) #Indicador finalizacion.

PATH_CRED = '/home/pi/Desktop/cred.json'
URL_DB = 'https://arqui2-2021-default-rtdb.firebaseio.com/'
cred = credentials.Certificate(PATH_CRED)
firebase_admin.initialize_app(cred, {
    'databaseURL': URL_DB
})
REF = db.reference("/")

REF.set({
    'CarWash': 
    {
    }
})

REF = db.reference("/CarWash")

def insert():
    tiempo = datetime.now()
    REF.push({        
            "Tiempo de recepcion": str(entryTime),
            "Tamano": carSize,
            "Costo de agua": str(cost1),
            "Inicio agua": str(time1),
            "Fin agua": str(endTime1),
            "Costo de shampoo": str(cost2),
            "Inicio shampoo": str(time2),
            "Fin shampoo": str(endTime2),
            "Costo de rodillos": str(cost3),
            "Inicio rodillos": str(time3),
            "Fin rodillos": str(endTime3),
            "Costo de escobas": str(cost4),
            "Inicio escobas": str(time4),
            "Fin escobas": str(endTime4),
            "Costo de agua 2": str(cost5),
            "Inicio agua 2": str(time5),
            "Fin agua 2": str(endTime5),
            "Costo de rodillos 2": str(cost6),
            "Inicio rodillos 2": str(time6),
            "Fin rodillos 2": str(endTime6),
            "Fin proceso": str(finalProcess)
            })

while True:
    # Al entrar un carro
    if GPIO.input(11):
        GPIO.output(6, False)
        GPIO.output(21, True)
        entryTime = datetime.now()

        while GPIO.input(11):
            carSize = "Pequeno"
            sizeTime = datetime.now()
            
            if (sizeTime - entryTime).seconds >= 3:
                carSize = "Mediano"
            
            if (sizeTime - entryTime).seconds >= 6:
                carSize = "Grande"
        
        GPIO.output(21, False) #Termino la entrada.
        print("Ha entrado un vehiculo a las " +  str(entryTime))
        print("Tamano: " + carSize)
        time.sleep(2)
        GPIO.output(20, True) 
        time1 = datetime.now()
        print("Inicio de estacion de agua a las: " + str(time1))
        time.sleep(3)
        endTime1 = datetime.now()
        GPIO.output(20, False)
        print("Fin de la estacion de agua a las: " + str(endTime1))
        
        time.sleep(2)
        GPIO.output(26, True) 
        time2 = datetime.now()
        print("Inicio de estacion de shampoo a las: " + str(time2))
        time.sleep(3)
        endTime2 = datetime.now()
        GPIO.output(26, False)
        print("Fin de la estacion de shampoo a las: " + str(endTime2))
        
        time.sleep(2)
        GPIO.output(16, True) 
        time3 = datetime.now()
        print("Inicio de estacion de rodillos a las: " + str(time3))
        time.sleep(4)
        endTime3 = datetime.now()
        GPIO.output(16, False)
        print("Fin de la estacion de rodillos a las: " + str(endTime3))
        
        time.sleep(2)
        GPIO.output(19, True) 
        time4 = datetime.now()
        print("Inicio de estacion de escobas a las: " + str(time4))
        time.sleep(3)
        endTime4 = datetime.now()
        GPIO.output(19, False)
        print("Fin de la estacion de escobas a las: " + str(endTime4))
        
        time.sleep(2)
        GPIO.output(13, True) 
        time5 = datetime.now()
        print("Inicio de estacion de agua 2 a las: " + str(time5))
        time.sleep(3)
        endTime5 = datetime.now()
        GPIO.output(13, False)
        print("Fin de la estacion de agua 2 a las: " + str(endTime5))
        
        time.sleep(2)
        GPIO.output(12, True) 
        time6 = datetime.now()
        print("Inicio de estacion de rodillos 2 a las: " + str(time6))
        time.sleep(4)
        endTime6 = datetime.now()
        GPIO.output(12, False)
        print("Fin de la estacion de rodillos 2 a las: " + str(endTime6))
        
        time.sleep(3)
        GPIO.output(6, True) 
        finalProcess = datetime.now()
        print("Fin del proceso a las: " + str(finalProcess))
        
        if carSize == "Pequeno":
            cost1 = 2 * (endTime1 - time1).seconds
            cost2 = 2 * (endTime2 - time2).seconds
            cost3 = 2 * (endTime3 - time3).seconds
            cost4 = 2 * (endTime4 - time4).seconds
            cost5 = 2 * (endTime5 - time5).seconds
            cost6 = 2 * (endTime6 - time6).seconds
            
        if carSize == "Mediano":
            cost1 = 4 * (endTime1 - time1).seconds
            cost2 = 4 * (endTime2 - time2).seconds
            cost3 = 4 * (endTime3 - time3).seconds
            cost4 = 4 * (endTime4 - time4).seconds
            cost5 = 4 * (endTime5 - time5).seconds
            cost6 = 4 * (endTime6 - time6).seconds
            
        if carSize == "Grande":
            cost1 = 6 * (endTime1 - time1).seconds
            cost2 = 6 * (endTime2 - time2).seconds
            cost3 = 6 * (endTime3 - time3).seconds
            cost4 = 6 * (endTime4 - time4).seconds
            cost5 = 6 * (endTime5 - time5).seconds
            cost6 = 6 * (endTime6 - time6).seconds
        
        print("Costo agua: " + str(cost1))
        print("Costo shampoo: " + str(cost2))
        print("Costo rodillos: " + str(cost3))
        print("Costo escobas: " + str(cost4))
        print("Costo agua 2: " + str(cost5))
        print("Costo rodillos 2: " + str(cost6))
        insert()
        print("Datos guardados en la base de datos.")
        
GPIO.cleanup()