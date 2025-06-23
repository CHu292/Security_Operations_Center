from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from .websocket_handler import ConnectionManager
import jwt
import os

SECRET_KEY = "chuvandoan"
ALGORITHM = "HS256"


app = FastAPI()
manager = ConnectionManager()

# Функция для декодирования JWT
# Эта функция принимает JWT-токен в качестве параметра, расшифровывает его с использованием секретного ключа,
# и возвращает имя пользователя (username) из полезной нагрузки. Если декодирование не удалось (например, токен недействителен),
# возвращается None.
def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("username")
    except jwt.PyJWTError:
        return None

# Маршрут для обработки WebSocket-соединения
# Эта функция обрабатывает соединение WebSocket. Она принимает WebSocket и имя комнаты в качестве параметров,
# а также токен для проверки аутентификации.
# Если токен недействителен или не содержит имени пользователя, соединение закрывается.
@app.websocket("/ws/{room_name}")
async def websocket_endpoint(websocket: WebSocket, room_name: str, token: str = None):
    # Декодирование токена и получение имени пользователя
    username = decode_jwt(token)
    if not username:
        await websocket.close(code=1008)  # Закрытие соединения при отсутствии действительного имени пользователя
        return

    # Подключение пользователя к менеджеру соединений
    await manager.connect(websocket, username)
    try:
        # Оповещение о присоединении пользователя к чату
        await manager.broadcast(f"{username} присоединился к чату")
        while True:
            # Получение сообщений от клиента
            data = await websocket.receive_text()
            # Передача сообщения всем пользователям в чате
            await manager.broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        # Отключение пользователя и оповещение других пользователей
        manager.disconnect(websocket)
        await manager.broadcast(f"{username} покинул чат")

