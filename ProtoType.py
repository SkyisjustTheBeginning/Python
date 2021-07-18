import tweepy
import datetime
import random
consumer_key = '1b6XGTKX0l9UWtlZdYPknMSSA'
consumer_secret = 'ypU2ukq50hjD4iget4tKkkMFehDzB492YV5r2oJO4fUn6fDdxp'
access_token = '1282212543784599552-sppgzZOAQK1RSv8xNoNo55B35B9rxb'
access_token_secret = '8w6slvlv4JzDuIgSA5dDBbArz7Ygsbf6Z6nCJDScji7TN'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
import datetime
file1 = open('Naive.txt', 'r')
Lines = file1.readlines()
count = 0
Olympus = []
# Strips the newline character
for line in Lines:
    count += 1
    Olympus.append(line)
api.update_status(random.choice(Olympus))
print(Lines)

print(datetime.date.today().weekday())
# above code will print 6 if today was Sunday, 0 if today was Monday, 1 if today was Tuesday and so on.
