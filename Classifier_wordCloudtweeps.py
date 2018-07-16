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
    text = text.translate(string.punctuation)
    text = text.translate('1234567890')
    text = text.strip()
    text = text.lower()
    words = text.split()
    for word in words:
        if len(word) < 4 : continue
        counts[word] = counts.get(word,0) + 1
        print(counts[word])
        
x = sorted(counts, key=counts.get, reverse=True)
highest = None
lowest = None
for k in x[:100]:
    if highest is None or highest < counts[k] :
        highest = counts[k]
    if lowest is None or lowest > counts[k] :
        lowest = counts[k]
print('Range of counts:',highest,lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('gword.js','w')
fhand.write("gword = [")
first = True
for k in x[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")

print("Output written to gword.js")
