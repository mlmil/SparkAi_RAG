# Final Project Summary: Local PDF RAG Application

**Goal Achieved:** We successfully built a fully functioning local Retrieval-Augmented Generation (RAG) web application using Streamlit, LangChain, FAISS, and Google Gemini.

### System Architecture
- **Frontend:** Streamlit (`rag_app/app.py`)
- **Backend Orchestration:** LangChain LCEL (`rag_app/rag_core.py`)
- **Document Loading:** `PyPDFLoader` & `TextLoader` (Supports PDF, MD, TXT)
- **Chunking:** `RecursiveCharacterTextSplitter` (1000 chars, 200 overlap)
- **Embeddings:** `GoogleGenerativeAIEmbeddings` (using `models/gemini-embedding-2`)
- **Vector Database:** FAISS (Local persistence stored in `company_vector_db`)
- **Language Model:** `ChatGoogleGenerativeAI` (using `gemini-2.5-flash`)

### How to Run the App
Simply double-click the `Start_App.command` file in your project folder from your Mac's Finder, or run the following in your terminal:
```bash
cd "/Volumes/VADER/Antigravity Tutorials/PDF RAG"
source .venv/bin/activate
streamlit run rag_app/app.py
```

### The Journey (Work Steps)
1. **Environment Setup**: Created a Python virtual environment and installed core dependencies via `requirements.txt`.
2. **API Keys**: Configured your Google Gemini key safely in a `.env` file and protected it with `.gitignore`.
3. **Document Ingestion**: Wrote the backend logic to split documents and convert them into numerical vector embeddings.
4. **Retrieval Chain**: Used modern LangChain Expression Language (LCEL) to connect our vector database to the Gemini chat model.
5. **Streamlit UI**: Built the web frontend to upload files, display chat history, and manage the vector database in `session_state`.
6. **Database Persistence**: Added `save_local` and `load_existing_db` so the local business doesn't have to re-upload their massive documents every time the app opens.
7. **Multi-Format Support**: Upgraded the app to support Markdown and Text files in addition to PDFs.
8. **Bug Fixes**: Upgraded our initial code to use modern LCEL syntax and switched to Google's absolute latest `gemini-embedding-2` API model string to resolve cloud API changes.

### Files & Folders Created
- `rag_app/app.py` (Main UI script)
- `rag_app/rag_core.py` (Main Backend script)
- `.env` & `.gitignore` (Security)
- `requirements.txt` & `.venv/` (Environment setup)
- `company_vector_db/` (The physical database folder on your hard drive)
- `Start_App.command` (Clickable Mac shortcut)
- `Work steps/` (Folder containing detailed breakdowns of every single step we took)
