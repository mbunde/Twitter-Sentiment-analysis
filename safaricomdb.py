# %load savingToDB.py
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pymysql
import time
import json
import sentiment_mod as s
import time
from urllib.error import HTTPError
from requests.exceptions import Timeout, ConnectionError
from requests.packages.urllib3.exceptions import ReadTimeoutError



#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
conn = pymysql.connect("localhost","root","","smm_sentiproject", charset = 'utf8mb4')

c = conn.cursor()


#consumer key, consumer secret, access token, access secret.
ckey="P6kMnErRqCVqKpcYbOkLo5xLm"
csecret="km5IAnW06Nj2nxLseW1MXlB57faVOddkWLodC7TcvDviDv1v5c"
atoken="736849652-q4trxnc3TBXQcnySO9vSCVDV2DYYrwVeR7HHgxVy"
asecret="2yPbePhIKm09rwOiAlsNsiJeA6bR1xwQT7JnZNcJghH0y"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        
        username = all_data["user"]["screen_name"]
        
        sentimentvalue, confidence = s.sentiment(tweet)
        
        #"INSERT INTO mediciones_historial(column1,column2,column3) VALUES({0},{1},{2})".format(sensor, data, data_type)
        
        c.execute("INSERT INTO safaricom (time,username,tweet,sentimentvalue,confidence) VALUES (%s,\"%s\",\"%s\",\"%s\",%s)",
            (time.time(),username,tweet,sentimentvalue,confidence))

        conn.commit()

        print((username,tweet,sentimentvalue,confidence))
        time.sleep(15)
        
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["safaricom"])

