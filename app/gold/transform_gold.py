from sqlalchemy import create_engine
import pandas as pd
import os

DB_URL = (
    f"postgresql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DB_URL)

def transform_gold():

    query = """
        SELECT *
        FROM silver_movies
    """

    df = pd.read_sql(query, engine)

    gold_df = (
        df.groupby("original_language")
        .agg(
            total_filmes=("id", "count"),
            media_nota=("vote_average", "mean"),
            total_votos=("vote_count", "sum")
        )
        .reset_index()
    )

    gold_df.to_sql(
        "gold_movies",
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✅ Gold finalizada - {len(gold_df)} registros")