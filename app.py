import streamlit as st
from bert_summarizer import BertSummarizer
from gpt2_summarizer import GPT2Summarizer
from xlnet_summarizer import XLNetSummarizer

# Initialize summarizers
bert_summarizer = BertSummarizer()
gpt2_summarizer = GPT2Summarizer()
xlnet_summarizer = XLNetSummarizer()

def summarize_text(text, model_choice):
    if model_choice == "BERT":
        return bert_summarizer.summarize(text, min_length=60)
    elif model_choice == "GPT2":
        return gpt2_summarizer.summarize(text, min_length=60)
    elif model_choice == "XLNet":
        return xlnet_summarizer.summarize(text, min_length=60)
    else:
        return "Invalid model selection."

# Streamlit App Layout
st.title("Text Summarization App")

# Input text box
input_text = st.text_area("Enter Text to Summarize", height=250)

# Model selection
model_choice = st.selectbox("Choose a Summarization Model", ["BERT", "GPT2", "XLNet"])

# Summarize button
if st.button("Summarize"):
    if input_text:
        with st.spinner("Generating Summary..."):
            summary = summarize_text(input_text, model_choice)
            st.subheader("Summary:")
            st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
