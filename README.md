# PDF Question Answering and Document Interaction App
## URL : https://pdfinteractor.streamlit.app/

# Overview

This is a Streamlit-based web application that allows users to interact with PDF documents, ask questions, and retrieve answers based on the content of the document. The application uses Groq LLM (Language Model), Google Generative AI, and Langchain for document processing and question answering.

## Features

- **Interact with Document**: Ask questions about the uploaded PDF, and the app will provide answers based on the document’s content.
- **Generate Questions from Document**: Generate questions related to a specific topic and get detailed answers based on the document.
- **Multiple PDF Upload**: Upload multiple PDFs for processing.
- **Styled Response Cards**: Answers are displayed in styled cards for a clean UI.
- **API Integration**: Utilizes Groq's powerful AI model and Google Generative AI embeddings for document processing and question answering.

## Prerequisites

Before running the app, ensure you have the following:

- Python 3.7+ installed
- Streamlit, Langchain, Groq API, and other dependencies

### Required Libraries

- `streamlit`
- `langchain`
- `langchain_groq`
- `langchain_community`
- `langchain_google_genai`
- `python-dotenv`
- `FAISS`
- `PyPDFDirectoryLoader`
- `PDFprocess_sample`

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Uzee62/Pdf_interactor.git
   cd Uzee62/Pdf_interactor
