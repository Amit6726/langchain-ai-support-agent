# from tools.rag_tool import get_rag_answer

# if __name__ == "__main__":
#     query = input("Ask something: ")
#     result = get_rag_answer(query)
#     print("\nAI Response:\n", result)


# from tools.rag_tool import get_rag_answer
# from tools.order_tool import get_order_status
# from services.utils import extract_order_id

# if __name__ == "__main__":
#     query = input("Ask something: ")

#     # 👉 Check if order query
#     if "order" in query.lower():
#         order_id = extract_order_id(query)

#         if order_id:
#             result = get_order_status(order_id)
#         else:
#             result = "Please provide a valid order ID"

#     else:
#         result = get_rag_answer(query)

#     print("\nAI Response:\n", result)



from graph import graph

if __name__ == "__main__":
    query = input("Ask something: ")

    result = graph.invoke({"input": query})

    print("\nAI Response:\n", result["output"])