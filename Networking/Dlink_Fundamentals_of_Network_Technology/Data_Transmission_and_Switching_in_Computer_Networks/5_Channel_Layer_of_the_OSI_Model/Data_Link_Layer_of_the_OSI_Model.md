# 5. Tầng Liên Kết Dữ Liệu Trong Mô Hình OSI

**Tầng liên kết dữ liệu** (*Data Link Layer*) là tầng thứ hai trong mô hình OSI, nằm giữa tầng vật lý và tầng mạng. Nó đảm bảo việc truyền dữ liệu nhận được từ tầng mạng thông qua tầng vật lý đến các thiết bị được kết nối trực tiếp.

**Các chức năng chính của tầng liên kết dữ liệu:**
- Quản lý quyền truy cập vào môi trường truyền dẫn;
- Quản lý luồng dữ liệu;
- Địa chỉ hóa ở mức vật lý (phần cứng);
- Định dạng và tạo khung dữ liệu;
- Đảm bảo tính xác thực của dữ liệu nhận được;
- Cung cấp địa chỉ hóa cho giao thức của tầng trên.

**Các giao thức của tầng liên kết dữ liệu:**
Hoạt động của tầng liên kết dữ liệu được quyết định bởi các giao thức của nó. Ví dụ về các giao thức này bao gồm:
- Họ giao thức Ethernet (IEEE 802.3);
- Giao thức mạng không dây (IEEE 802.11).

**Các thiết bị hoạt động ở tầng liên kết dữ liệu:**
- Bộ điều hợp mạng (network adapters);
- Bộ chuyển đổi (switches);
- Bộ điều hợp mạng thông minh với các chức năng nâng cao;
- Điểm truy cập (access points).

---

## 5.1 Phương Pháp Chuyển Mạch

Trong thực tế, việc truyền tải luồng dữ liệu từ nhiều người dùng bằng cách sử dụng chung một môi trường truyền dẫn là điều phổ biến. Trong cấu trúc mạng cục bộ thường gặp như "ngôi sao mở rộng", các đường kết nối giữa thiết bị người dùng (máy tính, máy chủ, máy in) và thiết bị truyền dẫn (switch, router) là riêng biệt, trong khi đó kết nối giữa các thiết bị truyền dẫn là dùng chung vì nó phải xử lý lưu lượng từ nhiều thiết bị người dùng khác nhau. 

Để có thể truyền đồng thời nhiều tín hiệu từ các người dùng qua một cáp duy nhất, các phương pháp ghép kênh (multiplexing) được sử dụng. Các thiết bị truyền dẫn trong trường hợp này cần có khả năng xác định hướng truyền dữ liệu, tức là thực hiện chuyển mạch (*switching*).

Phương pháp ghép kênh đồng bộ và không đồng bộ dựa trên chia sẻ thời gian (TDM) đã trở thành nền tảng cho hai nguyên lý cơ bản của chuyển mạch trong mạng máy tính:
- **Chuyển mạch kênh (circuit switching)**;
- **Chuyển mạch gói (packet switching)**.
---

### 5.1.1 Chuyển Mạch Kênh

**Chuyển mạch kênh** dựa trên TDM đồng bộ. Phương pháp này cung cấp cho mỗi cặp thiết bị đang giao tiếp một chuỗi các kênh (logic) riêng để sử dụng độc quyền.

Trong các mạng sử dụng chuyển mạch kênh, các thiết bị đầu cuối có thể được cung cấp:
- **Kênh chuyển mạch**: Kênh chỉ tồn tại trong thời gian phiên kết nối diễn ra và được giải phóng sau khi phiên kết thúc.
- **Kênh không chuyển mạch**: Kênh cố định, không bị thay đổi theo thời gian.

Kênh liên lạc, nơi dữ liệu được truyền tải, chỉ được thiết lập sau khi kết nối giữa hai hệ thống giao tiếp được hình thành. Những kênh này được gọi là **kênh chuyển mạch** hoặc **kênh tạm thời**. Kênh chỉ tồn tại trong thời gian phiên truyền dữ liệu và sẽ được giải phóng ngay khi phiên kết thúc. Quá trình chuyển mạch chỉ diễn ra vào thời điểm bắt đầu phiên kết nối. Thiết bị khởi tạo sẽ gửi yêu cầu qua mạng đến thiết bị đích, tạo ra một chuỗi kênh liên tiếp để kết nối chúng. 

 Ưu điểm và nhược điểm
- **Ưu điểm**: Chi phí thấp.
- **Nhược điểm**: Thời gian chờ kết nối lâu và khả năng bị chặn khi kênh bị "bận".

 Ví dụ thực tế
