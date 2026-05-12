import pandas as pd
from sqlalchemy import create_engine
from app.ingestion.tmdb_extractor import fetch_movies_2026
import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT"),
}

def load_bronze():

    movies = fetch_movies_2026()

    df = pd.DataFrame(movies)

    engine = create_engine(
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )

    df.to_sql(
    "bronze_movies",
    engine,
    if_exists="replace",
    index=False
    )

    print(f"{len(df)} filmes inseridos na Bronze")
    print("✅ Bronze finalizada")