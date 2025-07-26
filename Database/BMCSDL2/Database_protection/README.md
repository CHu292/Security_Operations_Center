# Bảo vệ cơ sở dữ liệu
---
## Mục tiêu:
Luyện kỹ năng tạo hệ thống giám sát đơn giản, phân quyền truy cập và mã hóa bằng các công cụ của Hệ Quản Trị Cơ Sở Dữ Liệu (CSDL).
## Nhiệm vụ:
### 1.  Nhiệm vụ giám sát CSDL
- Tạo bảng nhật ký, riêng biệt với các thực thể chính trong CSDL của bạn.
- Tạo trình kích hoạt (trigger) cho mỗi bảng chính trong DB của bạn để kích hoạt khi có bất kỳ thay đổi nào xảy ra trong DB (chèn dữ liệu mới, thay đổi các bản ghi hiện có, xóa các bộ dữ liệu khỏi bảng). Khi được kích hoạt, trình kích hoạt (trigger) sẽ nhập thông tin vào bảng nhật ký về thời điểm thực hiện thay đổi, yêu cầu được nhận từ vai trò nào, các bộ dữ liệu nào đã thay đổi, giá trị cũ và mới.
- Trình bày cách hệ thống ghi nhật ký hoạt động cho các hoạt động và mối quan hệ khác nhau
### 2. Nhiệm vụ mã hóa dữ liệu.
- Tạo một bảng có dữ liệu bí mật, tách biệt với các thực thể chính của bạn. Ví dụ: đây có thể là bảng có mã thông báo hoặc khóa truy cập cho từng lớp người dùng.
- Mã hóa nội dung của bảng này, sử dụng bất kỳ thuật toán mã hóa đối xứng nào làm thuật toán mã hóa. Khóa mã hóa cho bảng này không được lưu trữ trong IS. Khóa mã hóa có thể được lấy từ mật khẩu riêng để giải mã siêu người dùng (mật khẩu không liên quan đến mật khẩu để đăng nhập vào DBMS). Mật khẩu riêng của siêu người dùng và khóa mã hóa có thể được liên hệ thông qua hàm một chiều. Ví dụ, hãy để mật khẩu riêng là tổ hợp "!stroNgpsw31234", tính toán hàm băm xác định từ mật khẩu này (ví dụ: sha-256), sử dụng hàm băm kết quả làm khóa mã hóa/giải mã cho thuật toán mã hóa đối xứng cho bảng có dữ liệu bí mật (ví dụ: đối với AES-256)
- Chúng tôi chứng minh rằng ngay cả khi có toàn quyền quản trị viên, nhưng không biết mật khẩu riêng, thì không thể lấy được nội dung của bảng có dữ liệu bí mật
### 3. Nhiệm vụ phân định quyền truy cập vào CSDL
- Tạo ít nhất 2 vai trò trong DBMS (siêu người dùng không được tính) cho mỗi lớp người dùng thông tin;
- Sử dụng các công cụ DBMS nội bộ, xác định một tập hợp các đặc quyền cho từng vai trò liên quan đến các bảng trong DB của bạn. Thực hiện theo nguyên tắc đặc quyền tối thiểu: nếu một nhóm người dùng nhất định không cần truy cập vào một số bảng/thuộc tính nhất định (danh sách các tác vụ DB được biên dịch trong khuôn khổ của Lab1), thì quyền truy cập vào các bảng/thuộc tính này không được cung cấp. Chúng tôi phân biệt quyền truy cập vào các chế độ xem được tạo trong Lab 1, cũng như các bảng ghi nhật ký (chỉ siêu người dùng mới có thể xem các bảng ghi nhật ký)
- Trình bày hoạt động của hệ thống kiểm soát truy cập của bạn. Đi sâu vào từng vai trò và hiển thị các mối quan hệ có sẵn từ mỗi vai trò.
