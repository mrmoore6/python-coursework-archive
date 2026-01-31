import requests
import json

response = requests.get('http://api.open-notify.org/iss-now.json')

print(response.json())

response2 = requests.get('http://api.open-notify.org/astros.json')

print(response2.json())

response3 = requests.get('http://api.open-notify.org/iss-pass.json?lat=41.7318&lon=93.6001&n=5')

print(response3.json())

