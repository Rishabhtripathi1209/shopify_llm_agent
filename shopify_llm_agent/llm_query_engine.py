import openai
import os

# Load the API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

def interpret_query(query: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Extract filter criteria from order-related query."},
                {"role": "user", "content": query}
            ],
            temperature=0.3
        )
        filters = response.choices[0].message["content"].strip()
        return eval(filters)
    except Exception as e:
        print("GPT error:", e)
        return {}

def filter_orders(orders, filters):
    return [
        o for o in orders
        if o.get("region") == filters.get("region") and o.get("amount", 0) >= filters.get("min_amount", 0)
    ]
