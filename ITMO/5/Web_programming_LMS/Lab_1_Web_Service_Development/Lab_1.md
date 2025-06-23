## Cây thư mục

```css
project-root/
├── .gitignore                  # Loại trừ các file/thư mục không cần thiết khi push lên Git
├── .dockerignore              # Loại trừ các file/thư mục không cần thiết khi build Docker image
├── docker-compose.yml         # Cấu hình Docker Compose cho toàn bộ dự án
│
├── website/                   # Microservice quản lý người dùng và phòng chat
│   ├── app/
│   │   ├── main.py            # Điểm khởi đầu của ứng dụng website
│   │   ├── database.py        # Cấu hình kết nối với PostgreSQL và ORM
│   │   ├── models.py          # Các model cho người dùng và phòng chat
│   │   ├── schemas.py         # Các schema cho dữ liệu đầu vào/đầu ra
│   │   ├── routers/           # Các route cho website
│   │   │   ├── auth.py        # Đăng ký và đăng nhập người dùng
│   │   │   ├── chat.py        # Quản lý phòng chat (tạo, tìm kiếm)
|   |   |   └── websocket_handler.py
│   │   ├── templates/         # Các template HTML sử dụng Jinja2
│   │   │   ├── index.html     # Template cho trang chủ
|   |   |   ├── chat.html 
|   |   |   ├── login.html
|   |   |   ├── register.html
|   |   |   └── room_chat.html
│   │   └── static/            
|   |       └── favicon.ico
│   ├── Dockerfile             # Dockerfile cho website service
│   ├── requirements.txt       # Các thư viện cần thiết cho website
|   └── .gitignore 
│
├── chat/                      # Microservice WebSocket cho phòng chat
│   ├── app/
│   │   ├── main.py            # Điểm khởi đầu cho WebSocket server
│   │   └── websocket_handler.py # Xử lý các sự kiện WebSocket
│   ├── Dockerfile             # Dockerfile cho chat service
│   └── requirements.txt       # Các thư viện cần thiết cho chat
│
├── db/                        # Cấu hình cho cơ sở dữ liệu PostgreSQL
|   ├── dump/
│   ├── Dockerfile             # Dockerfile cho PostgreSQL
│   └── init.sql               # Cấu trúc bảng và dữ liệu khởi tạo
│
└── nginx/                     # Cấu hình cho Nginx
    ├── nginx.conf             # Cấu hình reverse proxy cho website và chat
    └── Dockerfile             # Dockerfile cho Nginx
```

### Mô tả cây thư mục


### Root-Level Files
- **.gitignore**: Chứa danh sách các tệp và thư mục cần loại trừ khi đẩy mã nguồn lên Git, chẳng hạn như các tệp `.env`, tệp log, tệp cache, và các thư mục tạm thời không cần thiết.
  
- **.dockerignore**: Loại trừ các tệp và thư mục không cần thiết khỏi quá trình build Docker image, ví dụ như thư mục `.git`, tệp log, cache, và các tệp cấu hình cục bộ.

- **docker-compose.yml**: Tệp cấu hình Docker Compose cho phép quản lý toàn bộ các dịch vụ của dự án, bao gồm `website`, `chat`, `db` (PostgreSQL), và `nginx`. Định nghĩa các container, volume, network, và các biến môi trường cần thiết.

### `website` - Microservice quản lý người dùng và phòng chat
- **website/Dockerfile**: Định nghĩa cách xây dựng Docker image cho microservice `website`, cài đặt các thư viện cần thiết từ `requirements.txt` và chạy ứng dụng.

- **website/requirements.txt**: Chứa danh sách các thư viện cần thiết cho `website`, như `FastAPI`, `SQLAlchemy`, `Jinja2`, và `psycopg2`.

