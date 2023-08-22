import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

st.title("Kaiako")

def maoriTranslator(maori_word):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0
    )
    system_template = """You are an assistant that provides translations and explanations for Maori words and phrases."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please provide the translation or explanation for the Maori word or phrase: '{maori_word}'."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(maori_word=maori_word)
    return result

maori_word = st.text_input("Enter the Maori word or phrase you want to learn")
response = ""

if st.button("Submit"):
    if maori_word:
        response = maoriTranslator(maori_word)

st.markdown(response)
