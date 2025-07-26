**Mục tiêu của bài thực hành**

Nâng cao kỹ năng sử dụng các ngôn ngữ lập trình phía máy chủ, framework làm việc với cơ sở dữ liệu và hệ thống ORM.

**Yêu cầu**

1. Dựa trên cơ sở dữ liệu đã được tạo trong các bài thực hành trước, cần phát triển một dịch vụ tương tác với cơ sở dữ liệu đã thiết kế. Dịch vụ này có thể là:
   - Giao diện web;
   - Ứng dụng desktop;
   - API;
   - Các dịch vụ tiền xử lý dữ liệu, phục vụ việc điền dữ liệu vào cơ sở dữ liệu (như xử lý kết nối websocket, phân tích trang web, xử lý JSON, v.v.);
   - Các dịch vụ bảo vệ dữ liệu trong quá trình xử lý, ghi và đọc từ cơ sở dữ liệu (mã hóa, ẩn danh hóa, bảo mật mạng, v.v.);
   - (Danh sách này không bao gồm toàn bộ các dịch vụ có thể triển khai, xem mục 4 trong ghi chú).

   Hãy giải thích ngắn gọn lý do chọn môi trường phát triển, ngôn ngữ và framework mà bạn sử dụng để tương tác với cơ sở dữ liệu.

2. Trong khuôn khổ bài thực hành này, mô tả cách bạn tương tác với cơ sở dữ liệu: sử dụng framework hoặc ngôn ngữ nào. Hãy minh họa một số ví dụ về việc truy vấn, thêm, xóa dữ liệu từ cơ sở dữ liệu của bạn thông qua framework hoặc ngôn ngữ lập trình đã chọn. Kiểm tra tính chính xác của hệ thống ghi log và phân quyền đã được triển khai trong các bài thực hành 1-3.

3. Đối với dịch vụ đã triển khai, nêu ngắn gọn các chức năng chính, mục đích và mô tả ngắn gọn về cấu trúc của dịch vụ. Đồng thời, mô tả và đánh giá các phương pháp bảo vệ dữ liệu đã triển khai cũng như các phương pháp có sẵn trong dịch vụ đã phát triển. Nêu bật các phương pháp tương tự, nhược điểm và ưu điểm của giải pháp đã triển khai.

**Ghi chú**

Khi viết các truy vấn phức tạp, hãy lựa chọn các mối quan hệ phù hợp với vai trò người dùng. Trong báo cáo cần cung cấp đầy đủ mã nguồn của giao diện người dùng để có thể chạy mã nguồn. Nếu cần môi trường hoặc công cụ bổ sung để biên dịch/chạy, hãy mô tả ngắn gọn các công cụ này.

Trong báo cáo, cần mô tả ngắn gọn mục đích và thuật toán của tất cả các module trong giao diện người dùng đã được phát triển. 

Trong bài thực hành này, có thể xem xét các lựa chọn thay thế, chẳng hạn như phát triển API với các phương thức truy vấn cơ sở dữ liệu hoặc thay vì giao diện có thể triển khai một lớp tiền xử lý dữ liệu trước khi đưa thông tin vào cơ sở dữ liệu. 

Ngoài ra, các giải pháp lập trình khác đáp ứng các yêu cầu sau đây cũng có thể được chấp nhận: 
Giải pháp lập trình tương tác với cơ sở dữ liệu đã thiết kế và hệ thống bảo mật của nó (tiêu thụ hoặc cập nhật, tạo dữ liệu cho cơ sở dữ liệu); 

Đối với giải pháp lập trình đã phát triển, cũng cần xem xét các vấn đề bảo mật thông tin. Ví dụ, nếu phát triển một API trên cơ sở dữ liệu, bạn có thể đưa vào báo cáo các thông tin về thuật toán xác thực đang sử dụng (như OAuth2, v.v.).
