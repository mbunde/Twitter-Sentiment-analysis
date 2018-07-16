import time
import pymysql
import time
import urllib.request, urllib.parse, urllib.error
import zlib
import string

conn = pymysql.connect("localhost","root","","sentitwit", charset = 'utf8mb4')
conn.text_factory = str
cur = conn.cursor()

cur.execute('SELECT time, username FROM safaricom')
subjects = dict()
for message_row in cur :
    subjects[message_row[0]] = message_row[1]
# print (message_row)
    
# cur.execute('SELECT time,username, tweet, FROM sentitwit')
cur.execute('SELECT time FROM safaricom')
counts = dict()
for message_row in cur :
    text = subjects[message_row[0]]
    text = text.translate(None, string.punctuation)
    text = text.translate(None, '1234567890')
    text = text.strip()
    text = text.lower()
    words = text.split()
    for word in words:
        if len(word) < 4 : continue
        counts[word] = counts.get(word,0) + 1
        print(counts[word])
