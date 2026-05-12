from app.bronze.load_bronze import load_bronze
from app.silver.transform_silver import transform_silver
from app.gold.transform_gold import transform_gold


def run_pipeline():
    print("🚀 Iniciando pipeline TMDB")

    load_bronze()
    print("✅ Bronze finalizada")

    transform_silver()
    print("✅ Silver finalizada")

    transform_gold()
    print("✅ Gold finalizada")

    print("🎬 Pipeline concluído")


if __name__ == "__main__":
    run_pipeline()