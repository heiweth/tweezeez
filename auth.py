import tweepy

consumer_key = "2CkNhJGkeTfgzBCC6jGIZBrMM"
consumer_secret = "OnXnt1YG7vBn3TR9AmWaEn3dp0l06itQLGLdxErVQzYy4dKmyL"
access_token = "376124093-HEw2fJdUjSTsZ24TkQcfLpJEUzqHXo16Wr69jg86"
access_token_secret = "7kTvILfDF8Dp8nKvLXf9Q6a0WLJEcE00nVEoOyWy3LCWr"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)