# Shopify LLM Agent

This project connects to the Shopify API, retrieves sales order data, and allows users to query this data using natural language processing (NLP) with OpenAI’s GPT model.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/shopify_llm_agent.git
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your **Shopify API credentials** and **OpenAI API key** in the respective files:
    - `shopify_client.py`: Set your `SHOPIFY_API_KEY`, `SHOPIFY_PASSWORD`, and `SHOPIFY_STORE_URL`.
    - `llm_query_engine.py`: Set your `openai.api_key`.

5. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

6. Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Example Queries

- "Show me all orders from California over $100"
- "How many orders were shipped to California in March?"

## License

MIT License
