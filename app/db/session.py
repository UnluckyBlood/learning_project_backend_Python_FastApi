from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# строчка подключения postgresql://пользователь:пароль@хост:порт/имя_базы
DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_engine(DATABASE_URL)
#чтоб внести изменения и сохранить требуется сделать коммити или флушь и привязывается к нашему урл(гулигули)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# функция вызова бдшки, пробуется пока работает, закончили закрываем бдшку
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()