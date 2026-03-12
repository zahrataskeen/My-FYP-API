import requests
import json

url = "http://209.20.159.228:9000/" # Your API URL

headers = {
    'Content-Type': 'application/json'
}

data = {
    'input': 'Input text' # Your input string
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Response Status Code: ", response.status_code)
print("Response Content: ", response.json())