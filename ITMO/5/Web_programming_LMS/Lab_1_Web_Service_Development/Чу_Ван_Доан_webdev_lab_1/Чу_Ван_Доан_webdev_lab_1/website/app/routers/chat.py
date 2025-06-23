# Импортируем необходимые модули из FastAPI и других библиотек
import jwt
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect, Request, Form
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse
from .. import models, database
from .websocket_handler import ConnectionManager
from fastapi.templating import Jinja2Templates
import os

# Khởi tạo router và manager cho WebSocket
router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
manager = ConnectionManager()

SECRET_KEY = "chuvandoan"
ALGORITHM = "HS256"

# Функция для получения сессии базы данных
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Функция для декодирования JWT
def decode_jwt(token: str):
    if token is None:
        return None
    try:
        token = token.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except jwt.PyJWTError:
        return None

# Обработка GET-запроса для страницы чата
@router.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse(url="/login", status_code=302)

    user_email = decode_jwt(token)
    if not user_email:
        return RedirectResponse(url="/login", status_code=302)

    user = db.query(models.User).filter(models.User.email == user_email).first()
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    user_rooms = db.query(models.ChatRoom).filter(models.ChatRoom.owner_id == user.id).all()
    return templates.TemplateResponse("chat.html", {"request": request, "rooms": user_rooms, "user": user})

# Обработка POST-запроса для создания новой комнаты
@router.post("/create-room", response_class=HTMLResponse)
async def create_room(request: Request, room_name: str = Form(...), db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    user_email = decode_jwt(token)
    user = db.query(models.User).filter(models.User.email == user_email).first()

    if not user:
        return RedirectResponse(url="/login", status_code=302)

    existing_room = db.query(models.ChatRoom).filter(models.ChatRoom.name == room_name).first()
    if existing_room:
        raise HTTPException(status_code=400, detail="Room already exists")

    new_room = models.ChatRoom(name=room_name, owner_id=user.id)
    db.add(new_room)
    db.commit()
    return RedirectResponse(url="/chat", status_code=302)

# Обработка POST-запроса для удаления комнаты
@router.post("/delete-room", response_class=HTMLResponse)
async def delete_room(request: Request, room_id: int = Form(...), db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    user_email = decode_jwt(token)
    user = db.query(models.User).filter(models.User.email == user_email).first()

    if not user:
        return RedirectResponse(url="/login", status_code=302)

    room = db.query(models.ChatRoom).filter(models.ChatRoom.id == room_id, models.ChatRoom.owner_id == user.id).first()
    if not room:
        raise HTTPException(status_code=403, detail="Not authorized to delete this room")

    db.delete(room)
    db.commit()
    return RedirectResponse(url="/chat", status_code=302)

# функция поиска комнат
@router.get("/search-rooms", response_class=HTMLResponse)
async def search_rooms(request: Request, search_query: str, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    user_email = decode_jwt(token)
    user = db.query(models.User).filter(models.User.email == user_email).first()

    if not user:
        return RedirectResponse(url="/login", status_code=302)

    rooms = db.query(models.ChatRoom).filter(models.ChatRoom.name.contains(search_query)).all()
    return templates.TemplateResponse("chat.html", {"request": request, "rooms": rooms, "user": user, "search_query": search_query})

# Обработка GET-запроса для страницы чата в конкретной комнате
@router.get("/chat/{room_name}", response_class=HTMLResponse)
async def room_chat_page(request: Request, room_name: str, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    user_email = decode_jwt(token)
    user = db.query(models.User).filter(models.User.email == user_email).first()

    if not user:
        return RedirectResponse(url="/login", status_code=302)

    room = db.query(models.ChatRoom).filter(models.ChatRoom.name == room_name).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    messages = db.query(models.Message).filter(models.Message.room_id == room.id).order_by(models.Message.timestamp).all()
    return templates.TemplateResponse("room_chat.html", {"request": request, "room": room, "user": user, "messages": messages})

# Обработка WebSocket-соединения
@router.websocket("/ws/{room_name}")
async def websocket_endpoint(websocket: WebSocket, room_name: str, db: Session = Depends(get_db)):
    await manager.connect(websocket, room_name)

    room = db.query(models.ChatRoom).filter(models.ChatRoom.name == room_name).first()
    if not room:
        await websocket.close()
        return

    token = websocket.cookies.get("access_token")
    user_email = decode_jwt(token)
    user = db.query(models.User).filter(models.User.email == user_email).first()
    
    if not user:
        await websocket.close()
        return

    username = user.username

    try:
        while True:
            data = await websocket.receive_text()
            new_message = models.Message(content=data, room_id=room.id, username=username)
            db.add(new_message)
            db.commit()
            await manager.broadcast(f"{username}: {data}", room_name)
    except WebSocketDisconnect:
        manager.disconnect(websocket, room_name)
