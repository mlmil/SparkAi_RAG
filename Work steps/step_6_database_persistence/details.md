# Step 6 (Bonus): Database Persistence

**Objective:** Save the vector database directly to the hard drive so the user does not have to upload their company documents every time the web application is restarted.

### What we did
1. **Added `save_local` logic**: In `rag_core.py`, modified the `ingest_pdf` function to call `vector_store.save_local("company_vector_db")`. This creates a physical folder on the hard drive containing the FAISS index and the document chunks.
2. **Added `load_existing_db` function**: A new function to read `"company_vector_db"` from disk.
3. **Streamlit Persistence on Startup**: Modified `app.py` so that when the app boots up, it checks if `company_vector_db` exists in the local directory. If it does, it loads it immediately into `st.session_state`, allowing the user to begin chatting with their documents instantly.
4. **Enhanced Reset Button**: Updated the clear button to completely delete the `company_vector_db` folder so the user can wipe the knowledge base and start from scratch when needed.

### Files & Folders Created
- `Work steps/step_6_database_persistence/` (Folder)
- `Work steps/step_6_database_persistence/details.md` (File)
- `company_vector_db/` (Folder - created dynamically when running the app)
