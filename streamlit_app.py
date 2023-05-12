import streamlit as st
from streamlit_chat import message

#Source : https://towardsdatascience.com/build-your-own-chatgpt-like-app-with-streamlit-20d940417389

# Setting page title and header
st.set_page_config(page_title="BOB", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>BOB - a totally harmless chatbob 😬</h1>", unsafe_allow_html=True)

# Initialise session state variables
if 'bot_answers' not in st.session_state:
    st.session_state['bot_answers'] = []
if 'user_prompt' not in st.session_state:
    st.session_state['user_prompt'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    

# generate a response
def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})

    response = 'Dummy response'
    st.session_state['messages'].append({"role": "assistant", "content": response})
    return response

# container for chat history
response_container = st.container()
# container for text box
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("You:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        output = generate_response(user_input)
        st.session_state['user_prompt'].append(user_input)
        st.session_state['bot_answers'].append(output)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['bot_answers'])):
            message(st.session_state["user_prompt"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["bot_answers"][i], key=str(i))
            
clear_button = st.button("Clear Conversation", key="clear")
# reset everything
if clear_button:
    st.session_state['bot_answers'] = []
    st.session_state['user_prompt'] = []
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
