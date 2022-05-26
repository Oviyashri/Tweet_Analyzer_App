import streamlit as st
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
from PIL import Image



#APIkey 
#APIKeySecret       # Confidential
#accesstoken
#accesstokensecret
#BearerToken 


#authenticate = tweepy.OAuthHandler(APIkey, APIKeySecret) # Create OAuthHandler object
#authenticate.set_access_token(accesstoken, accesstokensecret) # Set access token and access token secret
#api = tweepy.API(authenticate)  # Creating tweepy API object to fetch tweet















#plt.style.use('fivethirtyeight')









def app():


	st.title("Tweet Analyzer 🔥")


	activities=["Tweet Analyzer","Generate Twitter Data"]

	choice = st.sidebar.selectbox("Select Your Activity",activities)

	

	if choice=="Tweet Analyzer":

		st.subheader("Analyze the tweets of Air India")

		st.subheader("This tool performs the following tasks :")

		st.write("1. Fetches the 5 most recent tweets")
#		st.write("2. Generates a Word Cloud")
		st.write("2. Performs Sentiment Analysis a displays it in form of a Bar Graph")


		


		raw_text = st.text_area("Enter the exact tweet (without @)")



		st.markdown("<--------     Also Do checkout the another cool tool from the sidebar")

		Analyzer_choice = st.selectbox("Select the Activities",  ["Show Recent Tweets","Visualize the Sentiment Analysis"])


		if st.button("Analyze"):

			
			if Analyzer_choice == "Show Recent Tweets":

				st.success("Fetching last 5 Tweets")

				
				def Show_Recent_Tweets(raw_text):
					# create your client 
                    # client = tweepy.Client(bearer_token=BearerToken)
					# Extract 100 tweets from the twitter user
					posts = client.search_recent_tweets(query="Air India",max_results = 100, tweet_fields=['created_at','lang'])

					
					def get_tweets():

						l=[]
						i=1
						for tweet in posts[:10]:
							l.append(tweet.full_text)
							i= i+1
						return l

					recent_tweets=get_tweets()		
					return recent_tweets

				recent_tweets= Show_Recent_Tweets(raw_text)

				st.write(recent_tweets)



			elif Analyzer_choice=="Generate WordCloud":

				st.success("Generating Word Cloud")

				def gen_wordcloud():

					posts = client.search_recent_tweets(query="Air India",max_results = 100, tweet_fields=['created_at','lang'])


					# Create a dataframe with a column called Tweets
					df = pd.DataFrame([tweet.text for tweet in posts.data], columns=['Tweets'])
					# word cloud visualization
					allWords = ' '.join([twts for twts in df['Tweets']])
					wordCloud = WordCloud(width=500, height=300, random_state=21, max_font_size=110).generate(allWords)
					plt.imshow(wordCloud, interpolation="bilinear")
					plt.axis('off')
					plt.savefig('WC.jpg')
					img= Image.open("WC.jpg") 
					return img

				img=gen_wordcloud()

				st.image(img)



			else:



				
				def Plot_Analysis():

					st.success("Generating Visualisation for Sentiment Analysis")

					


					posts = client.search_recent_tweets(query="Air India",max_results = 100, tweet_fields=['created_at','lang'])

					df = pd.DataFrame([tweet.text for tweet in posts.data], columns=['Tweets'])


					
					# Create a function to clean the tweets
					def cleantweet(text):
					 text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
					 text = re.sub('#', '', text) #Removing '#' hash tag
					 text = re.sub('RT[\s]+', '', text) #Removing RT
					 text = re.sub('https?:\/\/\S+', '', text) #Removing hyperlink
					 
					 return text


					# Clean the tweets
					df['Tweets'] = df['Tweets'].apply(cleantweet)


					def getSubjectivity(text):
					   return TextBlob(text).sentiment.subjectivity

					# Create a function to get the polarity
					def getPolarity(text):
					   return  TextBlob(text).sentiment.polarity


					# Create two new columns 'Subjectivity' & 'Polarity'
					df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
					df['Polarity'] = df['Tweets'].apply(getPolarity)


					def getAnalysis(score):
					  if score < 0:
					    return 'Negative'
					  elif score == 0:
					    return 'Neutral'
					  else:
					    return 'Positive'
					    
					df['Analysis'] = df['Polarity'].apply(getAnalysis)


					return df



				df= Plot_Analysis()



				st.write(sns.countplot(x=df["Analysis"],data=df))


				st.pyplot(use_container_width=True)

				

	

	else:

		st.subheader("This tool fetches the last 100 tweets from the twitter handel & Performs the following tasks")

		st.write("1. Converts it into a DataFrame")
		st.write("2. Cleans the text")
		st.write("3. Analyzes Subjectivity of tweets and adds an additional column for it")
		st.write("4. Analyzes Polarity of tweets and adds an additional column for it")
		st.write("5. Analyzes Sentiments of tweets and adds an additional column for it")






		user_name = st.text_area("*Enter the exact tweet (without @)*")

		st.markdown("<--------     Also Do checkout the another cool tool from the sidebar")

		def get_data(user_name):

			posts = client.search_recent_tweets(query="Air India",max_results = 100, tweet_fields=['created_at','lang'])

			df = pd.DataFrame([tweet.text for tweet in posts.data], columns=['Tweets'])

			def cleantweet(text):
				text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
				text = re.sub('#', '', text) #Removing '#' hash tag
				text = re.sub('RT[\s]+', '', text) #Removing RT
				text = re.sub('https?:\/\/\S+', '', text) #Removing hyperlink
				return text

			# Clean the tweets
			df['Tweets'] = df['Tweets'].apply(cleantweet)


			def getSubjectivity(text):
				return TextBlob(text).sentiment.subjectivity

						# Create a function to get the polarity
			def getPolarity(text):
				return  TextBlob(text).sentiment.polarity


						# Create two new columns 'Subjectivity' & 'Polarity'
			df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
			df['Polarity'] = df['Tweets'].apply(getPolarity)

			def getAnalysis(score):
				if score < 0:
					return 'Negative'

				elif score == 0:
					return 'Neutral'


				else:
					return 'Positive'

		
						    
			df['Analysis'] = df['Polarity'].apply(getAnalysis)
			return df

		if st.button("Show Data"):

			st.success("Fetching Last 100 Tweets")

			df=get_data(user_name)

			st.write(df)



			








if __name__ == "__main__":
	app()