from app.utils.db import get_connection

def transform_silver():
    print("Transformando camada Silver...")

    conn = get_connection()
    cur = conn.cursor()

    # 🔥 cria tabela silver
    cur.execute("""
        CREATE TABLE IF NOT EXISTS silver_movies AS
        SELECT
            id,
            title,
            release_date,
            vote_average,
            popularity
        FROM bronze_movies
        WHERE release_date IS NOT NULL;
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("Silver criada com sucesso!")