from fastapi import WebSocket
from typing import Dict, List

class ConnectionManager:
    def __init__(self):
        # Инициализация объекта ConnectionManager.
        # Хранение активных подключений в виде словаря, где ключ — имя комнаты,
        # а значение — список объектов WebSocket для этой комнаты.
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, room_name: str):
        # Метод для подключения пользователя к определенной комнате.
        # Принимает объект WebSocket и имя комнаты в качестве параметров.
        await websocket.accept()  # Подтверждение соединения WebSocket.
        if room_name not in self.active_connections:
            # Если комнаты нет в словаре, создается новая запись с пустым списком.
            self.active_connections[room_name] = []
        # Добавление подключения в список подключений для данной комнаты.
        self.active_connections[room_name].append(websocket)

    def disconnect(self, websocket: WebSocket, room_name: str):
        # Метод для отключения пользователя от определенной комнаты.
        # Если комната существует, удаляем объект WebSocket из списка подключений.
        if room_name in self.active_connections:
            self.active_connections[room_name].remove(websocket)

    async def broadcast(self, message: str, room_name: str):
        # Метод для отправки сообщения всем подключенным пользователям в комнате.
        # Перебирает все соединения в указанной комнате и отправляет сообщение.
        for connection in self.active_connections[room_name]:
            await connection.send_text(message)

