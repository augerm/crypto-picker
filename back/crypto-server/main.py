from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# print(analyzeSentiment(tweet.get['text']))

def analyzeSentiment(tweet):
    vs = analyzer.polarity_scores(tweet)
    if(vs['compound'] > .5):
        return "Positive"
    elif(vs['compound'] < -.5):
        return "Negative"
    else:
        return "Neutral"






