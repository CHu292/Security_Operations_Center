-- Создаем таблицу пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,  -- Уникальный идентификатор пользователя (автоинкрементируемый)
    email VARCHAR(255) UNIQUE NOT NULL,  -- Уникальный адрес электронной почты, не может быть пустым
    hashed_password VARCHAR(255) NOT NULL,  -- Хэшированный пароль пользователя, не может быть пустым
    username VARCHAR(50) UNIQUE NOT NULL  -- Уникальное имя пользователя, не может быть пустым
);

-- Создаем таблицу комнат чата
CREATE TABLE chat_rooms (
    id SERIAL PRIMARY KEY,  -- Уникальный идентификатор комнаты чата (автоинкрементируемый)
    name VARCHAR(255) UNIQUE NOT NULL,  -- Уникальное имя комнаты, не может быть пустым
    owner_id INTEGER REFERENCES users(id) ON DELETE CASCADE  -- Внешний ключ, ссылающийся на пользователя, который владеет комнатой
    -- При удалении пользователя комната также будет удалена
);

-- Создаем таблицу сообщений
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,  -- Уникальный идентификатор сообщения (автоинкрементируемый)
    content TEXT NOT NULL,  -- Содержимое сообщения, не может быть пустым
    room_id INTEGER REFERENCES chat_rooms(id) ON DELETE CASCADE,  -- Внешний ключ, ссылающийся на комнату, в которой было отправлено сообщение
    -- При удалении комнаты все сообщения в ней также будут удалены
    username VARCHAR(50) NOT NULL,  -- Имя пользователя, отправившего сообщение, не может быть пустым
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Метка времени, указывающая время отправки сообщения, по умолчанию устанавливается текущее время
);

