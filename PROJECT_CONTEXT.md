# PROJECT_CONTEXT.md

Use this file for stable project background that is too detailed for `AGENTS.md`.

## What This Project Is
A local PDF Retrieval-Augmented Generation (RAG) web application tutorial, built step-by-step.

## Current Goal
Build the application following a 5-step roadmap.

## Tech Stack
- **UI Framework:** Streamlit
- **Orchestration:** LangChain (`langchain`, `langchain-community`, `langchain-google-genai`)
- **Vector Database:** FAISS (in-memory `faiss-cpu`)
- **Embedding Model:** Google Cloud Embeddings via `GoogleGenerativeAIEmbeddings`
- **Chat Model:** Google Gemini via `ChatGoogleGenerativeAI`
- **Document Processing:** PyPDF (`pypdf`)

## Roadmap
- [x] **Step 1:** Environment Setup & Installing Dependencies
- [x] **Step 2:** Configuring Google Cloud / Gemini API Keys safely
- [x] **Step 3:** Building the Document Ingestion Pipeline
- [x] **Step 4:** Building the Retrieval & Question-Answering Chain
- [x] **Step 5:** Integrating Everything into a Clean Streamlit User Interface

## Success Criteria
This project is successful when the user has built a fully functioning local PDF RAG app using Streamlit and Gemini, having understood each step of the process.
