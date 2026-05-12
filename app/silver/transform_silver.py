import pandas as pd
from sqlalchemy import create_engine
import os
import ast
from datetime import datetime, timedelta
from app.utils.genres import get_genres_map

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT"),
}

def transform_silver():

    engine = create_engine(
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )

    query = """
        SELECT *
        FROM bronze_movies
    """

    df = pd.read_sql(query, engine)

    print(f"Total Bronze: {len(df)}")

    # =========================
    # REMOVER DUPLICADOS
    # =========================

    df = df.drop_duplicates(subset=["id"])

    # =========================
    # DATA
    # =========================

    df["release_date"] = pd.to_datetime(
        df["release_date"],
        errors="coerce"
    )

    df = df.dropna(subset=["release_date"])

    df["release_year"] = df["release_date"].dt.year

    
    # =========================
    # GENRES
    # =========================

    genres_map = get_genres_map()

    # Converter string para lista
    def parse_genres(x):

        if pd.isna(x):
            return []

        if isinstance(x, list):
            return x

        if isinstance(x, str):

            try:
                return ast.literal_eval(x)
            except:
                return []

        return []

    df["genre_ids"] = df["genre_ids"].apply(parse_genres)

    # Converter ids -> nomes
    def convert_genres(genre_list):

        if not genre_list:
            return None

        # Converter set/list para lista
        genre_list = list(genre_list)

        first_genre_id = genre_list[0]

        return str(genres_map.get(first_genre_id, "Desconhecido"))

# CRIA A COLUNA genres
    df["genres"] = df["genre_ids"].apply(convert_genres)

    silver_df = df[
        [
            "id",
            "title",
            "release_date",
            "release_year",
            "vote_average",
            "vote_count",
            "popularity",
            "genres",
            "original_language",
        ]
    ]

    print(silver_df.head())

    # =========================
    # SALVAR
    # =========================

    silver_df["genres"] = silver_df["genres"].astype(str)

    silver_df.to_sql(
        "silver_movies",
        engine,
        if_exists="replace",
        index=False
    )
    print(f"✅ Silver finalizada - {len(silver_df)} registros")