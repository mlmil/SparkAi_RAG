# Step 3: Building the Document Ingestion Pipeline

**Objective:** Write the backend logic to read a PDF file, split its contents into manageable chunks, compute vector embeddings using Google's models, and store them in a local FAISS database for fast retrieval.

### What we did
1. **Created `rag_core.py`**: This script will serve as the engine for our RAG app.
2. **Added `ingest_pdf()` function**:
   - Uses `PyPDFLoader` to extract text from the PDF.
   - Uses `RecursiveCharacterTextSplitter` to chunk the text (1000 characters per chunk, with 200 characters overlap to maintain context between chunks).
   - Uses `GoogleGenerativeAIEmbeddings` to convert the text into numerical vectors.
   - Uses `FAISS` to construct and return a searchable vector database.

### Files & Folders Created
- `rag_core.py` (File)
- `Work steps/step_3_document_ingestion/` (Folder)
- `Work steps/step_3_document_ingestion/details.md` (File)
