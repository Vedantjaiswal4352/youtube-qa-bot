<img width="1920" height="964" alt="2" src="https://github.com/user-attachments/assets/a22c107d-273e-4a55-b074-e4f1f75653ce" /># 🎥 YouTube QA Bot

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
<img width="1920" height="971" alt="1" src="https://github.com/user-attachments/assets/934ed684-f44a-494e-8d0c-e62b1350e598" />
<img width="1920" height="964" alt="2" src="https://github.com/user-attachments/assets/fba99fae-09f6-4075-afda-4589cbcc8129" />
<img width="1920" height="960" alt="3" src="https://github.com/user-attachments/assets/71613d2f-a94e-485a-9b43-eea4874f3665" />
<img width="1920" height="961" alt="4" src="https://github.com/user-attachments/assets/fce1fe15-1389-4c7c-b260-106c51bda56f" />
<img width="1920" height="969" alt="5" src="https://github.com/user-attachments/assets/e72b3247-fae3-4e82-88f2-209729d42aac" />
<img width="1920" height="969" alt="6" src="https://github.com/user-attachments/assets/4bd342ed-b162-446c-8fdc-4a5773a63d57" />
<img width="1920" height="974" alt="7" src="https://github.com/user-attachments/assets/a68f748e-0ea2-4593-a7ea-2267741ac0d0" />

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

🔗 Repositor
https://github.com/Vedantjaiswal4352/youtube-qa-bot


---
