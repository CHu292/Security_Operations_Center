
# Hướng Dẫn Sử Dụng Chương Trình Mã Hóa Thông Tin Hệ Thống

## Mô Tả
Chương trình này thu thập thông tin hệ thống và lưu vào một file có tên `sys.tat`. Thông tin này bao gồm:
- Tên người dùng
- Tên máy tính
- Dung lượng bộ nhớ
- Thông tin CPU
- Phiên bản hệ điều hành

Sau khi thông tin được lưu, chương trình sẽ mã hóa file `sys.tat` để bảo vệ dữ liệu.

## Cấu Trúc Thư Mục
Dưới đây là cấu trúc thư mục của dự án:
```
Lab_3/
│
├── sys_doc.py             # File mã nguồn chính để thực thi chương trình
├── secur.py               # File mã nguồn mã hóa
├── key.key                # File chứa khóa mã hóa được tạo tự động
├── public_key.pem         # File khóa công khai (nếu có yêu cầu sử dụng)
└── README.md              # Hướng dẫn sử dụng
```

## Các Thành Phần Chính
- **`sys_doc.py`**: Đây là chương trình chính, dùng để thu thập thông tin hệ thống và lưu vào file `sys.tat`, sau đó mã hóa file này.
- **`secur.py`**: File mã nguồn phụ trợ có chứa các chức năng mã hóa và giải mã (nếu có).
- **`key.key`**: File chứa khóa mã hóa tự động tạo ra mỗi khi chạy chương trình, dùng để mã hóa và giải mã thông tin trong `sys.tat`.

## Yêu Cầu
- Python 3
- Thư viện `cryptography` để mã hóa (cài đặt bằng `pip install cryptography`)
- Thư viện `psutil` để lấy thông tin bộ nhớ (cài đặt bằng `pip install psutil`)

## Cách Thực Thi Chương Trình

1. **Di chuyển đến thư mục chứa mã nguồn:**
   ```bash
   cd /path/to/Lab_3
   ```

2. **Chạy chương trình chính `sys_doc.py`:**
   ```bash
   python3 sys_doc.py
   ```

3. **Thông tin đầu ra:**
   - Sau khi thực thi, chương trình sẽ:
     - Tạo file `sys.tat` trong thư mục hiện tại, chứa thông tin hệ thống.
     - Mã hóa nội dung của `sys.tat`.
     - Sao chép các file `secur.py` và `key.key` vào thư mục hiện tại nếu chưa tồn tại.
   - Thông báo thành công sẽ được hiển thị trong terminal:  
     ```
     Hoàn tất. File sys.tat đã được tạo và mã hóa trong thư mục hiện tại.
     ```

## Chi Tiết Kỹ Thuật
1. **Mã Hóa**: 
   - File `sys.tat` được mã hóa bằng thuật toán Fernet của thư viện `cryptography`.
   - Mỗi khi chạy, chương trình sẽ tạo một khóa ngẫu nhiên và lưu vào file `key.key` để sử dụng khi mã hóa.

2. **Thông Tin Hệ Thống**:
   - Thông tin hệ thống được thu thập bao gồm tên người dùng, tên máy, dung lượng bộ nhớ, thông tin CPU, và phiên bản hệ điều hành.

## Lưu Ý
- **File `key.key`**: Đảm bảo giữ an toàn file `key.key`, vì đây là file chứa khóa để giải mã file `sys.tat`. Nếu mất file này, dữ liệu trong `sys.tat` sẽ không thể phục hồi được.
- Chương trình sẽ kiểm tra và không sao chép `secur.py` và `key.key` nếu chúng đã có trong thư mục hiện tại.

## Gỡ lỗi
- **Lỗi `SameFileError`**: Nếu gặp lỗi này, chương trình đang cố sao chép một file mà file đó đã tồn tại trong thư mục hiện tại. Hãy chắc chắn rằng file `secur.py` và `key.key` không bị trùng trong thư mục đích hoặc sửa lại đường dẫn.
- **Lỗi không tìm thấy `cryptography` hoặc `psutil`**: Hãy cài đặt thư viện bằng lệnh `pip install cryptography psutil`.

## Tác Giả
Chu Văn Đoàn và Chat GPT của anh ấy :)
