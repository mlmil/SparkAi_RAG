import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# We define the embedding model here so both save and load functions can use it
embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")

def ingest_document(file_path: str, db_path: str = "company_vector_db"):
    """
    Loads a document (PDF, MD, TXT), chunks the text, creates embeddings, and saves the FAISS vector store.
    """
    print(f"Loading {file_path}...")
    
    # Determine which loader to use based on the file extension
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif file_ext in [".md", ".markdown", ".txt"]:
        loader = TextLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_ext}")

    documents = loader.load()

    print("Chunking text...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)

    print("Creating embeddings and storing in FAISS...")
    # Create the vector store from our chunks
    vector_store = FAISS.from_documents(chunks, embedding_model)
    
    # Save the database permanently to the hard drive
    vector_store.save_local(db_path)
    print("Ingestion complete and database saved locally!")
    
    return vector_store

def load_existing_db(db_path: str = "company_vector_db"):
    """
    Loads an existing FAISS database from the hard drive.
    """
    # allow_dangerous_deserialization=True is required because FAISS uses pickle. 
    # This is safe because we created the database files ourselves locally.
    return FAISS.load_local(db_path, embedding_model, allow_dangerous_deserialization=True)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def ask_question(vector_store, query: str):
    """
    Takes a FAISS vector store and a user query, retrieves relevant chunks, 
    and generates an answer using Gemini with LangChain Expression Language (LCEL).
    """
    # 1. Initialize the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
    
    # 2. Define the system prompt
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, say that you don't know. "
        "Use three sentences maximum and keep the answer concise.\n\n"
        "{context}"
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    # 3. Create the retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 3}) 
    
    # 4. Build the modern LCEL (LangChain Expression Language) Chain
    rag_chain = (
        {"context": retriever | format_docs, "input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    # 5. Execute
    print(f"Asking Gemini: {query}")
    return rag_chain.invoke(query)
