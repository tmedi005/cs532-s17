import json
import pandas as pd
import matplotlib.pyplot as plt
import re


tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
		#print tweet['expanded_url']
		
	except:
		continue

#print  len(tweets_data)
tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

def word_in_text(word, text):
	word = word.lower()
	text = text.lower()
	match = re.search(word, text)
	if match:
		return True
	return False

tweets['superbowl'] = tweets['text'].apply(lambda tweet: word_in_text('superbowl', tweet))


#print tweets['superbowl'].value_counts()[True]

def extract_link(text):
	regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
	match = re.search(regex, text)
	if match:
		return match.group()
	return ''
	
tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

tweets_relevant = tweets[tweets['superbowl'] == True]	
tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']


print tweets_relevant_with_link[tweets_relevant_with_link['superbowl'] == True]['link']
	




