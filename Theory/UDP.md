# UDP

UDP (User Datagram Protocol) là một giao thức truyền tải dữ liệu thuộc tầng vận chuyển trong mô hình TCP/IP, cho phép gửi các gói dữ liệu (datagram) mà không cần thiết lập kết nối trước. UDP không đảm bảo việc truyền dữ liệu thành công, không kiểm soát thứ tự gói tin và không có cơ chế sửa lỗi, nhưng bù lại, nó giảm độ trễ và tăng tốc độ truyền tải. 

**Đặc điểm của UDP:**

- **Không kết nối (connectionless):** Không cần thiết lập kết nối trước khi truyền dữ liệu, giúp giảm thời gian chờ. 

- **Không đảm bảo độ tin cậy:** Gói tin có thể bị mất hoặc nhận không theo thứ tự; ứng dụng phải tự xử lý nếu cần. 

- **Không kiểm soát tắc nghẽn:** UDP không có cơ chế kiểm soát tắc nghẽn tích hợp, vì vậy ứng dụng của bạn nên có cách để quản lý việc sử dụng băng thông. 

**Ứng dụng của UDP:**

UDP thường được sử dụng trong các ứng dụng yêu cầu tốc độ cao và chấp nhận một mức độ mất mát dữ liệu nhất định, như:

- **Truyền phát video và âm thanh trực tuyến:** Yêu cầu độ trễ thấp để đảm bảo trải nghiệm người dùng. 

- **Trò chơi trực tuyến:** Cần phản hồi nhanh, chấp nhận mất mát gói tin nhỏ để duy trì tốc độ. 

- **Giao thức DNS (Domain Name System):** Yêu cầu truy vấn nhanh chóng, không cần thiết lập kết nối. 

Hiểu rõ về UDP giúp bạn lựa chọn giao thức phù hợp cho ứng dụng, cân bằng giữa tốc độ và độ tin cậy trong truyền tải dữ liệu. 
