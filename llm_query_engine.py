# Fallback mock implementation for the LLM query engine
try:
    import openai
except ImportError:
    def interpret_query(query: str):
        # Naive mock query parser
        return {"region": "California", "min_amount": 100}

    def filter_orders(orders, filters):
        # Simple filtering logic based on region and amount
        return [
            o for o in orders
            if o.get("region") == filters.get("region") and o.get("amount", 0) >= filters.get("min_amount", 0)
        ]
