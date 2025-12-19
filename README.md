# 🎥 YouTube QA Bot

A Retrieval-Augmented Generation (RAG) chatbot built with **Streamlit** and **LangChain** that answers questions from YouTube video transcripts.  
Users simply paste a YouTube link, and the system fetches the transcript, chunks it, embeds it, stores it in FAISS, and then uses a retriever + LLM to generate contextual answers in a chat-style interface.

---

## ✨ Features
- 📺 **YouTube Transcript Input**: Paste a YouTube link directly in the Streamlit frontend.
- 🧩 **Chunking & Embedding**: Transcript is split into chunks and embedded for semantic search.
- 📚 **FAISS Vector Store**: Embeddings are stored in FAISS for efficient similarity search.
- 🔍 **Retriever**: Retrieves relevant transcript chunks based on user queries.
- 📝 **Prompt Engineering**: Uses LangChain `PromptTemplate` to combine retriever context + user question.
- 🤖 **LLM Generation**: Hugging Face integration with **Google Gemma-2-2b-it** for final answer generation.
- 💬 **Chat-style UI**: Streamlit frontend styled with markdown and chat components for a modern conversational experience.
- ⚡ **RAG System**: Context from the vector store is injected every time for grounded responses.

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** (frontend)
- **LangChain** (prompting + orchestration)
- **FAISS** (vector store)
- **Hugging Face Transformers**
- **Google Gemma-2-2b-it** (LLM backend)

## 📂 Project Structure
```
youtube-qa-bot/
│── app.py # Main chatbotapp
│── app2.py # Alternate app version
│── yt_1_indexing.py    # Transcript indexing & embedding
│── yt_2_retrieval.py   # Retriever logic
│── yt_3_augmentation.py# Prompt augmentation
│── yt_4_generation.py  # Answer generation
│── requirements.txt    # Dependencies
│── .gitignore          # Ignored file
```


---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Vedantjaiswal4352/youtube-qa-bot.git
cd youtube-qa-bot
```
### 2. Create a virtual environment
```bash
python -m venv venv_youtubeqa
source venv_youtubeqa/bin/activate   # Mac/Linux
venv_youtubeqa\Scripts\activate      # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the app
```bash
streamlit run app.py
```

## 📖 How It Works
- **Input**: User enters a YouTube link in the Streamlit frontend.
- **Indexing**: Transcript is fetched, chunked, and embedded.
- **Storage**: Embeddings are stored in FAISS.
- **Retrieval**: Similarity search retrieves relevant chunks.
- **Prompt Creation**: LangChain PromptTemplate merges retriever context + user query.
- **Generation**: Hugging Face LLM (Gemma-2-2b-it) produces the final answer.
- **Frontend**: Answer is displayed in a chat-style Streamlit UI.


## 🖼️ UI Preview
(Add a screenshot here of your Streamlit chatbot interface with chat bubbles)

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

🔗 Repositor
https://github.com/Vedantjaiswal4352/youtube-qa-bot


---
