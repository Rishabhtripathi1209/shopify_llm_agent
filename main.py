from fastapi import FastAPI
from pydantic import BaseModel

# Fallback mock implementations to prevent import errors in sandbox
try:
    from shopify_client import fetch_orders
except ImportError:
    def fetch_orders():
        return [
            {"id": 1, "amount": 120, "state": "shipped", "region": "California", "date": "2024-03-15"},
            {"id": 2, "amount": 90, "state": "processing", "region": "Texas", "date": "2024-03-20"},
            {"id": 3, "amount": 250, "state": "shipped", "region": "California", "date": "2024-03-10"}
        ]

try:
    from llm_query_engine import interpret_query, filter_orders
except ImportError:
    def interpret_query(query: str):
        # Naive mock parser
        return {"region": "California", "min_amount": 100}

    def filter_orders(orders, filters):
        return [
            o for o in orders
            if o.get("region") == filters.get("region") and o.get("amount", 0) >= filters.get("min_amount", 0)
        ]

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_sales_data(request: QueryRequest):
    orders = fetch_orders()
    filters = interpret_query(request.query)
    results = filter_orders(orders, filters)
    return {"query": request.query, "filters": filters, "results": results}
