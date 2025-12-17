import streamlit as st
from yt_1_indexing import generate_vector_store as gvs
from yt_2_retrieval import retriever_function as rf
from yt_3_augmentation import return_final_prompt as rfp
from yt_4_generation import give_answer as ga

st.set_page_config(page_title="YouTube QA Bot", layout="centered")
st.header("🎥 YouTube QA Bot")

# Step 1: Input YouTube link (only shown if no vector store yet)
if "vector_store" not in st.session_state:
    video_link = st.text_input("Enter YouTube video link:")

    if st.button("Process Video"):
        with st.spinner("Fetching transcript and generating embeddings..."):
            vector_store = gvs(video_link)
            if isinstance(vector_store, str):
                st.error("Transcript not available for this video.")
            else:
                st.session_state.vector_store = vector_store
                st.success("Transcript processed! You can now ask questions.")

# Step 2: Chatbot screen (only shown if vector store exists)
if "vector_store" in st.session_state:
    st.subheader("Ask questions about the video transcript")
    user_query = st.text_input("Enter your question:")

    if st.button("Generate Answer"):
        with st.spinner("Generating answer..."):
            retriever = rf(st.session_state.vector_store)
            final_prompt = rfp(user_query, retriever)
            result = ga(final_prompt)
            st.write(result)

    # Exit button to clear state and go back
    if st.button("Exit"):
        del st.session_state["vector_store"]
        st.rerun()