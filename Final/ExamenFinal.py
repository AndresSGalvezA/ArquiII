import RPi.GPIO as GPIO
import time

counter = 0
myMorse = ''
entry = ''
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN) # Enviar uno
GPIO.setup(3, GPIO.IN) # Enviar todo
GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(21, GPIO.OUT) # Emisor

def binToDec(num):
    if num == '0000':
        return '0'
    elif num == '0001':
        return '1'
    elif num == '0010':
        return '2'
    elif num == '0011':
        return '3'
    elif num == '0100':
        return '4'
    elif num == '0101':
        return '5'
    elif num == '0110':
        return '6'
    elif num == '0111':
        return '7'
    elif num == '1000':
        return '8'
    elif num == '1001':
        return '9'
    else:
        return 'e'

def showMorse(morse):
    if morse == '0':
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
    elif morse == '1':
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
    elif morse == '2':
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
    elif morse == '3':
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
    elif morse == '4':
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
    elif morse == '5':
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
    elif morse == '6':
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
    elif morse == '7':
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
    elif morse == '8':
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
    elif morse == '9':
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(1.5)
        GPIO.output(21, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        time.sleep(0.5)
        GPIO.output(21, False)
    else:
        GPIO.output(21, False)

print("Empieza el programa...")

while True:
    GPIO.output(21, False)
    counter = 0
    entry = ''
    myMorse = ''
    
    while counter < 11:
        # Enviar un dato
        if GPIO.input(2):
            print("Se recibio un dato...")
            time.sleep(1)
            counter = counter + 1
            entry = ''
            
            if GPIO.input(6):
                entry = entry + '1'
            else:
                entry = entry + '0'
        
            if GPIO.input(13):
                entry = entry + '1'
            else:
                entry = entry + '0'
            
            if GPIO.input(19):
                entry = entry + '1'
            else:
                entry = entry + '0'
            
            if GPIO.input(26):
                entry = entry + '1'
            else:
                entry = entry + '0'
            
            print("Dato recibido: " + binToDec(entry))
            myMorse = myMorse + binToDec(entry)
            entry = ''
            
        # Enviar todo
        if GPIO.input(3):
            myMorse = myMorse + 'e'
            print("Se procede a mostrar por peticion...")
            time.sleep(1)
            counter = 11
            i = 0
            
            while not myMorse[i] == 'e':
                showMorse(myMorse[i])
                time.sleep(1)
                i = i + 1
            
            print("Fin de la muestra luminica...")
                    
        if counter == 10:
            myMorse = myMorse + 'e'
            print("Se procede a mostrar porque se alcanzo el limite...")
            counter = 11
            i = 0
            
            while not myMorse[i] == 'e':
                showMorse(myMorse[i])
                time.sleep(1)
                i = i + 1
            
            print("Fin de la muestra luminica...")
                
GPIO.cleanup()