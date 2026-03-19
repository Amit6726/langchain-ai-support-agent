ORDERS = {
    "101": {"status": "shipped", "delivery": "tomorrow"},
    "102": {"status": "processing", "delivery": "in 2 days"},
    "103": {"status": "delivered", "delivery": "today"},
}

def get_order_status(order_id: str):
    order = ORDERS.get(order_id)

    if not order:
        return "Order not found"

    return f"Order {order_id} is {order['status']} and will arrive {order['delivery']}"