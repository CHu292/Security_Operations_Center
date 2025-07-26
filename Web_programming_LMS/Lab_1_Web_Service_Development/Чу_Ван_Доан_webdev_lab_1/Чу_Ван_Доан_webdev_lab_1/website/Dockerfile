# Используем Python 3.8 в качестве базового образа
FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости из requirements.txt
RUN pip install -r requirements.txt

# Устанавливаем конкретную версию bcrypt, чтобы избежать ошибки AttributeError
RUN pip install bcrypt==3.2.0

# Копируем все файлы из локальной директории в рабочую директорию контейнера
COPY . .

# Запускаем приложение с помощью uvicorn
# app.main:app указывает на приложение FastAPI (app — это модуль, app — объект FastAPI)
# --host "0.0.0.0" позволяет приложению принимать соединения из любой точки
# --port "8000" устанавливает порт, на котором будет запущено приложение
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

