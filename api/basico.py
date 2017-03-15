 from requests_oauthlib import OAuth1Session
>>> session = OAuth1Session(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


response = session.get('https://api.twitter.com/1.1/search/tweets.json?q=%23python')
>>> print response.status_code



print requests.utils.quote("#python")
%23python
>>> url = "https://api.twitter.com/1.1/search/tweets.json?q=%s"
>>> url = url % (requests.utils.quote("#python"))
>>> response = session.get(url)


import json
>>> tweets = json.loads(response.content)




print tweets.keys()

print tweets['statuses'][0].keys()