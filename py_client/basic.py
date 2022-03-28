import requests

endpoint = 'http://localhost:8000/api/'

sumn = requests.get(endpoint)

print(sumn.json())