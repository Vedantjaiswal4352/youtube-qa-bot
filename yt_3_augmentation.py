# Imports
from langchain_core.prompts import PromptTemplate


def return_final_prompt(question,retriever):
    # Step 3 Augmentation
    prompt = PromptTemplate(
        template="""
        You are an helpful assistant.
        Answer only from the tranwscript context provided.
        If the content is insufficient, just say ypu dont know.
        Context: {context}
        Question: {question}
        """,
        input_variables=['context','question']
    ) 

    retrieved_docs = retriever.invoke(question)
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    final_prompt = prompt.invoke({'context':context_text,'question':question})
    return final_prompt