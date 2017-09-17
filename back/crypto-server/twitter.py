import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json
import sentiment
import server

print("ASYNC")
consumer_key='0Apql2NUD1DkbpqNSRwIh4Ory'
consumer_secret='zjSGgToPMbqT3AX9UXayQYAi0i4WyBQ4QMqY6130Ivz6yjt6Bh'
access_token_key='219067513-3jMVUEKlibTCdNkuoZ3YiaOItf6kIS4ybzYAg73i'
access_token_secret='z7n5n7dVBSCO3Lxv7bRHN2nhdrVpu90oBBPQwgA3u8arg'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

# List of unread tweets
unreadTweets  = []
class MyListener(StreamListener):
    def on_data(self, data):
    	tweet = json.loads(data)
    	sentimentData = sentiment.analyzeSentiment(tweet.get('text'), tweet['user']['followers_count'], tweet.get('created_at'))
    	server.send_message_to_client(sentimentData)
    def on_error(self, status):
        print(status)
        return True
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#bitcoin', '#Crypto', '#ETH'])

def getTweets():
	oldUnreadTweets = unreadTweets
	unreadTweets = []
	return oldUnreadTweets