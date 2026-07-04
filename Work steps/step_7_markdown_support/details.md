# Step 7 (Bonus): Multi-Format Support (Markdown and Text)

**Objective:** Expand the RAG application's capabilities to ingest raw text and markdown files in addition to PDFs.

### What we did
1. **Imported `TextLoader`**: In `rag_core.py`, added LangChain's built-in `TextLoader`.
2. **Renamed `ingest_pdf` to `ingest_document`**: Updated the function name to reflect its broader purpose.
3. **Added extension routing**: Modified `ingest_document` to inspect the `file_path`. If it's `.pdf`, it uses `PyPDFLoader`. If it's `.md` or `.txt`, it uses `TextLoader`.
4. **Updated UI limits**: In `app.py`, we changed the file uploader to accept `type=["pdf", "md", "txt"]`.
5. **Preserved file extensions**: Updated the temporary file creation logic in Streamlit so that the saved temporary file has the exact same extension as the uploaded file, allowing `ingest_document` to correctly route it.

### Files Modified
- `rag_app/rag_core.py`
- `rag_app/app.py`
- `Work steps/step_7_markdown_support/` (Folder)
- `Work steps/step_7_markdown_support/details.md` (File)
