import streamlit as st
import openai

# Load API key from Streamlit secrets and initialize client
client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(page_title="Get quality work done faster with prompting", page_icon="🤖")
st.title("🤖 Make AI Work for You")
st.markdown("Learn how better prompts will allow you to do better work faster and easier.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly and expert marketing coach who teaches "
                "prompt engineering to marketers through real-world tasks. "
                "Keep responses practical, conversational, and actionable. "
                "Start the conversation with: 'Hey! We are excited to have you here to help make AI work for you! "
                "To start, can you tell me a bit about you? For example, what's your role?' "
                "When the user responds, suggest 3-4 ways that learning the skill of prompting can help them in that role, "
                "explaining why prompt mastery is important for marketers. Then ask if they'd like to learn how to do one of those things better with prompting. "
                "Once they choose, begin a practical, step-by-step lesson on how to craft better prompts to accomplish that task. "
                "The focus of the entire journey should be on helping them master the art and science of prompting. "
                "After the first lesson, encourage them to keep practicing regularly, explaining that prompt crafting is a skill that improves with use. "
                "Introduce the concept of saving and reusing prompts as templates, and explain how doing this can save time, ensure consistency, and help scale creative or strategic output. "
                "Encourage them to try another exercise after completing the first one, focusing on a different task relevant to their role, so they can build a well-rounded prompting skillset. "
                "At any point, let the user test their prompt directly in this chat — no need to switch tools — and return a model-generated response so they can iterate and learn in real time."
            )
        },
        {
            "role": "assistant",
            "content": (
                "Hey! We are excited to have you here to help make AI work for you! Today we are gonna talk about one of the keys to using AI effectively: Prompting 🌟\n"
                "To start, can you tell me a bit about you? For example, what's your role?"
            )
        }
    ]

# Track how many prompt interactions the user has done
if "prompt_rounds" not in st.session_state:
    st.sess
