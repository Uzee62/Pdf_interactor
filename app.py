import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from  PDFprocess_sample import process_pdf

# Loading GROQ and Google API
load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"]= os.getenv('GOOGLE_API_KEY')

#Loading CSS files

def load_css(file_name):
    with open(file_name) as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css('CSS/style.css')

#setting up LLM
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="Llama3-8b-8192"
)


prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question. Try to answer in detail in 1500 words
    <context>
    {context}
    <context>
    Questions: {input}
    """
)

input_method = st.sidebar.selectbox("Choose a method" , ["Choose input method...","Interact with Doc", "Get Ques from Doc"])



st.sidebar.title("Upload your pdf")

main_placeholder = st.empty()
#Document upload
uploaded_file = st.sidebar.file_uploader("_____________________________________", type="pdf", accept_multiple_files=True)
st.sidebar.write("Press Submit to process:")
process = st.sidebar.button("Submit")

#Document processing to convert it into vectors
if process:
    if uploaded_file:
        # Process the uploaded PDF file
        process_pdf(uploaded_file)
    else:
        st.warning("Please upload a PDF file.")
        
if input_method == "Choose input method...":
    st.title(f"Welcome You all!")
    st.title("Choose an option in the sidebar")
    st.title("Now, let's get started!") 
    
        
#If User wants to interact with the document
elif input_method == "Interact with Doc":
    st.title(f"let's Interact with pdf's")

    prompt1 = st.text_input("______", placeholder="Enter your Question")


    # Generate response if question is entered
    if prompt1 and "vectors" in st.session_state:
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vectors.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        
        
        response = retrieval_chain.invoke({'input': prompt1})

        # st.write(response['answer'])
        
        #Get the respose in the card
        st.markdown(
        f"""
        <div class="card">
            <div class="response">{response['answer']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
        
        
        
#When User wants to get questions from the doc based on certain topic
elif input_method == "Get Ques from Doc":
    st.title(f"Let's Get Ques from Document")
    
    prompt2 = """Based on the topic of {topic}, 
                kindly provide a comprehensive list of all possible questions that could arise. 
                For each question, provide detailed and explanatory answers in atleast 1000 words detail based on the context,
                ensuring that the responses are as informative as possible.
                make sure you strictly follow the {topic}"""
    topic = st.text_input("Enter a topic", placeholder="What is your topic")
    
    # Generate response if question is entered
    if topic and "vectors" in st.session_state:
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vectors.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        
        
        response = retrieval_chain.invoke({'input': prompt2})
        
        #Get the respose in the card
        st.markdown(
        f"""
        <div class="card">
            <div class="response">{response['answer']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    