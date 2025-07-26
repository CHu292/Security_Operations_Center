# NGINX - Web Server

## NGINX  là gì?
- Nginx là một web server mã nguồn mở (open source) mạnh mẽ và nổi tiếng. Nó sử dụng các kiến trúc đơn luồng, hướng sự kiện (event-driven), không đồng bộ (asynchronous). Do đó, nó có hiệu suất, sự ổn định tối đa hơn hẳn Apache server.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/NGINX/Nginx-la-gi-1.jpg" alt="Nginx là một web server mã nguồn mở" width="1000">
</p>
<p align="center"><b>Nginx là một web server mã nguồn mở</b></p>

- Sau 2 năm triển khai nghiên cứu, Igor Sysoev đã chính thức cho xuất bản Nginx vào tháng 10/2004. Ban đầu, Nginx được ra đời nhằm phục vụ web HTTP. Tuy nhiên, ngày nay, chúng đã được ứng dụng rộng rãi hơn, dùng làm reverse proxy, HTTP load balancer, email proxy. Có tới 1 – 4% tổng số lượng tên miền trên thế giới sử dụng Nginx, điển hình như Facebook, Google, Microsoft,….

## Nguyên lý hoạt động

- Không giống như các chương trình server khác, Nginx hoạt động không dựa vào luồng (threads) để xử lý những truy vấn (request). Thay vào đó, nó sẽ hoạt động theo kiến trúc sự kiện không đồng bộ. Điều này có nghĩa là các luồng tương tự sẽ được quản lý trong một tiến trình. Trong mỗi tiến trình này lại chứa các đơn vị nhỏ hơn gọi là worker connection, chịu trách nhiệm xử lý các threads cung cấp các yêu cầu của work process và gửi tới master process. Sau đó, master process sẽ đảm nhiệm nhiệm vụ trả kết quả cho những yêu cầu đó.
- Nghe qua tưởng chừng cách hoạt động này có vẻ đơn giản. Thế nhưng, mỗi worker connection lại có thể xử lý tới 1024 yêu cầu tương tự nhau. Từ đó giúp xử lý được hàng ngàn yêu cầu khác nhau mà không gặp phải bất cứ trở ngại gì. Chính đặc điểm này khiến Nginx được nhiều người lựa chọn cho các website có nhiều yêu cầu như trang thương mại điện tử, trình tìm kiếm, cload storage.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/NGINX/Nginx-la-gi-2.jpg" alt="Nguyên lý hoạt động của Nginx" width="1000">
</p>
<p align="center"><b>Nguyên lý hoạt động của Nginx</b></p>

## Các tính năng của Nginx là gì?

**Tính năng của máy chủ HTTP Nginx**

- Xử lý hơn 10.000 kết nối cùng một lúc với bộ nhớ thấp.
- Phục vụ static file, index file và lập chỉ mục tập tin.
- Gia tăng tốc độ reverse proxy, cân bằng tải đơn giản và khả năng chịu lỗi vô cùng tốt.
- Tăng tốc bộ nhớ đệm của FastCGI, uWSGI, SCGI và máy chủ memcached.
- Hỗ trợ kiến trúc modular, tăng tốc độ nạp trang thông qua cách nén gzip tự động.
- Hỗ trợ WebSockets từ 1.3.13, hỗ trợ mã hoá SSL và TLS, truyền tải file FLV và MP4.
- Máy chủ ảo VPS hoạt động dựa trên địa chỉ IP và tên có khả năng tương thích lên đến IPv6.

**Tính năng máy chủ mail proxy của Nginx**

- Máy chủ mail proxy của Nginx có 3 phương pháp xác thực: POP3 (USER/PASS, APOP LOGIN/PLAIN/CRAM-MD5), IMAP (LOGIN, AUTH LOGIN/PLAIN/CRAM-MD5), SMTP (AUTH LOGIN/PLAIN/CRAM-MD5). Ngoài ra, chúng còn hỗ trợ SSL, STARTTLS và STLS.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/NGINX/Nginx-la-gi-3.jpg" alt="Tính năng của Nginx" width="1000">
</p>
<p align="center"><b>Tính năng của Nginx</b></p>

## Ưu, nhược điểm của Nginx là gì?

**Ưu điểm của Nginx**

Nginx trở nên phổ biến và ngày càng được ứng dụng nhiều là do chúng sở hữu một số điểm mạnh như:

- Cung cấp cơ chế bộ nhớ đệm tốt, giúp tăng hiệu suất của ứng dụng khi người dùng truy cập vào cùng 1 địa chỉ trong thời gian ngắn.
- Là web server trọng lượng nhẹ chuyển tiếp các yêu cầu người dùng tới máy chủ ứng dụng.
- Quy tắc ghi lại của Nginx đã đem đến sự linh hoạt hơn khi định cấu hình chuyển hướng vĩnh viễn hoặc tạm thời cho một số URL.
- Nginx dễ dàng tuỳ chỉnh và phân phối qua giao thức HTTPS.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/NGINX/Nginx-la-gi-4.jpg" alt="Nginx giúp gia tăng hiệu suất của ứng dụng" width="1000">
</p>
<p align="center"><b>Nginx giúp gia tăng hiệu suất của ứng dụng</b></p>

**Nhược điểm của Nginx**

Bên cạnh những ưu điểm nổi bật trên, Nginx còn tồn tại một số nhược điểm như:

- Cân bằng tải còn hạn chế so với các máy chủ khác.
- Cơ chế lưu trữ, cung cấp các lệnh cần phải cải thiện.
- Việc điều hướng giữa trang chủ Nginx và bộ phận hỗ trợ khách hàng thực hiện rất khó.
