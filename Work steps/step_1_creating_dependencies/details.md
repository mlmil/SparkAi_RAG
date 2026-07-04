# Step 1: Environment Setup & Installing Dependencies

**Objective:** Set up a clean, isolated Python environment and install the required libraries for our local PDF RAG web application.

### What we did
1. **Created a virtual environment** to isolate our project dependencies from the rest of the system.
2. **Activated the virtual environment**.
3. **Created a `requirements.txt` file** containing the core libraries needed for the project.
4. **Installed the dependencies** using `pip`.

### Dependencies installed (`requirements.txt`)
- `streamlit`: For building the web UI.
- `langchain`: The core framework for orchestrating language model workflows.
- `langchain-community`: Contains integrations like FAISS (vector DB) and PyPDF (document loader).
- `langchain-google-genai`: The specific integration for using Google's Gemini models and embeddings.
- `faiss-cpu`: A fast, local, in-memory vector database for similarity search.
- `pypdf`: Used to parse and extract text from our PDF documents.

### Terminal Commands Executed
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Files & Folders Created
- `requirements.txt` (File)
- `.venv/` (Folder - Python virtual environment)
- `Work steps/step_1_creating_dependencies/` (Folder)
- `Work steps/step_1_creating_dependencies/details.md` (File)
