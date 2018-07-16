import time
import sqlite3
import time
import urllib.request, urllib.parse, urllib.error
import zlib
import string

conn = sqlite3.connect('smm_sentiproject.sqlite')
conn.text_factory = str
cur = conn.cursor()

cur.execute('SELECT id, username FROM safaricom WHERE username LIKE "%safaricom%"')
subjects = []
for message_row in cur :
        print (message_row[1])
    
