#!/usr/bin/python3

import requests
import json
import logging

url = 'https://official-joke-api.appspot.com/random_joke'

response = requests.get(url)
response = json.loads(response.text)

id = response['id']
type = response['type']
setup = response ['setup']
punch = response['punchline']

print(setup, punch)

