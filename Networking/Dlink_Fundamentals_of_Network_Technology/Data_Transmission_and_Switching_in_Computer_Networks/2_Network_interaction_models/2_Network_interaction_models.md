# Mô hình tương tác mạng

## 2.1 Mô hình OSI

Vào cuối thập niên 1970, hai dự án độc lập đã được khởi động nhằm xác định tiêu chuẩn thống nhất cho kiến trúc của các hệ thống mạng. Một dự án được thực hiện bởi Tổ chức Tiêu chuẩn hóa Quốc tế (International Organization for Standardization, ISO), và dự án kia do Ủy ban Cố vấn Quốc tế về Điện báo và Điện thoại (International Telegraph and Telephone Consultative Committee, CCITT) thực hiện. Cả hai tổ chức đều phát triển các tài liệu mô tả các mô hình mạng tương tự nhau. Vào năm 1983, những tài liệu này đã được hợp nhất thành một tiêu chuẩn gọi là "Mô hình tham chiếu cơ bản cho kết nối hệ thống mở" (The Basic Reference Model for Open Systems Interconnection). Tiêu chuẩn này, thường được gọi là mô hình tham chiếu OSI (Open Systems Interconnection Reference Model) hoặc mô hình OSI, đã được ISO công bố (dưới tên ISO 7498) và CCITT (dưới tên X.200) vào năm 1984. Hiện tại, CCITT được gọi là ITU-T (Sektor Tiêu chuẩn hóa Viễn thông của Liên minh Viễn thông Quốc tế).

Mô hình tham chiếu kết nối hệ thống mở hoặc mô hình OSI xác định các lớp của hệ thống tương tác, tên gọi chuẩn và các chức năng mà mỗi lớp phải thực hiện.

Ban đầu, mô hình OSI được tạo ra như là cơ sở để phát triển một bộ giao thức phổ quát, gọi là Bộ giao thức OSI (OSI Protocol Suite). Tuy nhiên, nó không được phổ biến rộng rãi, nhưng mô hình này đã trở thành một công cụ hữu ích cho việc học tập các công nghệ mạng và phát triển các giao thức và thiết bị.

## 2.2 Các lớp của mô hình OSI

Mô hình OSI chia nhiệm vụ truyền thông tin giữa các nút thành bảy cấp độ, mỗi cấp độ thực hiện một nhiệm vụ cụ thể và tương tác với các cấp độ phía trên và phía dưới. Các cấp độ tương đối độc lập với nhau, vì vậy các nhiệm vụ liên quan đến từng cấp độ có thể được thực hiện một cách độc lập. Điều này cho phép thay đổi cách giải quyết các vấn đề ở một cấp độ mà không gây xung đột với các cấp độ khác. Việc phân chia theo cấp độ này được gọi là biểu diễn phân cấp, vì vậy mô hình OSI thường được gọi là mô hình phân cấp.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_1_OSI_model.png" alt="Hình 2.1 - OSI model" width="1000">
</p>
<p align="center"><b>Mô hình OSI</b></p>

- Các lớp dưới của mô hình OSI (từ tầng 1 đến tầng 3) quản lý việc truyền tải vật lý dữ liệu qua mạng và được triển khai dưới dạng phần cứng và phần mềm.

- Các lớp trên của mô hình OSI (4 đến 7) cho phép phân phối dữ liệu chính xác giữa các ứng dụng chạy trên các nút mạng và thường chỉ được triển khai trong phần mềm.

- Mỗi lớp, ngoại trừ lớp ứng dụng, cung cấp các dịch vụ cho lớp trên. Bất kỳ lớp nào ngoài lớp vật lý đều sử dụng các dịch vụ được cung cấp bởi lớp bên dưới. Nói cách khác, lớp N cung cấp dịch vụ cho lớp N+1 và sử dụng các dịch vụ từ lớp N-1

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_2_services_provided_by_the_layers_of_the_OSI_model.png" alt="Các dịch vụ được cung cấp bởi các lớp của mô hình OSI" width="1000">
</p>
<p align="center"><b>Hình 2.2 - Các dịch vụ được cung cấp bởi các lớp của mô hình OSI</b></p>

