import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():
    
    # Type the API key and secret token from Twitter API.
    access_key = ""
    access_secret = ""
    consumer_key = ""
    consumer_secret = ""

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # Creating an API object
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name='@elonmusk',
                               # 200 is the maximum allowed count
                               count=200,
                               # Include re-tweets
                               include_rts=False,
                               # Necessary to keep full text.
                               # Otherwise only first 140 words is extracted.
                               tweet_mode='extended'
                               )

    list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"User": tweet.user.screen_name,
                         'Text': text,
                         'Favorite_Count': tweet.favorite_count,
                         'Retweet_Count': tweet.retweet_count,
                         'Created_At': tweet.created_at}
        list.append(refined_tweet)

    df = pd.DataFrame(list)
    df.to_csv("s3://Type your Bucket Name/tweets.csv")
