from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from urllib.parse import urlparse, parse_qs

def return_video_id(link: str) -> str:
    parsed_url = urlparse(link)

    # Case 1: Standard YouTube link
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        query = parse_qs(parsed_url.query)
        return query.get("v", [None])[0]

    # Case 2: Shortened youtu.be link
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path.lstrip("/")

    return None



def generate_vector_store(video_link):
    video_id = return_video_id(video_link)
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.fetch(video_id)
        transcript_text = " ".join(snippet.text for snippet in transcript_list.snippets)
    except Exception as e:
        print(e)
        return "No Transcript on video"
    
    # Step 1b Indexing (Text Splitting)
    splitter = RecursiveCharacterTextSplitter()
    chunks = splitter.create_documents([transcript_text])

    # Step 1c, 1d Indexing (Embedding and storing in Vectorstore)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vector_store = FAISS.from_documents(chunks,embeddings)

    return vector_store
