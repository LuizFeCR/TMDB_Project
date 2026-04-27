import requests
from app.config.settings import API_KEY, BASE_URL

def fetch_movies_2025(page=1):
    url = f"{BASE_URL}/discover/movie"
    
    params = {
        "api_key": API_KEY,
        "primary_release_year": 2025,
        "page": page
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data.get("results", [])  # 🔥 CORREÇÃO PRINCIPAL