- Mô hình OSI không mô tả các dịch vụ và giao thức được sử dụng ở mỗi lớp, nó xác định một tập hợp các hành động mà lớp đó phải thực hiện để truyền thông tin giữa các nút. Tuy nhiên, ISO cũng đã phát triển các tiêu chuẩn cho từng cấp độ không có trong mô hình tham chiếu mà mỗi cấp độ được công bố dưới dạng Tiêu chuẩn quốc tế riêng biệt.


### 2.2.1 Tương tác giữa các lớp

- Mô hình OSI xác định sơ đồ trao đổi dữ liệu giữa các nút mạng, nhưng bản thân nó không phải là một phương thức trao đổi như vậy. Trao đổi dữ liệu được thực hiện nhờ các giao thức.
- **Giao thức-protocol** là một bộ quy tắc và thỏa thuận chính thức chi phối việc trao đổi thông tin giữa các nút trên mạng. Nó thực hiện các chức năng của một hoặc nhiều lớp OSI.
- Có một số lượng lớn các giao thức trao đổi dữ liệu - *giao thức mạng cục bộ và toàn cầu, giao thức định tuyến, giao thức mạng.*
- **Các giao thức mạng cục bộ-local network protocol** hoạt động ở cấp độ liên kết vật lý và dữ liệu của mô hình OSI và xác định các quy tắc trao đổi dữ liệu qua các kênh liên lạc khác nhau được sử dụng trong mạng cục bộ.
- **Các giao thức mạng toàn cầu-global network protocol** xác định các quy tắc trao đổi dữ liệu qua các kênh truyền thông mạng toàn cầu khác nhau.
- **Giao thức định tuyến-routing protocol** là các giao thức hoạt động ở lớp mạng của mô hình OSI và cho phép bạn xác định tuyến đường tốt nhất để truyền dữ liệu giữa các nút.
- **Các giao thức mạng-network protocol** bao gồm các giao thức khác nhau hoạt động ở cấp độ mạng trở lên.

- Theo mô hình OSI, mỗi cấp độ của nút gửi thông tin một cách hợp lý (theo chiều ngang) tương tác với cấp độ tương tự của nút nhận thông tin theo quy tắc của một giao thức cụ thể. Mỗi cấp độ “dường như” tương tác trực tiếp với cùng cấp độ của một nút khác. Điều này cho phép tương tác giữa trình duyệt Web và máy chủ Web, ứng dụng email và máy chủ email, v.v.

- Tuy nhiên, kết nối vật lý của các thiết bị chỉ xảy ra ở lớp vật lý của mô hình OSI; vì vậy, để dữ liệu được truyền qua mạng đến một thiết bị khác, nó phải "xuống" từ lớp ứng dụng xuống lớp vật lý trong nút truyền. Khi dữ liệu được truyền qua kênh liên lạc, lớp vật lý của thiết bị nhận sẽ trích xuất nó từ môi trường truyền và chuyển lên lớp trên. Do đó, sự tương tác thực sự của các lớp cùng tên diễn ra theo chiều dọc thông qua việc tương tác với các lớp liền kề (lớp dưới và lớp trên) của ngăn xếp giao thức-protocol stack của chúng.
- **Ngăn xếp giao thức-protocol stack** là tập hợp các giao thức ở các cấp độ khác nhau. Nổi tiếng nhất là ngăn xếp giao thức TCP/IP.
- Các quy tắc và thủ tục chịu trách nhiệm tương tác giữa các lớp liền kề được gọi là giao diện - interfaces.
- Thông tin dữ liệu và dịch vụ được truyền giữa các cấp theo cả hai hướng. Có các giao diện nổi tiếng giữa các lớp, cho phép chúng giao tiếp với nhau mà không cần suy nghĩ về việc triển khai.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_3_Interaction_between_levels.png" alt="Tương tác giữa các lớp" width="1000">
</p>
<p align="center"><b>Hình 2.3 - Tương tác giữa các lớp</b></p>

### 2.2.2 Đóng gói dữ liệu - Data Encapsulation

