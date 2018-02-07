import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys
import re
import codecs
import http.client as httplib, urllib
import charts
from pprint import pprint

print("charts.py imported")

# accessKey = '18a3308199b1444598f9cad6929cb058'
accessKey = 'a0c9d2e00b634d9d81b5840208d565dd'

uri = 'eastus2.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

def GetSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

consumer_key = '7uOb6nd14A5yL6q8Bv9CALrI9'
consumer_secret = 'nP3xLlxmQ1hUBcaDLYMrEt7p8Zv91e4240afxGojqNoKQGnP65'
access_token = '3144537862-Sl9coCTeUcDSpiXnbhn3IbrncTIVR1BFIu3VPzq'
access_secret = 'y8hGsP9sAtCsVLZO0nBIjT9uRSusLJqXOFvQGeUYJmnkB'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweetsWanted=1000

count=100
# theme='#fuerzamexico'
# query=[f'🤚 OR 🤛 OR 🤜 OR 🤝 OR 🤞 OR 🤤 OR 🤥 OR 🤠 OR 🤡 OR 🤢 OR 🙁 OR 🙂 OR 🙃 OR 🙄 OR 🤣 OR 😀 OR 😃 OR 😄 OR 😁 OR 😂 {theme}',f'😅 OR 🤧 OR 😆 OR 😇 OR 😈 OR 👿 OR 😉 OR 😊 OR 😋 OR 😌 OR 😍 OR 😎 OR 😏 OR 😐 OR 😑 OR 😒 OR 😓 OR 😔 OR 😕 OR 😖 {theme}',f'😗 OR 😘 OR 😙 OR 😚 OR 😛 OR 😜 OR 😝 OR 😞 OR 😟 OR 😠 OR 😡 OR 😢 OR 😣 OR 😤 OR 😥 OR 😦 OR 😧 OR 😨 OR 😩 OR 😪 {theme}',f'😫 OR 😬 OR 😭 OR 😮 OR 😯 OR 😰 OR 😱 OR 😲 OR 😳 OR 😴 OR 😵 OR 😶 OR 😷 OR 👆 OR 👇 OR 👈 OR 👉 OR 👊 OR 👌 OR 👍 {theme}', f"👎 OR 🖐 OR 🖖 OR 🤐 OR 🤑 OR 🤒 OR 🤓 OR 🤔 OR 🤕 OR 🤗 OR 🤘 OR 💩 OR 👺 OR 👹 OR ☝ OR 🙏 OR ✊ OR 🤐 {theme}"]
# print(len(query))


# query1='from:MKBHD'
query1='#iphone'
# query1='🤚 OR 🤛 OR 🤜 OR 🤝 OR 🤞 OR 🤤 OR 🤥 OR 🤠 OR 🤡 OR 🤢 OR 🙁 OR 🙂 OR 🙃 OR 🙄 OR 🤣 OR 😀 OR 😃 OR 😄 OR 😁 OR 😂 OR 😅 OR 🤧 OR 😆 OR 😇 OR 😈 OR 👿 OR 😉 OR 😊 OR 😋 OR 😌 OR 😍 OR 😎 OR 😏 OR 😐 OR 😑 OR 😒 OR 😓 OR 😔 OR 😕 OR 😖 OR 😗 OR 😘 OR 😙 OR 😚 OR 😛 OR 😜 OR 😝 OR 😞 OR 😟 OR 😠 OR 😡 OR 😢 OR 😣 OR 😤 OR 😥 OR 😦 OR 😧 OR 😨 OR 😩 OR 😪 OR 😫 OR 😬 OR 😭 OR 😮 OR 😯 OR 😰 OR 😱 OR 😲 OR 😳 OR 😴 OR 😵 OR 😶 OR 😷 OR 👆 OR 👇 OR 👈 OR 👉 OR 👊 OR 👌 OR 👍 OR 👎 OR 🖐 OR 🖖 OR 🤐 OR 🤑 OR 🤒 OR 🤓 OR 🤔 OR 🤕 OR 🤗 OR 🤘 OR 💩 OR 👺 OR 👹 OR ☝ OR 🙏 OR ✊ OR 🤐 #love'
# query1='🤚 OR 🤛 OR 🤜 OR 🤝 OR 🤞 OR 🤤 OR 🤥 OR 🤠 OR 🤡 OR 🤢 OR 🙁 OR 🙂 OR 🙃 OR 🙄 OR 🤣 OR 😀 OR 😃 OR 😄 OR 😁 OR 😂 #feliz'
# query2='😅 OR 🤧 OR 😆 OR 😇 OR 😈 OR 👿 OR 😉 OR 😊 OR 😋 OR 😌 OR 😍 OR 😎 OR 😏 OR 😐 OR 😑 OR 😒 OR 😓 OR 😔 OR 😕 OR 😖 #feliz'
# query3='😗 OR 😘 OR 😙 OR 😚 OR 😛 OR 😜 OR 😝 OR 😞 OR 😟 OR 😠 OR 😡 OR 😢 OR 😣 OR 😤 OR 😥 OR 😦 OR 😧 OR 😨 OR 😩 OR 😪 #feliz'
# query4='😫 OR 😬 OR 😭 OR 😮 OR 😯 OR 😰 OR 😱 OR 😲 OR 😳 OR 😴 OR 😵 OR 😶 OR 😷 OR 👆 OR 👇 OR 👈 OR 👉 OR 👊 OR 👌 OR 👍 #feliz'
# query5='👎 OR 🖐 OR 🖖 OR 🤐 OR 🤑 OR 🤒 OR 🤓 OR 🤔 OR 🤕 OR 🤗 OR 🤘 OR 💩 OR 👺 OR 👹 OR ☝ OR 🙏 OR ✊ OR 🤐 #feliz'

