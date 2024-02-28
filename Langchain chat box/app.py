from langchain.llms import OpenAI 
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables
load_dotenv()

# Function to load OpenAI model and get responses
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    response = llm(question)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded") 

# Header
st.title("Langchain Q&A Application")

# User Input
input_question = st.text_input("Input your question:", key="input")

# Ask Button
if st.button("Ask the question"):
    if input_question:
        with st.spinner("Thinking..."):
            response = get_openai_response(input_question)
            st.success("Here's the response:")
            st.write(response)
    else:
        
        st.warning("Please input a question before asking.")

# Footer
st.markdown("---")
st.write("Made with ❤️ by Your Abhishek")