- Sự tương tác giữa các lớp giống nhau trong mô hình OSI được thực hiện theo logic bằng cách sử dụng các quy tắc của từng giao thức cụ thể. Sự tương tác này diễn ra dưới dạng truyền tin nhắn, gọi là các đơn vị dữ liệu giao thức (protocol data units, PDU). Mỗi PDU có một định dạng đặc biệt, được xác định theo các chức năng và yêu cầu của giao thức cụ thể.
- Để tổ chức việc truyền dữ liệu, giao thức của tầng N phải chuyển PDU xuống tầng dưới N-1. Giao thức của tầng N-1 sẽ cung cấp dịch vụ cho tầng trên N, tức là nó sẽ nhận PDU của giao thức tầng N, thứ sẽ trở thành dữ liệu cho tầng N-1, xử lý chúng và tiếp tục chuyển xuống tầng N-2. Ở tầng N-1, PDU của giao thức tầng N sẽ được gọi là đơn vị dữ liệu dịch vụ (service data unit, SDU). Để cung cấp dịch vụ, giao thức của tầng N-1 đặt SDU nhận được từ tầng N vào trường dữ liệu của PDU của mình và thêm thông tin điều khiển (header và/hoặc trailer) cần thiết cho giao thức để thực hiện chức năng của nó. Quá trình này được gọi là đóng gói dữ liệu (data encapsulation).
- Đóng gói (Encapsulation) là quá trình trong đó thông tin điều khiển của một giao thức (của tầng) được thêm vào dữ liệu trước khi gửi vào mạng.
- Các thuật ngữ đặc biệt được sử dụng để chỉ định PDU của một số giao thức. PDU của giao thức TCP, hoạt động ở tầng vận chuyển (transport) của mô hình OSI và ngăn xếp TCP/IP, được gọi là đoạn (segment). PDU của giao thức IP, hoạt động ở tầng mạng của mô hình OSI và tầng Internet của ngăn xếp TCP/IP, được gọi là gói tin (packet) hoặc datagram IP. Ở tầng liên kết dữ liệu (data link) của mô hình OSI và tầng truy cập mạng (network access) của ngăn xếp TCP/IP, PDU được gọi là khung (frame).
- Hãy xem xét quá trình đóng gói dữ liệu khi truyền dữ liệu giữa các nút, được minh họa trong Hình 2.4. Khi một ứng dụng trên máy tính A gửi tin nhắn đến ứng dụng trên máy tính B, nó sẽ chuyển tin nhắn này đến tầng ứng dụng của máy tính A. Sau đó, từ tầng ứng dụng, dữ liệu được truyền xuống tầng trình bày, rồi gửi xuống tầng phiên. Tầng phiên chuyển tiếp dữ liệu đến tầng vận chuyển, và tầng này tạo ra một đoạn (segment) bằng cách thêm thông tin điều khiển, rồi chuyển nó đến tầng mạng của mô hình OSI. Tầng mạng nhận đoạn đó và thêm tiêu đề của mình, hình thành một gói tin (packet), rồi chuyển gói tin xuống tầng dưới. Tầng liên kết dữ liệu tạo ra một khung (frame) bằng cách thêm tiêu đề và phần cuối của tầng liên kết dữ liệu, sau đó chuyển khung này đến tầng vật lý. Ở tầng vật lý, luồng bit được chuyển đổi thành các tín hiệu điện, điện từ, hoặc quang học và được gửi qua môi trường truyền dẫn đến máy tính B.

- Tầng vật lý của máy tính B nhận các tín hiệu từ môi trường truyền dẫn và trích xuất thông tin từ các tín hiệu đó dưới dạng luồng bit. Sau đó, từ luồng bit này, một khung (frame) được tạo ra và truyền lên tầng liên kết dữ liệu. Tầng liên kết dữ liệu nhận khung và phân tích thông tin điều khiển được gửi đến nó. Nếu không có lỗi nào, tầng liên kết dữ liệu sẽ trích xuất dữ liệu từ thông điệp, được gửi lên tầng mạng, và chuyển dữ liệu này lên tầng trên. Quá trình này lặp lại ở mỗi tầng phía trên cho đến tầng ứng dụng. Tầng ứng dụng của máy tính B truyền thông tin đến ứng dụng đích và quá trình trao đổi dữ liệu hoàn tất. Nói cách khác, khi thông điệp đến nút nhận, nó sẽ đi qua tất cả các tầng theo thứ tự ngược lại (từ tầng 1 đến tầng 7), lần lượt được chuyển đổi tại mỗi tầng bằng cách sử dụng thông tin điều khiển tương ứng, cho đến khi đến ứng dụng đích. Quá trình này được gọi là giải đóng gói dữ liệu (decapsulation).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_4_Data_exchange_between_network_nodes_according_to_the_OSI_model.png" alt="Trao đổi dữ liệu giữa các nút mạng theo mô hình OSI" width="1000">
</p>
<p align="center"><b>Hình 2.4 - Trao đổi dữ liệu giữa các nút mạng theo mô hình OSI</b></p>