# for i in range(5):
#     print(query[i])

#EMOJI DICTIONARY CREATE
emojis = {}
with open("emojiEmotion.txt") as f:
    for line in f:
       (key, vig,ext,adm,terr,asom,dol,aborr,fur,polaridad,certainty) = line.split()
       emojis[key] = [float(polaridad),float(certainty)]

# print(str(emojis['U+1F921']))
f.close()

#TWEET CRAWL
# file = codecs.open("tweetabase.json", "w", "utf-8")
file=open("tweetabase.json","w")
fileSentiment=open("tweetsentiments.json","w")
# file.write(u"\ufeff")
fileOut= open("outE.txt","w")
fileIdk= open("outIdk.txt","w")

searched_tweets = []
found_emojis={}
found_class={}
final_emojis={}
final_texts={}
# tweet_ids=[] IDSHIT
max_tweets=tweetsWanted
last_id = -1
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)%max_tweets
    try:
        new_tweets = api.search(q=query1,lang='es', count=count, max_id=str(last_id - 1), tweet_mode="extended")
        if not new_tweets:
            break
        for tweet in new_tweets:
            searched_tweets.append(tweet)
            last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        print('exception raised, waiting 15 minutes')
        print('(until:', dt.datetime.now()+dt.timedelta(minutes=15), ')')
        time.sleep(15*60)
print('Tweet search count')
print(len(searched_tweets))

#IN CASE YOU WANT TO FILTER BY EMOJIS
# max_tweets=tweetsWanted/5
# for i in range(5):
#     last_id = -1
#     while len(searched_tweets)-max_tweets*i < max_tweets:
#         count = max_tweets - len(searched_tweets)%max_tweets
#         try:
#             new_tweets = api.search(q=query[i], count=count, max_id=str(last_id - 1), tweet_mode="extended")
#             if not new_tweets:
#                 break
#             for tweet in new_tweets:
#                 searched_tweets.append(tweet)
#                 # tweet_ids.append(str(tweet.id)) IDSHIT
#                 last_id = new_tweets[-1].id
#         except tweepy.TweepError as e:
#             print('exception raised, waiting 15 minutes')
#             print('(until:', dt.datetime.now()+dt.timedelta(minutes=15), ')')
#             time.sleep(15*60)
#     print('done with one loop')
#     print(len(searched_tweets))