Một ví dụ điển hình của chuyển mạch kênh là **hệ thống điện thoại cố định**. Người dùng phải quay số trước khi bắt đầu cuộc gọi, và một kênh liên lạc liên tục được thiết lập thông qua các bộ chuyển mạch trung gian. Trong thời gian kênh được thiết lập, không thiết bị nào khác có thể sử dụng cùng kênh này. Sau khi kết thúc cuộc gọi, kết nối bị phá vỡ và kênh được giải phóng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/5_Channel_Layer_of_the_OSI_Model/img/5_1.png" alt="Hình minh họa 5.1: Quá trình chuyển mạch kênh." width="1000">
</p>
<p align="center"><b>Hình minh họa 5.1: Quá trình chuyển mạch kênh.</b></p>


Các kênh liên lạc giữa các hệ thống đầu cuối, sẵn sàng để truyền dữ liệu trong thời gian dài nhờ vào kết nối cố định với các đặc tính được chỉ định, được gọi là **kênh chuyên dụng (dedicated channels)** hoặc **kênh không chuyển mạch (non-switched channels)**. Kênh chuyên dụng còn được gọi là **kênh thuê bao (leased channels)**, luôn sẵn sàng cho việc truyền dữ liệu. Tuy nhiên, chi phí của các kênh này cao hơn so với **kênh chuyển mạch (switched channels)**.

Trong TDM đồng bộ (*synchronous TDM*), thời gian hoạt động của kênh vật lý được chia thành các chu kỳ lặp lại, bao gồm các khung TDM (*TDM frames*). Mỗi khung TDM bắt đầu bằng một chuỗi đồng bộ hóa (*synchronization sequence*) và bao gồm các khe thời gian (*time slots*) có độ dài bằng nhau, mỗi khe thời gian được gán cho một kênh logic riêng. Các khe thời gian được phân bổ cho tất cả các kênh đầu vào (*input channels*), được đánh số và sắp xếp theo thứ tự trong khung TDM. Các kênh đầu vào lần lượt truyền các khối dữ liệu có kích thước bằng nhau trong mỗi chu kỳ để thiết bị truyền tải ở đầu bên kia có thể hiểu đúng và định tuyến dữ liệu đến địa chỉ tương ứng.

Để thực hiện điều này, thiết bị truyền tải cần duy trì một bảng chuyển mạch (*switching table*), bảng này xác định mối quan hệ giữa:
- Cổng thuê bao đầu vào (*incoming subscriber port*) và cổng/khung thời gian đầu ra trên đường trục (*outgoing trunk port/time slot*);
- Cổng đường trục đầu vào (*incoming trunk port*) và cổng/khung thời gian đầu ra trên đường trục trung gian (*outgoing trunk port/time slot*), nếu dữ liệu được truyền qua các nút trung gian;
- Cổng đường trục đầu vào và cổng thuê bao đầu ra (*outgoing subscriber port*).

Do các hệ thống giao tiếp nhận dữ liệu trong cùng một chu kỳ và với cùng một số khe thời gian, các khối dữ liệu truyền đến phía nhận trong cùng một khoảng thời gian với độ trễ tối thiểu. Vì vậy, mạng sử dụng chuyển mạch kênh (*circuit-switched networks*) rất phù hợp cho việc truyền tải lưu lượng thoại (*voice traffic*) hoặc lưu lượng dữ liệu (*data traffic*) đồng bộ.

 Nhược điểm của chuyển mạch kênh
Một trong những nhược điểm chính của mạng chuyển mạch kênh là việc sử dụng không hiệu quả băng thông (*bandwidth inefficiency*). Trong thời gian phiên kết nối, các khe thời gian trong kênh được phân bổ nhưng không phải lúc nào cũng được sử dụng đầy đủ, dẫn đến việc các kênh còn lại không được khai thác hiệu quả.

---

### 5.1.2 Chuyển Mạch Gói

**Công nghệ chuyển mạch gói (Packet Switching)** dựa trên việc sử dụng **TDM không đồng bộ (asynchronous TDM)** hoặc **TDM thống kê (statistical TDM)**. Phương pháp này cho phép các hệ thống đầu cuối truyền dữ liệu qua mạng mà không cần chiếm dụng độc quyền kênh truyền dẫn, ngay cả trong suốt phiên kết nối. Dữ liệu được chia thành các khối nhỏ hơn, gọi là **gói (packet)**, và được truyền qua cùng một kênh dựa trên nhu cầu, không phụ thuộc vào nguồn gốc và đích đến của chúng. Các hệ thống giao tiếp chỉ chiếm dụng kênh trong thời gian cần thiết để truyền gói.

 Cơ chế hoạt động
