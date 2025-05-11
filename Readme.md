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





# 🧠 Shopify LLM Agent

A FastAPI-based backend agent that connects to Shopify and lets you query sales data using **natural language**. It uses OpenAI's GPT-3.5 to interpret user queries and return filtered order data.

---

## 📦 Features

- 🔌 Connects to Shopify (mocked for now)
- 🧠 Uses OpenAI to interpret queries like:  
  > "Show me all California orders over $100"
- 🧹 Filters order data based on LLM-generated rules
- 🛡️ Includes basic error handling and clean API design

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Rishabhtripathi1209/shopify_llm_agent
cd shopify_llm_agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up `.env`

```env
OPENAI_API_KEY=your_openai_key_here
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

### 5. Send a sample query

```json
POST /query
{
  "query": "Show me orders from California over $100"
}
```

---

## 🏗️ System Architecture

### ⚙️ Components

| Layer            | Role                                         |
|------------------|----------------------------------------------|
| `main.py`        | FastAPI server, receives and processes query |
| `shopify_client.py` | Simulates Shopify order fetch              |
| `llm_query_engine.py` | Uses GPT to turn query into JSON filters and apply them |

### 🔁 Flow

```text
User Query (POST /query)
        ↓
FastAPI Server (main.py)
        ↓
fetch_orders() ←─ Shopify Client
        ↓
interpret_query() ←─ OpenAI GPT-3.5
        ↓
filter_orders()
        ↓
Response → {"query": "...", "filters": {...}, "results": [...]}
```

---

## 📚 Example Response

```json
{
  "query": "Show me all shipped orders over $200 from California",
  "filters": {
    "region": "California",
    "min_amount": 200,
    "state": "shipped"
  },
  "results": [
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

---

## 🛡️ Error Handling

| Case                          | Status | Message                          |
|-------------------------------|--------|----------------------------------|
| No orders found               | 404    | "No orders retrieved from Shopify" |
| Invalid LLM query result      | 400    | "Unable to interpret the query"  |
| Server or LLM failure         | 500    | "Internal server error"          |

---

## 🔮 Future Improvements

- Real Shopify API integration
- LLM confidence scoring
- User authentication
- Dashboard with frontend

---

## 🧑‍💻 Author

[Rishabh Tripathi](https://github.com/Rishabhtripathi1209)

---

- "How many orders were shipped to California in March?"

## License

MIT License
