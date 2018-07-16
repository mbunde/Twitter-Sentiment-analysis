import sqlite3
import time
import urllib.request, urllib.parse, urllib.error
import zlib

conn = sqlite3.connect('sentiment_project.sqlite')
conn.text_factory = str
cur = conn.cursor()


cur.execute('SELECT id,time,username,tweet,sentimentvalue,confidence FROM safaricom')
messages = dict()
for message_row in cur :
    messages[message_row[0]] = (message_row[1],message_row[2],message_row[3],message_row[4],message_row[5])
print("Loaded messages=",len(messages))
for key in messages:
    print (key, messages[key])
  
##mentions = dict()
#for (message_id, message) in list(messages.items()):
  #  score = message[5]
 #   tweeps =message[2]
 #   if score <= 0.8: continue
 #   polarity[score] = polarity.get(score,0)+ 1
    
        

#pick the top polarty
#senti_score = sorted(polarity,key=polarity.get, reverse =True)
#senti_score =senti_score[:10]
#print("higher polarity score")
#print(senti_score)
