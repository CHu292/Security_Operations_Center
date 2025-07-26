# Импортируем необходимые модули из SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime  # Типы данных для колонок и внешние ключи
from sqlalchemy.orm import relationship  # Для определения взаимосвязей между моделями
from .database import Base  # Импортируем базовый класс моделей из базы данных
from datetime import datetime  # Для работы с датой и временем

# Определяем модель User, представляющую таблицу пользователей
class User(Base):
    __tablename__ = "users"  # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор пользователя
    email = Column(String, unique=True, index=True)  # Электронная почта пользователя, уникальная и индексированная
    hashed_password = Column(String)  # Хэшированный пароль пользователя
    username = Column(String, unique=True, index=True)  # Уникальное имя пользователя, индексированное
    chat_rooms = relationship("ChatRoom", back_populates="owner")  # Связь с таблицей чатов, указывающая владельца

# Определяем модель ChatRoom, представляющую таблицу комнат чата
class ChatRoom(Base):
    __tablename__ = "chat_rooms"  # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор комнаты
    name = Column(String, unique=True, index=True)  # Уникальное имя комнаты, индексированное
    owner_id = Column(Integer, ForeignKey('users.id'))  # Внешний ключ, ссылающийся на идентификатор владельца (пользователя)
    owner = relationship("User", back_populates="chat_rooms")  # Связь с моделью пользователя
    messages = relationship("Message", back_populates="room", cascade="all, delete")  # Связь с сообщениями в комнате

# Определяем модель Message, представляющую таблицу сообщений
class Message(Base):
    __tablename__ = "messages"  # Имя таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор сообщения
    content = Column(Text, nullable=False)  # Содержимое сообщения, не может быть пустым
    room_id = Column(Integer, ForeignKey('chat_rooms.id'))  # Внешний ключ, ссылающийся на комнату чата
    username = Column(String, nullable=False)  # Имя пользователя, отправившего сообщение
    timestamp = Column(DateTime, default=datetime.utcnow)  # Время отправки сообщения, по умолчанию текущее время
    room = relationship("ChatRoom", back_populates="messages")  # Связь с комнатой чата, в которой находится сообщение