#TWEET CLEAN, SAVE
c=1
file.write('{\n"documents": [')
for tweet in searched_tweets:
    pol=0
    fileIdk.write("Tweet "+str(c)+": "+tweet.full_text+"\n")
    # save=re.sub(r'(http|https|ftp)://[a-zA-Z0-9\\./]+','',tweet.full_text)
    # save=re.sub(r'(.)\1{2,}','',re.sub(r'(http|https|ftp)://[a-zA-Z0-9\\./]+','',tweet.text))
    fileOut.write("Tweet "+str(c)+": ")
    save=re.sub("\u201d",'"',re.sub(r'\u2019','',re.sub(r'@(\w+)','',re.sub(r'(http|https|ftp)://[a-zA-Z0-9\\./]+','',tweet.full_text))))
    save=re.sub("RT : ","",save)
    save=re.sub("#","",save)
    save=re.sub(r'(.)\1{2,}','',save)
    # emojs=re.findall(r'(🤚|🤛|🤜|🤝|🤞|🤤|🤥|🤠|🤡|🤢|🙁|🙂|🙃|🙄|🤣|😀|😃|😄|😁|😂|😅|🤧|😆|😇|😈|👿|😉|😊|😋|😌|😍|😎|😏|😐|😑|😒|😓|😔|😕|😖|😗|😘|😙|😚|😛|😜|😝|😞|😟|😠|😡|😢|😣|😤|😥|😦|😧|😨|😩|😪|😫|😬|😭|😮|😯|😰|😱|😲|😳|😴|😵|😶|😷|👆|👇|👈|👉|👊|👌|👍|👎|🖐|🖖|🤐|🤑|🤒|🤓|🤔|🤕|🤗|🤘|💩|👺|👹|☝|🙏|✊|🤐)',save)
    emojs=re.findall(r'(😀|😃|😄|😁|😆|😅|😂|🤣|☺|😊|😇|🙂|🙃|😉|😌|😍|😘|😗|😙|😚|😋|😜|😝|😛|🤑|🤗|🤓|😎|🤡|🤠|😏|😒|😞|😔|😟|😕|🙁|🙁|😣|😖|😫|😩|😤|😠|😡|😶|😐|😑|😯|😦|😧|😮|😲|😵|😳|😱|😨|😰|😢|😥|🤤|😭|😓|😪|😴|🙄|🤔|🤥|😬|🤐|🤢|🤧|😷|🤒|🤕|😈|👿|👹|👺|💩|🙏|🤝|👍|👎|👊|✊|🤛|🤜|🤞|✌|🤘|👌|👈|👉|👆|👇|☝|✋|🤚|🖐)',save)
    for e in emojs:
        if e in {'👿','😤','😠','😡'}:
            if 'Enojo' in found_class:
                found_class['Enojo']=found_class['Enojo']+1
            else:
                found_class['Enojo']=1
        elif e in {'🤗','😍','😘','😗','😙','😚'}:
            if 'Afecto' in found_class:
                found_class['Afecto']=found_class['Afecto']+1
            else:
                found_class['Afecto']=1
        elif e in {'😀','😃','😄','😁','😆','😅','😂','🤣','☺','😊','😇','🙂','😬'}:
            if 'Felicidad' in found_class:
                found_class['Felicidad']=found_class['Felicidad']+1
            else:
                found_class['Felicidad']=1
        elif e in {'😒','🙄'}:
            if 'Molestia' in found_class:
                found_class['Molestia']=found_class['Molestia']+1
            else:
                found_class['Molestia']=1
        elif e in {'😌','🤤','😴'}:
            if 'Alivio' in found_class:
                found_class['Alivio']=found_class['Alivio']+1
            else:
                found_class['Alivio']=1
        elif e in {'😢','😥','😞','😔','😭','😓','😪','😫','😩','😟','😕','🙁','🙁','🤥'}:
            if 'Tristeza' in found_class:
                found_class['Tristeza']=found_class['Tristeza']+1
            else:
                found_class['Tristeza']=1
        elif e in {'🤐','😐','😑','🙃','😶','🤔'}:
            if 'Neutro' in found_class:
                found_class['Neutro']=found_class['Neutro']+1
            else:
                found_class['Neutro']=1
        elif e in {'😯','😦','😧','😮','😲','😵','😳','😱','😨','😰'}:
            if 'Sorpresa' in found_class:
                found_class['Sorpresa']=found_class['Sorpresa']+1
            else:
                found_class['Sorpresa']=1
        elif e in {'🤢','🤧','😷','🤒','🤕','😣','😖'}:
            if 'Enfermo' in found_class:
                found_class['Enfermo']=found_class['Enfermo']+1
            else:
                found_class['Enfermo']=1
        elif e in {'😉','😛','🤑','🤓','😎','🤡','🤠','😋','😜','😝','😏','😈','💩','👹','👺'}:
            if 'Broma' in found_class:
                found_class['Broma']=found_class['Broma']+1
            else:
                found_class['Broma']=1
        if e in found_emojis:
            found_emojis[e]=found_emojis[e]+1
        else:
            found_emojis[e]=1
        pol=pol+((emojis[str(e)][0]-0.5)*emojis[str(e)][1])+0.5
        fileOut.write(e)

    if len(emojs)==0:
        final_emojis[c-1]=11111111111
    else:
        final_emojis[c-1]=pol/len(emojs)

    fileOut.write(" "+str(final_emojis[c-1])+" de polaridad\n")
    # fileOut.write(" "+str(final_emojis[c])+" de polaridad where "+str(pol)+"=pol and "+str(len(emojs))+"=len\n")
    output = {"id":c,"language": "es","text": save.lower()}
    json.dump(output, file)
    if c!=max_tweets:
        file.write(",\n")
    c=c+1
    # json.dump(,,file)

filehist=open("outHistogram.txt","w")
for a in found_emojis.keys():
    filehist.write(a+":")
    for i in range(found_emojis[a]):
        filehist.write("█ ")
    filehist.write("\n")

fileClass=open("outClassHistogram.txt",'w')
for a in found_class.keys():
    fileClass.write(a+":\b")
    for i in range(found_class[a]):
        fileClass.write("█ ")
    fileClass.write("\n")

file.write('\n]\n}')
file.close()

with open('tweetabase.json') as data_file:
    documents = json.load(data_file)


print ('Please wait a moment for the results to appear.\n')

result = json.loads(GetSentiment (documents))
# print (json.dump(json.loads(result), fileSentiment))

filetxtsent=open('outS.txt','w')
for i in range (max_tweets):
 final_texts[i]=result['documents'][i]['score']
 filetxtsent.write("Tweet "+str(i+1)+": "+str(final_texts[i])+" de polaridad en el texto\n")

filefinl=open('outFinal.txt','w')
finalval=[[] for i in range(max_tweets)]
for i in range (max_tweets):
    if final_emojis[i]==11111111111:
        finalval[i]=final_texts[i]
    else:
        finalval[i]=(final_texts[i]+final_emojis[i])/2
    filefinl.write("Tweet "+str(i+1)+": "+str(finalval[i])+" of Polarity\n")

#HISTOGRAM SHIT
charts.createHistogram(found_emojis)
