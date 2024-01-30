import streamlit as st
from dotenv import load_dotenv
from langchainAI import get_langchain_response

load_dotenv()
st.set_page_config(page_title="Conversation helper")
st.header("Let's talk! :)")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help?"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_langchain_response(prompt)
            st.write(response)

    # Update chat history with assistant's response
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
