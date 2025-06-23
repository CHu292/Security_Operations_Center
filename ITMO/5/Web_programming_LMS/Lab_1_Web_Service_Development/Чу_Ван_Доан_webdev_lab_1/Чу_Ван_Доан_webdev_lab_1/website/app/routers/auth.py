# Импортируем необходимые модули из FastAPI и других библиотек
from fastapi import APIRouter, Depends, HTTPException, Request, Form  # Импортируем классы и функции для работы с API
from fastapi.responses import HTMLResponse, RedirectResponse  # Импортируем классы для ответа HTML и перенаправления
from sqlalchemy.orm import Session  # Импортируем класс для работы с сессиями SQLAlchemy
from passlib.context import CryptContext  # Импортируем контекст для хэширования паролей
from .. import models, database  # Импортируем модели и базу данных из текущего пакета
import jwt  # Импортируем библиотеку для работы с JWT
from datetime import datetime, timedelta  # Импортируем классы для работы с датой и временем
from fastapi.templating import Jinja2Templates  # Импортируем класс для работы с шаблонами Jinja2

# Создаем объект маршрутизатора
router = APIRouter()
# Указываем директорию для шаблонов
templates = Jinja2Templates(directory="app/templates")

# Конфигурация для JWT
SECRET_KEY = "chuvandoan"  # Секретный ключ для кодирования JWT
ALGORITHM = "HS256"  # Алгоритм для кодирования JWT
# Настраиваем контекст для хэширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Функция для получения сессии базы данных
def get_db():
    db = database.SessionLocal()  # Создаем новую сессию
    try:
        yield db  # Возвращаем сессию для использования
    finally:
        db.close()  # Закрываем сессию после использования

# Функция для создания токена доступа
def create_access_token(data: dict):
    to_encode = data.copy()  # Копируем данные для кодирования
    expire = datetime.utcnow() + timedelta(hours=1)  # Устанавливаем время истечения токена на 1 час
    to_encode.update({"exp": expire})  # Добавляем время истечения в данные
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Кодируем и возвращаем токен

# Обработка GET-запроса на получение формы регистрации
@router.get("/register", response_class=HTMLResponse)
async def get_register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})  # Возвращаем шаблон для регистрации

# Обработка POST-запроса на регистрацию пользователя
@router.post("/register")
def register(
    username: str = Form(...),  # Получаем имя пользователя из формы
    email: str = Form(...),  # Получаем электронную почту из формы
    password: str = Form(...),  # Получаем пароль из формы
    db: Session = Depends(get_db)  # Получаем сессию базы данных
):
    # Проверяем, существует ли уже пользователь с таким email или username
    db_user_email = db.query(models.User).filter(models.User.email == email).first()
    db_user_username = db.query(models.User).filter(models.User.username == username).first()
    if db_user_email or db_user_username:
        raise HTTPException(status_code=400, detail="Email or username already registered")  # Возвращаем ошибку, если существует

    # Хэшируем пароль и сохраняем в базе данных
    hashed_password = pwd_context.hash(password)  # Хэшируем пароль
    db_user = models.User(email=email, hashed_password=hashed_password, username=username)  # Создаем объект пользователя
    db.add(db_user)  # Добавляем пользователя в сессию
    db.commit()  # Коммитим изменения в базе данных
    db.refresh(db_user)  # Обновляем информацию о пользователе

    return RedirectResponse(url="/login", status_code=302)  # Перенаправляем на страницу входа

# Обработка GET-запроса на получение формы входа
@router.get("/login", response_class=HTMLResponse)
async def get_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})  # Возвращаем шаблон для входа

# Обработка POST-запроса на вход пользователя
@router.post("/login")
async def login(
    request: Request,  # Получаем объект запроса
    email: str = Form(...),  # Получаем электронную почту из формы
    password: str = Form(...),  # Получаем пароль из формы
    db: Session = Depends(get_db)  # Получаем сессию базы данных
):
    # Ищем пользователя по email
    db_user = db.query(models.User).filter(models.User.email == email).first()
    
    # Проверяем пароль
    if not db_user or not pwd_context.verify(password, db_user.hashed_password):
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error_message": "Invalid email or password. Please try again."  # Возвращаем сообщение об ошибке
        })

    # Создаем JWT токен
    access_token = create_access_token(data={"sub": db_user.email, "username": db_user.username})
    
    # Устанавливаем JWT токен в cookie
    response = RedirectResponse(url="/chat", status_code=302)  # Перенаправляем на страницу чата
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)  # Устанавливаем токен в cookie
    return response  # Возвращаем ответ
