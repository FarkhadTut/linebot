import requests
import json

data = {'name': 'Fara',
        'surname': 'Tutkabaev'}


r = requests.post('http://127.0.0.1:5000/webhook', data=json.dumps(data), headers={'Content-Type': 'application/json'})