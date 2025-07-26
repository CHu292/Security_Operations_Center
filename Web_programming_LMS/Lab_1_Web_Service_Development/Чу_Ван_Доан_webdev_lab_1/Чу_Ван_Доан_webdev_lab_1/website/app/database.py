# Импортируем необходимые модули из SQLAlchemy
from sqlalchemy import create_engine  # Для создания подключения к базе данных
from sqlalchemy.ext.declarative import declarative_base  # Для создания базового класса моделей
from sqlalchemy.orm import sessionmaker  # Для создания сессий работы с базой данных
import os  # Для работы с переменными окружения

# Получаем URL базы данных из переменной окружения
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем объект engine для подключения к базе данных с использованием указанного URL
engine = create_engine(DATABASE_URL)

# Создаем фабрику сессий, которая будет использоваться для получения объектов сессий
# autocommit=False отключает автоматическую фиксацию транзакций
# autoflush=False отключает автоматическую очистку
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем базовый класс для определения моделей данных
Base = declarative_base()

# Функция get_db для предоставления доступа к сессии базы данных
def get_db():
    db = SessionLocal()  # Получаем новую сессию из фабрики
    try:
        yield db  # Возвращаем сессию для использования в зависимости
    finally:
        db.close()  # Закрываем сессию после использования

