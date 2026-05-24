import streamlit as st

from assistants.oss_assistant import get_oss_response

st.title("OSS AI Assistant")

user_input = st.chat_input("Type your message")

if user_input:

    response = get_oss_response(user_input)

    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)