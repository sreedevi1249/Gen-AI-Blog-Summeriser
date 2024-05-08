import os
from llama_index.llms.llama_api import LlamaAPI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_blogsummary_response(blogurl):
    llm = LlamaAPI(model="llama-70b-chat",api_key=os.environ["LLAMA_API_Key"])
    response = llm.complete(f"summerise this link {blogurl} in 5 points")
    return response

st.set_page_config(page_title="Blog Summeriser")
st.header("Blog Summeriser Application")
input  = st.text_input("Blog Url: ",key="url")
response = get_blogsummary_response(input)
submit = st.button("Enter blog url")

if submit:
    st.subheader("summary is")
    st.write(response)




