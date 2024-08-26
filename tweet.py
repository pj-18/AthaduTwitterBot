import tweepy
import os
from datetime import date

bearer_token = os.getenv('BEARER_TOKEN')
api_key = os.getenv('API_KEY')
api_key_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client( bearer_token = bearer_token,
                    consumer_key = api_key,
                    consumer_secret = api_key_secret,
                    access_token = access_token,
                    access_token_secret = access_token_secret)

def tweet_countdown():
    today = date.today()
    releaseDate = date(2025, 8, 9)
    # Only tweet if today is before the release date
    if today <= releaseDate:
        daysLeft = (releaseDate - today).days - 1
        tweet = f"{daysLeft}"
        client.create_tweet(text=tweet)
        print("Tweeted:", tweet)
    else:
        print("No more tweets. The release date has passed.")

tweet_countdown()

#image_path = 'path_to_your_image.jpg'
#client.create_tweet(text=tweet, media_ids=[client.media_upload(image_path).media_id])