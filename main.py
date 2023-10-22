import streamlit as st
import csv
import os

# Filepaths to store data
HISTORY_FILE_PATH = "chat_history.csv"
FEEDBACK_FILE_PATH = "feedback.csv"

# Function to load existing chat data
def load_history():
    if os.path.exists(HISTORY_FILE_PATH):
        with open(HISTORY_FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            return [row for row in reader]
    return []

# Function to load feedback
def load_feedback():
    if os.path.exists(FEEDBACK_FILE_PATH):
        with open(FEEDBACK_FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            return [row for row in reader]
    return []

# Function to save chat data
def save_history(history):
    with open(HISTORY_FILE_PATH, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(history)

# Function to save feedback
def save_feedback(feedback):
    with open(FEEDBACK_FILE_PATH, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(feedback)

# Dummy function for chatbot's response (remove this if you have a real function)
def get_response(user_input):
    return "This is the chatbot's reply to " + user_input

history = load_history()
feedback_data = load_feedback()

# Streamlit UI

st.title("ChatGPT-like Interface")
st.sidebar.header("Instructions")
st.sidebar.text("Enter your message and click 'Send'.\nProvide feedback using thumbs up/down.")

col1, col2 = st.columns([3,1])

# Display chat history
for chat in history:
    if chat[0] == 'user':
        col1.write(f"You: {chat[1]}", unsafe_allow_html=True)
    else:
        col1.write(f"ChatGPT: {chat[1]}", unsafe_allow_html=True)

# User input
with col1:
    user_input = st.text_input("You")

# Send button
if col2.button('Send'):
    history.append(['user', user_input])
    response = get_response(user_input)
    history.append(['bot', response])
    save_history(history)
    st.experimental_rerun()

# Feedback
feedback = st.radio("Was this helpful?", ["👍", "👎"])
comments = st.text_area("Any comments?")

# Submit feedback button
if st.button('Submit Feedback'):
    feedback_data.append([feedback, comments])
    save_feedback(feedback_data)
    st.success("Thanks for your feedback!")
