import time
import sqlite3
import time
import urllib.request, urllib.parse, urllib.error
import zlib
import string

conn = sqlite3.connect('smm_sentiproject.sqlite')
conn.text_factory = str
cur = conn.cursor()

#OPEN LETTER CONTROVERSY
cur.execute('SELECT id,username,tweet FROM safaricom WHERE tweet LIKE "%OPEN LETTER%"')
subjects = []
for message_row in cur :
        print (message_row)
    
