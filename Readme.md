# Shopify LLM Agent

This project connects to Shopify to fetch order data and processes queries using a basic language model. It provides an API to query orders based on different filters.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Rishabhtripathi1209/shopify_llm_agent.git
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

5. Access the API at `http://127.0.0.1:8000`.

## Endpoints

- `POST /query`: Queries sales data based on the request body.
    - **Request**:
    ```json
    {
      "query": "Get all shipped orders from California with amount > 100"
    }
    ```

    - **Response**:
    ```json
    {
      "query": "Get all shipped orders from California with amount > 100",
      "filters": {
        "region": "California",
        "min_amount": 100
      },
      "results": [
        {
          "id": 1,
          "amount": 120,
          "state": "shipped",
          "region": "California",
          "date": "2024-03-15"
        },
        {
          "id": 3,
          "amount": 250,
          "state": "shipped",
          "region": "California",
          "date": "2024-03-10"
        }
      ]
    }
    ```

## License

MIT License
