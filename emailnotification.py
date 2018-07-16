# %load twitanalysis.py
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
import time
from urllib.error import HTTPError
from requests.exceptions import Timeout, ConnectionError
from requests.packages.urllib3.exceptions import ReadTimeoutError
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#consumer key, consumer secret, access token, access secret.
ckey = "0pYJ3OpXCgXLqZvOfkL6DmOLx"
csecret = "zHKospQ4tyDk3B0wgJRvIOAvqSdwrshFrndT2RVxHmdUXXGudn"
atoken = "736849652-l5MrQ6QwFqdrPZZHeHUfKSxvuszs601M7xND1Ezz"
asecret = "xXgmQBFZZnk7Apt8CNuAXecjWgYnoaR8VqjeKVycSuAUd"

#from twitterapistuff import *

class listener(StreamListener):
    def notify(self, data):
        try:
            fromaddr = "collinsbunde@gmail.com"
            toaddr = "collinsbunde@yahoo.com"

            msg = MIMEMultipart()

            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "ATTACHMENT"

            body = str(data)
            
            filename = "twitter-out.txt"
            attachment = open(filename, "rb")

            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            msg.attach(part)

            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "MULEcob1494")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
         
        except:
            return 
            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)
    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(tweet, sentiment_value, confidence )
                output.write('\n')
                output.close()
                
                TweetSend = 'Tweet: ' + tweet + '\n'
                Svalue = 'Negative Comment\n'
                
                info = [TweetSend,Svalue, confidence]
            
                return
                time.sleep(20)

            return True
        except (Timeout, ReadTimeoutError, ConnectionError) as exc:
            time.sleep(15)
            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["safaricom"])
