import re

def extract_order_id(query: str):
    match = re.search(r"\d+", query)
    return match.group() if match else None