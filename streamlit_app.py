import streamlit as st
import cohere
import random
import time
import openai

# App title
st.set_page_config(page_title="India MoF-WIP")

# Define a dictionary of user inputs and corresponding responses (rule-based)
responses = {
    "balance": "Your account balance is $5,000.",
    "transaction history": "You have three recent transactions: \n1. $100 deposit on 2023-09-25 \n2. $50 withdrawal on 2023-09-24 \n3. $200 deposit on 2023-09-23",
    "interest rates": "The current interest rate for savings accounts is 2.5% per annum.",
    "contact info": "You can reach our customer support at support@bank.com or call us at +1-800-123-4567.",
    "help": "I'm here to provide information about your account and our services. How can I assist you today?",
}

with st.sidebar:
		st.title('India MoF')
		# st.text('c6pobgap7gKlXOuU29e97W3Q0A2mJhg01hfbWwlJ')
		# openai_api_key = st.text_input('Cohere API Key')
		cohere_api_key = 'c6pobgap7gKlXOuU29e97W3Q0A2mJhg01hfbWwlJ'
        openai.api_key = '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 
		st.button('Proceed!')
		if not (openai_api_key):
			st.warning('Please enter your credentials!', icon='⚠️')
		else:
			st.success('Proceed to entering your prompt message!', icon='👉')

co = cohere.Client(cohere_api_key)

co = openai.

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "नमस्ते! कैसे मदद कर सकताहूँ?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
chat_history = []

# OpenAI function
def generate_response_oi(prompt_input):
        response = openai.ChatCompletion.create(
  			model="gpt-3.5-turbo",
			messages=[
					{"role": "system", "content": "You are a helpful assistant."},
					{"role": "user", "content": prompt_input},
				]
				)
        user_message = {"user_name": "User", "text": prompt_input}
        bot_message = {"user_name": "Chatbot", "text": response['choices'][0]['message']['content']}
        chat_history.append(user_message)
        chat_history.append(bot_message)
        return response['choices'][0]['message']['content']

# Cohere function
def generate_response_co(prompt_input):
		response = co.chat(
		prompt_input, 
		model="command-nightly", 
		# chat_history= chat_history,
		temperature=0.3
		)
		user_message = {"user_name": "User", "text": prompt_input}
		bot_message = {"user_name": "Chatbot", "text": response.text}
		chat_history.append(user_message)
		chat_history.append(bot_message)
		
		return response.text

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

load ='''
    Instructions: Consider that you are helpful chatbot for Indian bank, helping customer visiting bank by filling their forms. Reply bank in Hindi language if possible
'''

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
                if prompt in responses:
                        time.sleep(random.randint(1,3))
                        response = responses[prompt]
                else:
                        # response = generate_response_co(load+prompt)
                        response = generate_response_oi(load+prompt)
    st.write(response)
    message = {"role": "assistant", "content":response}
    st.session_state.messages.append(message)