Khác với **TDM đồng bộ (synchronous TDM)**, trong TDM không đồng bộ không có sự gắn kết cố định giữa khe thời gian (*time slots*) và thiết bị đích. Do đó, trong mạng sử dụng chuyển mạch gói, các khối dữ liệu cần được cung cấp thông tin định tuyến (**addressing information**). Mỗi gói dữ liệu bao gồm hai phần:
- **Tiêu đề (header)**: Chứa thông tin quản lý cần thiết để truyền gói, như địa chỉ, thứ tự gói, v.v.;
- **Dữ liệu (payload)**: Chứa thông tin cần truyền.

Thứ tự truyền gói, kích thước gói, và nội dung cụ thể của tiêu đề được xác định bởi giao thức mạng. Vì vậy, không giống như TDM đồng bộ, TDM không đồng bộ không minh bạch với các giao thức. Trong mạng chuyển mạch gói, cả thiết bị đầu cuối và thiết bị truyền dẫn (như **switches** và **routers**) đều phải hỗ trợ cùng một giao thức.

 Đặc điểm của gói dữ liệu
Thuật ngữ "gói" trong trường hợp này được dùng để chỉ khối dữ liệu được truyền. Ở mỗi tầng mạng, khối dữ liệu này được gọi bằng tên khác nhau:
- Ở **tầng liên kết dữ liệu (Data Link Layer)**: gọi là **khung (frame)**;
- Ở **tầng mạng (Network Layer)**: gọi là **gói (packet)** hoặc **datagram**;
- Ở **tầng vận chuyển (Transport Layer)**: gọi là **đoạn (segment)**.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/5_Channel_Layer_of_the_OSI_Model/img/5_2.png" alt="Hình 5.2 quá trình chuyển mạch gói" width="1000">
</p>
<p align="center"><b>Hình 5.2 quá trình chuyển mạch gói</b></p>


Để tăng độ tin cậy cho mạng sử dụng **chuyển mạch gói (packet switching)**, cũng như đảm bảo việc phân phối tải, cấu trúc mạng cần cung cấp nhiều tuyến đường để truyền gói giữa các hệ thống giao tiếp. Nghĩa là, các thiết bị truyền tải phải được kết nối qua nhiều kênh dự phòng. Thiết bị truyền tải sẽ dựa trên thông tin địa chỉ (*addressing information*) để định tuyến gói qua chuỗi kênh truyền, cuối cùng đến thiết bị đích. Các thiết bị này gom các gói nhận được theo đúng thứ tự để tái tạo lại thông tin ban đầu.

Các thiết bị truyền tải trong mạng chuyển mạch gói (bao gồm **switches** và **routers**) khác biệt với thiết bị của mạng chuyển mạch kênh bởi bộ nhớ đệm nội bộ (*buffer memory*). Bộ nhớ này được dùng để lưu tạm thời các gói nhận được, khi chưa xác định được cổng ra. Việc quản lý các bộ nhớ đệm này, khi đầy, sẽ dựa trên **phương pháp điều khiển luồng (flow control)**.

Thông thường, các gói được lưu trong các bộ đệm **FIFO (First Input, First Output)**, tức là gói đến trước được xử lý trước. Tuy nhiên, để tối ưu hơn, mạng có thể áp dụng các mức ưu tiên nhằm đảm bảo **chất lượng dịch vụ (Quality of Service, QoS)**, cho phép các gói quan trọng được truyền đi trước.

Các Phương Pháp Xử Lý Gói
Trước khi quyết định truyền một gói, thiết bị sẽ nhận và phân tích nội dung gói để quyết định hành động tiếp theo. Trong các thiết bị hiện đại, hai phương pháp xử lý chính được sử dụng:
- **Chuyển mạch lưu trữ và chuyển tiếp (store-and-forward)**;
- **Chuyển mạch không lưu trữ (cut-through)**.

1. **Chuyển mạch lưu trữ và chuyển tiếp (store-and-forward)**  
   Đây là phương pháp xuất hiện sớm nhất. Toàn bộ gói được sao chép vào bộ nhớ đệm của thiết bị trước khi kiểm tra lỗi. Nếu phát hiện lỗi, gói sẽ bị loại bỏ. Nếu không có lỗi, thiết bị sử dụng **bảng chuyển mạch (forwarding table)** để xác định cổng ra và truyền gói.

