# Импортируем необходимые модули из FastAPI
from fastapi import FastAPI  # Основной класс приложения FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse  # Ответы на HTTP-запросы
from fastapi.staticfiles import StaticFiles  # Для работы со статическими файлами
from .routers import auth, chat  # Импортируем маршрутизаторы для аутентификации и чата
from .database import engine, Base  # Импортируем engine и базовый класс моделей из базы данных

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Инициализируем таблицы в базе данных, создавая их на основе моделей
Base.metadata.create_all(bind=engine)

# Регистрируем маршрутизаторы для аутентификации и чата
app.include_router(auth.router)  # Регистрация маршрутов аутентификации
app.include_router(chat.router)  # Регистрация маршрутов чата

# Определяем маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)  # Указываем, что ответ будет HTML
async def read_root():
    # Возвращаем HTML-код для главной страницы
    return """
    <html>
        <head>
            <title>Chat App</title>
        </head>
        <body>
            <h1>Welcome to the Chat App!</h1>
            <p>Go to <a href="/register">Register</a> or <a href="/login">Login</a>.</p>
        </body>
    </html>
    """

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="app/static"), name="static")  # Устанавливаем путь к статическим файлам

# Определяем маршрут для иконки сайта (favicon)
@app.get("/favicon.ico", include_in_schema=False)  # Игнорируем этот маршрут в схеме документации
async def favicon():
    return RedirectResponse(url="/static/favicon.ico")  # Перенаправляем на статическую иконку

