import requests
import json
response = requests.get('http://universities.hipolabs.com/search?country=United+States&name=Iowa')

print(json.dumps(response.json(), sort_keys=True, indent=4))