2. **Chuyển mạch không lưu trữ (cut-through)**  
   Trong phương pháp này, thiết bị chỉ kiểm tra địa chỉ đích của gói và ngay lập tức bắt đầu truyền mà không cần lưu toàn bộ gói trong bộ đệm. Điều này giúp giảm đáng kể độ trễ (*latency*), nhưng không cho phép kiểm tra lỗi trong gói. Phương pháp này có thể mất ưu thế trong các trường hợp mạng quá tải, khi xuất hiện lỗi ở các gói đến.

Bảng Chuyển Mạch và Định Tuyến
Chuyển mạch gói dựa vào hai loại bảng chính:
- **Bảng chuyển mạch (Forwarding Database, FDB)**: Được sử dụng ở tầng liên kết dữ liệu (*Data Link Layer*), dùng để định tuyến các gói dựa trên địa chỉ vật lý (*MAC address*).
- **Bảng định tuyến (Routing Table)**: Được sử dụng trong các bộ định tuyến (*routers*) ở tầng mạng (*Network Layer*), dùng để xác định đường đi dựa trên địa chỉ mạng.

Các **bảng định tuyến (routing tables)** thường được lưu trong các router (thiết bị tầng 3) và hỗ trợ quá trình định tuyến (*routing*), cho phép truyền gói giữa các mạng cục bộ hoặc các mạng khác nhau. Trong khi đó, **bảng chuyển mạch (forwarding tables)** được thiết lập ở tầng liên kết dữ liệu, dùng để phân tích và xử lý địa chỉ vật lý (MAC).

Hệ thống mạng cục bộ xây dựng bảng chuyển mạch bằng cách học địa chỉ MAC của các thiết bị kết nối. Quá trình này gọi là **học địa chỉ (address learning)**.

---

## 5.2 Giao Thức Mạng Và Phương Pháp Chuyển Mạch

Các giao thức mạng được chia thành hai loại dựa trên cách thiết lập kết nối:

 1. **Giao thức có thiết lập kết nối (Connection-Oriented Protocol)**
Những giao thức này yêu cầu thiết lập một kết nối logic giữa hai thiết bị trước khi truyền dữ liệu. Quá trình này thường bao gồm:
- Thiết lập các quy tắc để khởi tạo, quản lý, và kết thúc kết nối.
- Một thiết bị gửi yêu cầu kết nối đến thiết bị khác.
- Sau khi kết nối được thiết lập, hai thiết bị trao đổi thông tin điều khiển và thiết lập các tham số của kết nối.

Khi kết nối được thiết lập thành công, quá trình truyền dữ liệu bắt đầu. Sau khi truyền xong, các thiết bị sẽ kết thúc kết nối.

 2. **Giao thức không thiết lập kết nối (Connectionless Protocol)**
Những giao thức này không yêu cầu thiết lập kết nối trước. Khi thiết bị có dữ liệu cần truyền, quá trình truyền bắt đầu ngay lập tức.


 Sử dụng thực tế
Dựa trên cách phân loại này, có thể kết luận rằng:
- **Giao thức có thiết lập kết nối** thường được sử dụng trong các mạng chuyển mạch kênh (*circuit-switched networks*).
- **Giao thức không thiết lập kết nối** thường được sử dụng trong các mạng chuyển mạch gói (*packet-switched networks*).

Tuy nhiên, quan điểm này không hoàn toàn chính xác. Mặc dù mạng chuyển mạch kênh dựa trên việc thiết lập kết nối giữa các thiết bị, không phải tất cả các giao thức đều yêu cầu thiết lập kết nối.

 Ví dụ về giao thức
Trong giao thức tầng vận chuyển (*transport protocols*), có hai giao thức phổ biến:
- **TCP (Transmission Control Protocol)**: Đảm bảo truyền dữ liệu đáng tin cậy bằng cách thiết lập một kết nối logic giữa thiết bị gửi và nhận. TCP thường được sử dụng cho các ứng dụng như FTP (File Transfer Protocol), Telnet, hoặc các ứng dụng yêu cầu truyền dữ liệu đáng tin cậy.
- **UDP (User Datagram Protocol)**: Không thiết lập kết nối trước và không đảm bảo truyền dữ liệu đáng tin cậy. UDP thường được sử dụng cho các ứng dụng như DNS (Domain Name System), IPTV, hoặc trò chơi trực tuyến.


 Kết hợp giao thức
Một giao thức không nhất thiết chỉ hoạt động trên một kiểu kết nối. Ví dụ:
- Giao thức TCP (tầng vận chuyển) thường dựa vào giao thức IP (tầng mạng), một giao thức không thiết lập kết nối.
- Trong các mạng như ATM (Asynchronous Transfer Mode), các kênh ảo được thiết lập giữa thiết bị gửi và nhận trước khi truyền dữ liệu.

