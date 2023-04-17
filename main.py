import pandas as pd
import snscrape.modules.twitter as sntwitter
from tqdm.notebook import tqdm

scraper = sntwitter.TwitterSearchScraper('#machine learning')
tweets = []
n_tweets = int(input('How many data you want to pull from twitter?'))
for i, tweet in tqdm(enumerate(scraper.get_items()), total=n_tweets):
    data = [tweet.date,
            tweet.id,
            tweet.content,
            tweet.user.username,
            tweet.likeCount,
            tweet.retweetCount
            ]
    tweets.append(data)
    if i > n_tweets:
        break
tweet_df = pd.DataFrame(tweets,columns=['Date','Id','Content','username','like_count','retweet_count'])
tweet_df.to_csv('machine-learning-tweets.csv',index=False)
