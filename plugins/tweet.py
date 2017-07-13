import tweepy
import time
import json
import slackbot_settings
from key import twkey
from twlist import twlist
from slacker import Slacker

def lookup():
    user_timeline= api.user_timeline(k)
    diff_tweet(user_timeline[0].id_str)

def diff_tweet(tweet_id):
    if tweeted[count1][count2] != tweet_id:
        tweet = "https://twitter.com/" + k + "/status/" + tweet_id
        slack.chat.post_message(fjson[str(count1)]["channel_name"],tweet)
        print(tweet)
        tweeted[count1][count2] = tweet_id


tweeted = [[0 for j in range(100)] for k in range(100)]

auth = twkey.twitter_api()
api = tweepy.API(auth)
slack = Slacker(slackbot_settings.API_TOKEN)

f = open("./twlist/twlist.json" , "r")
fjson = json.load(f)

arr = [[0 for j in range(100)] for k in range(100)]

import slackbot_settings
count1 = 0
count2 = 0
while 1:
    for i in fjson:
        for k in fjson[str(count1)]["user"]:
            count2 += 1
            lookup()
        count2 = 0
        count1 += 1
    count1 = 0
    time.sleep(3)
