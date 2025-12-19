import streamlit as st
from yt_1_indexing import generate_vector_store as gvs
from yt_2_retrieval import retriever_function as rf
from yt_3_augmentation import return_final_prompt as rfp
from yt_4_generation import give_answer as ga

st.set_page_config(page_title="YouTube QA Bot", layout="centered")
# st.markdown(
#     """
#     <style>
#     /* Page background */
#     .stApp {
#         background: radial-gradient(circle at top, #cab8d5, #ffefc1);
#         font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
#     }
#     /* Force headings and text to be darker */
#     h1, h2, h3, h4, h5, h6, p, div {
#         color: #1a1a1a !important; /* dark gray/black */
#     }


#     /* Main chat container */
#     section.main > div {
#         max-width: 420px;
#         margin: auto;
#         background: white;
#         border-radius: 20px;
#         box-shadow: 0 20px 50px rgba(0,0,0,0.12);
#         padding: 18px;
#     }

#     /* Chat messages */
#     .stChatMessage {
#         padding: 0;
#         margin-bottom: 14px;
#     }

#     /* Assistant bubble */
#     .stChatMessage[data-testid="stChatMessage-assistant"] > div {
#         background: #f3f4f6;
#         border-radius: 18px;
#         padding: 12px 14px;
#         color: #111827;
#         max-width: 85%;
#     }

#     /* User bubble */
#     .stChatMessage[data-testid="stChatMessage-user"] > div {
#         background: #6f42c1;
#         color: white;
#         border-radius: 18px;
#         padding: 12px 14px;
#         max-width: 85%;
#         margin-left: auto;
#     }

#     /* Quick reply buttons (pill style) */
#     .stButton > button {
#         width: 100%;
#         background: white;
#         border: 2px solid #6f42c1;
#         color: #6f42c1;
#         border-radius: 999px;
#         padding: 10px 14px;
#         font-weight: 500;
#         margin-top: 6px;
#     }

#     .stButton > button:hover {
#         background: #6f42c1;
#         color: white;
#     }

#     /* Input box */
#     textarea {
#         border-radius: 999px !important;
#         padding-left: 16px !important;
#     }

#     /* Remove Streamlit footer */
#     footer { visibility: hidden; }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.markdown("""
<style>
/* ========================================
   PRODUCTION CHATBOT - MODERN MESSAGING UI
   ======================================== */

/* Global Styles */
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
    padding: 10px;
}

/* Force dark text */
h1, h2, h3, h4, h5, h6, p, div, span, label {
    color: #1f2937 !important;
}

/* Main Chat Container - Centered Card */
section.main > div > div > div {
    max-width: 500px !important;
    margin: 0 auto !important;
    background: rgba(255, 255, 255, 0.95) !important;
    backdrop-filter: blur(20px);
    border-radius: 24px !important;
    box-shadow: 
        0 25px 50px -12px rgba(0, 0, 0, 0.25),
        0 0 0 1px rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    overflow: hidden;
}

/* Chat Messages Container */
.stChatMessage {
    margin: 0 !important;
    padding: 0 20px 16px 20px !important;
}

/* User Message Bubble */
.stChatMessage[data-testid="stChatMessage-user"] {
    padding-top: 12px !important;
}

.stChatMessage[data-testid="stChatMessage-user"] > div > div {
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
    color: white !important;
    border-radius: 20px 20px 4px 20px !important;
    padding: 14px 18px !important;
    margin: 0 0 0 auto !important;
    max-width: 80% !important;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    font-weight: 500;
    line-height: 1.5;
    position: relative;
}

.stChatMessage[data-testid="stChatMessage-user"] > div > div::before {
    content: '';
    position: absolute;
    right: -8px;
    top: 12px;
    width: 0;
    height: 0;
    border: 8px solid transparent;
    border-left-color: #3b82f6;
}

/* Assistant Message Bubble */
.stChatMessage[data-testid="stChatMessage-assistant"] {
    padding-top: 12px !important;
}

