import tweepy
import time

# create an application in twitter API console, and paste in given credentials and tokens
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# get timeline tweets
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# get user info
user_info = api.me()
print(user_info.name)
print(user_info.screen_name)
print(user_info.followers_count)

def tweeter_api_limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(500)

# Follow all followers back
for follower in tweeter_api_limit_handler(tweepy.Cursor(api.followers).items()):
  if follower.name == 'username': # enter follower name here
    follower.follow()
    break

# search tweets, like and retweet them
search_term = 'python'
tweet_count = 3

for tweet in tweeter_api_limit_handler(tweepy.Cursor(api.search, search_term).items(tweet_count)):
  try:
    tweet.favorite()
    tweet.retweet()
    print('Liked the tweet and re-tweeted')
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break