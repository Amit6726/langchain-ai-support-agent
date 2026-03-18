from tools.rag_tool import get_rag_answer

if __name__ == "__main__":
    query = input("Ask something: ")
    result = get_rag_answer(query)
    print("\nAI Response:\n", result)