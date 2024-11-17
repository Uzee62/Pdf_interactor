import tempfile
import streamlit as st
import pickle
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import faiss 


def process_pdf(uploaded_file):
    
    all_documents = []
    st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    main_placeholder = st.empty()
    # Creating  a temporary file to store the uploaded PDF's
    main_placeholder.text("Data Loading...Started...✅✅✅")
    for uploaded_file in uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False , suffix='.pdf') as temp_file:
            temp_file.write(uploaded_file.read()) ## write file to temporary
            temp_file_path = temp_file.name  # Get the temporary file path
            
            
            # Load the PDF's from the temporary file path
            
        
        loader = PyPDFLoader(temp_file_path) # Document loader
        doc= loader.load() # load Document 
        main_placeholder.text("Text Splitter...Started...✅✅✅")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # Recursive Character String
        #final_documents = text_splitter.split_documents(doc)# splitting
        final_documents = text_splitter.split_documents(doc)
        all_documents.extend(final_documents)
        
        
        if all_documents:
            main_placeholder.text("Embedding Vector Started Building...✅✅✅")
            st.session_state.vectors = FAISS.from_documents(all_documents,st.session_state.embeddings)
            st.session_state.docs = all_documents 
            
            # Save FAISS vector store to disk
            faiss_index = st.session_state.vectors.index  # Extract FAISS index
            faiss.write_index(faiss_index, "faiss_index.bin")  # Save index to a binary file
            main_placeholder.text("Vector database created!...✅✅✅")   
            
        else:
            st.error("No documents found after processing the uploaded files or the pdf is corrupted / unsupported.")
        
