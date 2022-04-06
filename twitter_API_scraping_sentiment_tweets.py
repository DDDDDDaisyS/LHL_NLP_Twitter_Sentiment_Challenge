import twitter
import os
import json

# Load the values of access tokens and keys from environmental variables to python variables
consumer_key = os.environ["Twitter_API_Key"]
consumer_secret = os.environ["Twitter_API_Key_Secret"]
access_token = os.environ["Twitter_Access_Token"]
access_token_secret = os.environ["Twitter_Access_Token_Secret"]

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

# filter tweets with given conditions; write filtered tweets into file sentiment.txt
def filter_tweets(FILTER, LANGUAGES, LOCATIONS):
    """
    FILTER: type(list) to filter tweets mentioning given strings in it
    LANGUAGES: type(list) to filter tweets only in the given languages
    LOCATION: type(list) to filter tweets by locations where they were posted
    """
    
    with open('sentiment.txt', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(track=FILTER, languages=LANGUAGES, locations=LOCATIONS):
            f.write(json.dumps(line))
            f.write('\n\n')
            
filter_tweets([':)',':('], ['en'], ['-74,40,-73,41'])
