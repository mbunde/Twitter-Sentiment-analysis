import time
import sqlite3
import time
import urllib.request, urllib.parse, urllib.error
import zlib
import string

conn = sqlite3.connect('smm_sentiproject.sqlite')
conn.text_factory = str
cur = conn.cursor()

cur.execute('SELECT id,username,tweet, sentimentvalue,confidence FROM safaricom WHERE   confidence >0.8 LIMIT 100')
subjects = []
for message_row in cur :
        print (message_row)
    
