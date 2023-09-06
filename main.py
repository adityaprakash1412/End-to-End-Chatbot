import os

import nltk

import ssl

import streamlit as st

import random

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from chatbot import chatbot

counter = 0

def main():
    global counter
    st.write("Chatbot")
    st.write("Welcome to Chatbot. Please type a message and press enter to start a conversation!!!!")
    
    counter += 1
    user_input = st.text_input("You:", key=f"user_input_{counter}")
    
    if user_input:
        response = chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=f"chatbot_response_{counter}")
    
    
        if response.lower() in ['goodbye', 'bye']:
                st.write("Thank you for chatting with me. Have a great day!")
                st.stop()

if __name__ == '__main__':
    main()