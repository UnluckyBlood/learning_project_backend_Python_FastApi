import psycopg2
from app.core.config import settings

try:
    conn = psycopg2.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME
    )
    print("Подключилися")
    conn.close()
except Exception as e:
    print(f"ошибка подключения: {e}")