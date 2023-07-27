#tweepy modules
import tweepy

#my credentials
import twitter_creds as tc

#Data Analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Data Preprocessing and Feature Engineering
from textblob import TextBlob
import emoji
import re

#Sentimental Analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def remove_emojis(data):
    emoj = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    u"\U00002500-\U00002BEF"  # chinese char
    u"\U00002702-\U000027B0"
    u"\U00002702-\U000027B0"
    u"\U000024C2-\U0001F251"
    u"\U0001f926-\U0001f937"
    u"\U00010000-\U0010ffff"
    u"\u2640-\u2642" 
    u"\u2600-\u2B55"
    u"\u200d"
    u"\u23cf"
    u"\u23e9"
    u"\u231a"
    u"\ufe0f"  # dingbats
    u"\u3030"
    "]+", re.UNICODE)
    return re.sub(emoj, '', data)


def cleanTweet(tweet):
    if 'RT' in tweet[:3]:
        tweet = tweet.replace('RT','')
    tweet = remove_emojis(tweet)
    tweet = tweet.replace(':','')
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.EMOJI_DATA) #Remove Emojis
    tweet = tweet.replace("#", "").replace("_", " ") #Remove '#' and '_' sign but keep the text
    return tweet

def percentage(part,whole):
    return 100 * float(part)/float(whole)

def cleanDf(df,columnName):
    cleanList = []
    for tweet in df[columnName]:
        clean_tweet = cleanTweet(tweet)
        cleanList.append(clean_tweet)
    df[columnName] = cleanList

def count_values_in_column(data,feature):
    total=data.loc[:,feature].value_counts(dropna=False)
    percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])

def get_tweets(topic, lim = 100):
    client = tweepy.Client(bearer_token=tc.bearer_token)
    query = topic
    lst=[]

    # Replace the limit=1000 with the maximum number of Tweets you want
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                                tweet_fields=['context_annotations', 'created_at'], max_results=lim).flatten(limit=lim):
        a = tweet.text
        lst.append(a)
    
    df = pd.DataFrame(lst,columns=['text'])
    
    #Droping duplicate rows and NaN values if present
    df = df.drop_duplicates()
    df = df.dropna()

    cleanDf(df, 'text')

    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    tweet_list = []
    neutral_list = []
    negative_list = []
    positive_list = []
    sid = SentimentIntensityAnalyzer()

    for tweet in df['text']:
        tweet_list.append(tweet)
        analysis = TextBlob(tweet)
        score = sid.polarity_scores(tweet)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        comp = score['compound']
        polarity += analysis.sentiment.polarity
        
        if neg > pos:
            negative_list.append(tweet)
            negative += 1

        elif pos > neg:
            positive_list.append(tweet)
            positive += 1

        elif pos == neg:
            neutral_list.append(tweet)
            neutral += 1

    

    noOfTweet = len(df['text'])

    #Calculating Negative, Positive, Neutral and Compound values
    df[['polarity', 'subjectivity']] = df['text'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
    for index, row in df['text'].items():
        score = SentimentIntensityAnalyzer().polarity_scores(row)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        comp = score['compound']
        if neg > pos:
            df.loc[index, 'sentiment'] = "negative"
        elif pos > neg:
            df.loc[index, 'sentiment'] = "positive"
        else:
            df.loc[index, 'sentiment'] = "neutral"
        df.loc[index, 'neg'] = neg
        df.loc[index, 'neu'] = neu
        df.loc[index, 'pos'] = pos
        df.loc[index, 'compound'] = comp

    positive = percentage(positive, noOfTweet)
    positive = format(positive, '.1f')
    negative = percentage(negative, noOfTweet)
    negative = format(negative, '.1f')
    neutral = percentage(neutral, noOfTweet)
    neutral = format(neutral, '.1f')
    polarity = percentage(polarity, noOfTweet)

    #Number of Tweets (Total, Positive, Negative, Neutral)
    tweet_list = pd.DataFrame(tweet_list)
    neutral_list = pd.DataFrame(neutral_list)
    negative_list = pd.DataFrame(negative_list)
    positive_list = pd.DataFrame(positive_list)

    #Count_values for sentiment
    result = count_values_in_column(df,"sentiment")
    
    y = np.array([len(positive_list), len(negative_list), len(neutral_list)])
    mylabels = ["Positive", "Negative", "Neutral"]
    myexplode = [0.2, 0, 0]

    plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
    plt.legend(title = "Sentiments:")
    plt.savefig('static/bar.png') 

    return result