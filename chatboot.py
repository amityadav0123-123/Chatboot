import streamlit as st
import google.generativeai as genai
from datetime import date
import time

# Streamlit app configuration
st.set_page_config(page_title="ChatBot", page_icon='🤖', layout='wide', initial_sidebar_state='collapsed')

# Add custom markdown header for a clean, modern look
st.markdown("<h2 style='text-align: center; font-family: Arial, sans-serif; color: #fff;'>🤖 ChatBot</h2>", unsafe_allow_html=True)

# Initialize session state with model start chat message
if 'chat' not in st.session_state:
    api_key = "AIzaSyA1cn1sv6CQciDScQ60tDcFQvvg3A1trlA"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.history = []

# Initialize session state with today's date
if 'today_date' not in st.session_state:
    st.session_state.today_date = date.today().strftime("%d %B %Y")

# Caching the response generation function to optimize performance
@st.cache_data
def get_response(question):
    try:
        response = st.session_state.chat.send_message(question)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Sorry, there was an issue processing your message."

# Styling with modern UI elements and animations
st.markdown("""
    <style>
        /* Background with gradient */
        .stApp {
            background: linear-gradient(to right, #a1c4fd, #c2e9fb);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Chat window styling */
        .chat-box {
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 20px;
            width: 100%;
            max-width: 800px;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.1);
            overflow-y: auto;
            height: 400px;
        }

        /* User message styling */
        .user-message {
            background-color: #4a90e2;
            color: white;
            padding: 12px 20px;
            border-radius: 12px;
            margin: 10px 0;
            max-width: 80%;
            animation: fadeIn 0.5s ease-out;
        }

        /* Bot message styling */
        .bot-message {
            background-color: #ffffff;
            color: #333;
            padding: 12px 20px;
            border-radius: 12px;
            margin: 10px 0;
            max-width: 80%;
            border: 1px solid #e0e0e0;
            animation: fadeIn 0.5s ease-out;
        }

        /* Date banner */
        .date-banner {
            text-align: center;
            background-color: #333;
            color: #fff;
            padding: 10px;
            border-radius: 25px;
            font-size: 20px;
            width: 80%;
            margin-bottom: 20px;
        }

        /* Chat container styling */
        .message-container {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }

        /* Animation for messages */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }

    </style>
""", unsafe_allow_html=True)

# Display the current date in a sleek banner
st.markdown(f'<div class="date-banner">{st.session_state.today_date}</div>', unsafe_allow_html=True)

# Create a box to contain all chat messages
with st.container():
    chat_box = st.empty()  # Create an empty container for the chat messages
    
    # Display chat history
    for message in st.session_state.history:
        if message["user"]:
            st.markdown(f'<div class="message-container">'
                        f'<div class="user-message">{message["user"]}</div></div>', unsafe_allow_html=True)
        if message["bot"]:
            st.markdown(f'<div class="message-container">'
                        f'<div class="bot-message">{message["bot"]}</div></div>', unsafe_allow_html=True)

# Display a loading spinner while waiting for the bot response
with st.spinner("🤖 Generating response... please wait!"):
    # Input box for user questions
    question = st.chat_input("Ask me anything!")

    if question:
        # Add user message with placeholder for bot response
        st.session_state.history.append({"user": question, "bot": "..."})
        
        # Generate response for the current question
        response = get_response(question)
        
        # Replace the placeholder with the actual response
        st.session_state.history[-1]["bot"] = '🤖\n\n' + response
        
        # Automatically update the UI after generating the response
        st.experimental_rerun()  # Refresh the UI with the new chat message
