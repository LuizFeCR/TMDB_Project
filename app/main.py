from app.bronze.load_bronze import load_bronze
from app.silver.transform_silver import transform_silver
from app.gold.transform_gold import transform_gold

def run_pipeline():
    print("Iniciando pipeline...")

    load_bronze()
    print("Bronze OK")

    transform_silver()
    print("Silver OK")

    transform_gold()
    print("Gold OK")

    print("Pipeline finalizado!")

if __name__ == "__main__":
    run_pipeline()