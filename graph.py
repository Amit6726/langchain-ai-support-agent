from typing import TypedDict
from langgraph.graph import StateGraph
from tools.rag_tool import get_rag_answer
from tools.order_tool import get_order_status
from services.utils import extract_order_id


#  1. Define State (shared data across nodes)
class AgentState(TypedDict):
    input: str
    output: str


# 2. RAG Node (handles FAQ / knowledge queries)
def rag_node(state: AgentState):
    query = state["input"]

    answer = get_rag_answer(query)

    return {
        "output": answer
    }


#  3. Order Node (handles dynamic order queries)
def order_node(state: AgentState):
    query = state["input"]

    order_id = extract_order_id(query)

    if not order_id:
        return {
            "output": "Please provide a valid order ID"
        }

    result = get_order_status(order_id)

    return {
        "output": result
    }


# 4. Router (decides which node to use)
def router(state: AgentState):
    query = state["input"].lower()

    if "order" in query:
        return "order"
    else:
        return "rag"


#  5. Build Graph
builder = StateGraph(AgentState)

# Add nodes
builder.add_node("rag", rag_node)
builder.add_node("order", order_node)

#  Entry point (decision)
builder.set_conditional_entry_point(router)

#  Define flow (edges)
builder.add_edge("rag", "__end__")
builder.add_edge("order", "__end__")

#  Compile graph
graph = builder.compile()