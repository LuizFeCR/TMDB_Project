import requests
from time import sleep
from datetime import datetime, timedelta
from app.config.settings import API_KEY, BASE_URL


CURRENT_YEAR = 2026


def fetch_movies_2026():
    all_movies = []

    today = datetime.today()

    # Regra: filmes precisam ter no mínimo 7 dias
    cutoff_date = today - timedelta(days=7)

    page = 1
    total_pages = 1

    while page <= total_pages:
        url = f"{BASE_URL}/discover/movie"

        params = {
            "api_key": API_KEY,
            "language": "pt-BR",
            "region": "BR",
            "primary_release_date.gte": f"{CURRENT_YEAR}-01-01",
            "primary_release_date.lte": cutoff_date.strftime("%Y-%m-%d"),
            "sort_by": "primary_release_date.desc",
            "vote_count.gte": 10,
            "include_adult": False,
            "page": page
        }
                

        try:
            response = requests.get(url, params=params)

            if response.status_code != 200:
                print(f"Erro API: {response.status_code}")
                break

            data = response.json()

            if page == 1:
                total_pages = data.get("total_pages", 1)
                print(f"Total de páginas encontradas: {total_pages}")

            results = data.get("results", [])

            if results:
                all_movies.extend(results)
                print(f"Página {page} processada - Total acumulado: {len(all_movies)}")
            else:
                print(f"Página {page} sem resultados")

            page += 1
            sleep(0.2)

        except Exception as e:
            print(f"Erro na extração: {e}")
            break

    return all_movies