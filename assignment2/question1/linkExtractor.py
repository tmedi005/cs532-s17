#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json



#Variables that contains the user credentials to access Twitter API 
access_token = "952384183-cwYOb7LYBHqVkYnclU39pHNRUe0Hn9nPpbX7aJ6R"
access_token_secret = "BcnkVt1PWuE0d0Uw9itqcts4gE7FTX9P7EkdLqEACZTJK"
consumer_key = "l1tsh3QrpT8uuteksvDLtDSM5"
consumer_secret = "GmAR39QA135i7UNiTDOpuaQEW3MapTqfwl3BaGzVlHWCrAt1Rj"

#This is a basic listener that just prints received tweets to stdout.
MAX_NUM_TWEETS = 999
class StdOutListener(StreamListener):
	def __init__(self):
		self.count = 0
	
	def on_data(self, data):
		self.count +=1
		print data
		#print self.count
		if self.count > MAX_NUM_TWEETS :
			return False
		return True
	
	def on_error(self, status):
		print status
	

	
	

    


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['superbowl'])

