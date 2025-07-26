Dự án này là một ứng dụng chat trực tuyến, bao gồm các thành phần microservice sử dụng kiến trúc web socket để cung cấp chức năng trò chuyện thời gian thực. Dưới đây là mô tả chi tiết về cách hoạt động của từng thành phần trong dự án.

### 1. Thành phần và kiến trúc tổng quát
Dự án này được chia thành các microservice chính sau:

- **Website microservice**: Chịu trách nhiệm quản lý người dùng và các phòng chat. Đây là nơi người dùng có thể đăng ký, đăng nhập, tạo phòng chat, tìm kiếm phòng chat và gửi tin nhắn.
- **Chat WebSocket microservice**: Xử lý các kết nối WebSocket cho các phòng chat, giúp truyền tải tin nhắn giữa các người dùng trong cùng phòng chat.
- **Database (PostgreSQL)**: Lưu trữ dữ liệu về người dùng, các phòng chat và tin nhắn.
- **Nginx**: Hoạt động như một reverse proxy, chuyển tiếp các yêu cầu HTTP cho website microservice và các kết nối WebSocket cho chat microservice.

### 2. Cách thức hoạt động của từng thành phần

#### 2.1 Website Microservice
- **Quản lý người dùng**: Người dùng có thể đăng ký tài khoản mới bằng email, username và mật khẩu. Khi đăng ký, hệ thống sẽ lưu trữ thông tin này trong bảng `users` của cơ sở dữ liệu với mật khẩu được mã hóa.
- **Đăng nhập và xác thực**: Khi người dùng đăng nhập, hệ thống sẽ kiểm tra thông tin xác thực (email và mật khẩu) và, nếu hợp lệ, tạo một token JWT để xác thực phiên làm việc của người dùng. Token này sẽ được lưu dưới dạng cookie trong trình duyệt để xác thực các yêu cầu tiếp theo.
- **Tạo phòng chat**: Người dùng đã đăng nhập có thể tạo các phòng chat mới. Thông tin về phòng chat sẽ được lưu trữ trong bảng `chat_rooms` với ID của người tạo (owner_id) để xác định quyền xóa phòng.
- **Tìm kiếm phòng chat**: Người dùng có thể tìm kiếm các phòng chat dựa trên tên phòng, cho phép họ tham gia vào các cuộc trò chuyện có sẵn.
- **Xóa phòng chat**: Chỉ chủ sở hữu phòng chat mới có thể xóa phòng đó. Khi phòng bị xóa, tất cả các tin nhắn trong phòng cũng sẽ bị xóa.

#### 2.2 Chat WebSocket Microservice
- **Quản lý kết nối WebSocket**: Khi người dùng tham gia vào phòng chat, hệ thống sẽ thiết lập một kết nối WebSocket tới chat microservice qua một endpoint `/ws/{room_name}`. Tại đây, `room_name` là tên của phòng chat mà người dùng muốn tham gia.
- **Gửi và nhận tin nhắn**: Sau khi kết nối thành công, người dùng có thể gửi tin nhắn đến các thành viên khác trong phòng chat. Tin nhắn sẽ được truyền tới chat WebSocket microservice, nơi sẽ phát sóng tin nhắn đến tất cả người dùng hiện đang kết nối trong cùng phòng chat đó.
- **Lưu trữ tin nhắn**: Khi một tin nhắn mới được gửi đến, nó sẽ được lưu vào bảng `messages` trong cơ sở dữ liệu với thông tin về nội dung, tên người gửi, và thời gian gửi.

#### 2.3 Database (PostgreSQL)
Cơ sở dữ liệu được dùng để lưu trữ toàn bộ dữ liệu của dự án:
- **Bảng `users`**: Lưu trữ thông tin người dùng, bao gồm `id`, `email`, `username`, và `hashed_password`.
- **Bảng `chat_rooms`**: Lưu trữ thông tin phòng chat, bao gồm `id`, `name` (tên phòng), và `owner_id` (ID của người tạo).
- **Bảng `messages`**: Lưu trữ các tin nhắn, bao gồm `id`, `content` (nội dung tin nhắn), `room_id` (ID của phòng chứa tin nhắn), `username` (người gửi), và `timestamp` (thời gian gửi tin nhắn).

#### 2.4 Nginx
Nginx được cấu hình như một reverse proxy để chuyển tiếp các yêu cầu đến các microservice khác nhau:
- **Chuyển tiếp HTTP**: Các yêu cầu HTTP từ người dùng sẽ được chuyển đến website microservice, bao gồm các yêu cầu như đăng nhập, đăng ký, tạo phòng chat, và tìm kiếm phòng chat.
- **Chuyển tiếp WebSocket**: Các kết nối WebSocket từ người dùng sẽ được chuyển tiếp đến chat WebSocket microservice, giúp thực hiện chức năng trò chuyện thời gian thực giữa các người dùng trong phòng chat.

### 3. Quy trình hoạt động của hệ thống

1. **Người dùng truy cập trang chính**: Người dùng có thể đăng ký hoặc đăng nhập bằng email và mật khẩu.
2. **Tạo phòng chat**: Sau khi đăng nhập, người dùng có thể tạo một phòng chat mới hoặc tìm kiếm các phòng chat hiện có để tham gia.
3. **Tham gia vào phòng chat**: Khi tham gia vào một phòng chat, kết nối WebSocket được thiết lập để người dùng có thể gửi và nhận tin nhắn trong thời gian thực.
4. **Gửi và nhận tin nhắn**: Tin nhắn được phát sóng tới tất cả người dùng trong phòng qua kết nối WebSocket, và được lưu lại trong cơ sở dữ liệu để người dùng có thể xem lại khi truy cập lại phòng chat sau này.
5. **Kết thúc phiên làm việc**: Khi người dùng ngắt kết nối WebSocket hoặc thoát khỏi phòng chat, hệ thống sẽ tự động ngắt kết nối.

