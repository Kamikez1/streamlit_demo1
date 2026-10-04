import os
import streamlit as st
from langchain_openai import ChatOpenAI

# Get API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create LangChain model
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY
)

# Streamlit UI
st.title("🤖 My AI Assistant")
st.write("Ask a question and get an answer from GPT-4o.")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            response = llm.invoke(question)

        st.write("### Answer")
        st.write(response.content)
    else:
        st.warning("Please enter a question.")
