import streamlit as st

from assistants.oss_assistant import get_oss_response
from assistants.memory import add_to_memory, get_memory

st.title("OSS AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    add_to_memory("user", user_input)

    memory = get_memory()

    full_prompt = ""

    for chat in memory:
        full_prompt += f"{chat['role']}: {chat['content']}\n"

    response = get_oss_response(full_prompt)

    add_to_memory("assistant", response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        st.write(response)