import json

def lambda_handler(event, context):
    if event['pulse'] == '1':
        return '1101100'