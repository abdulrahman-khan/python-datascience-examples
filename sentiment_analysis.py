import tweepy
from textblob import TextBlob
import config

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# public_tweets = api.search_geo('FFXIV', count=10)
# api = tweepy.API(auth)

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'Pendulum'
response = client.search_recent_tweets(query=query, max_results=10)
print(response)


# for tweet in public_tweets:
#     print(tweet.text)
#     analysis = TextBlob(tweet.text)
#     print(analysis.sentiment)
#     if analysis.sentiment.polarity > 0:
#         print("Positive")
#     elif analysis.sentiment.polarity == 0:
#         print("Neutral")
#     else:
#         print("Negative")




