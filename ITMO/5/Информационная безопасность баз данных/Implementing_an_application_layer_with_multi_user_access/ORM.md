# ORM là gì?

ORM (Object-Relational Mapping) là một kỹ thuật lập trình tiên tiến giúp ánh xạ cấu trúc của cơ sở dữ liệu quan hệ phức tạp vào các đối tượng trong phần mềm được viết bằng các ngôn ngữ hướng đối tượng. ORM cung cấp một lớp trừu tượng (abstraction layer) giúp giảm thiểu sự phụ thuộc vào các truy vấn SQL phức tạp, đơn giản hóa việc thao tác với dữ liệu và nâng cao tính bảo trì của code.

Ví dụ: SQLAlchemy là một framework ORM phổ biến cho Python, cho phép developers làm việc với cơ sở dữ liệu quan hệ một cách dễ dàng và hiệu quả.

# Ưu và nhược điểm của ORM là gì?

Sau khi hiểu được ORM là gì, chúng ta hãy cùng đi sâu vào phân tích ưu và nhược điểm của kỹ thuật này.

## Về ưu điểm 

- **Tăng năng suất**: ORM giúp giảm thời gian và công sức cần thiết để viết các truy vấn dữ liệu bằng cách cung cấp một API đơn giản để tạo, đọc, cập nhật và xóa dữ liệu. Thay vì viết các câu lệnh SQL phức tạp, nhà phát triển có thể sử dụng ORM để truy cập thông tin này chỉ bằng một vài dòng code.
- **Cải thiện khả năng bảo trì**: Logic truy vấn dữ liệu được tách biệt khỏi code nghiệp vụ, giúp code dễ đọc, dễ hiểu và dễ bảo trì hơn.
- **Giảm thiểu lỗi**: ORM có thể giúp giảm lỗi do đánh máy trong các câu lệnh SQL. Ví dụ, ORM tự động xử lý việc thoát các ký tự đặc biệt, giúp giảm nguy cơ lỗi SQL injection.
- **Tính độc lập với cơ sở dữ liệu**: ORM giúp code ứng dụng độc lập hơn với cơ sở dữ liệu, do ORM có khả năng ánh xạ với các hệ quản trị cơ sở dữ liệu khác nhau.

## Về nhược điểm 

- **Mất hiệu suất**: Trong một số trường hợp, ORM có thể tạo ra các truy vấn SQL kém hiệu quả so với việc viết tay.
- **Tính linh hoạt hạn chế**: ORM có thể không hỗ trợ đầy đủ tất cả các tính năng của SQL. Một số truy vấn SQL phức tạp có thể khó thực hiện bằng ORM.
- **Độ phức tạp**: ORM có thể làm tăng độ phức tạp của code đối với các nhà phát triển không quen thuộc với chúng.

Có thể thấy, ORM đem đến những ưu điểm vượt trội song vẫn còn tồn tại một số mặt hạn chế. Tùy thuộc vào mục đích và hoàn cảnh để quyết định có nên sử dụng ORM Framework hay không.

# Các loại ORM phổ biến 

Sử dụng ORM, developer có thể thao tác với dữ liệu thông qua các đối tượng quen thuộc, thay vì phải viết các truy vấn SQL phức tạp. Điều này giúp tiết kiệm thời gian, giảm thiểu lỗi và cải thiện tính bảo trì của code.

Các loại ORM phổ biến hiện nay bao gồm:

1. **SQLAlchemy**: ORM mạnh mẽ và linh hoạt hỗ trợ nhiều hệ quản trị cơ sở dữ liệu khác nhau, thường được sử dụng với Python.
2. **Django ORM**: ORM tích hợp sẵn với framework Django, giúp xây dựng nhanh chóng các ứng dụng web trên nền tảng Python.
3. **TypeORM**: ORM được thiết kế cho JavaScript và TypeScript, tương thích với nhiều hệ quản trị cơ sở dữ liệu phổ biến.
4. **Ruby on Rails**: Framework Ruby on Rails đi kèm với Active Record, một ORM mạnh mẽ và dễ sử dụng.
5. **Entity Framework**: ORM phổ biến dành cho các ứng dụng .NET, hỗ trợ nhiều loại cơ sở dữ liệu khác nhau.
6. **Hibernate**: ORM lâu đời được sử dụng rộng rãi với Java, cung cấp tính năng ánh xạ đối tượng-quan hệ hiệu quả.

# ORM hoạt động như thế nào?

ORM có đặc trưng cơ bản là gói gọn (encapsulate) toàn bộ cấu trúc của CSDL vào trong một đối tượng của ứng dụng. Đối tượng này được thiết kế để xử lý dữ liệu theo logic của lập trình hướng đối tượng, sau đó chuyển đổi thành các câu lệnh truy vấn tương thích với cấu trúc quan hệ của cơ sở dữ liệu.

[Bài viết được tham khảo ở đây](https://vietnix.vn/orm-la-gi/#orm-la-gi)
