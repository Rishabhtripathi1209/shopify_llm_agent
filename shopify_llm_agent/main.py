from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from shopify_client import fetch_orders
from llm_query_engine import interpret_query, filter_orders

# FastAPI app
app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_sales_data(request: QueryRequest):
    # Fetch orders from Shopify
    orders = fetch_orders()

    # Process query using the LLM interpreter
    filters = interpret_query(request.query)

    # Filter orders based on the interpreted filters
    results = filter_orders(orders, filters)

    # Return the response
    return {"query": request.query, "filters": filters, "results": results}
