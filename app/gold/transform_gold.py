from app.utils.db import get_connection

def transform_gold():
    print("Criando camada Gold...")

    conn = get_connection()
    cur = conn.cursor()

    # 🔥 TOP FILMES
    cur.execute("""
        CREATE TABLE IF NOT EXISTS gold_top_movies AS
        SELECT
            title,
            vote_average,
            popularity
        FROM silver_movies
        ORDER BY vote_average DESC
        LIMIT 20;
    """)

    # 🔥 MÉDIA POR POPULARIDADE
    cur.execute("""
        CREATE TABLE IF NOT EXISTS gold_avg_stats AS
        SELECT
            AVG(vote_average) AS avg_rating,
            AVG(popularity) AS avg_popularity
        FROM silver_movies;
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("Gold criada com sucesso!")