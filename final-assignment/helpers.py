import re

def remove_urls(txt):
    return re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', txt, flags=re.MULTILINE)

def replace_usernames(txt):
    return re.sub(r'(^|\s)@(\w+)', ' @user', txt, flags=re.MULTILINE)

def preprocess_tweets(tweets):
    output = [remove_urls(tweet) for tweet in tweets]
    output = [replace_usernames(tweet) for tweet in output]

    return output