.stChatMessage[data-testid="stChatMessage-assistant"] > div > div {
    background: #ffffff !important;
    color: #1f2937 !important;
    border-radius: 20px 20px 20px 4px !important;
    padding: 16px 20px !important;
    margin: 0 !important;
    max-width: 80% !important;
    box-shadow: 
        0 2px 8px rgba(0, 0, 0, 0.08),
        0 1px 2px rgba(0, 0, 0, 0.04);
    border: 1px solid rgba(0, 0, 0, 0.05);
    font-weight: 400;
    line-height: 1.6;
    position: relative;
}

.stChatMessage[data-testid="stChatMessage-assistant"] > div > div::before {
    content: '';
    position: absolute;
    left: -8px;
    top: 12px;
    width: 0;
    height: 0;
    border: 8px solid transparent;
    border-right-color: #ffffff;
    border-top-color: #ffffff;
}

/* Chat Avatar */
.stChatMessage[data-testid="stChatMessage-user"] > div::before {
    content: '🧑';
    font-size: 24px;
    position: absolute;
    right: 12px;
    top: 8px;
    z-index: 10;
}

.stChatMessage[data-testid="stChatMessage-assistant"] > div::before {
    content: '🤖';
    font-size: 24px;
    position: absolute;
    left: 12px;
    top: 8px;
    z-index: 10;
}

/* Input Container */
.stTextArea textarea {
    border-radius: 24px !important;
    border: 2px solid #e5e7eb !important;
    padding: 16px 20px !important;
    font-size: 16px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    transition: all 0.2s ease !important;
    background: #fafbfc !important;
    font-family: inherit !important;
    min-height: 56px !important;
}

.stTextArea textarea:focus {
    border-color: #3b82f6 !important;
    box-shadow: 
        0 0 0 3px rgba(59, 130, 246, 0.1),
        0 4px 12px rgba(0, 0, 0, 0.12) !important;
    background: white !important;
}

/* Primary Button */
.stButton > button {
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 24px !important;
    padding: 12px 24px !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4) !important;
    height: 48px !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.5) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* Secondary Buttons (Quick replies) */
button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.9) !important;
    border: 2px solid #d1d5db !important;
    color: #374151 !important;
    border-radius: 20px !important;
    padding: 10px 20px !important;
    font-weight: 500 !important;
    margin: 4px !important;
    transition: all 0.2s ease !important;
}

button[kind="secondary"]:hover {
    background: #3b82f6 !important;
    border-color: #3b82f6 !important;
    color: white !important;
    transform: translateY(-1px) !important;
}

/* Hide Streamlit elements */
footer, header, .stStatusWidget {
    visibility: hidden !important;
}

/* Scrollbar */
section.main::-webkit-scrollbar {
    width: 6px;
}

section.main::-webkit-scrollbar-track {
    background: rgba(0, 0, 0, 0.02);
    border-radius: 10px;
}

section.main::-webkit-scrollbar-thumb {
    background: rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}

section.main::-webkit-scrollbar-thumb:hover {
    background: rgba(0, 0, 0, 0.15);
}

/* Typing Animation */
@keyframes typing {
    0%, 60%, 100% { transform: translateY(0); }
    30% { transform: translateY(-8px); }
}

.typing-indicator {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 16px;
    background: rgba(243, 244, 246, 0.8);
    border-radius: 20px 20px 20px 4px;
    max-width: 80%;
}

.typing-dots {
    display: flex;
    gap: 4px;
}

.typing-dots span {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #9ca3af;
    animation: typing 1.4s infinite ease-in-out;
}

.typing-dots span:nth-child(2) { animation-delay: 0.2s; }
.typing-dots span:nth-child(3) { animation-delay: 0.4s; }

/* Responsive */
@media (max-width: 768px) {
    section.main > div > div > div {
        max-width: 95vw !important;
        margin: 5px !important;
        border-radius: 20px !important;
    }
    
    .stChatMessage > div > div {
        max-width: 90% !important;
    }
}
</style>
""", unsafe_allow_html=True)

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