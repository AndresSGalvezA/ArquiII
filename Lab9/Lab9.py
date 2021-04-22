import RPi.GPIO as GPIO
import requests

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
endpoint = 'https://clzkr8khla.execute-api.us-east-2.amazonaws.com/v1/'
pulse = '?pulse=0'

while True:
    pulse = '?pulse=0'
 
    if GPIO.input(3):
        pulse = '?pulse=1'
        response = requests.post(endpoint + pulse)
        print(response.status_code)
        print(response.text)
    
        if response.text[1] == '1':
            GPIO.output(12, True)
        else:
            GPIO.output(12, False)
 
        if response.text[2] == '1':
            GPIO.output(16, True)
        else:
            GPIO.output(16, False)
 
        if response.text[3] == '1':
            GPIO.output(20, True)
        else:
            GPIO.output(20, False)
 
        if response.text[4] == '1':
            GPIO.output(21, True)
        else:
            GPIO.output(21, False)
 
        if response.text[5] == '1':
            GPIO.output(13, True)
        else:
            GPIO.output(13, False)
 
        if response.text[6] == '1':
            GPIO.output(19, True)
        else:
            GPIO.output(19, False)
 
        if response.text[7] == '1':
            GPIO.output(26, True)
        else:
            GPIO.output(26, False)
        
        # Activador del relay.
        if response.text[8] == '1':
            GPIO.output(6, True)
        else:
            GPIO.output(6, False)
    
GPIO.cleanup()
