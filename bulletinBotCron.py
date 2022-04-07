#!/usr/bin/python3
from ctypes import resize
from multiprocessing.spawn import old_main_modules
import os
from urllib import response
import requests
import time
from datetime import datetime, timedelta
import os

# import token from config.py
from config import MASTODON_TOKEN

### Mastodon BOT to post content from newsbulletinboard from Hochschule Karlsruhe on projekt-mastodon.h-ka-iwi.de ###
### Author: Henrik Wiegand

##SETUP##
# sudo systemctl stop bulletinBot.service
# sudo systemctl daemon-reload
# sudo systemctl start bulletinBot.service
##CHECK STATUS##
# sudo systemctl status bulletinBot.service
# --> Active: active (running)

SLEEPTIME = 5
AUTHTOKEN_MASTODON = MASTODON_TOKEN
LOGFILE = 'botLog.txt'


logfile = open(LOGFILE, 'a')
logfile.write("Hello World")
logfile.close()


# Servertimezone = UTC
# Sommerzeit = 2
# Winterzeit = 1
TimeZoneDelta = 2

statusMessage = ''

# define Timeformat to fit with the mastodon request
timeFormat = "%Y-%m-%d %H:%M:%S.%f"

# hka-API credetials
hkaUrl = 'https://www.iwi.h-ka.de/iwii/REST/newsbulletinboard/INFM'
hkaHeaders = { 'accept': 'application/json' }

# Mastodon credetials
url = 'https://projekt-mastodon.h-ka-iwi.de/api/v1/statuses'
auth = {'Authorization': 'Bearer ' + AUTHTOKEN_MASTODON}


def shorten(text):
    text = (text[:700] + '... (Der Text wurde hier gekürzt)') if len(text) > 700 else text
    return text

# Delete LOGFILE after approx. one Day
# Deletes if its size is bigger than SLEEPTIME * Min * Hour * sizeAfterOneRun
def resetLogFile(LOGFILE):
    file = open(LOGFILE, 'a')
    file_size = os.path.getsize(LOGFILE)

    if file_size > SLEEPTIME*60*24*1020:
        print('Delete', file_size)
        file.close()
        os.remove(LOGFILE)
    else:
        print(file_size)
        file.close()

# Welcome Message for NuwsBulletinBot
print('Starting NewsBulletinBOT!!!\n\n\n')

# Main Bot-Loop
# define Systemtime
systemTime = datetime.now() + timedelta(hours=TimeZoneDelta)

# get request from hka API for news
response = requests.get(hkaUrl, headers=hkaHeaders)
news = response.json()
    


for docs in news:

    # open file for Logs
    # serverpath(root): ~/botLog.txt
    logfile = open(LOGFILE, 'a')

    # empty out the hashtags for the next entry
    hashtags = ''

    # compare Timestamps and log result - optional for debugging
    logfile.write('\nSystemTimestamp: ' + str(systemTime) +'\nPostTimestamp: ' + docs['publicationTimestamp'] + '\nTitle: ' + docs['title'] + '\n')
    logfile.write('Compare to systime - 5min: ' + str(datetime.strptime(docs['publicationTimestamp'], timeFormat) > (systemTime - timedelta(minutes=SLEEPTIME)))+'\n')
        
    # compare Timestamps and print result - optional for debugging
    print(datetime.strptime(docs['publicationTimestamp'], timeFormat) > (systemTime - timedelta(minutes=SLEEPTIME)),'\n')
    print(datetime.strptime(docs['publicationTimestamp'], timeFormat), '>', (systemTime - timedelta(minutes=SLEEPTIME)),'\n')
        
    # look for posts that are not older than SLEEPTIME minutes
    # to ensure not to post old posts witch might be already posted we compare the time of the posts and look if the news are max SLEEPTIME minutes old
    if datetime.strptime(docs['publicationTimestamp'], timeFormat) > (systemTime - timedelta(minutes=SLEEPTIME)):

        # get hashtags for course and combine them
        for course in docs['courseOfStudies']:
            hashtags += '#' + course + ','
        
        # concatinate post content with shorted postContend and hashtags
        statusMessage = docs['title'] + '\n' + docs['subTitle'] + '\n' + shorten(docs['content']) + '\nLG ' + docs['nameOwner'] + '\n' + hashtags + '\n' + '#' + docs['type']
        
        # log the status message
        logfile.write(statusMessage + '\n')
        # print(statusMessage)

        # Toot the statusMessage on mastodon
        response = requests.post(url, data={'status': statusMessage}, headers=auth)

        # log the response of the Toot-request --> should be 200(OK)
        logfile.write(response + '\n')
        
        
    else:
        # concatinate logmessage with post-id and timestamp 
        oldFileMessage = 'OLD POST DETECTED: PostID: ' + str(docs['id']) + ' with Timestamp ' + docs['publicationTimestamp']
        logfile.write(oldFileMessage + '\n')
        
    # cleanup and close logfile
    logfile.close()

# sleep x min --> defined in SLEEPTIME
# time.sleep(SLEEPTIME*60)

# delete LOGFILE if its to large --> aprox. after one day
resetLogFile(LOGFILE)