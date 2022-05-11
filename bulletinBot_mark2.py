from mastodon import Mastodon
from config import MASTODON_TOKEN, LOGFILE
from datetime import datetime, timedelta
import requests

LOGFILE += 'botLog.txt'

mastodon = Mastodon(
    access_token = MASTODON_TOKEN,
    api_base_url = 'https://projekt-mastodon.h-ka-iwi.de/'
)


# hka-API credetials
hkaUrl = 'https://www.iwi.h-ka.de/iwii/REST/newsbulletinboard/INFM'
hkaHeaders = { 'accept': 'application/json' }


# define Systemtime
# systemTime = datetime.now() + timedelta(hours=TimeZoneDelta)

# get request from hka API for news
response = requests.get(hkaUrl, headers=hkaHeaders)
news = response.json()
print(news)

logfile = open(LOGFILE, 'a')
# logfile.write("Hello World mark 2!")
logfile.close()
    


# print(mastodon.toot('Hello World mark2'))
message = '@admin Hello World mark2'
'''
toot = Mastodon.status_post(self=mastodon, 
    status=message, 
    in_reply_to_id=None, 
    media_ids=None, 
    sensitive=False, 
    visibility='direct', 
    spoiler_text=None, 
    language=None, 
    idempotency_key=None, 
    content_type=None, 
    scheduled_at=None, 
    poll=None, 
    quote_id=None)
print(toot)
id = toot['id']
print(id)
'''