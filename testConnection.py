import requests
from config import MASTODON_TOKEN
# hka-API credetials
hkaUrl = 'https://www.iwi.h-ka.de/iwii/REST/newsbulletinboard/INFM'
hkaHeaders = { 'accept': 'application/json' }

# Mastodon credetials
url = 'https://projekt-mastodon.h-ka-iwi.de/api/v1/statuses'
auth = {'Authorization': 'Bearer ' + MASTODON_TOKEN}


response = requests.get(hkaUrl, headers=hkaHeaders)
print(response)

response = requests.post(url, headers=auth, data={'status': 'Hello World'})
print(response)