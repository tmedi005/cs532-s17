import tweepy
from tweepy import OAuthHandler
import time

# Authentication details. To  obtain these visit dev.twitter.com
access_token = "952384183-cwYOb7LYBHqVkYnclU39pHNRUe0Hn9nPpbX7aJ6R"
access_token_secret = "BcnkVt1PWuE0d0Uw9itqcts4gE7FTX9P7EkdLqEACZTJK"
consumer_key = "l1tsh3QrpT8uuteksvDLtDSM5"
consumer_secret = "GmAR39QA135i7UNiTDOpuaQEW3MapTqfwl3BaGzVlHWCrAt1Rj"

if __name__ == '__main__':
    # Create authentication token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    data = api.get_user('phonedude_mln')
    
    for user in tweepy.Cursor(api.followers, screen_name="phonedude_mln", count = 200).items():
		print   user.followers_count