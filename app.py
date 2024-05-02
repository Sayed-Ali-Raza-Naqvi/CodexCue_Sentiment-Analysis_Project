# Importing the libraries.
import streamlit as st
import time
import pickle

# Loading the model.
with open('twitter_sentiment_analysis.pkl', 'rb') as file:
    model = pickle.load(file)

# Driver function.
def main():
    st.title('Twitter Sentiment Analysis')
    tweet = st.text_input('Enter your tweet: ')
    submit = st.button('Analyze Sentiment')

    if submit:
        if tweet.strip() == '':
            st.write('Please enter your tweet.')
        else:
            start = time.time()
            prediction = model.predict([tweet])[0]
            end = time.time()
            st.write(f'Time taken to predict: {round(end-start, 2)}')
            st.write(f'Predicted Sentiment: {prediction}')

if __name__ == '__main__':
    main()