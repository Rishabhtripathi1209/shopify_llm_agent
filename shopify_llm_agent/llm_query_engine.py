import openai
import os
import json
from typing import List, Dict

openai.api_key = os.getenv("OPENAI_API_KEY")

def interpret_query(query: str) -> Dict:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": (
                    "You are a query-to-filter converter. Extract JSON filters from the user's sales query. "
                    "Return ONLY a JSON object. Example: "
                    '{"region": "California", "min_amount": 100}'
                )},
                {"role": "user", "content": query}
            ],
            temperature=0.3
        )

        content = response.choices[0].message["content"].strip()

        # Safely parse the LLM output as JSON
        filters = json.loads(content)
        return filters if isinstance(filters, dict) else {}

    except Exception as e:
        print(f"[LLM ERROR] Failed to interpret query: {e}")
        return {}

def filter_orders(orders: List[Dict], filters: Dict) -> List[Dict]:
    filtered = []

    for order in orders:
        # Match region
        if "region" in filters and order.get("region") != filters["region"]:
            continue

        # Match minimum amount
        if "min_amount" in filters and order.get("amount", 0) < filters["min_amount"]:
            continue

        # Match state
        if "state" in filters and order.get("state") != filters["state"]:
            continue

        filtered.append(order)

    return filtered
