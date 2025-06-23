# Bài thực hành số 3

## A) Thực hiện trên hệ điều hành cục bộ.

### 1. Tạo tài liệu văn bản (sys.tat) chứa thông tin "Hệ thống".
### 2. Viết chương trình cài đặt sys_doc.exe cho tài liệu này, chương trình sẽ hiển thị dưới dạng cài đặt bản cập nhật (với thanh tiến trình) cho một phần mềm nào đó (ví dụ Notepad hoặc Paint) với các chức năng sau:

- Yêu cầu người dùng chọn thư mục (cho phép lựa chọn thư mục có sẵn hoặc tạo mới) để sao chép thông tin "Hệ thống".
- Ghi vào thư mục một file với mã thực thi của chương trình secur.exe (tương tự yêu cầu cho `template.tbl` trong Bài thực hành số 1), bảo vệ file sys.tat.
- Thu thập thông tin (có thể) về máy tính đang cài đặt chương trình.
- Mã hóa thông tin này và ghi vào file sys.tat.
- Ký thông tin bằng khóa cá nhân của người dùng và ghi chữ ký, ví dụ vào Windows Registry tại `HKEY_CURRENT_USER\Software\Ho_Ten_Sinh_Vien` dưới dạng tham số `Signature`.
- Khởi chạy secur.exe để bảo vệ sys.tat khỏi truy cập trái phép.
- Đặt secur.exe chạy khi thực thi chức năng Open cho sys.tat để bảo vệ hoạt động cả sau khi khởi động lại hệ điều hành (có thể sử dụng một số phương pháp "liên kết" này).

### 3. Chương trình bảo vệ secur.exe cần có các chức năng sau:

- Yêu cầu người dùng nhập thông tin về tên của khóa trong Registry chứa chữ ký số điện tử (tên sinh viên).
- Đọc chữ ký từ khóa Registry đã nêu trên và kiểm tra bằng khóa công khai của người dùng.
- Cho phép hoặc từ chối xem thông tin "Hệ thống" trong file sys.tat dựa trên tính chính xác của khóa được chỉ định.

### 4. Nếu việc kiểm tra không thành công, chương trình bảo vệ phải ngừng hoạt động và thông báo lỗi phù hợp.

### 5. Thông tin thu thập về máy tính phải bao gồm tối thiểu các thông tin sau:

- Tên người dùng,
- Tên máy tính,
- Cấu hình máy tính (ít nhất là bộ nhớ và bộ xử lý) và phiên bản hệ điều hành.

## B) Thực hiện trên mạng cục bộ (hoặc mạng ảo).

### 1. Tạo một script thực hiện việc thu thập thông tin từ xa mà người dùng không hay biết (người dùng chỉ cần mở một trang web từ người tạo script), bao gồm thông tin về máy tính và hệ thống của họ (theo mục 5 của yêu cầu trước) và lưu vào ổ đĩa mạng cục bộ (được người tạo script truy cập) trong một thư mục có tên là địa chỉ IP hoặc địa chỉ Mac của máy người dùng.

### 2. Thiết lập quyền truy cập vào thông tin này (có thể ghi vào ổ đĩa từ xa).

### 3. Kiểm thử trên 3–5 thiết bị khách và thu thập thống kê.

## Lưu ý
Mọi giải pháp sáng tạo đều được hoan nghênh và khuyến khích! Trong báo cáo, hãy mô tả các cải tiến và cách giải quyết của bạn để đánh giá phù hợp.