- **website/app**: Thư mục chính của mã nguồn ứng dụng `website`.
  - **main.py**: Điểm khởi đầu của ứng dụng FastAPI cho `website`, cài đặt ứng dụng và các route cần thiết.
  - **database.py**: Cấu hình kết nối với cơ sở dữ liệu PostgreSQL thông qua SQLAlchemy, bao gồm hàm để khởi tạo phiên làm việc với cơ sở dữ liệu.
  - **models.py**: Định nghĩa các model của SQLAlchemy cho các bảng trong cơ sở dữ liệu như `User` và `ChatRoom`.
  - **schemas.py**: Định nghĩa các schema của Pydantic để đảm bảo tính hợp lệ của dữ liệu đầu vào và đầu ra, ví dụ như `UserCreate` và `ChatRoomCreate`.

  - **routers**: Chứa các route của FastAPI cho `website`.
    - **auth.py**: Quản lý đăng ký và đăng nhập người dùng, bao gồm tạo và xác thực mã JWT cho phiên người dùng.
    - **chat.py**: Quản lý các phòng chat, bao gồm chức năng tạo, tìm kiếm, và xóa phòng chat.
    - **websocket_handler.py**: Xử lý các kết nối WebSocket, quản lý các kết nối và gửi tin nhắn cho các thành viên trong phòng chat.

  - **templates**: Chứa các tệp HTML được render với Jinja2.
    - **index.html**: Template cho trang chủ của `website`.
    - **chat.html**: Template để hiển thị danh sách phòng chat và giao diện để người dùng có thể tham gia phòng.
    - **login.html**: Template cho trang đăng nhập người dùng.
    - **register.html**: Template cho trang đăng ký người dùng.
    - **room_chat.html**: Template cho giao diện phòng chat cụ thể, nơi người dùng có thể gửi và xem tin nhắn.

  - **static**: Chứa các tài nguyên tĩnh như biểu tượng trang web (`favicon.ico`).

### `chat` - Microservice WebSocket cho phòng chat
- **chat/Dockerfile**: Định nghĩa cách xây dựng Docker image cho microservice `chat`, cài đặt các thư viện cần thiết từ `requirements.txt` và chạy ứng dụng.

- **chat/requirements.txt**: Danh sách các thư viện cần thiết cho microservice `chat`, bao gồm `FastAPI` và các thư viện hỗ trợ WebSocket.

- **chat/app**: Thư mục chính chứa mã nguồn của ứng dụng `chat`.
  - **main.py**: Điểm khởi đầu của server WebSocket. Cấu hình các endpoint và thiết lập kết nối WebSocket.
  - **websocket_handler.py**: Quản lý các sự kiện WebSocket, bao gồm kết nối người dùng, xử lý gửi/nhận tin nhắn, và ngắt kết nối.

### `db` - Cấu hình cho cơ sở dữ liệu PostgreSQL
- **db/Dockerfile**: Định nghĩa cách xây dựng Docker image cho dịch vụ PostgreSQL, bao gồm việc sao chép các tệp cấu hình và khởi tạo dữ liệu.

- **db/dump**: Thư mục chứa các bản sao lưu (backup) của cơ sở dữ liệu để lưu trữ dữ liệu vĩnh viễn trên ổ đĩa máy chủ.

- **db/init.sql**: Tệp SQL khởi tạo chứa câu lệnh để tạo bảng cho các model như `User` và `ChatRoom` trong PostgreSQL, cũng có thể chứa dữ liệu mẫu để kiểm thử.

### `nginx` - Cấu hình cho Nginx làm reverse proxy
- **nginx/nginx.conf**: Tệp cấu hình Nginx để thiết lập reverse proxy cho các microservice `website` và `chat`. Nginx sẽ chuyển hướng các yêu cầu HTTP đến `website` và yêu cầu WebSocket đến `chat`.

- **nginx/Dockerfile**: Định nghĩa cách xây dựng Docker image cho Nginx, sao chép tệp cấu hình `nginx.conf` vào container. 

---
