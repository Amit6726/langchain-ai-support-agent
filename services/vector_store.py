from langchain_community.vectorstores import FAISS
from config import embeddings

def create_vector_store():
    with open("data/docs.txt", "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    vectorstore = FAISS.from_texts(lines, embeddings)

    return vectorstore