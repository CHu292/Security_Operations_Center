# 1. Thiết lập môi trường
## 1.1 Tạo và kích hoạt môi trường ảo (khuyến nghị):

```bash
sudo apt install python3.10-venv
````

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate    # Trên MacOS/Linux
venv\Scripts\activate       # Trên Windows
```

## 1.2 Cài đặt các thư viện cần thiết: Dựa vào tệp requirements.txt, cài đặt tất cả các thư viện bằng lệnh:

```bash
pip install -r requirements.txt
```

# 2.  Cấu hình biến môi trường

Tạo một tệp .env ở thư mục gốc của dự án (nếu chưa có) và thêm các biến môi trường cần thiết:

```
# .env - Các biến môi trường cần thiết
SECRET_KEY=mysecretkey
DATABASE_URL=postgresql+psycopg2://username:password@localhost/coffee_shop_db
DEBUG=True
```
Lưu ý:

Thay username, password, và localhost/coffee_shop_db bằng thông tin kết nối cơ sở dữ liệu thực tế của bạn.



Cài đặt Flask-Migrate

```bash
pip install Flask-Migrate
```
 pip install SQLAlchemy==1.4.46
 
pip install -r requirements.txt

flask db init

flask db migrate -m "Initial migration"

flask db upgrade
