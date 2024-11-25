import streamlit as st
from transformers import pipeline

# Load the summarization model
@st.cache_resource
def load_model():
    summarizer = pipeline("summarization", model="t5-small")
    return summarizer

summarizer = load_model()

# Streamlit UI
st.title("Chatbot Text Summarizer")
st.subheader("Summarize any text quickly!")

# User input
input_text = st.text_area("Enter text to summarize", height=200)

# Summarization
if st.button("Summarize"):
    if input_text.strip():
        with st.spinner("Summarizing..."):
            summary = summarizer(input_text, max_length=50, min_length=10, do_sample=False)
            st.success("Summarization Completed!")
            st.write("### Summary:")
            st.write(summary[0]['summary_text'])
    else:
        st.error("Please enter some text to summarize.")
