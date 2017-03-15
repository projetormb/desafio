
import json
import requests.utils

from requests_oauthlib import OAuth1Session


API_KEY = 'u9JQJ77IwU59dPM6RXYNo3HiR'
API_SECRET = 'vGt9rsNMl4TPp7H3g5GIsCEpUE050MREopHDNI35Xf8FLm4neI'
ACCESS_TOKEN = '42063631-gDtvbUX5BzfIyBfkpO7zSt9j0vCy11VU5ua8HR9I0'
ACCESS_TOKEN_SECRET = 'M0ar8Yggt0OpE4zwjyTXPt2ctFM56pAmP0TTHbMFbeUOm'

session = OAuth1Session(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#response = session.get('https://api.twitter.com/1.1/search/tweets.json?q=%23python')
#print response.status_code
#print requests.utils.quote("#python")
#url = "https://api.twitter.com/1.1/search/tweets.json?q=%s"
#url = url % (requests.utils.quote("#python"))
#response = session.get(url)
#tweets = json.loads(response.content)

#print tweets.keys()
#print tweets['statuses'][0].keys()

#print '-----------------------'

output_file = open('logs.txt', 'w')


url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=rmbertoni&count=5'
output_file.write('URL: ' + str(url) + '\n\n')

response = session.get(url)
output_file.write('response.status_code: ' + str(response.status_code) + '\n\n')

tweets = json.loads(response.content)
output_file.write('len tweets: ' + str(len(tweets)) + '\n\n')

for t in tweets:
    output_file.write('t: ' + str(t) + '\n')

output_file.write('\n\n\n')
output_file.write('-------------------------------------')
output_file.write('\n\n\n')

output_file.write('content tweets: \n')
output_file.write(str(tweets))
output_file.write('\n\n\n')

output_file.close()

