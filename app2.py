import streamlit as st
from yt_1_indexing import generate_vector_store as gvs
from yt_2_retrieval import retriever_function as rf
from yt_3_augmentation import return_final_prompt as rfp
from yt_4_generation import give_answer as ga

st.set_page_config(page_title="YouTube QA Bot", layout="centered")
st.markdown(
    """
    <style>
    /* Page background */
    .stApp {
        background: radial-gradient(circle at top, #cab8d5, #ffefc1);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    /* Force headings and text to be darker */
    h1, h2, h3, h4, h5, h6, p, div {
        color: #1a1a1a !important; /* dark gray/black */
    }


    /* Main chat container */
    section.main > div {
        max-width: 420px;
        margin: auto;
        background: white;
        border-radius: 20px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.12);
        padding: 18px;
    }

    /* Chat messages */
    .stChatMessage {
        padding: 0;
        margin-bottom: 14px;
    }

    /* Assistant bubble */
    .stChatMessage[data-testid="stChatMessage-assistant"] > div {
        background: #f3f4f6;
        border-radius: 18px;
        padding: 12px 14px;
        color: #111827;
        max-width: 85%;
    }

    /* User bubble */
    .stChatMessage[data-testid="stChatMessage-user"] > div {
        background: #6f42c1;
        color: white;
        border-radius: 18px;
        padding: 12px 14px;
        max-width: 85%;
        margin-left: auto;
    }

    /* Quick reply buttons (pill style) */
    .stButton > button {
        width: 100%;
        background: white;
        border: 2px solid #6f42c1;
        color: #6f42c1;
        border-radius: 999px;
        padding: 10px 14px;
        font-weight: 500;
        margin-top: 6px;
    }

    .stButton > button:hover {
        background: #6f42c1;
        color: white;
    }

    /* Input box */
    textarea {
        border-radius: 999px !important;
        padding-left: 16px !important;
    }

    /* Remove Streamlit footer */
    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🎥 YouTube QA Bot")

# Step 1: Input YouTube link (only shown if no vector store yet)
if "vector_store" not in st.session_state:
    st.markdown("### 📺 Load a YouTube video")
    video_link = st.text_input("Paste YouTube video link here:")

    if st.button("Process Video", use_container_width=True):
        with st.spinner("Fetching transcript and generating embeddings..."):
            vector_store = gvs(video_link)
            if isinstance(vector_store, str):
                st.error("Transcript not available for this video.")
            else:
                st.session_state.vector_store = vector_store
                st.session_state.chat_history = []  # initialize chat history
                st.success("Transcript processed! You can now chat with the bot.")

# Step 2: Chatbot screen (only shown if vector store exists)
if "vector_store" in st.session_state:
    st.markdown("### 💬 Chat with the transcript")

    # Display previous chat messages
    if "chat_history" in st.session_state:
        for role, text in st.session_state.chat_history:
            with st.chat_message(role):
                st.markdown(text)

    # Chat input at the bottom
    user_query = st.chat_input("Ask a question about the video...")
    if user_query:
        # Show user message
        st.session_state.chat_history.append(("user", user_query))
        with st.chat_message("user"):
            st.markdown(user_query)

        # Generate answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                retriever = rf(st.session_state.vector_store)
                final_prompt = rfp(user_query, retriever)
                result = ga(final_prompt)
                st.markdown(result)
                st.session_state.chat_history.append(("assistant", result))

    # Exit button to clear state and go back
    if st.button("Exit", use_container_width=True):
        st.session_state.clear()
        st.rerun()