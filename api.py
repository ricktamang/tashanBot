import requests
from config import API_URL

def fetch_latest_result():
    try:
        response = requests.get(API_URL, timeout=5)
        data = response.json().get("data", {})
        return {
            "number": data.get("number", 0),
            "color": data.get("color", "unknown"),
            "size": data.get("size", "unknown"),
            "period": data.get("period", "unknown")
        }
    except:
        return {"number": 0, "color": "error", "size": "error", "period": "error"}