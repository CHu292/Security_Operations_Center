# Socket
## Socket là gì?
- Socket, hay còn gọi là ổ cắm mạng, là một điểm cuối (end point) phần mềm trong hệ thống máy tính, đóng vai trò như một kênh giao tiếp để gửi và nhận dữ liệu qua mạng. Socket hoạt động như một giao diện lập trình ứng dụng (API) cho phép các chương trình tương tác với mạng máy tính.
  
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/socket/what_is_.png" alt="" width="700">
</p>

- Socket cho phép giao tiếp giữa hai process khác nhau trên cùng một máy hoặc hai máy khác nhau. Nói chính xác hơn, đó là một cách để nói chuyện với các máy tính khác bằng cách sử dụng các file descriptor Unix tiêu chuẩn.
- Trong Unix. Mọi hành động I/O được thực hiện bằng cách write hoặc read một File descriptor. File descriptor chỉ là một số nguyên được liên kết với một file đang mở. Và nó có thể là kết nối mạng, file văn bản, thiết bị đầu cuối hoặc một cái gì đó khác.
- Các socket được giới thiệu lần đầu tiên trong 2.1BSD. Và sau đó được tinh chỉnh thành dạng hiện tại với 4.2BSD. Tính năng socket hiện có sẵn với hầu hết các bản phát hành hệ thống UNIX hiện tại.
- Một trong những chức năng khác của socket là giúp các tầng TCP hoặc TCP Layer định danh ứng dụng mà dữ liệu sẽ được gửi tới thông qua sự ràng buộc với một cổng port (thể hiện là một con số cụ thể), từ đó sẽ tiến hành kết nối giữa client và server.

## Socket có vai trò như thế nào?
### 1. Giao tiếp hiệu quả
- Socket cung cấp một kênh giao tiếp trực tiếp giữa các ứng dụng trên mạng, cho phép truyền dữ liệu nhanh chóng và tin cậy. So với các phương thức giao tiếp truyền thống như HTTP, socket có khả năng xử lý dữ liệu theo thời gian thực, đáp ứng nhu cầu của các ứng dụng đòi hỏi độ trễ thấp và tương tác liên tục.

### 2. Linh hoạt
- Socket không bị giới hạn bởi các giao thức cụ thể, cho phép người dùng lựa chọn giao thức phù hợp nhất với nhu cầu của mình.
- Ví dụ: Giao thức TCP (Transmission Control Protocol) đảm bảo truyền dữ liệu an toàn và đáng tin cậy, trong khi giao thức UDP (User Datagram Protocol) ưu tiên tốc độ truyền tải hơn độ chính xác.

### 3. Khả năng mở rộng
- Socket có thể được sử dụng để xây dựng các ứng dụng có khả năng mở rộng cao, đáp ứng nhu cầu ngày càng tăng của người dùng. Bằng cách thêm nhiều socket vào hệ thống, ứng dụng có thể xử lý đồng thời nhiều kết nối và luồng dữ liệu, đảm bảo hiệu suất ổn định và đáp ứng nhanh chóng.

### 4. Hiệu suất cao
- Socket được tối ưu hóa cho truyền dữ liệu hiệu quả, giúp giảm thiểu overhead và tối đa hóa tốc độ truyền tải. So với các phương thức giao tiếp khác, socket có thể truyền tải lượng dữ liệu lớn một cách nhanh chóng và tiết kiệm tài nguyên hệ thống.

### 5. Kiểm soát chi tiết
- Socket cung cấp cho người dùng quyền kiểm soát chi tiết hơn đối với quá trình truyền dữ liệu. Bằng cách lập trình socket, người dùng có thể tùy chỉnh các thông số như kích thước gói tin, thời gian chờ và cơ chế kiểm soát lỗi, đáp ứng các yêu cầu cụ thể của ứng dụng.

### 6. Hỗ trợ đa nền tảng
- Socket được hỗ trợ rộng rãi trên nhiều hệ điều hành và ngôn ngữ lập trình, giúp người dùng dễ dàng tích hợp socket vào các ứng dụng của họ.

### 7. Phát triển ứng dụng mạng

- Socket là nền tảng cơ bản cho việc phát triển nhiều loại ứng dụng mạng phổ biến, bao gồm web server, ứng dụng chat, ứng dụng chơi game trực tuyến và các hệ thống phân tán.
- Nhìn chung, socket là công cụ mạnh mẽ và linh hoạt cho phép người dùng xây dựng các ứng dụng mạng hiệu quả, mở rộng và đáp ứng nhu cầu đa dạng.
- Tuy nhiên, việc sử dụng socket cũng đòi hỏi kiến thức lập trình và kỹ năng mạng nhất định. Người dùng cần hiểu rõ cách thức hoạt động của socket, các giao thức mạng liên quan và các vấn đề bảo mật tiềm ẩn để có thể khai thác tối đa lợi ích của socket và xây dựng các ứng dụng mạng thành công.
## Cách thức hoạt động của Socket như thế nào?
- Socket hoạt động dựa trên nguyên tắc trao đổi dữ liệu giữa hai điểm cuối trên mạng. Mỗi socket được xác định bởi hai yếu tố chính:
  - Địa chỉ IP: Xác định vị trí của socket trên mạng.
  - Số hiệu cổng: Xác định ứng dụng cụ thể nào trên máy tính mà socket sẽ giao tiếp.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/socket/How_Sockets_Work.png" alt="" width="1000">
</p>

<p align="center"><b>Socket hoạt động trên nguyên tắc trao đổi dữ liệu giữa hai điểm cuối trên mạng</b></p>


