# QUIC

QUIC (Quick UDP Internet Connections) là một giao thức truyền tải mạng do Google phát triển vào năm 2012, nhằm cải thiện hiệu suất truyền thông trên Internet. Không giống như TCP, QUIC hoạt động trên nền tảng UDP và tích hợp các tính năng của TCP, TLS và HTTP/2, giúp giảm độ trễ và tăng tốc độ kết nối. 

**Ưu điểm của QUIC:**

- **Giảm độ trễ kết nối:** QUIC cho phép thiết lập kết nối nhanh hơn so với TCP, nhờ việc kết hợp quá trình bắt tay (handshake) của TLS và truyền tải dữ liệu trong một bước duy nhất. 

- **Khả năng phục hồi lỗi tốt hơn:** QUIC sử dụng cơ chế điều khiển tắc nghẽn và phục hồi lỗi hiệu quả, giúp duy trì kết nối ổn định ngay cả khi mạng gặp sự cố. 

- **Hỗ trợ đa luồng (multiplexing):** QUIC cho phép truyền tải nhiều luồng dữ liệu đồng thời trên một kết nối mà không gặp vấn đề chặn đầu dòng (head-of-line blocking) như trong TCP. 

**Ứng dụng của QUIC:**

QUIC được áp dụng trong giao thức HTTP/3, phiên bản mới nhất của HTTP, nhằm cải thiện tốc độ tải trang và trải nghiệm người dùng trên web. 

Việc triển khai QUIC đang được nhiều trình duyệt và dịch vụ web hỗ trợ, góp phần nâng cao hiệu suất và bảo mật trong truyền tải dữ liệu trên Internet.  
