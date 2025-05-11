import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

# Simulated Shopify order fetcher
def fetch_orders() -> List[Dict]:
    try:
        # In real integration, call Shopify API here
        orders = [
            {"id": 1, "amount": 120, "state": "shipped", "region": "California", "date": "2024-03-15"},
            {"id": 2, "amount": 90, "state": "processing", "region": "Texas", "date": "2024-03-20"},
            {"id": 3, "amount": 250, "state": "shipped", "region": "California", "date": "2024-03-10"}
        ]
        logger.info(f"{len(orders)} orders fetched successfully.")
        return orders
    except Exception as e:
        logger.error(f"Error fetching orders: {str(e)}")
        return []
