
import streamlit as st
import openai

st.set_page_config(page_title="Prompt Coach for Marketers", page_icon="🤖")

# --- Setup ---
st.title("🤖 Prompt Coach for Marketers")
st.markdown("Learn how to prompt better to do your job better.")

# --- API Key Input ---
api_key = st.text_input("Enter your OpenAI API key:", type="password")
if not api_key:
    st.warning("Please enter your OpenAI API key to start.")
    st.stop()

openai.api_key = api_key

# --- Session State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly and expert marketing coach who teaches prompt engineering to marketers through real-world tasks. Keep responses practical and engaging."},
        {"role": "assistant", "content": "Hi there! 👋 I'm your Prompt Coach. Ready to boost your marketing game with better AI prompts?"}
    ]

# --- Chat Display ---
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# --- User Input ---
user_input = st.chat_input("Ask your coach about prompting…")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # --- Call OpenAI API ---
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o",
                    messages=st.session_state.messages
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"Error: {str(e)}"
            st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
