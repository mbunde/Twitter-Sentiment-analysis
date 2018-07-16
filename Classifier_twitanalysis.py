from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
import time
from urllib.error import HTTPError
from requests.exceptions import Timeout, ConnectionError
from requests.packages.urllib3.exceptions import ReadTimeoutError

#consumer key, consumer secret, access token, access secret.
ckey = "0pYJ3OpXCgXLqZvOfkL6DmOLx"
csecret = "zHKospQ4tyDk3B0wgJRvIOAvqSdwrshFrndT2RVxHmdUXXGudn"
atoken = "736849652-l5MrQ6QwFqdrPZZHeHUfKSxvuszs601M7xND1Ezz"
asecret = "xXgmQBFZZnk7Apt8CNuAXecjWgYnoaR8VqjeKVycSuAUd"

#from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except (Timeout, ReadTimeoutError, ConnectionError) as exc:
            time.sleep(10)
            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["safaricom"])
