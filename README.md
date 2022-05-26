This is a cool web app integrated with twitter which takes the twitter handel as as input and does :

1. Analyze the tweets of live air asia's customer tweets 

This tool performs the following tasks :

Fetches the most recent tweets from the given twitter handel

Performs Sentiment Analysis a displays it in form of a Bar Graph

2. This tool fetches the last 100 tweets from the twitter handel & Performs the following tasks Converts it into a DataFrame

Cleans the text

Analyzes Subjectivity of tweets and adds an additional column for it
Analyzes Polarity of tweets and adds an additional column for it
Analyzes Sentiments of tweets and adds an additional column for it

**Procfile** : To generate command to run the app

**twitter_sentiment_analysis.ipynb** : Model building File

**Twitter Data** : File created after every query on the web app

**Requirements.txt** : Requirement file

**setup.sh** : predefined file for streamlit on heroku

This app is created on a tool called Streamlit which saves you from the headache of front-end devlopment ,you can install it by: Streamlit documentation: https://docs.streamlit.io/en/latest/

**pip install streamlit**

& to run it on local host : streamlit run app.py
