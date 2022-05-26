A web app integrated with twitter which takes the live tweets as an input and does :

# 1. Analyze the tweets of live Air India's customer tweets

This tool performs the following tasks :

a) Fetches the most recent tweets from the given twitter handel

b) Performs Sentiment Analysis a displays it in form of a Bar Graph

# 2. This tool fetches the last 100 tweets from the twitter handel & Performs the following tasks :**

a) Converts it into a DataFrame

b) Cleans the text

c) Analyzes Subjectivity of tweets and adds an additional column for it

d) Analyzes Polarity of tweets and adds an additional column for it

e) Analyzes Sentiments of tweets and adds an additional column for it

# Other files

**Procfile** : To generate command to run the app

**twitter_sentiment_analysis.ipynb** : Model building File

**Twitter Data** : File created after every query on the web app

**requirements.txt** : Requirement file

**setup.sh** : predefined file for streamlit on heroku

This app is created on a tool called Streamlit, Installed it by: Streamlit documentation: https://docs.streamlit.io/en/latest/

**pip install streamlit**

To run it on local host : **streamlit run app.py**

**Web App**

Tweet Analyzer

![appcrop1](https://user-images.githubusercontent.com/92749977/170442652-197de182-b5f2-4062-9f9c-e9c831a42c2d.jpg)


Generate Twitter Data

![appcrop2](https://user-images.githubusercontent.com/92749977/170442688-f49d5c3e-5aff-4ea4-90b3-bbc9b79d2623.jpg)


