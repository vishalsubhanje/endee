import streamlit as st
from utils.loader import load_document
from utils.chunker import chunk_text

st.set_page_config(page_title="AI Document Assistant", layout="wide")

st.title("AI Document Assistant using Endee")
st.write("Upload a TXT or PDF file and ask questions from it.")

uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf"])

if uploaded_file is not None:
    st.success(f"File uploaded successfully: {uploaded_file.name}")

    document_text = load_document(uploaded_file)

    if document_text:
        st.subheader("Extracted Text Preview")
        st.text_area("Document Text", document_text[:2000], height=250)

        chunks = chunk_text(document_text)

        st.subheader("Generated Chunks")
        st.write(f"Total chunks created: {len(chunks)}")

        for i, chunk in enumerate(chunks[:5]):
            st.text_area(f"Chunk {i+1}", chunk, height=150)
    else:
        st.error("Could not read the uploaded file.")
else:
    st.info("Please upload a TXT or PDF file.")