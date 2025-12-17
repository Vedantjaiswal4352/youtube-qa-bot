
def retriever_function(vector_store):
    # Step 2 Retrieval
    retriever = vector_store.as_retriever(search_type="similarity",search_kwargs={"k":2})
    return retriever