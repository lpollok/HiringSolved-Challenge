import json
import requests


url = 'https://challenge.hiringsolved.com/038FD8'
name = 'First Last'
email = 'name@example.com'
phone = '6025555555'
twitter = 'https://twitter.com/example'

final_url = '&'.join([
    url,
    'hirable=true',
    'name=' + name,
    'email=' + email,
    'phone=' + phone,
    'twitter=' + twitter])

response = requests.post(url, data=json.dumps(payload))
print(response)
print(response.text)
