import requests

url = 'https://api.agify.io?name=seungwon'

response = requests.get(url).json()

print(response)