### 2.2.3 Mô tả các lớp của mô hình OSI

- **Tầng ứng dụng (Application layer)** là tầng thứ bảy, gần với người dùng nhất trong mô hình OSI. Nó khác biệt so với các tầng khác ở chỗ không cung cấp dịch vụ cho bất kỳ tầng nào khác trong mô hình OSI, mà chỉ phục vụ các tiến trình ứng dụng nằm ngoài phạm vi của mô hình OSI. Ví dụ có thể là trình duyệt Web, vốn là một tiến trình ứng dụng được chạy trên máy tính và sử dụng các dịch vụ do giao thức tầng ứng dụng HTTP (Hypertext Transfer Protocol) cung cấp; hoặc ứng dụng email sử dụng các dịch vụ của giao thức POP3 (Post Office Protocol Version 3).

- Tầng ứng dụng xác định và thiết lập khả năng kết nối với các đối tác truyền thông dự kiến, đồng bộ hóa các chương trình ứng dụng làm việc cùng nhau, cũng như thỏa thuận về các quy trình khôi phục sau lỗi và kiểm soát tính toàn vẹn của dữ liệu. Tầng ứng dụng cũng xác định mức độ đầy đủ của các tài nguyên để thực hiện việc liên lạc dự kiến.
  
- **Tầng trình bày (Presentation layer)** là tầng thứ sáu trong mô hình OSI. Nó chịu trách nhiệm đảm bảo rằng thông tin được tầng ứng dụng của một hệ thống gửi đi có thể được đọc bởi tầng ứng dụng của hệ thống khác. Khi cần thiết, tầng trình bày chuyển đổi các định dạng dữ liệu bằng cách sử dụng một định dạng chung để biểu diễn thông tin. Ngoài ra, nó có thể thực hiện nén (giải nén) dữ liệu nhằm tăng băng thông mạng. Hơn nữa, tại tầng trình bày, có thể thực hiện mã hóa (giải mã) dữ liệu, ví dụ như sử dụng giao thức SSL (Secure Sockets Layer). Tuy nhiên, mã hóa dữ liệu không chỉ được thực hiện ở tầng 6 của mô hình OSI, mà còn có thể được thực hiện ở các tầng thấp hơn. Ví dụ điển hình là công nghệ IPSec. Cần lưu ý rằng tầng trình bày không phải lúc nào cũng được sử dụng trong quá trình tổ chức tương tác mạng, vì các chức năng của nó có thể được thực hiện trong tầng ứng dụng hoặc đơn giản là không cần thiết trong trường hợp cụ thể.
- **Tầng phiên (Session layer)** là tầng thứ năm trong mô hình OSI. Như tên gọi của nó, tầng này cho phép hai tiến trình ứng dụng thiết lập, quản lý và kết thúc các phiên liên lạc (sessions) với nhau. Tầng phiên đồng bộ hóa cuộc hội thoại giữa các tiến trình ứng dụng và chịu trách nhiệm khôi phục các phiên liên lạc bị gián đoạn đột ngột. Các công nghệ của tầng phiên thường được thực hiện dưới dạng một bộ công cụ phần mềm, được gọi là application program interfaces (API, giao diện lập trình ứng dụng). API cung cấp một tập hợp các dịch vụ, cho phép lập trình viên phát triển các ứng dụng mạng mà không phải lo lắng về việc vận chuyển, địa chỉ hóa và truyền tải dữ liệu. Những chức năng này được thực hiện bởi các tầng bên dưới trong mô hình OSI.
- **Tầng vận chuyển (Transport layer)** là tầng thứ tư trong mô hình OSI. Các hệ điều hành hiện đại là đa nhiệm, do đó, người dùng có thể cùng lúc làm việc với nhiều ứng dụng khác nhau, gửi và nhận dữ liệu qua mạng. Tầng vận chuyển là liên kết giữa các tầng ứng dụng, tầng trình bày và tầng phiên, những tầng chỉ xử lý các tiến trình ứng dụng, và các tầng bên dưới, những tầng xử lý việc truyền tải dữ liệu trực tiếp. Nó cô lập các tầng trên của mô hình OSI khỏi các vấn đề liên quan đến việc truyền tải bất kỳ thông tin nào và chịu trách nhiệm đảm bảo việc truyền dữ liệu đáng tin cậy giữa các ứng dụng tương tác trên các máy tính khác nhau thông qua việc sử dụng các phương tiện địa chỉ hóa và đa hợp/giải hợp (một quá trình truyền tải dữ liệu đồng thời từ nhiều tiến trình ứng dụng qua một kết nối và sau đó gửi chúng đến các ứng dụng tương ứng). Ngoài ra, tầng vận chuyển ở phía người gửi chia nhỏ dữ liệu nhận được từ các tầng trên thành các khối có kích thước nhỏ, được gọi là đoạn (segments), và chuyển chúng đến người nhận theo đúng thứ tự. Quá trình này được gọi là phân đoạn (segmentation). Tại tầng vận chuyển của người nhận, các đoạn này được gom lại thành luồng dữ liệu ban đầu.
- Các giao thức của tầng vận chuyển có thể cung cấp các dịch vụ có thiết lập kết nối (connection-oriented) và không có thiết lập kết nối (connectionless). Các giao thức có thiết lập kết nối chịu trách nhiệm về việc thiết lập, duy trì và kết thúc kết nối giữa người gửi và người nhận. Chúng có thể thực hiện việc chẩn đoán và sửa chữa các lỗi phát sinh trong quá trình truyền tải thông tin, cũng như cung cấp các cơ chế kiểm soát luồng dữ liệu (flow control). Một ví dụ về các giao thức loại này là giao thức TCP (Transmission Control Protocol, giao thức điều khiển truyền tải). Các giao thức không có thiết lập kết nối thì không thực hiện việc thiết lập kết nối trước khi truyền dữ liệu và không đảm bảo việc giao hàng đáng tin cậy. Giao thức UDP (User Datagram Protocol, giao thức datagram người dùng) là một ví dụ về giao thức tầng vận chuyển không có thiết lập kết nối.
- **Tầng mạng (Network layer)** là tầng thứ ba trong mô hình OSI. Đây là một trong những tầng quan trọng nhất của mô hình OSI và chịu trách nhiệm kết nối các nút nằm trong các mạng địa lý khác nhau. Tầng mạng thực hiện hai chức năng chính: *địa chỉ logic và định tuyến*. Mỗi thiết bị được kết nối với mạng đều được gán một địa chỉ logic, còn được gọi là địa chỉ tầng 3. Địa chỉ này được sử dụng để định tuyến các gói tin. Định tuyến là quá trình xác định lộ trình tốt nhất để truyền thông tin từ người gửi đến người nhận, khi người gửi và người nhận nằm trong các mạng khác nhau và được kết nối một cách ngẫu nhiên. Tại tầng mạng, các nhiệm vụ liên quan đến quản lý luồng dữ liệu và chẩn đoán lỗi truyền tải cũng được giải quyết. Tầng mạng thực hiện việc đóng gói các đoạn dữ liệu nhận được từ tầng vận chuyển thành các gói (còn được gọi là datagram). Giao thức chính của tầng mạng là giao thức IP (Internet Protocol).
- **Tầng liên kết dữ liệu (Data link layer)** là tầng thứ hai trong mô hình OSI. Tầng này cung cấp cho các nút mạng quyền truy cập vào môi trường truyền dẫn và giải quyết các vấn đề về địa chỉ vật lý (trái ngược với địa chỉ mạng hoặc địa chỉ logic), phát hiện và sửa lỗi, đảm bảo việc truyền tải khung một cách có thứ tự, và cấu trúc logic của mạng. Tầng liên kết dữ liệu hoàn tất quá trình đóng gói và đưa các datagram (gói tin) nhận được từ tầng mạng vào trong các khung (frame). Ví dụ về các giao thức của tầng liên kết dữ liệu có thể kể đến là bộ giao thức Ethernet IEEE 802.3 và các giao thức mạng không dây IEEE 802.11.

