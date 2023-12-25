import streamlit as st
from transformers import pipeline


# Function to load the model
@st.cache_data
def load_model():
    summarizer = pipeline("text2text-generation", model="pk248/pegasus-samsum")
    return summarizer


# Load the model
model = load_model()

# Streamlit UI
st.title("Dialogue Summarization App")
st.write("This app uses the pk248/pegasus-samsum model to summarize coversations.")

# Text input
user_input = st.text_area("Enter text to summarize:", height=200)

# Summarize button
if st.button("Summarize"):
    if user_input:
        # Model inference
        summary = model(user_input, max_length=1000, min_length=5, length_penalty=2.0)
        st.write(summary[0]["generated_text"])
    else:
        st.write("Please enter some text to summarize.")
