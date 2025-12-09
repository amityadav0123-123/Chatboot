# 🤖 AI ChatBot using Streamlit & Google Gemini

This project is a beautifully designed AI ChatBot web application built using Streamlit and Google Gemini (gemini-pro model).
It provides a smooth chat experience with animations, gradient UI, and real-time conversation history.

## 🚀 Features
✅ 1. Intelligent Chatbot (Gemini Pro)

Uses Google Generative AI to generate human-like responses.

Maintains chat history using st.session_state.

## ✅ 2. Modern UI with Animations

Gradient background

Floating chat window

Smooth fade-in animation for messages

Stylish date banner

## ✅ 3. Persistent Chat Session

Chat session maintained until browser refresh.

Uses model.start_chat() to keep conversation context.

# ✅ 4. Optimized Performance

Response generation wrapped in @st.cache_data to avoid redundant API calls.

### ✅ 5. Streamlit Chat Input

Clean input box (st.chat_input) for natural chat experience.

### 🛠️ Tech Stack
Technology	Purpose
Streamlit	Frontend UI, interactions
Google Gemini (gemini-pro)	Chat response generation
Python	Core logic
HTML/CSS inside Streamlit	Custom UI styling
Session State	History & state management

### 📁 Project Structure
├── app.py
├── README.md
└── requirements.txt

### 📦 Installation Guide
1. Clone the Repository
git clone https://github.com/your-username/streamlit-chatbot.git
cd streamlit-chatbot

### 2. Create Virtual Environment (optional)
python -m venv venv
source venv/Scripts/activate   # Windows

### 3. Install Dependencies
pip install -r requirements.txt

🔑 Add Your Google Gemini API Key

Inside the code:

api_key = "YOUR_API_KEY"


Or store it securely using a .env file.

### ▶️ Run the Application

Start Streamlit app using:

streamlit run app.py


The app will open automatically in your browser at:

http://localhost:8501

### 📝 How It Works

When the app starts, it initializes:

Google Gemini model

Chat session (start_chat)

Empty chat history

User enters a message

App sends it to Gemini

Response is displayed with animations

Conversation continues with full context

### 🎨 UI Highlights

✔ Animated messages
✔ Gradient background
✔ Glass-morphism chat card
✔ Responsive layout
✔ Modern typography

### ⚠️ Notes

Requires a stable internet connection to call Gemini API.

Do NOT expose API keys publicly (use .env in production).

st.cache_data may cache responses for repeated questions—use wisely.

📜 License

This project is open-source and free to use for learning or enhancement.
