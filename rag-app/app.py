import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv(dotenv_path="/Users/vishalsubhanje/endee/rag-app/.env")

from query import retrieve_relevant_context

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Heart Risk Assist", page_icon="❤️")
st.title("Heart Risk Assist")
st.write("A RAG-based heart health awareness system using Endee")

question = st.text_input("Ask a heart-health question:")

if question:
    context = retrieve_relevant_context(question)

    prompt = f"""
You are a heart health awareness assistant.
Answer the user's question using only the context below.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Retrieved Context")
    st.write(context)

st.caption("For educational purposes only. Not medical advice.")