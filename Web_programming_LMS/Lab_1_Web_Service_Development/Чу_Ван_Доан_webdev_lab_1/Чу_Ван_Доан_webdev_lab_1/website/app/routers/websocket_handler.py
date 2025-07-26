from fastapi import WebSocket  # Импортируем класс WebSocket из FastAPI
from typing import Dict, List  # Импортируем классы для аннотирования типов

# Класс для управления подключениями WebSocket
class ConnectionManager:
    def __init__(self):
        # Инициализируем словарь для хранения активных соединений по имени комнаты
        self.active_connections: Dict[str, List[WebSocket]] = {}

    # Асинхронный метод для подключения WebSocket к комнате
    async def connect(self, websocket: WebSocket, room_name: str):
        await websocket.accept()  # Принимаем входящее WebSocket-соединение
        if room_name not in self.active_connections:  # Если комната не существует в словаре
            self.active_connections[room_name] = []  # Создаем новый список для этой комнаты
        self.active_connections[room_name].append(websocket)  # Добавляем WebSocket в список активных соединений комнаты

    # Метод для отключения WebSocket из комнаты
    def disconnect(self, websocket: WebSocket, room_name: str):
        if room_name in self.active_connections:  # Проверяем, существует ли комната
            self.active_connections[room_name].remove(websocket)  # Удаляем WebSocket из списка соединений
            if not self.active_connections[room_name]:  # Если в комнате не осталось подключений
                del self.active_connections[room_name]  # Удаляем комнату из словаря

    # Асинхронный метод для широковещательной рассылки сообщения всем подключенным пользователям в комнате
    async def broadcast(self, message: str, room_name: str):
        if room_name in self.active_connections:  # Проверяем, существует ли комната
            for connection in self.active_connections[room_name]:  # Перебираем все соединения в комнате
                await connection.send_text(message)  # Отправляем сообщение каждому подключенному WebSocket

