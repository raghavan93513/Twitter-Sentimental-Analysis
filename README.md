# Twitter Sentiment Analysis


## Project Description
This project uses machine learning techniques (Natural Language Processing) to analyze the sentiment of Twitter tweets dynamically. By examining the language used in tweets, we can make predictions about the author's sentiment (positive, negative, neutral). This tool is beneficial in various fields such as marketing, politics, and public relations.
<br/>
<br/>
Use Case Diagram:- <br/>
![alt text](https://github.com/raghavan93513/Twitter-Sentimental-Analysis/blob/main/Screenshots/Usecasediagram.png)

## Getting Started

### Prerequisites

Need to know concepts about these libraries:-
- tweepy
- numpy
- pandas
- matplotlib
- textblob
- emoji
- re
- string
- nltk
- flask
- os

Need to have a bearer token from the website:-
```https://developer.twitter.com/```


### Installation

```pip install -r requirements.txt``` <br/>
Run to install all of the Python modules and packages listed in your requirements.txt file.

## About the Project

It uses the Tweepy library to fetch the tweets, then processes and analyzes the sentiment of each tweet. It also generates a pie chart of the sentiment distribution and returns the result.

- Connects to the Twitter API and fetches tweets about a specific topic.
- Cleans the fetched tweets using the cleanTweet function to clean all the text and emojis.
- Uses TextBlob and SentimentIntensityAnalyzer to determine the sentiment of each tweet.
- Determines the overall sentiment distribution and visualizes it using a pie chart.
- The sentiment of each tweet is determined based on the polarity scores for the text. If the negative score is greater than the positive score, the tweet is classified as negative. If the positive score is greater, the tweet is classified as positive. If they are equal, the tweet is classified as neutral.

## Metrics calculated

### Polarity
This is a metric derived from TextBlob's sentiment analysis, which uses a form of rule-based sentiment analysis. This is a measure of the sentiment expressed in the tweet. Polarity can be positive (expressing a positive sentiment), negative (expressing a negative sentiment), or neutral (expressing no particular sentiment). It's usually a value between -1 and 1, where -1 represents an extremely negative sentiment, 1 represents an extremely positive sentiment, and 0 represents a neutral sentiment. It is derived from the sentiment analysis of the text.

### Subjectivity
Subjectivity in sentiment analysis refers to the expression of personal feelings, opinions, beliefs, etc. in the text. It's usually a value between 0 and 1. A subjectivity score closer to 0 refers to more objective statements (fact-based), while a score closer to 1 refers to more subjective statements (opinion-based).

### Negetivity
This is the score that represents the negative sentiment in the tweet. It's a value between 0 and 1. The higher the score, the more negative sentiment is expressed in the text.

### Neutrality
This is the score that represents the neutral sentiment in the tweet. Like 'neg', it's a value between 0 and 1. A higher 'neu' score represents a more neutral (neither positive nor negative) sentiment in the text.

### Positivity
This is the score that represents the positive sentiment in the tweet. Also a value between 0 and 1, the 'pos' score measures the level of positive sentiment expressed in the text. The higher the score, the more positive sentiment is expressed.

### Compound
This is a metric from VADER (Valence Aware Dictionary for Sentiment Reasoning), a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. The Compound score is a normalized, weighted composite score computed by summing the valence scores of each word in the lexicon, adjusted for modifiers, intensity, and the context of the word in the sentence. It is normalized between -1 (most extreme negative) and +1 (most extreme positive). It is the overall sentiment of the text. If the compound score is closer to +1, the text is assessed as positive, if it's closer to -1, the text is assessed as negative.

## Text Transformation Techniques

### Punctiations
In the context of text processing and sentiment analysis, it is used for removing punctuation from the text data. It also removes any digits from the text. The processed text is stored in a new column 'punct'.

### Tokenized
Tokenization is the process of breaking down the text into individual words or tokens. The text is tokenized, i.e., split into individual words or tokens. The resulting tokens are stored in a new column 'tokenized'. It's important to note that before tokenization, the text is converted to lower case to maintain consistency.

### Nonstop
In text processing, 'nonstop' refers to the removal of stop words. Stop words are common words in a language (like 'is', 'the', 'and' in English) that are often removed during text preprocessing because they don't carry much meaningful information.

### Stemmed
Stemming is the process of reducing inflected or derived words to their base or root form. For example, 'running' and 'runs' are stemmed to 'run'. This can help in grouping together words of similar meaning, and thus simplify the text analysis process.

## Output Screenshots

### Results
![alt text](https://github.com/raghavan93513/Twitter-Sentimental-Analysis/blob/main/Screenshots/Table.png)
![alt text](https://github.com/raghavan93513/Twitter-Sentimental-Analysis/blob/main/Screenshots/Classification.png)
![alt text](https://github.com/raghavan93513/Twitter-Sentimental-Analysis/blob/main/Screenshots/Percentage.png)
![alt text](https://github.com/raghavan93513/Twitter-Sentimental-Analysis/blob/main/Screenshots/Classification2.png)

### UI/UX
![alt text](https://github.com/raghavan93513/Twitter-Sentimental-Analysis/blob/main/Screenshots/Frontend.png)
<br/>
When you click on 'here'
<br/>
![alt text](https://github.com/raghavan93513/Twitter-Sentimental-Analysis/blob/main/Screenshots/piechart.png)
