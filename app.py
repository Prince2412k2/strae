import streamlit as st
from main import search_and_answer

st.set_page_config(page_title="Chatbot", page_icon=":robot_face:", layout="wide")

st.title("Interactive Chatbot")
st.write("Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = search_and_answer(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
