from app.utils.db import get_connection
from app.ingestion.tmdb_extractor import fetch_movies_2025

def load_bronze():
    print("Carregando dados na camada bronze...")

    movies = fetch_movies_2025()

    conn = get_connection()
    cur = conn.cursor()

    # 🔹 Criar tabela
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bronze_movies (
            id INT PRIMARY KEY,
            title TEXT,
            release_date DATE,
            vote_average FLOAT,
            popularity FLOAT
        );
    """)

    # 🔹 Inserir dados
    for movie in movies:
        cur.execute("""
            INSERT INTO bronze_movies (id, title, release_date, vote_average, popularity)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (
            movie.get("id"),
            movie.get("title"),
            movie.get("release_date"),
            movie.get("vote_average"),
            movie.get("popularity")
        ))

    conn.commit()
    cur.close()
    conn.close()

    print(f"{len(movies)} filmes carregados na bronze.")