- **Tầng vật lý (Physical layer)** là tầng thấp nhất trong mô hình OSI. Tầng này thực hiện việc truyền tải luồng bit, nhận được từ tầng liên kết dữ liệu, qua môi trường vật lý dưới dạng tín hiệu điện, quang học hoặc sóng vô tuyến. Tầng vật lý chịu trách nhiệm kích hoạt, duy trì và ngưng hoạt động của kênh vật lý giữa các hệ thống cuối. Các thông số kỹ thuật của tầng vật lý mô tả chi tiết các giao diện cơ học, quang học, điện và chức năng với môi trường truyền dẫn: điện áp, tần số, bước sóng, đầu nối, số lượng và chức năng của các tiếp điểm, sơ đồ mã hóa tín hiệu, v.v. Ngoài ra, tầng vật lý cũng xem xét các vấn đề liên quan đến cấu trúc vật lý của mạng.

**Bảng 2.1: Bảng so sánh các tầng trong mô hình OSI**

| **Tầng** | **Tên Tầng**               | **Loại dữ liệu được xử lý**  | **Chức năng**                                                  |
|----------|---------------------------|-------------------------------|---------------------------------------------------------------|
| 7        | Appication Layer          | User data                     | Cung cấp dịch vụ cho các ứng dụng mạng                       |
| 6        | Presentation Layer        | User data                     | Định dạng chung để biểu diễn dữ liệu, nén và mã hóa          |
| 5        | Session Layer             | User data                     | Thiết lập, quản lý và kết thúc các phiên giữa các ứng dụng   |
| 4        | Transport Layer           | Segments/Datagram             | Địa chỉ hóa tiến trình, phân đoạn/tái cấu trúc dữ liệu, kiểm soát luồng, giao hàng đáng tin cậy |
| 3        | Network Layer             | Packages/Datagram             | Truyền tải tin nhắn giữa các thiết bị từ xa, chọn lộ trình tốt nhất, địa chỉ logic |
| 2        | Data Link Layer           | Khung (Frame)                 | Quyền truy cập vào môi trường truyền dẫn, truyền tải tin nhắn giữa các thiết bị cục bộ, địa chỉ vật lý |
| 1        | Physical Layer            | Bit                           | Truyền tải tín hiệu điện, quang học hoặc sóng vô tuyến giữa các thiết bị |


