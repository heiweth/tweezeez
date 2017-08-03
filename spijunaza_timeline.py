# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The Twitter user who we want to get tweets from
name = "Precarobna"
# Number of tweets to pull
tweetCount = 100
query="ultimatum"

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)
res = api.search(q=query)


# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print tweet.text