### 4. Kết luận
Dự án này xây dựng thành công hệ thống chat trực tuyến với các chức năng cơ bản như đăng ký, đăng nhập, tạo phòng, tham gia phòng, và gửi tin nhắn thời gian thực. Việc sử dụng các công nghệ như FastAPI, WebSocket và Nginx cho phép dự án đạt được hiệu suất và khả năng mở rộng tốt, phù hợp với các hệ thống chat lớn.



---

### Подробное описание работы проекта

Этот проект представляет собой онлайн-чат с использованием архитектуры микросервисов и протокола WebSocket для обеспечения функции обмена сообщениями в режиме реального времени. Ниже приводится подробное описание работы каждого компонента проекта.

### 1. Компоненты и общая архитектура

Проект состоит из следующих основных микросервисов:

- **Микросервис "Website"**: отвечает за управление пользователями и чат-комнатами. Здесь пользователи могут зарегистрироваться, войти в систему, создать чат-комнату, найти комнаты и отправить сообщения.
- **Микросервис WebSocket "Chat"**: обрабатывает соединения WebSocket для чат-комнат, передавая сообщения между пользователями в одной и той же комнате.
- **База данных (PostgreSQL)**: хранит данные о пользователях, чат-комнатах и сообщениях.
- **Nginx**: выступает в роли обратного прокси, перенаправляя HTTP-запросы к микросервису "Website" и WebSocket-соединения к микросервису "Chat".

### 2. Принципы работы каждого компонента

#### 2.1 Микросервис "Website"
- **Управление пользователями**: пользователи могут создать новый аккаунт, указав email, имя пользователя и пароль. При регистрации система сохраняет эти данные в таблице `users` в зашифрованном виде.
- **Авторизация**: при входе пользователя система проверяет учетные данные и, если они верны, создает JWT-токен для дальнейшей аутентификации. Этот токен сохраняется в cookies браузера для использования в последующих запросах.
- **Создание комнаты**: авторизованный пользователь может создать новую комнату. Информация о комнате сохраняется в таблице `chat_rooms` вместе с идентификатором создателя комнаты.
- **Поиск комнат**: пользователь может искать чат-комнаты по имени, чтобы присоединиться к уже существующим беседам.
- **Удаление комнаты**: только владелец комнаты может ее удалить. При удалении комнаты также удаляются все сообщения в ней.

#### 2.2 Микросервис WebSocket "Chat"
- **Управление WebSocket-соединениями**: когда пользователь входит в чат-комнату, устанавливается WebSocket-соединение с микросервисом по пути `/ws/{room_name}`, где `room_name` — это имя комнаты.
- **Отправка и получение сообщений**: после успешного подключения пользователь может отправлять сообщения другим участникам. Сообщение передается микросервису "Chat", который затем передает его всем пользователям, подключенным к этой комнате.
- **Хранение сообщений**: каждое новое сообщение сохраняется в таблице `messages` с содержимым, именем отправителя и временем отправки.

#### 2.3 База данных (PostgreSQL)
База данных используется для хранения всей информации проекта:
- **Таблица `users`**: хранит информацию о пользователях, включая `id`, `email`, `username`, и `hashed_password`.
- **Таблица `chat_rooms`**: хранит информацию о чат-комнатах, включая `id`, `name` (имя комнаты) и `owner_id` (идентификатор создателя).
- **Таблица `messages`**: хранит сообщения, включая `id`, `content` (текст сообщения), `room_id` (идентификатор комнаты), `username` (имя отправителя), и `timestamp` (время отправки).

#### 2.4 Nginx
Nginx настроен как обратный прокси-сервер, перенаправляющий запросы к различным микросервисам:
- **Перенаправление HTTP-запросов**: HTTP-запросы пользователей перенаправляются на микросервис "Website", включая запросы на вход в систему, регистрацию, создание и поиск чат-комнат.
- **Перенаправление WebSocket-соединений**: WebSocket-соединения перенаправляются на микросервис "Chat", обеспечивая обмен сообщениями в реальном времени между пользователями в комнате.

### 3. Процесс работы системы

1. **Пользователь заходит на главную страницу**: ему предлагается зарегистрироваться или войти в систему.
2. **Создание комнаты**: после входа в систему пользователь может создать новую комнату или найти существующие комнаты для присоединения.
3. **Вход в комнату**: при входе в комнату устанавливается WebSocket-соединение, позволяя пользователю отправлять и получать сообщения в режиме реального времени.
4. **Отправка и получение сообщений**: сообщения передаются всем пользователям в комнате через WebSocket, а также сохраняются в базе данных для возможности последующего просмотра.
5. **Завершение сеанса**: при отключении пользователя от комнаты соединение WebSocket закрывается.

### 4. Заключение
Проект успешно реализует систему онлайн-чата с базовой функциональностью, такой как регистрация, вход, создание и удаление комнат, а также обмен сообщениями в реальном времени. Использование таких технологий, как FastAPI, WebSocket и Nginx, обеспечивает высокую производительность и масштабируемость системы, подходящую для больших чатов.
