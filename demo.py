import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'TDGvqeQdDJ8zQ5y0m7kSNoz63'
consumer_secret= 'GunVtg9twtBavIsqecJ1f79hUerkkkCDcM6Pbx3IkqkfdVawR9'

access_token='4555337915-vOcFh5XXfxmkWh7oSd5SXhQg9jfKNN2Z2o3uJyO'
access_token_secret='rI70mLt5kFnVdnQK9ZE33O2uVTnBlICrVWyzF8WLI9twU'

#Creating our authentication variables
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Our main variable to work with twitter
api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('China')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)

    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
