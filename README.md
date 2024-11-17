## PDF Interactor
## URL : https://pdfinteractor.streamlit.app/

# Overview


PDF Interactor is a Streamlit-based application that allows users to upload PDF documents and interact with them by asking questions. It leverages LangChain, Google Generative AI Embeddings, and FAISS for document processing and retrieval.

# Features

Upload multiple PDF documents.

Process and split PDFs into smaller chunks for efficient query processing.

Search and retrieve relevant content from PDFs using vector embeddings.

Answer detailed questions based on the uploaded content.

Interactive and user-friendly Streamlit interface.


# Technologies Used

Python

Streamlit for the front end

FAISS for vector storage

LangChain for text splitting and processing

Google Generative AI Embeddings for embedding generation

PyPDFLoader for document loading

# Usage

Upload PDF files using the sidebar.

Press Submit button to process the data

Once the files are processed, enter your question in the text input box.

The application will return an answer based on the uploaded content.