Mỗi tầng trong mô hình OSI có thể hỗ trợ cả hai loại giao thức, tùy thuộc vào yêu cầu của ứng dụng hoặc cấu trúc mạng cụ thể.

---

## 5.3 Giao Thức Tầng Liên Kết Dữ Liệu

Các giao thức tầng liên kết dữ liệu (*Data Link Layer Protocols*) xác định tập hợp các quy tắc cho phép tổ chức và quản lý tương tác giữa các nút mạng được kết nối với cùng một phân đoạn mạng.

Dữ liệu tại tầng liên kết dữ liệu được xem như một dòng bit tuần tự (*sequential bit stream*). Trước khi được truyền qua kênh vật lý, dòng dữ liệu này được chia thành các phần nhỏ hơn, mỗi phần được bổ sung một **tiêu đề (header)** chứa các thông tin điều khiển. Phần này tạo thành **khung (frame)**. Cấu trúc của tiêu đề khung phụ thuộc vào tập hợp các nhiệm vụ mà giao thức cụ thể đảm nhận.

Phân loại
Các giao thức tầng liên kết dữ liệu có thể được chia thành hai nhóm:
- **Giao thức cho các kết nối kiểu "điểm-điểm" (point-to-point protocols)**;
- **Giao thức cho các mạng có cấu trúc phức tạp, chẳng hạn như mạng cục bộ (LANs)**.

---

### 5.3.1 Cấu Trúc Khung Dữ Liệu

Cấu trúc tiêu đề của khung (*frame header*) phụ thuộc vào nhiều yếu tố, bao gồm các chức năng mà giao thức thực hiện. Một số trường thông tin thường xuất hiện trong tiêu đề khung bao gồm:

1. **Trường đặc biệt để xác định biên của khung (frame boundary)**  
   Do trong môi trường vật lý thường xuyên có các tín hiệu nhiễu, thiết bị nhận cần có khả năng xác định chính xác khi nào một khung bắt đầu và khi nào nó kết thúc.

2. **Trường địa chỉ của thiết bị gửi và thiết bị nhận (address field)**  
   Đây là trường chứa địa chỉ của nguồn và đích, giúp xác định các thiết bị tham gia vào quá trình truyền dữ liệu.

3. **Trường xác định giao thức tầng mạng (network protocol field)**  
   Trường này giúp xác định giao thức tầng mạng mà dữ liệu trong khung sẽ được truyền theo. Ví dụ, trên cùng một máy tính, các module phần mềm của nhiều giao thức tầng mạng có thể hoạt động đồng thời, và trường này giúp dữ liệu được phân phối đúng theo giao thức cần thiết.

4. **Trường kiểm tra lỗi hoặc mã kiểm soát (checksum or control code)**  
   Trường này cho phép thiết bị nhận kiểm tra dữ liệu nhận được có lỗi hay không.

| **Trường xác định bắt đầu khung** | **Địa chỉ nguồn và đích** | **Thông tin giao thức tầng mạng** | **Dữ liệu (*Data*)** | **Kiểm tra lỗi (*Checksum*)** | **Trường xác định kết thúc khung** |
|-----------------------------------|----------------------------|-----------------------------------|----------------------|-------------------------------|------------------------------------|
| Đánh dấu vị trí bắt đầu của khung | Xác định thiết bị gửi và nhận dữ liệu | Chỉ định giao thức tầng mạng được sử dụng | Chứa nội dung dữ liệu cần truyền | Xác định tính toàn vẹn của dữ liệu nhận | Đánh dấu vị trí kết thúc của khung |

<p align="center"><b>Bảng 5.3 Cấu trúc khung dữ liệu</b></p>


Hạn chế về kích thước dữ liệu trong khung
Đối với hầu hết các giao thức tầng liên kết dữ liệu, có một giới hạn về kích thước tối đa của dữ liệu có thể truyền trong một khung. Giới hạn này được quyết định bởi các yếu tố kỹ thuật và được gọi là **MTU (Maximum Transmission Unit)**.  
- **MTU** xác định kích thước tối đa của khối dữ liệu (tính theo byte) có thể truyền tại tầng liên kết dữ liệu.  
- Giá trị MTU có thể được xác định bởi tiêu chuẩn (như trong **Ethernet**) hoặc được cấu hình trong quá trình thiết lập kết nối (thường trong trường hợp kết nối **point-to-point**).