- Cần lưu ý rằng trong mô hình OSI, một giao thức riêng biệt không phải lúc nào cũng tương ứng với một trong bảy tầng. Đôi khi, một giao thức tương ứng với nhiều hơn một tầng của mô hình OSI. Ví dụ, giao thức ARP (Address Resolution Protocol-Giao thức phân giải địa chỉ), chuyển đổi các địa chỉ mạng IPv4 (tầng 3 của mô hình OSI) thành các địa chỉ MAC vật lý (tầng 2 của mô hình OSI), có thể được gọi là giao thức "tầng 2.5". Ngoài ra, nhiều giao thức có thể được triển khai trong cùng một tầng, như các giao thức định tuyến tầng 3 như RIP (Routing Information Protocol-Giao thức thông tin định tuyến), OSPF (Open Shortest Path First-Đường đi ngắn nhất mở đầu tiên), v.v.

- Trong một số trường hợp, PDU của giao thức tầng N có thể được đóng gói (encapsulate) trong PDU của giao thức tầng N+1, điều này đặc trưng, đặc biệt là đối với các mạng riêng ảo (VPN). Trong nhiều triển khai VPN, các giao thức của tầng liên kết (Ethernet) hoặc tầng mạng (IP) được đóng gói trong các giao thức của tầng vận chuyển (thường là UDP). Khi truyền tải thông điệp, giao thức định tuyến tầng 3 như RIP sử dụng giao thức của tầng vận chuyển UDP.

## 2.3 Mô hình TCP/IP và Stack Protocol của TCP/IP

- Trước khi mô hình OSI ra đời, đã có nhiều mô hình mạng và stack protocol khác nhau được phát triển, vì vậy stack protocol được xây dựng hoàn toàn theo mô hình OSI không được phổ biến. Mặc dù vậy, mô hình OSI vẫn là một mô hình khái niệm và là một công cụ thuận tiện cho việc học các công nghệ mạng cũng như phát triển các giao thức và thiết bị.

- Stack protocol TCP/IP được phát triển trước mô hình OSI, do đó, các nhà phát triển của nó không sử dụng mô hình OSI để mô tả kiến trúc của ngăn xếp này. Họ đã phát triển một mô hình riêng, có nhiều tên gọi, bao gồm mô hình TCP/IP (ransmission Control Protocol/Internet Protocol-Giao thức điều khiển truyền tải/Giao thức Internet), mô hình DARPA (Defense Advanced Research Projects Agency-Cơ quan Dự án Nghiên cứu Quốc phòng Hoa Kỳ) (DARPA hoặc ARPA) hoặc mô hình DOD (United States Department of Defense-Bộ Quốc phòng Hoa Kỳ).

