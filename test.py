# Imports
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-9b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm = llm,temperature=0.2)

def give_answer(prompt_given):
  result = model.invoke(prompt_given)
  return result.content

que = "What is the capital on INdia? "
print(give_answer(que))