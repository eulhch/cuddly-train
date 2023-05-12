
import streamlit as st
import pandas as pd

conversation = {
    "Hi": "Hello! How can I assist you today?",
    "How are you?": "I'm doing well, thank you. How about you?",
    "I'm good, thanks.": "Great to hear! How can I help you today?",
    "Can you tell me a joke?": "Sure, why did the tomato turn red? Because it saw the salad dressing!",
    "Goodbye": "Goodbye! Have a great day.",
}

with st.beta_container():
    st.title("Dummy Robot")
    user_input = st.text_input("User Input")
    if st.button("Send"):
        if user_input in conversation:
            st.write(f"Robot: {conversation[user_input]}")
        else:
            st.write("Robot: Sorry, I didn't understand what you said. Please try again.")
```
