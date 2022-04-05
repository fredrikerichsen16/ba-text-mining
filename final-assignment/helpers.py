import re

def remove_urls(txt):
    return re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', txt, flags=re.MULTILINE)

def replace_usernames(txt):
    return re.sub(r'(^|\s)@(\w+)', ' @user', txt, flags=re.MULTILINE)

def preprocess_tweets(tweets):
    return [preprocess_tweet(tweet) for tweet in tweets]

def preprocess_tweet(tweet):
    tweet = remove_urls(tweet)
    tweet = replace_usernames(tweet)
    tweet = tweet.replace('\n', ' ')
    
    return tweet