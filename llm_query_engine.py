# Naive mock parser for query interpretation
def interpret_query(query: str):
    # A simple query parser returning mock filters based on the query
    return {"region": "California", "min_amount": 100}

# Function to filter orders based on the filters from the query
def filter_orders(orders, filters):
    return [
        o for o in orders
        if o.get("region") == filters.get("region") and o.get("amount", 0) >= filters.get("min_amount", 0)
    ]
