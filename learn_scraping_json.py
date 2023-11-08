import requests
import json
from bs4 import BeautifulSoup

url = 'https://glomark.lk/coconut/p/11624'

result = requests.get(url)

soup = BeautifulSoup(result.text, 'html.parser')

script = soup.find('script', {'type': 'application/ld+json'})

jsonl1 = json.loads(script.text)

price = jsonl1['offers'][0]['price']
name = jsonl1['name']

print(name)