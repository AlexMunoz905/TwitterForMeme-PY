import tweepy
auth = tweepy.OAuthHandler("Consumer-API-Key", "Consumer-API-Key-Secret")
auth.set_access_token("API-Key", "API-Key-Secret")
api = tweepy.API(auth)
print ("Tweet Message!")
print ("Twitter For?")
tweet = input("Conjure Up A Tweet")
api.update_status(status =(tweet))
print ("Done!")
