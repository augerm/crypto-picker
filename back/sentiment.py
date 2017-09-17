import pandas as pd
import statistics as s
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import dateutil.parser
from datetime import datetime
import utilities
# import graph
# from matplotlib.pyplot import figure, draw

analyzer = SentimentIntensityAnalyzer()

sentiments = []
currentSentiment = []
currentTime = []
col_names = ['timeStamp','tweet','numFollowers']
TWENTY_MINUTES_MS = 1200000
tweet_collections = pd.DataFrame(columns=col_names)
CUR_TIME_MS = utilities.getCurrentTime()

# print(analyzeSentiment(tweet.get['text']))
def trackSentiment(tweet, user, time):
	vs = analyzer.polarity_scores(tweet)
	compound = vs['compound']
	weightedCompound = compound * (user['followers_count']/100)
	sentiments.append(weightedCompound)
	updateCurrentSentiment()
def analyzeSentiment(tweet, numFollowers, timeStamp):
    vs = analyzer.polarity_scores(tweet)
    msTime = dateutil.parser.parse(timeStamp).timestamp() * 1000
    sentiments.append({"compound": vs['compound'], "timeStamp": msTime})
    updateCurrentSentiment()
    # print("timeStamp:", timeStamp)
    # print("tweet:", tweet)
    # print("numFollowers:", numFollowers)

    # data = pd.DataFrame([[timeStamp, tweet, numFollowers]], columns=col_names)
    # print (data)
    # tweet_collections.append(data)
    # print(tweet_collections)

def updateCurrentSentiment():
	sentimentValues = []
	sentimentTimes = []
	for sentiment in sentiments:
		timeDiff = utilities.getCurrentTime() - sentiment.get('timeStamp')
		if(timeDiff > TWENTY_MINUTES_MS):
			sentiments.remove(sentiment)
		else:
			sentimentValues.append(sentiment.get('compound')/10)
			sentimentTimes.append((sentiment.get('timeStamp')-CUR_TIME_MS)/1000000 )
	if(len(sentimentValues) > 1):
		currentSentiment.append(s.mean(sentimentValues))
		currentTime.append(sentimentTimes[-1])
		print("sentimentValues:", sentimentValues)
		print("Current sentiment: ", currentTime)
		# graph.updateGraph(currentTime, currentSentiment)

def getCurrentSentiment():
	return currentSentiment

