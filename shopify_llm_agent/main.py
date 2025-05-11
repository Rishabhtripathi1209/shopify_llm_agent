from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from shopify_client import fetch_orders
from llm_query_engine import interpret_query, filter_orders

app = FastAPI(title="Shopify LLM Agent", version="1.0")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    filters: dict
    results: list

@app.post("/query", response_model=QueryResponse)
async def query_sales_data(request: QueryRequest):
    try:
        # Step 1: Fetch orders from Shopify
        orders = fetch_orders()
        if not orders:
            raise HTTPException(status_code=404, detail="No orders retrieved from Shopify")

        # Step 2: Interpret the user's query using the LLM
        filters = interpret_query(request.query)
        if filters is None:
            raise HTTPException(status_code=400, detail="Unable to interpret the query")

        # Step 3: Filter orders based on the interpreted query
        results = filter_orders(orders, filters)

        return QueryResponse(query=request.query, filters=filters, results=results)

    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
