### **Bài thực hành số 4: Hệ thống bảo vệ thông tin khỏi truy cập trái phép - Secret Net**

---

#### **Mục tiêu bài thực hành**
- Quản lý truy cập trong hệ thống **Secret Net 5.1**.
- Áp dụng các cơ chế bảo vệ thông tin như:
  - Quản lý truy cập có chọn lọc.
  - Quản lý truy cập toàn quyền.
  - Môi trường phần mềm khép kín (ЗПС).

---

#### **1. Tổng quan hệ thống Secret Net 5.1**
Hệ thống sử dụng các cơ chế sau để đảm bảo an toàn thông tin:
1. **Quản lý truy cập có chọn lọc (Discretionary Access Control)**: Sử dụng các cơ chế tiêu chuẩn của Windows và công cụ riêng để kiểm soát truy cập đến thiết bị (đĩa, cổng, v.v.).
2. **Quản lý truy cập toàn quyền (Mandatory Access Control)**: Hạn chế quyền truy cập dựa trên cấp độ bảo mật và kiểm soát dòng chảy thông tin.
3. **Môi trường phần mềm khép kín (ЗПС)**: Hạn chế người dùng chỉ được phép sử dụng các chương trình được phép.

---

#### **2. Các bước thực hiện**

##### **2.1. Phân quyền thiết bị**
Hệ thống phân chia thiết bị theo nhóm và loại:
- **Cài đặt quyền truy cập**:
  1. Vào **"Пуск | Все программы | Secret Net 5 | Локальная политика безопасности"**.
  2. Chọn **"Параметры безопасности | Параметры Secret Net | Устройства"**.
  3. Thiết lập quyền truy cập và chế độ hoạt động:
     - **Chế độ "мягкий" (mềm):** Ghi nhận truy cập không hợp lệ vào nhật ký.
     - **Chế độ "жесткий" (cứng):** Chặn truy cập trái phép.

##### **2.2. Quản lý toàn quyền**
- **Kiểm soát dòng thông tin:** Đảm bảo không phát tán thông tin mật ra ngoài.
- **Kiểm soát in ấn:** Chỉ cho phép người dùng có quyền in tài liệu mật. Nhật ký in ấn được lưu lại.

##### **2.3. Phân loại độ bảo mật**
- **Thiết lập quyền bảo mật tài nguyên:**
  1. Sử dụng **"Проводник"**, chọn **"Свойства"** và vào mục **"Secret Net"**.
  2. Chọn mức bảo mật: **"Конфиденциально"** (Bảo mật) hoặc **"Строго конфиденциально"** (Rất bảo mật).
  3. Áp dụng cho các thư mục và tệp tin.

##### **2.4. Môi trường phần mềm khép kín (ЗПС)**
- **Thiết lập danh sách chương trình được phép chạy:**
  1. Vào **"Пуск | Все программы | Secret Net 5 | Контроль программ и данных"**.
  2. Tạo danh sách chương trình được phép.
  3. Chuyển sang chế độ **"жесткий"** để chặn các chương trình không được phép.

---

#### **3. Các câu hỏi kiểm tra**
1. Các cơ chế quản lý truy cập nào được sử dụng trong hệ thống **Secret Net 5.1**?
2. Chế độ "мягкий" và "жесткий" khác nhau như thế nào?
3. Có thể thay đổi quyền truy cập trên ổ đĩa hệ thống (C:) không?
4. Mô hình dữ liệu trong **Secret Net 5.1** là gì? Nó bao gồm những đối tượng nào?
5. Người dùng nào có quyền thay đổi mức độ bảo mật tài nguyên?
6. Hệ thống file nào được hỗ trợ để áp dụng mức độ bảo mật?

---

#### **Hướng dẫn cài đặt thực hành**
1. Đăng nhập hệ thống bằng tài khoản quản trị viên.
2. Tạo cấu trúc thư mục và áp dụng mức độ bảo mật cho từng thư mục/tệp tin.
3. Cài đặt quyền truy cập thiết bị.
4. Kiểm tra hoạt động của môi trường phần mềm khép kín.

