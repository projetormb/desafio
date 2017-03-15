# -*- coding: latin1 -*-

import json
import requests.utils

from banco import Database

from requests_oauthlib import OAuth1Session


API_KEY = 'u9JQJ77IwU59dPM6RXYNo3HiR'
API_SECRET = 'vGt9rsNMl4TPp7H3g5GIsCEpUE050MREopHDNI35Xf8FLm4neI'
ACCESS_TOKEN = '42063631-gDtvbUX5BzfIyBfkpO7zSt9j0vCy11VU5ua8HR9I0'
ACCESS_TOKEN_SECRET = 'M0ar8Yggt0OpE4zwjyTXPt2ctFM56pAmP0TTHbMFbeUOm'


DB_PWD = 'Desafio2017'

session = OAuth1Session(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)



url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=rmbertoni&count=5'

response = session.get(url)

tweets = json.loads(response.content)

# registrando logs em um arquivo texto.

output_file = open('logs.txt', 'w')

output_file.write('URL: ' + str(url) + '\n\n')
output_file.write('response.status_code: ' + str(response.status_code) + '\n\n')
output_file.write('---------------------------------------------------------------\n\n')

output_file.write('REST retornado (json format): \n\n')
output_file.write(str(tweets))
output_file.write('\n\n')
output_file.write('---------------------------------------------------------------\n\n')

# https://twitter.com/rmbertoni/with_replies
# Nesta URL é possível visualizar os tweets que a API está me retornando.

output_file.write('Quantidade tweets: ' + str(len(tweets)) + '\n\n')

if len(tweets) > 0:

    db = Database()

    for tweet in tweets:
        output_file.write('tweet: ' + str(tweet) + '\n\n')
    output_file.write('---------------------------------------------------------------\n\n')

    for tweet in tweets:
        tweetText = tweet['text'].encode('utf8')

        db.Inserir('rmbertoni', tweetText)


        tweetLatin = tweetText.encode('latin1')
        db.Inserir('rmbertoni', tweetLatin)

        output_file.write('Texto de um tweet: ' + str(tweetText) + '\n')
    output_file.write('---------------------------------------------------------------\n\n')

output_file.close()

