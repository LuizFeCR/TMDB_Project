import requests
from app.config.settings import API_KEY, BASE_URL

def get_genres_map():

    url = f"{BASE_URL}/genre/movie/list"

    params = {
        "api_key": API_KEY,
        "language": "pt-BR"
    }

    response = requests.get(url, params=params)

    data = response.json()

    genres = data.get("genres", [])

    return {genre["id"]: genre["name"] for genre in genres}