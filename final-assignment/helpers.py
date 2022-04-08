import re

def remove_urls(txt):
    return re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', txt, flags=re.MULTILINE)

def replace_usernames(txt):
    return re.sub(r'(^|\s)@(\w+)', ' @user', txt, flags=re.MULTILINE)

def remove_trailing_and_leading_hashtags(tweet):
    # Remove leading
    tweet = re.sub(r'^(\#\w+\s?)+', '', tweet, flags=re.MULTILINE)

    # Remove trailing
    tweet = re.sub(r'(\#\w+\s?)+$', '', tweet, flags=re.MULTILINE)

    return tweet

def remove_whitespace(post):
    return re.sub(r'\s+', ' ', post, flags=re.MULTILINE)

def preprocess_tweets(tweets):
    return [preprocess_tweet(tweet) for tweet in tweets]

def preprocess_tweet(tweet):
    tweet = tweet.strip()
    tweet = remove_urls(tweet)
    tweet = replace_usernames(tweet)
    tweet = remove_trailing_and_leading_hashtags(tweet)
    tweet = remove_whitespace(tweet)
    
    return tweet

def preprocess_reddits(posts):
    return [preprocess_reddit(post) for post in posts]

def preprocess_reddit(post):
    post = post.strip()
    post = remove_urls(post)
    post = replace_usernames(post)
    post = remove_whitespace(post)

    return post