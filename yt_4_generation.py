# Imports
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generations"
)
model = ChatHuggingFace(llm = llm,temperature=0.2)

def give_answer(prompt_given):
  result = model.invoke(prompt_given)
  return result.content