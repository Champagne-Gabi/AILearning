import streamlit as st
import openai

# Load API key from Streamlit secrets and initialize client
client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(page_title="Prompt Coach for Marketers", page_icon="🤖")
st.title("🤖 Prompt Coach for Marketers")
st.markdown("Learn how to prompt better to do your job better.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly and expert marketing coach who teaches "
                "prompt engineering to marketers through real-world tasks. "
                "Keep responses practical, conversational, and actionable."
            )
        },
        {"role": "assistant", "content": "Hey there! Ready to sharpen your prompting skills? 🔥"}
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask your coach about prompting…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=st.session_state.messages
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"⚠️ Error: {str(e)}"
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
