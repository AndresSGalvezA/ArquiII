import json
import boto3
import time

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # a - Insertar entrada de Raspberry
    if event['pulse'][0] == 'a':
        body = event['pulse'][1] + event['pulse'][2] + event['pulse'][3] + event['pulse'][4]
        s3_response = s3.put_object(Bucket='archivos-arqui2', Key='rasp.txt', Body=body)
        return body
    
    # f - Insertar entrada de frontend
    elif event['pulse'][0] == 'f':
        if len(event['pulse']) == 3:
            body = event['pulse'][1] + event['pulse'][2]
        else:
            body = event['pulse'][1]
        
        s3_data = s3.get_object(Bucket='archivos-arqui2', Key='rasp.txt')
        content = str(s3_data['Body'].read())
        decimalResult = convertToDec(content[2] + content[3] + content[4] + content[5]) - int(body)
        
        if decimalResult < 0:
            decimalResult = 0
        
        binaryResult = convertToBin(decimalResult)
        
        if decimalResult < 10:
            strDecimalResult = '00' + str(decimalResult)
        else:
            strDecimalResult = str(decimalResult)
        
        save = s3.put_object(Bucket='archivos-arqui2', Key='result.txt', Body=str(binaryResult + strDecimalResult))
        return decimalResult
    
    elif event['pulse'][0] == 'q':
        s3_query = s3.get_object(Bucket='archivos-arqui2', Key='rasp.txt')
        content = str(s3_query['Body'].read())
        return content[2] + content[3] + content[4] + content[5]
    
    # c - limpia el resultado
    elif event['pulse'][0] == 'c':
        clear = s3.put_object(Bucket='archivos-arqui2', Key='result.txt', Body="0000000000")
        return clear
    
    # Mostrar en display
    else:
        s3_show = s3.get_object(Bucket='archivos-arqui2', Key='result.txt')
        display = str(s3_show['Body'].read())
        time.sleep(1)
        return str(display[2] + display[3] + display[4] + display[5] + display[6] + display[7] + display[8] + display[9] + display[10] + display[11])
        

def convertToDec(binary):
    decimal = 0
    
    for position, digit in enumerate(binary[::-1]):
        decimal += int(digit) * 2 ** position
    
    return decimal
    
def convertToBin(decimal):
    if decimal == 0:
        return "11111100"
    if decimal == 1:
        return "01100000"
    if decimal == 2:
        return "11011010"
    if decimal == 3:
        return "11110010"
    if decimal == 4:
        return "01100110"
    if decimal == 5:
        return "10110110"
    if decimal == 6:
        return "10111110"
    if decimal == 7:
        return "11100000"
    if decimal == 8:
        return "11111110"
    if decimal == 9:
        return "11110110"
    if decimal == 10:
        return "11111101"
    if decimal == 11:
        return "01100001"
    if decimal == 12:
        return "11011011"
    if decimal == 13:
        return "11110011"
    if decimal == 14:
        return "01100111"
    if decimal == 15:
        return "10110111"