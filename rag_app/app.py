import streamlit as st
import tempfile
import os
import shutil
from rag_core import ingest_document, ask_question, load_existing_db

# Set page config for a clean layout
st.set_page_config(page_title="PDF RAG Assistant", layout="wide")

st.title("📚 Company RAG Assistant")
st.markdown("Upload a PDF, Markdown, or Text document and ask questions about its contents using Google Gemini.")

DB_FOLDER = "company_vector_db"

# Initialize session state to store our vector database and chat history
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
    
    # Automatically load the database if it exists on the hard drive
    if os.path.exists(DB_FOLDER):
        st.session_state.vector_store = load_existing_db(DB_FOLDER)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for file upload
with st.sidebar:
    st.header("1. Upload & Embed Document")
    uploaded_file = st.file_uploader("Upload a document to embed it", type=["pdf", "md", "txt"])
    
    if uploaded_file is not None:
        with st.spinner("Processing document and generating embeddings..."):
            
            # Extract the correct file extension so our loader knows how to read it
            file_ext = os.path.splitext(uploaded_file.name)[1].lower()
            
            # Save the uploaded file to a temporary location 
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            
            try:
                # Ingest the document and save it directly to company_vector_db
                st.session_state.vector_store = ingest_document(tmp_file_path, DB_FOLDER)
                st.success("Document processed and saved to the local database!")
            finally:
                # Clean up temp file
                if os.path.exists(tmp_file_path):
                    os.unlink(tmp_file_path)
    
    if st.session_state.vector_store is not None:
        st.success("Database is loaded and ready!")
        if st.button("Clear Memory & Delete Database"):
            # Wipe memory
            st.session_state.vector_store = None
            st.session_state.chat_history = []
            
            # Delete the physical folder from the hard drive
            if os.path.exists(DB_FOLDER):
                shutil.rmtree(DB_FOLDER)
            
            st.rerun()

st.header("2. Ask Questions")

# Display previous chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input text box at the bottom
query = st.chat_input("Ask a question about your documents...")

if query:
    if st.session_state.vector_store is None:
        st.error("Please upload a document first in the sidebar.")
    else:
        # Display the user's question
        st.session_state.chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)
            
        # Get the response from our AI chain
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = ask_question(st.session_state.vector_store, query)
                st.markdown(answer)
                # Save answer to chat history
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
