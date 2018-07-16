# %load gline.py
import sqlite3
import time
import urllib.request, urllib.parse, urllib.error
import zlib

conn = sqlite3.connect('sentiment_project.sqlite')
conn.text_factory = str
cur = conn.cursor()

cur.execute('SELECT id, username FROM safaricom')
users = dict()
for message_row in cur :
    users[message_row[0]] = message_row[1]
    

cur.execute('SELECT id, time,username,tweet,sentimentvalue, confidence FROM safaricom')
messages = dict()
for message_row in cur :
    messages[message_row[0]] = (message_row[1],message_row[2],message_row[3],message_row[4], message_row[5])

print("Loaded messages=",len(messages),"users=",len(users))
#print(messages)

mentions = dict()
for (message_id, message) in list(messages.items()):
    user = message[1]
    #print (user)
    screen_name = message[1].split(",")
    #print(screen_name[0])
    #if len(screen_name) != 2 : continue
    tweepname = screen_name[0] 
    #print(tweepname)
    
    mentions[tweepname] = mentions.get(tweepname, 0) + 1
    #print (mentions[tweepname])
             #pick top tweepers
tweeps = sorted(mentions, key=mentions.get, reverse=True)
tweeps = tweeps[:10]
#print("Top 10 tweeps")
#print (tweeps)

counts = dict()
confidence = list()
# cur.execute('SELECT id, guid,sender_id,subject_id,sent_at FROM Messages')
for (message_id, message) in list(messages.items()):
    user = message[1]
    screen_name = message[1].split(",")
    tweepname = screen_name[0]
    if tweepname not in tweeps: continue
    #print (tweepname)
    #if dns not in orgs : continue
    score = messages[4]
    if score not in confidence : confidence.append(score)
    key = (score, tweepname)
    counts[key] = counts.get(key,0) + 1
    
confidence.sort()
#print (counts)
#print (confidence)   

fhand = open('gline.js','w')
fhand.write("gline = [ ['Year'")
for tweep in tweeps:
    fhand.write(",'"+tweep+"'")
fhand.write("]")

for score in confidence:
    fhand.write(",\n['"+str(score)+"'")
    for tweep in tweeps:
        key = (score, tweep)
        val = counts.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]");

fhand.write("\n];\n")

print("Output written to gline.js")

