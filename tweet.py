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

# Function to send the tweet
def tweet_countdown():
    today = date.today()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    release_date = date(2025, 8, 9)
    # Only tweet if today is before the release date
    if today <= release_date:
        days_left = (release_date - today).days
        tweet = f"JAI BABU {timestamp}"
        #tweet = f"{days_left} days left until the release!"
        client.create_tweet(text=tweet)
        print("Tweeted:", tweet)
    else:
        print("No more tweets. The release date has passed.")

# Call the function
tweet_countdown()

# Path to the image on your device
#image_path = 'path_to_your_image.jpg'

# Post the tweet with the image
#pi.update_status_with_media(status=tweet, filename=image_path)