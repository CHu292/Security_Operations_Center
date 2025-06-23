# System Information Collector

## Mô tả

Đây là một ứng dụng web được xây dựng bằng FastAPI, có khả năng thu thập thông tin về máy tính và hệ thống của người dùng từ xa. Khi người dùng truy cập vào một trang web cụ thể, ứng dụng sẽ thu thập các thông tin như tên người dùng, tên máy tính, thông tin CPU, bộ nhớ RAM và phiên bản hệ điều hành, sau đó ghi thông tin này vào một tệp trên một đĩa mạng có thể truy cập được.

## Yêu cầu

- Python 3.7+
- FastAPI
- Uvicorn
- psutil

## Cài đặt

1. **Clone Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Cài đặt các thư viện cần thiết**

   ```bash
   pip install fastapi uvicorn psutil
   ```

3. **Chạy ứng dụng**

   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

## Cách sử dụng

1. Mở trình duyệt web và truy cập vào địa chỉ:

   ```
   http://<địa chỉ_ip_của_server>:8000
   ```

   để xem thông điệp chào mừng.

2. Để thu thập thông tin hệ thống, yêu cầu người dùng truy cập vào:

   ```
   http://<địa chỉ_ip_của_server>:8000/system-info
   ```

3. Thông tin hệ thống sẽ được ghi vào một tệp `system_info.txt` trong thư mục được chỉ định theo địa chỉ IP của máy khách.

## Cấu trúc thư mục

```
.
├── app.py                      # Tệp chính của ứng dụng
├── requirements.txt            # Các thư viện cần thiết (nếu có)
└── README.md                   # Tài liệu hướng dẫn
```

## Lưu ý

- Hãy đảm bảo bạn có quyền truy cập vào thư mục đích nơi thông tin sẽ được ghi.
- Đảm bảo tuân thủ các quy định pháp lý và đạo đức về quyền riêng tư của người dùng trước khi thu thập thông tin.

## Thử nghiệm

- Ứng dụng đã được thử nghiệm trên nhiều máy khách để đảm bảo khả năng thu thập thông tin chính xác và hiệu quả.
