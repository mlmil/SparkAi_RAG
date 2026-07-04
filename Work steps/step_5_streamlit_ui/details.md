# Step 5: Integrating Everything into a Clean Streamlit User Interface

**Objective:** Build a graphical web interface that allows the user to upload a PDF, run the backend processing automatically, and chat with the document using an intuitive messaging UI.

### What we did
1. **Created `rag_app/app.py`**: This script uses Streamlit to render the web page.
2. **Built the File Uploader**: Added a sidebar where users can upload PDFs. Since `PyPDFLoader` requires a file path, we used `tempfile` to temporarily save the uploaded file stream to the hard drive, process it with our `ingest_pdf()` function, and then delete the temporary file to save space.
3. **Session State Management**: We leveraged `st.session_state` so the app doesn't forget the vector database (or the chat history) every time you type a new message or click a button.
4. **Built the Chat UI**: Used `st.chat_message()` and `st.chat_input()` to create a ChatGPT-like interface that feeds directly into our `ask_question()` function.

### Files & Folders Created
- `rag_app/app.py` (File)
- `Work steps/step_5_streamlit_ui/` (Folder)
- `Work steps/step_5_streamlit_ui/details.md` (File)
