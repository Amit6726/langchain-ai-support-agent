from services.vector_store import create_vector_store
from config import llm

# ✅ create vectorstore once
vectorstore = create_vector_store()

def get_rag_answer(query: str):
    docs = vectorstore.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a helpful support assistant.

    Answer clearly using the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)
    return response.content