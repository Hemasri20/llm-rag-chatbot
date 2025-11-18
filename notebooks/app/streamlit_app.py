import streamlit as st
from src.inference import answer_query

st.title("RAG Chatbot Demo")
user_input = st.text_input("Ask me anything:")

if user_input:
    response = answer_query(user_input)
    st.write(response)
