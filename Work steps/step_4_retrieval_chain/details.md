# Step 4: Building the Retrieval & Question-Answering Chain

**Objective:** Write the logic to take a user query, search our vector database for relevant chunks of text, and instruct the Gemini language model to answer the query based *only* on that context.

### What we did
1. **Refactored Project Structure**: At the user's request, we created a `rag_app/` folder to hold all the core application files moving forward, to keep the root directory clean. The `rag_core.py` script was moved here.
2. **Added `ask_question()` function** to `rag_app/rag_core.py`:
   - Configured `ChatGoogleGenerativeAI` to use the `gemini-2.5-flash` model.
   - Designed a system prompt to constrain the AI's answers to the retrieved text context.
   - Built a LangChain retrieval chain (`create_retrieval_chain`) that ties the vector store and the language model together.

### Files & Folders Created/Modified
- `rag_app/` (Folder - created)
- `rag_app/rag_core.py` (File - created, moving the logic from the root folder)
- `rag_core.py` in root (File - deleted)
- `Work steps/step_4_retrieval_chain/` (Folder)
- `Work steps/step_4_retrieval_chain/details.md` (File)
