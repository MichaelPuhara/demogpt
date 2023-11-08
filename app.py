import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

st.title("Māori Translation Bot")

def maoriTranslator(maori_word):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=50,
    )

    system_template = "You are an assistant that provides translations and explanations for Maori words and phrases."
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

    human_template = f"Please provide the translation or explanation for the Māori word or phrase: '{maori_word}'."
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    result = chat.get_response(chat_prompt, max_tokens=50, maori_word=maori_word)
    
    return result

maori_word = st.text_input("Enter the Māori word or phrase you want to learn:")
response = ""

if st.button("Translate"):
    if maori_word:
        response = maoriTranslator(maori_word)

st.markdown(response)
