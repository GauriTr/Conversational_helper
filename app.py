# app.py

import streamlit as st
from dotenv import load_dotenv
from langchainAI import get_langchain_response  


load_dotenv()

st.set_page_config(page_title="Conversation helping Chatbot")
st.header("Let's talk! :)")

input_text = st.text_input("Put the text here: ", key="input")


submit_button = st.button("Solve the query.")

if submit_button and input_text:
    
    response = get_langchain_response(input_text)

    
    st.subheader("The Response can be:")
    st.write(response)
elif submit_button:
    
    st.subheader("Put the query.")
