import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/research-lite"
API_KEY = "mysecret123"

st.set_page_config(page_title="AI Research Assistant", layout="wide")

# -----------------------
# Custom CSS
# -----------------------
st.markdown("""
<style>
.chat-container {
    max-width: 800px;
    margin: auto;
}

.user-msg {
    background-color: #2563eb;
    color: white;
    padding: 12px;
    border-radius: 10px;
    margin: 10px 0;
    text-align: right;
}

.bot-msg {
    background-color: #1e293b;
    color: #f1f5f9;
    padding: 12px;
    border-radius: 10px;
    margin: 10px 0;
}

.header {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subheader {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Header
# -----------------------
st.markdown('<div class="header">🧠 AI Research Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Chat with your AI research agent</div>', unsafe_allow_html=True)

# -----------------------
# Session state (chat history)
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------
# Chat container
# -----------------------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# Input box (bottom)
# -----------------------
query = st.chat_input("Ask anything...")

if query:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": query})

    # Call API
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                API_URL,
                json={"query": query},
                headers={
                    "x-api-key": API_KEY,
                    "Content-Type": "application/json"
                }
            )

            if response.status_code == 200:
                data = response.json()
                answer = data.get("answer", "No answer")

            else:
                answer = f"Error: {response.text}"

        except Exception as e:
            answer = f"Request failed: {str(e)}"

    # Add bot response
    st.session_state.messages.append({"role": "bot", "content": answer})

    # Rerun to update UI
    st.rerun()
