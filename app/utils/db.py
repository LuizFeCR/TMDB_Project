import psycopg
from app.config.settings import DB_CONFIG

def get_connection():
    return psycopg.connect(
        host=DB_CONFIG["host"],
        dbname=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        port=DB_CONFIG["ports"]
    )