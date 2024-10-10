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

#print(setup, punch)

logger = logging.getLogger(__name__)
logging.basicConfig(filename="joke.log", encoding="utf-8", level=logging.DEBUG)
logging.warning('%s:%s:%s', id, setup, punch)
