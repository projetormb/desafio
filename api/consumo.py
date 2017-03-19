# -*- coding: latin1 -*-


##############################################################################################
# verificar char set !!!!!!!!!!!!!!!!!
##############################################################################################
##############################################################################################

import json

from banco import Database
from flask import jsonify
from requests_oauthlib import OAuth1Session

def responseTwitter(screen_name, max_tweets):

    API_KEY = 'u9JQJ77IwU59dPM6RXYNo3HiR'
    API_SECRET = 'vGt9rsNMl4TPp7H3g5GIsCEpUE050MREopHDNI35Xf8FLm4neI'
    ACCESS_TOKEN = '42063631-gDtvbUX5BzfIyBfkpO7zSt9j0vCy11VU5ua8HR9I0'
    ACCESS_TOKEN_SECRET = 'M0ar8Yggt0OpE4zwjyTXPt2ctFM56pAmP0TTHbMFbeUOm'

    session = OAuth1Session(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='
    url += screen_name
    url += '&count='
    url += str(max_tweets)

    return session.get(url)

def consumoTwitter(screen_name, max_tweets):

    output_file = open('logs.txt', 'w')

    retorno = {}

    #response = session.get(url)

    output_file.write('chamar responseTwitter' + '\n\n')

    response = responseTwitter(screen_name, max_tweets)

    output_file.write('voltou responseTwitter' + '\n\n')
    output_file.write('---------------------------------------------------------------\n\n')


    ###############################################################################
    # MELHORAR
    # MELHORAR
    # MELHORAR
    # MELHORAR
    # MELHORAR
    ###############################################################################
    if response.status_code == 200:
        pass
    else:
        if response.status_code == 404:
            return retorno
        else:
            pass
    ###############################################################################


    tweets = json.loads(response.content)

    # registrando logs em um arquivo texto.


    #output_file.write('URL: ' + str(url) + '\n\n')
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

        #db = Database()

        output_file.close()
        output_file = open('logs.txt', 'a')

        for tweet in tweets:
            output_file.write('tweet: ' + str(tweet) + '\n\n')
        output_file.write('---------------------------------------------------------------\n\n')

        output_file.close()
        output_file = open('logs.txt', 'a')

        db = Database()

        index = -1

        for tweet in tweets:
            tweetText = tweet['text'].encode('utf8')

            index += 1
            retorno[index] = tweetText

            #tweetLatin = tweetText.decode('latin1')
            #db.Inserir('rmbertoni', tweetLatin)

            output_file.close()
            output_file = open('logs.txt', 'a')

            output_file.write('Texto de um tweet: ' + str(tweetText) + '\n')
            #output_file.write('tweetLatin: ' + str(tweetLatin.encode('utf8')) + '\n')

            output_file.close()
            output_file = open('logs.txt', 'a')
            output_file.write('inserir no DB: ' + str(tweetText) + '\n')
            output_file.close()
            output_file = open('logs.txt', 'a')

            ##############################################################################################
            # testar erro de caracteres como emotion icons !!!!!!!!!!!!!
            ##############################################################################################
            #db.Inserir(screen_name, tweetText)
            ##############################################################################################



            output_file.close()
            output_file = open('logs.txt', 'a')
            output_file.write('feito \n')


        output_file.write('---------------------------------------------------------------\n\n')

    """
    output_file.close()
    output_file = open('logs.txt', 'a')
    output_file.write('vai retornar o jsonify \n')
    output_file.write('retorno: ')
    output_file.write(str(retorno))
    output_file.write('\n')
    output_file.write('ate aqui ok: ')
    output_file.write('\n')
    """

    output_file.close()

    if len(retorno) == 0:
        retorno[0] = 'Nenhum tweet'


    return retorno
    #return jsonify(retorno)
