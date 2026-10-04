from langchain_ollama import ChatOllama
import streamlit as st
llm = ChatOllama(
    model="gemma3:1b",
    temperature=0
)

# Streamlit UI
st.title("🤖 My AI Assistant")
st.write("Ask a question and get an answer from Gemma.")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            response = llm.invoke(question)

        st.write("### Answer")
        st.write(response.content)
    else:
        st.warning("Please enter a question.")