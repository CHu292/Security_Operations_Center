# 1.5 Hệ thống phân tán

- Từ "phân tán - distributed" trong các thuật ngữ như "hệ thống phân tán - distributed system", "lập trình phân tán - distributed programming" và "thuật toán phân tán - distributed algorithm" ban đầu dùng để chỉ các mạng máy tính trong đó các máy tính riêng lẻ được phân bổ vật lý trong một khu vực địa lý. Những thuật ngữ này hiện được sử dụng theo nghĩa rộng hơn nhiều, thậm chí còn đề cập đến các quy trình tự trị chạy trên cùng một máy tính vật lý và giao tiếp với nhau thông qua việc truyền tin nhắn.
- Vì không có định nghĩa duy nhất về hệ thống phân tán nên trong bối cảnh mạng máy tính, chúng ta sẽ hiểu nó là một hệ thống có các thành phần nằm trên các máy tính khác nhau tương tác và phối hợp hành động của chúng bằng cách truyền tin nhắn cho nhau qua mạng.
- Các hệ thống phân tán sử dụng nhiều kiến ​​trúc phần cứng và phần mềm khác nhau. Ở mức độ thấp hơn, cần kết nối nhiều bộ xử lý bằng cách sử dụng một loại mạng nào đó, cho dù mạng đó được in trên bảng mạch hay được tổ chức thông qua các thiết bị và dây cáp. Ở cấp độ cao hơn, cần phải liên kết các tiến trình chạy trên các bộ xử lý này bằng một số loại hệ thống truyền thông.
- Mô hình máy khách-máy chủ (client - server) là nền tảng của hầu hết các dịch vụ và giao thức trong ngăn xếp TCP/IP. Ví dụ: một trình duyệt Web, được sử dụng để xem các trang trên Internet, về cơ bản là một ứng dụng khách Web phần mềm và trang web mà tài nguyên mà người dùng có quyền truy cập là một máy chủ Web.
- Mô hình client-server mô tả cách các tiến trình tương tác trong một ứng dụng phân tán. Thành phần máy chủ của một ứng dụng (máy chủ) cung cấp chức năng hoặc dịch vụ cho một hoặc nhiều thành phần máy khách (máy khách), khởi tạo các yêu cầu đối với các dịch vụ đó. Thông thường, một dịch vụ là sự trừu tượng hóa tài nguyên máy tính. Tài nguyên máy chủ được khách hàng chia sẻ có thể là bất kỳ thành phần phần mềm và phần cứng nào của nó.
- Các tiến trình máy khách và máy chủ có thể chạy trên cùng một thiết bị hoặc trên các thiết bị khác nhau được kết nối qua mạng máy tính.
- Máy khách và máy chủ trao đổi tin nhắn bằng cách sử dụng sơ đồ phản hồi yêu cầu (request-response). Máy khách gửi yêu cầu và máy chủ trả về phản hồi. Các quy tắc giao tiếp giữa máy khách và máy chủ, được đặt trên các thiết bị từ xa, được xác định trong giao thức truyền thông.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/1_Basic_concepts_of_network_technologies/image/5_Receiving_configuration_parameters_from_the_server_by_the_client_via_DHCP_protocol.png" alt="Nhận thông số cấu hình của máy khách từ máy chủ thông qua giao thức DHCP" width="1000">
</p>
<p align="center"><b>Nhận thông số cấu hình của máy khách từ máy chủ thông qua giao thức DHCP</b></p>

