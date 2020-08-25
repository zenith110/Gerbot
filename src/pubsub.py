from api_keys.twitter_keys import api_key, api_secret, access_token, access_token_secret
import tweepy
import re
"""
Fetches the latest pub sub deal 
"""
def get_pub_sub():
    """
    Our sub list
    """
    subs = ["Chicken Tender", "Boar's Head Turkey"]
    
    """
    Does user auth to log onto twitter dev account
    """
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    """
    Lets us get onto the timeline for the tweets
    """
    tweets = api.user_timeline(screen_name = "PubSubs_on_sale")
    """
    Gets us our tweets from the user
    """
    tweets_for_dump = [tweet.text for tweet in tweets] 
    
    sub_storage = []
    """
    Checks if we have the data matching correctly
    """
    for j in tweets_for_dump: 
        if any(f in j for f in subs):
            sub_storage.append(j)

    """
    Return the first tweet in the list
    """
    sub = sub_storage[0]
    return sub
if __name__ == "__main__":
    get_pub_sub()