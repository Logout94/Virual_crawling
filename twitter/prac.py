import tweepy
import json

TWEET = 'Hello twitter!'

def jsonLoad(path):
    json_file = open(path)
    project_info = json.load(json_file)
    return project_info

token = jsonLoad('key_token.json')
api_key = token['API']['key']
api_secret = token['API']['secret']
access_token = token['Token']['key']
access_token_secret = token['Token']['secret']

auth = tweepy.OAuth1UserHandler(consumer_key=api_key, consumer_secret=api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(status=TWEET)