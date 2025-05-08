# Fallback mock implementation to prevent ImportError in sandbox environment
try:
    import shopify
except ImportError:
    def fetch_orders():
        # Mock data for demonstration purposes
        return [
            {"id": 1, "amount": 120, "state": "shipped", "region": "California", "date": "2024-03-15"},
            {"id": 2, "amount": 90, "state": "processing", "region": "Texas", "date": "2024-03-20"},
            {"id": 3, "amount": 250, "state": "shipped", "region": "California", "date": "2024-03-10"}
        ]