- Vì mô hình OSI rất phổ biến, kiến trúc TCP/IP thường được mô tả bằng cách sử dụng các tên gọi của các tầng trong mô hình TCP/IP và các tầng tương ứng trong mô hình OSI.


### 2.3.1 Mô tả các lớp của mô hình TCP/IP

- Mô hình TCP/IP, giống như mô hình OSI, có cấu trúc nhiều tầng, nhưng để dữ liệu từ ứng dụng trên máy tính A được truyền đến ứng dụng trên máy tính B, chúng phải lần lượt đi qua 4 tầng: Application layer - tầng ứng dụng, Transport Layer - tầng vận chuyển, Internet Layer - tầng Internet và Network Access Layer - tầng truy cập môi trường.

- Như được chỉ ra trong hình 2.5, ba tầng trên cùng của mô hình OSI tương ứng với **tầng ứng dụng (Application layer)** trong mô hình TCP/IP, bao gồm các chức năng của việc trình bày, mã hóa và kiểm soát việc thiết lập kết nối. Có nhiều giao thức ở tầng ứng dụng, trong đó phổ biến nhất là FTP, TFTP, HTTP/HTTPS, DHCP, DNS, Telnet, SMTP, POP3, IMAP, và nhiều giao thức khác.
- ***Tầng vận chuyển (Transport layer)** của mô hình TCP/IP thực hiện các chức năng tương tự như tầng cùng tên trong mô hình OSI. Ở tầng này, có hai giao thức được xác định - TCP và UDP. Giao thức TCP (Transmission Control Protocol-Giao thức điều khiển truyền tải) đảm bảo việc giao hàng đáng tin cậy của các đoạn dữ liệu qua mạng thông qua việc thiết lập một kết nối logic giữa người gửi và người nhận dữ liệu. Giao thức UDP (User Datagram Protocol-Giao thức datagram người dùng), trái ngược với TCP, không thiết lập kết nối giữa người gửi và người nhận thông điệp và không đảm bảo việc giao hàng đáng tin cậy của dữ liệu.
- **Tầng Internet (Internet layer)** tương đương với các chức năng của tầng mạng trong mô hình OSI và đảm bảo tổ chức kết nối giữa các mạng và các phân mạng tạo thành một mạng tổng hợp. Giao thức chính của tầng Internet là IP, thực hiện hai chức năng chính - định địa chỉ các nút và chọn lộ trình tốt nhất đến mạng đích (định tuyến). Ngoài ra, ở tầng này còn có các giao thức ICMP, IGMP, cũng như các giao thức định tuyến như RIP, OSPF và BGP.
- **Tầng truy cập mạng (Network access layer)** kết hợp các chức năng của tầng liên kết và tầng vật lý trong mô hình OSI, đảm bảo việc truyền dữ liệu vật lý trong mạng. Có nhiều giao thức khác nhau ở tầng truy cập mạng, trong đó phổ biến nhất là Ethernet, Token Ring, FDDI, PPP, IEEE 802.11 (Wi-Fi), ATM và nhiều giao thức khác.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_5_Correspondence_between_the_layers_of_the_OSI_model_and_the_TCP_IP_model.png" alt="Sự tương ứng giữa các lớp của mô hình OSI và mô hình TCP/IP" width="1000">
</p>
<p align="center"><b>Hình 2.5 - Sự tương ứng giữa các lớp của mô hình OSI và mô hình TCP/IP</b></p>

- Hiện nay, stack TCP/IP là một trong những stack giao thức phổ biến nhất trong mạng máy tính. Stack TCP/IP có một số lợi thế so với các stack protocol khác (IPX/SPX, NetBIOS/SMB). Điều này bao gồm, đặc biệt, khả năng định tuyến gói tin, hệ thống địa chỉ linh hoạt và số lượng thông điệp quảng bá ít.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_6_stack_protocol_TCP_IP.png" alt="Stack Protocol TCP/IP" width="1000">
</p>
<p align="center"><b>Hình 2.6 Stack Protocol TCP/IP</b></p>
