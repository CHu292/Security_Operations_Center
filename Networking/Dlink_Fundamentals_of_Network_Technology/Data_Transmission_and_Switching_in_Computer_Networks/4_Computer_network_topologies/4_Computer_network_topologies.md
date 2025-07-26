# Các cấu trúc liên kết (topologies) của mạng máy tính

# 4.1 Khái niệm cấu trúc liên kết mạng (network topology)

Khi tổ chức một **mạng máy tính (computer network)**, một trong những vấn đề quan trọng là lựa chọn **cấu trúc liên kết (topology)** phù hợp, vì cấu hình mạng đúng đắn là cần thiết để đảm bảo hoạt động đáng tin cậy và hiệu quả cho toàn bộ mạng, cũng như khả năng mở rộng trong tương lai với chi phí thấp nhất.

**Cấu trúc liên kết mạng** là phương pháp mô tả cấu hình mạng, sơ đồ bố trí và kết nối các **thiết bị mạng (network devices)**.
Cần phân biệt giữa hai khái niệm **cấu trúc liên kết vật lý (physical topology)**, mô tả vị trí thực tế và kết nối của các nút mạng, và **cấu trúc liên kết logic (logical topology)** - các cách thức tương tác giữa các nút và cách tín hiệu truyền trong mạng theo cấu trúc liên kết vật lý.

Nói cách khác, cấu trúc liên kết vật lý xác định cách các thiết bị được bố trí và kết nối, trong khi cấu trúc liên kết logic xác định cách dữ liệu truyền giữa các thiết bị, bất kể vị trí vật lý của chúng.

**Cấu trúc liên kết logic và vật lý của mạng** không nhất thiết phải trùng khớp. Ví dụ, mạng **Ethernet cục bộ (Ethernet LAN)**, được xây dựng bằng **các hub (concentrators)** và **cáp xoắn đôi (twisted pair cable)** làm phương tiện truyền, có cấu trúc liên kết vật lý dạng **"sao" (star)**, nhưng cấu trúc liên kết logic lại là dạng **"bus" (bus)**. Cấu trúc liên kết logic thường được xác định bởi **các giao thức mạng (network protocols)** và liên quan đến các phương pháp quản lý quyền truy cập vào phương tiện truyền dẫn. Nó có thể được thay đổi linh hoạt nhờ việc sử dụng **thiết bị mạng (network equipment)** như **bộ định tuyến (routers)**, **bộ chuyển mạch (switches)** hoặc **điểm truy cập (access points)**.

Cấu trúc liên kết vật lý phụ thuộc vào vị trí và khả năng của các thiết bị mạng, phương tiện truyền dẫn và chi phí triển khai cơ sở hạ tầng mạng và cáp.

Có các cấu trúc liên kết cơ bản sau, dựa trên đó các mạng máy tính được xây dựng:

- **"bus" (bus)** - cấu trúc liên kết dạng **"dải"**,
- **"ring" (ring)** - cấu trúc liên kết dạng **"vòng"**,
- **"star" (star)** - cấu trúc liên kết dạng **"sao"**,
- **"tree" (tree)** - cấu trúc liên kết dạng **"cây"**,
- **cấu trúc liên kết lưới hoàn toàn kết nối (fully connected mesh)**,
- **cấu trúc liên kết lưới kết nối một phần (partially connected mesh)**.

Trước khi đi vào tìm hiểu các cấu trúc liên kết mạng, hãy cùng làm quen với các thiết bị mạng hỗ trợ việc hình thành cấu trúc của mạng.


# 4.2 Thiết bị mạng trong cấu trúc liên kết (network topology)

Để xây dựng một **mạng máy tính (computer network)**, cần có **thiết bị mạng hoặc thiết bị viễn thông (network or telecommunication equipment)**, với nhiệm vụ chính là kết nối các máy tính và các thiết bị khác vào mạng, truyền dữ liệu giữa chúng, kết nối các mạng máy tính có cấu trúc liên kết và công nghệ khác nhau với nhau, và tăng khoảng cách truyền tín hiệu. Ngoài ra, thiết bị mạng còn cho phép giải quyết các nhiệm vụ như đảm bảo **an ninh mạng (network security)**, quản lý **dòng dữ liệu (data flow)**, cung cấp **chất lượng dịch vụ (Quality of Service - QoS)**, và nhiều chức năng khác.

Tiếp theo trong phần này sẽ là mô tả ngắn gọn về các **thiết bị mạng (network devices)** được sử dụng trong **mạng cục bộ Ethernet (Ethernet LAN)** và **Wi-Fi**. Việc mô tả các thiết bị sẽ dựa trên chức năng của chúng tương ứng với các tầng của **mô hình OSI (OSI model)**, bắt đầu từ tầng vật lý.

--- 

## 4.2.1 Bộ lặp và Hub (Repeater và Hub)

**Bộ lặp (repeater)** là một trong những thiết bị mạng đơn giản nhất. Nó hoạt động ở **tầng vật lý (physical layer)** (tầng 1) của **mô hình OSI (OSI model)** và được sử dụng để kết nối các phân đoạn của phương tiện truyền dẫn nhằm tăng chiều dài tổng thể của mạng.

Khoảng cách mà tín hiệu từ một thiết bị có thể truyền đến thiết bị khác mà không bị biến dạng là có giới hạn. Điều này xảy ra vì nhiều lý do, một trong số đó là **suy hao tín hiệu (attenuation)**. Suy hao tín hiệu là sự mất mát công suất của tín hiệu. Để xây dựng mạng có độ dài lớn, cần phải khuếch đại tín hiệu ở một số điểm.

Trong các mạng **Ethernet** đầu tiên (10BASE2 và 10BASE5), mỗi máy tính được kết nối với các thiết bị khác thông qua một **cáp đồng trục (coaxial cable)** duy nhất. Các bộ lặp được sử dụng để tăng chiều dài của mạng. Chúng được trang bị hai cổng và kết nối hai phân đoạn vật lý, tức là hai sợi cáp.

Bộ lặp hoạt động như sau: nó nhận tín hiệu từ một phân đoạn mạng, khuếch đại chúng, khôi phục đồng bộ và truyền sang phân đoạn khác. Bộ lặp không xử lý lưu lượng. Tổng số bộ lặp trong mạng và các phân đoạn mà chúng kết nối bị giới hạn do độ trễ thời gian và các nguyên nhân khác.


**Ứng dụng của bộ lặp trong mạng**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_1.png" alt="Hình 4.1 Ứng dụng của bộ lặp trong mạng Ethernet sử dụng cáp đồng trục" width="1000">
</p>
<p align="center"><b>Hình 4.1 Ứng dụng của bộ lặp trong mạng Ethernet sử dụng cáp đồng trục</b></p>


Các thông số kỹ thuật của Ethernet 10BASE2 và 10BASE5 đã lỗi thời và bộ lặp cho các mạng này không còn được sản xuất và sử dụng.

Hiện nay, có các bộ lặp được sản xuất cho **mạng không dây (wireless networks)**.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_2.png" alt="Hình 4.2 Bộ lặp không dây" width="1000">
</p>
<p align="center"><b>Hình 4.2 Bộ lặp không dây</b></p>


**Bộ lặp không dây** khôi phục các tín hiệu vô tuyến để tăng bán kính hoạt động của mạng không dây. Bộ lặp không kết nối vật lý với bất kỳ phần nào của mạng không dây. Thay vào đó, nó nhận tín hiệu từ **điểm truy cập (access point)**, thiết bị khách, **bộ định tuyến không dây (wireless router)** hoặc một bộ lặp khác trên một kênh tần số vô tuyến xác định, khuếch đại và truyền lại trên cùng một kênh, không thay đổi khung tín hiệu. Nói cách khác, bộ lặp nằm giữa điểm truy cập và thiết bị ở xa, hoạt động như một điểm trung chuyển khung tín hiệu giữa chúng. Điều này giúp giảm suy hao của tín hiệu tần số vô tuyến. Hãng D-Link sản xuất các bộ lặp độc lập. Ngoài ra, điểm truy cập có thể được cấu hình để hoạt động ở chế độ bộ lặp.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_3.jpg" alt="Hình 4.3 Nguyên lý hoạt động của bộ lặp không dây" width="1000">
</p>
<p align="center"><b>Hình 4.3 Nguyên lý hoạt động của bộ lặp không dây</b></p>


Sau khi thông số kỹ thuật **Ethernet 10Base-T** ra đời, mỗi nút được kết nối bằng một cáp riêng biệt dạng **cáp xoắn đôi (twisted pair cable)** tới một thiết bị trung tâm — **hub** (còn gọi là concentrator).

**Hub (concentrator)** là một bộ lặp có nhiều cổng và kết nối nhiều phân đoạn vật lý của mạng (đoạn cáp). Hub hoạt động ở tầng vật lý (tầng 1) của mô hình OSI. Nhiệm vụ chính của nó là lặp lại tín hiệu nhận được từ một cổng sang tất cả các cổng khác, đồng thời khôi phục tín hiệu. Hub cũng không có chức năng xử lý lưu lượng, do đó mạng được xây dựng bằng hub có thể có cấu trúc liên kết vật lý khác nhau, nhưng cấu trúc liên kết logic luôn là dạng **"bus"**.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_4.png" alt="Hình 4.4 Truyền dữ liệu trong mạng qua hub" width="1000">
</p>
<p align="center"><b>Hình 4.4 Truyền dữ liệu trong mạng qua hub</b></p>


Hub tạo ra một môi trường truyền tín hiệu chung cho tất cả các nút trong **mạng cục bộ (LAN)**. Tại một thời điểm, chỉ có một máy tính trong mạng có thể truyền dữ liệu. Nếu tín hiệu đồng thời xuất hiện trên hai hoặc nhiều cổng của hub, sẽ xảy ra **va chạm (collision)**, dẫn đến hư hỏng các khung truyền. Vì vậy, tất cả các thiết bị kết nối với hub nằm trong cùng một **miền va chạm (collision domain)**.

- **Va chạm (collision)**: Là hiện tượng chồng lấn hoặc xung đột tín hiệu xảy ra khi hai hoặc nhiều nút truyền dữ liệu đồng thời, gây hỏng dữ liệu.
- **Miền va chạm (collision domain)**: Là một mạng Ethernet hoạt động ở chế độ bán song công (half-duplex) và sử dụng phương thức truy cập CSMA/CD.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_5.png" alt="Hình 4.5 Miền va chạm" width="1000">
</p>
<p align="center"><b>Hình 4.5 Miền va chạm</b></p>


Khi số lượng phân đoạn mạng và máy tính tăng lên, số lượng va chạm cũng tăng lên. Ngoài ra, số lượng hub và các phân đoạn mạng mà chúng kết nối bị giới hạn do độ trễ thời gian và giảm **băng thông mạng (network bandwidth)**. Hơn nữa, mạng được xây dựng bằng hub có mức độ bảo mật thấp, vì dữ liệu được truyền qua tất cả các cổng, cho phép thông tin truyền trong mạng bị “nghe lén”. Băng thông thấp và mức bảo mật kém dẫn đến việc hub không còn được sử dụng trong các mạng máy tính hiện đại; đầu tiên chúng được thay thế bằng **bridge (cầu nối)**, sau đó là **switch (bộ chuyển mạch)**.

---

## 4.2.2 Cầu nối (Bridge)

Cầu nối (bridge) được phát triển bởi công ty Digital Equipment Corporation (DEC) vào đầu những năm 1980 và là thiết bị hoạt động trên tầng vật lý (Physical Layer) và tầng liên kết dữ liệu (Data Link Layer) của mô hình OSI, dùng để kết nối hai mạng cục bộ (LAN) hoặc hai phân đoạn của cùng một mạng.

Không giống như bộ tập trung (hub) chỉ tăng cường và khôi phục dạng tín hiệu khi truyền từ cổng này sang cổng khác, cầu nối có các chức năng thông minh. Nó chỉ truyền qua các khung (frame - khối dữ liệu ở tầng liên kết dữ liệu) khi cần thiết, nghĩa là khi địa chỉ vật lý (MAC address - địa chỉ MAC) của thiết bị đích thuộc về phân đoạn mạng khác hoặc mạng khác. Cầu nối thực hiện điều này bằng cách sử dụng một bảng chuyển mạch được lưu trữ trong bộ nhớ - một bảng tương ứng giữa các cổng của nó và các địa chỉ MAC được sử dụng trong mỗi mạng hoặc phân đoạn mạng, bảng này được thiết lập ngay sau khi bật nguồn. Nhờ vậy, cầu nối cách ly lưu lượng của một phân đoạn mạng khỏi phân đoạn khác, giảm thiểu các va chạm (collision) bằng cách chia một miền va chạm lớn thành hai miền nhỏ hơn, từ đó cải thiện hiệu suất tổng thể của mạng. Cầu nối cũng làm giảm khả năng truy cập trái phép vào dữ liệu vì các khung không rời khỏi phân đoạn của nó, giúp khó bị tin tặc chặn lại hơn.



**Minh họa về kết nối hai phân đoạn mạng thông qua cầu nối**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_6.png" alt="Hình 4.6 Kết nối hai phân đoạn mạng bằng cầu nối" width="1000">
</p>
<p align="center"><b>Hình 4.6 Kết nối hai phân đoạn mạng bằng cầu nối</b></p>


Hiện nay, các cầu nối được sản xuất cho mạng không dây. Với các cầu nối không dây (wireless bridges), có thể kết nối các mạng có dây ở khoảng cách gần như các tòa nhà liền kề hoặc các phòng trong cùng một tòa nhà, hoặc ở khoảng cách lên tới vài km.

Các cầu nối được thiết kế để sử dụng trong nhà cho phép kết nối từ một đến nhiều thiết bị không có giao diện không dây vào mạng không dây. Ví dụ, chúng rất hữu ích khi kết nối các thiết bị như máy in hoặc máy chơi game, vốn chỉ có cổng Ethernet.


**Ví dụ về việc sử dụng cầu nối không dây**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_7.png" alt="Hình 4.7 Ví dụ về việc sử dụng cầu nối không dây" width="1000">
</p>
<p align="center"><b>Hình 4.7 Ví dụ về việc sử dụng cầu nối không dây</b></p>


---


## 4.2.3 Bộ chuyển mạch (Switches)

Các bộ cầu nối (bridge) cho mạng có dây hiện đã lỗi thời và được thay thế bằng các bộ chuyển mạch (switch). Bộ chuyển mạch là một cầu nối đa cổng (multi-port bridge) và hoạt động tương tự trong việc xử lý dữ liệu, nhưng hỗ trợ nhiều tính năng bổ sung hơn so với cầu nối. Bộ chuyển mạch hoạt động ở tầng liên kết dữ liệu (data link layer, tầng thứ hai) của mô hình OSI và được sử dụng để kết nối các thiết bị mạng trong cùng một hoặc nhiều phân đoạn (segment) của mạng.


Các thiết bị mạng có thể hoạt động trên một hoặc nhiều tầng của mô hình OSI. Thông thường khi mô tả thiết bị mạng, người ta sẽ nhắc đến tầng cao nhất của mô hình OSI mà thiết bị đó hỗ trợ. Điều này ngụ ý rằng thiết bị cũng có thể hoạt động trên các tầng thấp hơn. Ví dụ, khi nói rằng bộ chuyển mạch là thiết bị tầng liên kết dữ liệu (tầng thứ hai của OSI), tức là nó thực hiện các chức năng của cả tầng vật lý và tầng liên kết dữ liệu.


Bộ chuyển mạch có thể được trang bị nhiều cổng và thiết lập nhiều kết nối đồng thời giữa các cặp cổng khác nhau, cho phép các thiết bị kết nối với nó giao tiếp cùng lúc.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_8.png" alt=" Hình 4.8: Ứng dụng của bộ chuyển mạch trong mạng" width="1000">
</p>
<p align="center"><b> Hình 4.8: Ứng dụng của bộ chuyển mạch trong mạng</b></p>



Khi truyền khung (frame) qua bộ chuyển mạch, một kênh ảo hoặc thực (tùy theo kiến trúc) sẽ được tạo ra, qua đó dữ liệu được truyền trực tiếp từ cổng nguồn đến cổng đích với tốc độ cao nhất có thể theo công nghệ sử dụng. Nguyên tắc hoạt động này được gọi là "vi phân đoạn" (microsegmentation).


**Vi phân đoạn (microsegmentation)** là quá trình mà bộ chuyển mạch chia một miền va chạm (collision domain) của mạng LAN thành các miền nhỏ hơn cho mỗi cổng.


Nhờ vi phân đoạn, các bộ chuyển mạch có thể hoạt động ở chế độ song công toàn phần (full duplex), cho phép mỗi nút kết nối trực tiếp với cổng của bộ chuyển mạch có thể truyền và nhận dữ liệu đồng thời. Do đó, chế độ song công toàn phần đã loại bỏ khái niệm về miền va chạm (collision domain). Các nút không còn phải cạnh tranh băng thông với các thiết bị khác, nhờ đó không xảy ra va chạm và hiệu suất mạng được cải thiện.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_9.png" alt="Hình 4.9: Vi phân đoạn" width="800">
</p>
<p align="center"><b>Hình 4.9: Vi phân đoạn</b></p>


Bộ chuyển mạch truyền dữ liệu dựa trên bảng chuyển mạch (switching table), giống như cầu nối, cho phép nó cô lập lưu lượng trong các phân đoạn mạng. Khi nhận được khung, bộ chuyển mạch sẽ trích xuất địa chỉ MAC (MAC address) của đích và tìm kiếm địa chỉ này trong bảng chuyển mạch. Khi tìm thấy một bản ghi trong bảng chuyển mạch kết hợp địa chỉ MAC của đích với một trong các cổng của bộ chuyển mạch, khung sẽ được truyền qua cổng tương ứng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_10.png" alt=" Hình 4.10: Truyền khung qua bộ chuyển mạch" width="1000">
</p>
<p align="center"><b> Hình 4.10: Truyền khung qua bộ chuyển mạch</b></p>



Nếu trong bảng chuyển mạch không có bản ghi nào cho địa chỉ MAC của thiết bị và cổng hoặc địa chỉ MAC của đích là địa chỉ quảng bá (broadcast), bộ chuyển mạch sẽ truyền khung qua tất cả các cổng, giống như một bộ tập trung (hub). Trong trường hợp này, ta nói rằng bộ chuyển mạch tạo thành một miền quảng bá (broadcast domain).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_11.png" alt="Hình 4.11: Quảng bá qua bộ chuyển mạch" width="800">
</p>
<p align="center"><b>Hình 4.11: Quảng bá qua bộ chuyển mạch</b></p>



Hiện nay, các bộ chuyển mạch là thành phần chính trong việc xây dựng mạng LAN. Các bộ chuyển mạch Ethernet hiện đại ngoài nhiệm vụ chính còn có thể thực hiện nhiều chức năng bổ sung như tạo dự phòng và tăng cường khả năng chống lỗi của mạng, tạo các mạng LAN ảo (VLAN), kiểm soát và hạn chế quá tải trong mạng, bảo đảm an ninh, quản lý truyền phát đa điểm (multicast) và nhiều chức năng khác.

Thông tin chi tiết về các bộ chuyển mạch và các công nghệ được chúng hỗ trợ sẽ được trình bày trong Chương 6.

---


## 4.2.4 Điểm truy cập (Access Points)

Trong khi các **bộ chuyển mạch** (switch) là thành phần chính của mạng nội bộ có dây, thì **điểm truy cập** (access points) là yếu tố cơ bản trong việc xây dựng mạng nội bộ không dây. **Điểm truy cập** thường được sử dụng để tổ chức các mạng không dây truy cập internet ở những nơi công cộng như sân bay, quán cà phê, sân thể thao và trung tâm mua sắm. Trong mạng gia đình và văn phòng nhỏ, điểm truy cập có thể được sử dụng để kết nối tất cả các thiết bị di động (máy tính xách tay, điện thoại thông minh, máy tính bảng, camera IP không dây) vào một mạng không dây chung, hoặc để mở rộng mạng không dây hiện có, ví dụ, mạng được xây dựng bằng cách sử dụng **bộ định tuyến không dây** (wireless router).

**Điểm truy cập** (Access Point) hoạt động ở **tầng liên kết dữ liệu** (Data Link Layer) của **mô hình OSI**. Nó đóng vai trò như một trạm không dây, cung cấp quyền truy cập cho các **thiết bị khách không dây** (wireless client devices) đã được kết nối với nó, cho phép truy cập vào mạng có dây và/hoặc không dây thông qua môi trường truyền dẫn không dây. **Thiết bị khách không dây** bao gồm các thiết bị có tích hợp sẵn hoặc được cài đặt **bộ điều hợp mạng không dây** (wireless network adapter), tức là những thiết bị có **giao diện** (interface) để kết nối với mạng không dây.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_12.png" alt="Hình 4.12: Điểm truy cập DAP-300P" width="800">
</p>
<p align="center"><b>Hình 4.12: Điểm truy cập DAP-300P</b></p>

**Kết nối** giữa **điểm truy cập** và các **thiết bị khách không dây** được thực hiện thông qua công nghệ **Wi-Fi**. **Điểm truy cập** cung cấp sự tương tác và trao đổi thông tin giữa các khách hàng không dây, cũng như kết nối với mạng nội bộ có dây. Để thực hiện điều này, điểm truy cập có một **giao diện mạng** (uplink port), thường là một **cổng Ethernet** với đầu nối **RJ-45**. Thông qua giao diện này cũng có thể cấu hình điểm truy cập.

**Ứng dụng của điểm truy cập**


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_13.png" alt="Hình 4.13: Ứng dụng của điểm truy cập" width="800">
</p>
<p align="center"><b>Hình 4.13: Ứng dụng của điểm truy cập</b></p>

Hầu hết các **điểm truy cập** hiện đại hỗ trợ các tính năng tiên tiến, cũng như nhiều chế độ hoạt động khác nhau.

Thông tin chi tiết về công nghệ **Wi-Fi**, các chức năng và chế độ hoạt động của điểm truy cập sẽ được đề cập trong phần hai của khóa học.

--- 

## 4.2.5 Bộ định tuyến (Router)

Tất cả các thiết bị đã xem xét ở trên cho phép kết nối các nút trong một mạng cục bộ (**Local Area Network, LAN**), nhưng để kết nối giữa các mạng với nhau và kết nối LAN với mạng diện rộng (**Wide Area Network, WAN**), cần có thiết bị mạng đặc biệt - **bộ định tuyến**.

**Bộ định tuyến (router)** là thiết bị hoạt động ở **tầng mạng** (tầng thứ ba của mô hình OSI, **Network Layer**), với nhiệm vụ chính là phân tích **địa chỉ logic** (thường là **địa chỉ IP**) và xác định tuyến đường tốt nhất để truyền gói tin từ nguồn đến đích.

Bộ định tuyến thực hiện các chức năng của **tầng vật lý** (**Physical Layer**), **tầng liên kết dữ liệu** (**Data Link Layer**) và **tầng mạng** (**Network Layer**) của mô hình OSI. Ở hai tầng đầu tiên, nó tương tác với các mạng cục bộ hoặc các phân đoạn khác nhau của cùng một mạng, và ở tầng thứ ba, nó đưa ra quyết định về tuyến đường tiếp theo cho các gói tin.

Bộ định tuyến có thể kết nối ít nhất hai mạng với nhau. Các bộ định tuyến của D-Link, tùy thuộc vào kiểu máy, có thể được trang bị từ 1 đến 8 **giao diện LAN** (Local Area Network Interface), được sử dụng để kết nối các mạng cục bộ, và 1 hoặc 2 **giao diện WAN** (Wide Area Network Interface), được dùng để kết nối LAN với mạng bên ngoài, thường là mạng của nhà cung cấp dịch vụ internet, cung cấp cho khách hàng truy cập internet.

Các **giao thức** sử dụng ở các tầng vật lý, tầng liên kết dữ liệu và tầng mạng của các mạng khác nhau có thể khác nhau. Không giống như **bộ chuyển mạch** (**switch**), bộ định tuyến thay đổi các gói dữ liệu được truyền. Nó phân tích các gói đến tầng mạng và sau đó tạo lại các gói theo các quy tắc nhất định dựa trên công nghệ được hỗ trợ bởi giao diện mà dữ liệu sẽ được truyền đi. Nói cách khác, bộ định tuyến thực hiện **chuyển đổi giao thức** trước khi gửi dữ liệu đến một mạng khác hoặc phân đoạn khác của mạng. Vì lý do này, bộ định tuyến được sử dụng như một **cổng** (**gateway**) khi kết nối các mạng sử dụng các giao thức khác nhau.

Do đó, các bộ định tuyến giá rẻ dùng để kết nối các mạng gia đình và văn phòng nhỏ với internet thường được gọi là **internet gateway** (cổng internet). Các thiết bị này có thể tích hợp các chức năng của bộ chuyển mạch, điểm truy cập không dây (**Wireless Access Point**), modem ADSL, và được trang bị **tường lửa** (firewall) để ngăn chặn các cuộc tấn công từ mạng bên ngoài. Một ví dụ về **cổng internet** là bộ định tuyến D-Link DIR-822.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_14.png" alt="Hình 4.14 D-Link Router" width="700">
</p>
<p align="center"><b>Hình 4.14: D-Link Router</b></p>

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_15.png" alt=" Hình 4.15 Kết nối với internet thông qua cổng internet" width="800">
</p>
<p align="center"><b> Hình 4.15 Kết nối với internet thông qua cổng internet</b></p>


Sử dụng **địa chỉ logic** (**địa chỉ mạng, Network Addressing**), các bộ định tuyến cô lập lưu lượng giữa các phần khác nhau của mạng tốt hơn so với bộ chuyển mạch, tạo ra các phân đoạn logic riêng biệt.

Không giống như **địa chỉ vật lý** (địa chỉ MAC), địa chỉ logic (thường là địa chỉ IP) có trường **số mạng** (**network number**), do đó, tất cả các nút có cùng giá trị trường này thuộc về một phân đoạn, được gọi là **mạng con** (**subnetwork, subnet**). Mỗi giao diện của bộ định tuyến có thể kết nối với một mạng con.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_16.png" alt=" Hình 4.16 Kết nối các mạng khác nhau (mạng con) bằng bộ định tuyến" width="800">
</p>
<p align="center"><b> Hình 4.16 Kết nối các mạng khác nhau (mạng con) bằng bộ định tuyến</b></p>



Không có cấu hình đặc biệt, các bộ định tuyến không truyền các gói **broadcat** qua các cổng của chúng, do đó, chúng giới hạn khu vực lan truyền của lưu lượng broadcast, tức là chia nhỏ một **miền broadcast** lớn thành các miền nhỏ hơn.

Chi tiết về bộ định tuyến và các công nghệ hỗ trợ sẽ được giới thiệu trong phần ba của khóa học.

Cần lưu ý rằng vấn đề về lưu lượng broadcast trong các mạng được xây dựng bằng các bộ chuyển mạch có thể được giải quyết bằng công nghệ **mạng LAN ảo** (**Virtual LAN, VLAN**).

**Mạng LAN ảo (Virtual LAN, VLAN)** là một nhóm logic của các nút mạng mà lưu lượng của nó, bao gồm cả lưu lượng broadcast, được cô lập hoàn toàn khỏi các nút mạng khác ở tầng liên kết dữ liệu. Điều này có nghĩa là việc truyền các khung giữa các mạng ảo khác nhau dựa trên địa chỉ MAC là không thể, bất kể loại địa chỉ - cá nhân, nhóm hay broadcast. Trong khi đó, trong cùng một mạng ảo, các khung được truyền theo công nghệ chuyển mạch, tức là chỉ trên cổng có địa chỉ MAC của đích.

Bộ chuyển mạch có phần mềm hỗ trợ chức năng mạng LAN ảo cho phép phân đoạn mạng logic thông qua cấu hình phần mềm thích hợp. Nhờ đó, có thể tập hợp các máy tính vào các nhóm làm việc ảo (các phân đoạn logic) bất kể vị trí vật lý của chúng trong mạng. Chi tiết về công nghệ VLAN sẽ được trình bày trong chương 6.

Gần đây, trong các mạng doanh nghiệp và nhà cung cấp dịch vụ, các bộ định tuyến chủ yếu được thay thế bằng các **bộ chuyển mạch tầng 3** (**Layer 3 Switches**), cho phép chuyển mạch và lọc dựa trên địa chỉ ở tầng liên kết dữ liệu (tầng 2) và tầng mạng (tầng 3) của mô hình OSI. Các bộ chuyển mạch tầng 3 thực hiện chuyển mạch trong một nhóm làm việc và định tuyến giữa các mạng con khác nhau hoặc các mạng LAN ảo (VLAN).

---

## 4.2.6 Công cụ quản lý thiết bị mạng

Cấu trúc liên kết logic có thể thay đổi động bằng cách thực hiện các cài đặt khác nhau trên thiết bị mạng. Hầu hết các thiết bị hiện đại đều hỗ trợ các chức năng quản lý và giám sát khác nhau, bao gồm giao diện quản lý Web, giao diện dòng lệnh (Command Line Interface, CLI), Telnet, và quản lý SNMP.

Giao diện quản lý Web cho phép cấu hình và giám sát các thông số của thiết bị mạng bằng bất kỳ máy tính nào được trang bị trình duyệt Web. Nó có sẵn cho các điểm truy cập, cổng Internet, các bộ chuyển mạch có thể cấu hình và quản lý, thiết bị lưu trữ mạng (NAS), camera IP, cổng IP-điện thoại, và điện thoại IP. Thông qua giao diện Web, người quản trị có thể xem trạng thái thiết bị, thống kê hiệu suất, và thực hiện các cài đặt cần thiết.

Cần lưu ý rằng giao diện Web của các thiết bị khác nhau (và các phiên bản phần cứng khác nhau của cùng một mẫu thiết bị) có thể khác nhau. Mô tả về giao diện Web và cách sử dụng nó có sẵn trong hướng dẫn sử dụng của thiết bị.

Ví dụ, chúng ta hãy xem xét giao diện Web của điểm truy cập DAP-2310 (hình 4.17). Giao diện Web có thể được chia thành 3 khu vực. Khu vực 1 chứa danh sách các thư mục, kết hợp các nhóm chức năng dùng để thực hiện các nhiệm vụ khác nhau. Ở khu vực 3 hiển thị các cài đặt hiện tại của thiết bị hoặc các trường để thay đổi, tùy thuộc vào mục menu được chọn ở khu vực 1. Trong khu vực 2, tùy thuộc vào mẫu và loại thiết bị, có thể truy cập vào các cài đặt hoặc hiển thị hình ảnh đồ họa của bảng điều khiển phía trước của thiết bị trong thời gian thực.

Giao diện Web quản lý của điểm truy cập DAP-2310 

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_17.jpg" alt="Hình 4.17 Giao diện Web quản lý của điểm truy cập DAP-2310" width="800">
</p>
<p align="center"><b> Hình 4.17 Giao diện Web quản lý của điểm truy cập DAP-2310</b></p>


Giao diện Web quản lý bao gồm giao diện người dùng đồ họa (GUI), được chạy trên máy khách, và máy chủ HTTP/HTTPS, được chạy trên thiết bị.

Kết nối giữa máy khách và máy chủ thường được thực hiện qua kết nối TCP/IP với cổng 80 của giao thức HTTP. Khi kết nối lần đầu với máy chủ HTTP trên thiết bị mạng, nói chung cần thực hiện các bước sau:

Bước 1. Kết nối một đầu của cáp Ethernet với cổng Ethernet trên máy tính và đầu kia với bất kỳ cổng LAN Ethernet nào trên thiết bị. Ngoài ra, cũng có thể kết nối qua đường truyền không dây nếu thiết bị và máy tính được trang bị giao diện phù hợp.

Bước 2. Gán cho máy tính địa chỉ IP tĩnh từ cùng một mạng với địa chỉ IP của giao diện quản lý của thiết bị mạng (thông thường được nêu trong hướng dẫn sử dụng). Ví dụ, nếu bộ chuyển mạch được gán địa chỉ IP 10.90.90.90, thì máy tính cần được gán địa chỉ IP dạng 10.x.y.z (trong đó x và y là các số từ 0 đến 254, z là số từ 1 đến 254) và mặt nạ mạng con 255.0.0.0.

Địa chỉ IP hay địa chỉ cấp ba là địa chỉ logic, không gắn với phần cứng cụ thể (thẻ mạng, cổng, v.v.) và được gán bởi quản trị viên mạng, không phụ thuộc vào địa chỉ vật lý (địa chỉ MAC).
Bước 3. Trên máy tính, mở trình duyệt Web (Internet Explorer, Mozilla Firefox, Google Chrome), nhập địa chỉ IP của giao diện quản lý mặc định vào thanh địa chỉ (thường được nêu trong hướng dẫn sử dụng).

Địa chỉ IP của giao diện quản lý mặc định trong thanh địa chỉ của trình duyệt Web 

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_18.jpg" alt="Hình 4.18 Địa chỉ IP của giao diện quản lý mặc định trong thanh địa chỉ của trình duyệt Web" width="400">
</p>
<p align="center"><b>Hình 4.18 Địa chỉ IP của giao diện quản lý mặc định trong thanh địa chỉ của trình duyệt Web</b></p>


Bước 4. Trong cửa sổ xác thực hiện ra, cần nhập mật khẩu của quản trị viên (thường được nêu trong hướng dẫn sử dụng). Sau đó, cửa sổ giao diện Web của thiết bị mạng sẽ xuất hiện.

Cửa sổ xác thực người dùng 

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_19.jpg" alt="Hình 4.19 Cửa sổ xác thực người dùng của giao diện Web quản lý bộ chuyển mạch D-Link" width="400">
</p>
<p align="center"><b>Hình 4.19 Cửa sổ xác thực người dùng của giao diện Web quản lý bộ chuyển mạch D-Link</b></p>


Giao diện Web quản lý của bộ chuyển mạch DES-1100-16 

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_20.jpg" alt="Hình 4.20 Giao diện Web quản lý của bộ chuyển mạch DES-1100-16" width="800">
</p>
<p align="center"><b>Hình 4.20 Giao diện Web quản lý của bộ chuyển mạch DES-1100-16</b></p>



Chú ý: Phần mềm của thiết bị D-Link cho phép lựa chọn ngôn ngữ giao diện Web. Thông tin về hỗ trợ tiếng Nga của giao diện Web có thể được lấy từ bộ phận hỗ trợ kỹ thuật của công ty.

Chọn ngôn ngữ giao diện Web trên bộ định tuyến DIR-300 

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_21.png" alt="Hình 4.21 Chọn ngôn ngữ giao diện Web trên bộ định tuyến DIR-853" width="800">
</p>
<p align="center"><b>Hình 4.21 Chọn ngôn ngữ giao diện Web trên bộ định tuyến DIR-853</b></p>

Để đơn giản hóa việc quản lý nhiều thiết bị mạng, D-Link cung cấp các tiện ích quản lý khác nhau. Ví dụ, để quản lý nhiều bộ chuyển mạch D-Link dòng EasySmart từ một máy tính, có thể sử dụng tiện ích SmartConsole. Tiện ích này có thể cài đặt từ đĩa CD kèm theo thiết bị.

Truy cập vào giao diện dòng lệnh của thiết bị được thực hiện bằng cách kết nối với cổng console của thiết bị từ máy tính cá nhân có cài đặt phần mềm giả lập terminal. Cần lưu ý rằng không phải tất cả thiết bị đều có cổng console. Thường thì cổng này có trên các bộ chuyển mạch và bộ định tuyến được quản lý, dành cho mạng doanh nghiệp vừa và nhỏ (SMB, Small-to-Medium Business), mạng doanh nghiệp, và mạng của các nhà cung cấp dịch vụ. Phương pháp truy cập này thuận tiện nhất khi kết nối lần đầu với bộ chuyển mạch hoặc bộ định tuyến khi địa chỉ IP chưa được biết hoặc chưa được cấu hình, hoặc khi cần khôi phục mật khẩu và thực hiện cài đặt nâng cao cho thiết bị. Truy cập giao diện dòng lệnh cũng có thể được thực hiện qua mạng bằng giao thức Telnet.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_22.png" alt="Hình 4.22 Cửa sổ ban đầu của giao diện dòng lệnh" width="800">
</p>
<p align="center"><b>Hình 4.22 Cửa sổ ban đầu của giao diện dòng lệnh</b></p>

Một cách khác để quản lý thiết bị mạng là sử dụng giao thức SNMP (Simple Network Management Protocol). SNMP là giao thức tầng 7 của mô hình OSI và được phát triển đặc biệt để quản lý và giám sát các thiết bị mạng thông qua trao đổi thông tin quản lý giữa các đại lý nằm trên thiết bị mạng và các quản lý viên nằm trên các trạm quản lý.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_23.png" alt="Hình 4.23 Ví dụ sử dụng giao thức SNMP" width="800">
</p>
<p align="center"><b>Hình 4.23 Ví dụ sử dụng giao thức SNMP</b></p>

Cần lưu ý đến khả năng cập nhật phần mềm cho thiết bị mạng. Nhờ tính năng này, thiết bị có thể được sử dụng lâu dài, vì khi cập nhật phần mềm sẽ thêm vào các chức năng mới hoặc sửa lỗi hiện có. Công ty D-Link phát hành miễn phí các phiên bản phần mềm mới, có thể tải về từ trang web của công ty www.dlink.ru.

---

# 4.3 Tổng quan về các cấu trúc liên kết mạng  

Trong phần này, chúng ta sẽ xem xét các cấu trúc liên kết chính của mạng máy tính.

---

## 4.3.1 Cấu trúc liên kết "bus"  
Cấu trúc liên kết "bus" là phương án đơn giản nhất để tổ chức mạng cục bộ. Trong mạng với cấu trúc liên kết vật lý kiểu "bus", tất cả các nút đều được kết nối bình đẳng với môi trường truyền chung, do đó mỗi nút đều có thể "nghe" được những gì mà các nút khác đang truyền. Môi trường truyền chung trong mạng với cấu trúc liên kết vật lý kiểu "bus" không nhất thiết phải là cáp, mặc dù ban đầu cấu trúc liên kết "bus" được sử dụng trong các mạng Ethernet 10BASE2 và 10BASE5 dựa trên cáp đồng trục. Cáp này được gọi là "bus". Cả hai đầu của nó phải kết thúc bằng một tải điện trở, gọi là terminator, để ngăn chặn hiện tượng phản xạ tín hiệu.

Cấu trúc liên kết logic kiểu "bus" cho phép truyền dữ liệu sao cho tất cả các nút đều nhận được thông điệp được gửi đi, và mỗi nút kiểm tra xem thông điệp có phải dành cho mình hay không. Ví dụ về mạng có cấu trúc liên kết logic kiểu "bus" là mạng Ethernet 10BASE-T, được xây dựng với các bộ tập trung (hub) và cáp xoắn đôi làm môi trường truyền. Cấu trúc liên kết vật lý của mạng này là kiểu "sao".

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_24.png" alt="Hình 4.24 Mạng với cấu trúc liên kết vật lý kiểu "bus"" width="800">
</p>
<p align="center"><b>Hình 4.24 Mạng với cấu trúc liên kết vật lý kiểu "bus"</b></p>


Mặc dù cấu trúc liên kết "bus" đơn giản trong việc triển khai và có chi phí thấp, nhưng nó có một số nhược điểm quan trọng:

- Có giới hạn về khoảng cách giữa các nút trong mạng. Khoảng cách giữa các nút xa nhất phải nhỏ hơn khoảng cách suy giảm tín hiệu khi truyền qua môi trường vật lý đó. Trong các mạng không dây, khoảng cách này bị giới hạn từ 300 đến 400 mét.
- Có giới hạn về số lượng thiết bị được kết nối với mạng. Vì mạng được sử dụng chung, khi số lượng nút trong mạng tăng lên, số lượng va chạm cũng tăng lên, làm giảm hiệu suất chung của mạng và làm chậm hoạt động của nó.
- Nếu sử dụng cáp làm môi trường truyền, cáp sẽ là "điểm duy nhất gây lỗi". Nếu bất kỳ đoạn cáp nào bị đứt, toàn bộ mạng sẽ ngừng hoạt động.

Hiện nay, cấu trúc liên kết "bus" được sử dụng trong các mạng không dây 802.11 hoặc các mạng xây dựng dựa trên đường dây điện (PLC).


---

## 4.3.2 Cấu trúc liên kết "vòng"  
Khi xem xét cấu trúc liên kết "vòng" (ring), cần phân biệt sự khác nhau giữa cấu trúc liên kết vật lý và logic.

Trong cấu trúc liên kết logic kiểu "vòng", các khung dữ liệu được truyền tuần tự từ nút này đến nút khác theo một thứ tự đã được xác định trước. Các nút tạo thành một vòng khép kín và do đó, nút gửi khung dữ liệu sẽ là nút cuối cùng nhận lại nó. Ví dụ về mạng có cấu trúc liên kết logic kiểu "vòng" là mạng Token Ring. Cấu trúc liên kết vật lý của mạng Token Ring là kiểu "sao".

Cấu trúc liên kết vật lý kiểu "vòng" yêu cầu tổ chức mạng sao cho mỗi nút được kết nối với hai nút khác, để từ một nút nó nhận thông tin và truyền tiếp cho nút thứ hai cho đến khi dữ liệu được nhận bởi nút đích. Nút cuối cùng kết nối với nút đầu tiên, tạo thành vòng khép kín. Việc truyền dữ liệu trong vòng chỉ diễn ra theo một hướng, tuần tự từ nút này sang nút khác.

Mạng với cấu trúc liên kết kiểu "vòng"  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_25.jpg" alt="Hình 4.25 Mạng với cấu trúc liên kết logic kiểu "vòng"" width="600">
</p>
<p align="center"><b>Hình 4.25 Mạng với cấu trúc liên kết logic kiểu "vòng"</b></p>



Cấu trúc liên kết "vòng" cũng có những ưu và nhược điểm như cấu trúc liên kết "bus". Các ưu điểm bao gồm:

- Các nút có cơ hội truy cập bình đẳng vào môi trường truyền, do đó không nút nào có thể chiếm giữ độc quyền môi trường truyền;
- Không cần bộ kết thúc (terminator);
- Không xảy ra va chạm (collision);
- Có thể xây dựng các mạng có độ dài lớn.

Tuy nhiên, cấu trúc liên kết này cũng có các nhược điểm sau:

- Hiệu suất mạng thấp. Tùy thuộc vào số lượng nút trong mạng, thời gian truyền dữ liệu có thể khá lâu, vì tín hiệu phải đi tuần tự qua tất cả các nút, mỗi nút phải kiểm tra xem thông tin có được gửi cho mình hay không;
- Độ tin cậy của mạng không cao. Việc một nút ngừng hoạt động hoặc dây cáp bị đứt sẽ dẫn đến việc mạng hoàn toàn không hoạt động được. Để tránh việc dừng hoạt động của mạng khi một nút gặp sự cố hoặc cáp bị đứt, thường sử dụng vòng kép, điều này dẫn đến chi phí tài chính đáng kể;
- Khó mở rộng mạng. Việc thêm một nút mới vào mạng thường yêu cầu dừng hoạt động của mạng, làm gián đoạn hoạt động của tất cả các nút khác.

Hiện nay, cấu trúc liên kết "vòng" được hiểu là kết nối tuần tự dạng vòng.


---

## 4.3.3 Kết nối nối tiếp  
Kết nối nối tiếp (daisy chain) là một trong những cấu trúc liên kết đơn giản nhất, nếu không tính cấu trúc liên kết "bus". Có hai loại kết nối nối tiếp: tuyến tính (linear daisy chain) và vòng (ring daisy chain).

Trong kết nối tuyến tính hoặc dạng chuỗi (còn được gọi là "chuỗi", "dây đèn"), mỗi thiết bị được kết nối với thiết bị trước và sau nó bằng đường truyền "điểm-điểm" (tức là cáp riêng biệt), nhưng thiết bị đầu tiên và cuối cùng không kết nối với nhau. Trong trường hợp mạng có dây, các thiết bị được kết nối qua cáp riêng biệt, trong mạng không dây - thông qua môi trường truyền có dây.

**Kết nối nối tiếp tuyến tính**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_26.jpg" alt="Hình 4.26 Kết nối nối tiếp tuyến tính" width="600">
</p>
<p align="center"><b>Hình 4.26 Kết nối nối tiếp tuyến tính</b></p>


Các ưu điểm của kết nối tuyến tính bao gồm tính đơn giản, khả năng sử dụng thiết bị giá rẻ và tiêu thụ ít cáp (đối với mạng có dây). Tuy nhiên, nó cũng có những nhược điểm sau:

- Sự hỏng hóc của bất kỳ thiết bị nào hoặc cáp bị đứt sẽ làm gián đoạn chuỗi và gây ra việc các phần của mạng bị cách ly khỏi nhau, không thể phục vụ người dùng.
- Chuỗi càng dài, thời gian cần thiết để truyền thông tin qua nó càng lâu, việc tìm lỗi và bảo trì mạng càng khó khăn.

**Kết nối nối tiếp vòng** (hay còn gọi là "vòng") được tạo ra từ kết nối tuyến tính bằng cách kết nối thiết bị đầu tiên và cuối cùng. Trong kết nối vòng, mỗi thiết bị có thể truyền dữ liệu theo bất kỳ hướng nào.

**Kết nối nối tiếp vòng**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_27.jpg" alt="Hình 4.27 Kết nối nối tiếp vòng" width="600">
</p>
<p align="center"><b>Hình 4.27 Kết nối nối tiếp vòng</b></p>



Kết nối vòng đáng tin cậy hơn kết nối tuyến tính, vì nó không có "điểm duy nhất gây lỗi". Ngay cả khi một thiết bị gặp sự cố hoặc dây cáp bị hư hỏng (trong trường hợp mạng có dây), mạng vẫn duy trì được tính toàn vẹn và tiếp tục hoạt động vì có hai tuyến đến mỗi thiết bị trong mạng.

Các nhược điểm của cấu trúc liên kết này bao gồm:

- Mạng yêu cầu sử dụng các thiết bị có phần mềm hỗ trợ hoạt động trong mạch vòng.
- Chi phí cao và phức tạp trong việc cài đặt thiết bị.
- Khó khăn trong việc tìm lỗi và bảo trì mạng.
- Khi có hai hoặc nhiều thiết bị bị hỏng, hoạt động của mạng sẽ bị gián đoạn.

Các cấu trúc liên kết được thảo luận ở trên thường được áp dụng trong các mạng truy cập của nhà cung cấp dịch vụ, được xây dựng trên các bộ chuyển mạch Ethernet, cũng như trong các mạng không dây phân bố theo lãnh thổ. Cấu trúc liên kết tuyến tính chủ yếu được sử dụng bởi các nhà cung cấp dịch vụ nhỏ, mới bắt đầu vì nó không yêu cầu chi phí tài chính lớn, yêu cầu nhân viên có trình độ cao và thích ứng tốt với môi trường đô thị. Tuy nhiên, khi mạng phát triển và số lượng khách hàng tăng lên, mạng với kết nối tuyến tính sẽ không còn hiệu quả.

Kết nối vòng đáng tin cậy nhờ các liên kết dư thừa giữa các thiết bị, do đó nó thường được sử dụng trong các mạng truy cập của các nhà cung cấp dịch vụ vừa và lớn.

Khi kết nối các bộ chuyển mạch hoặc điểm truy cập thành vòng, cần nhớ rằng chúng không thể hoạt động chính xác trong các mạng có mạch vòng. Do đó, phần mềm của thiết bị phải hỗ trợ các giao thức đặc biệt để đảm bảo hoạt động trong các mạng có tuyến đường dư thừa. Đó là các giao thức Spanning Tree Protocol (STP hoặc các phiên bản cải tiến của nó như RSTP và MSTP) và/hoặc Ethernet Ring Protection Switching (ERPS). Nhiệm vụ của các giao thức này là chuyển đổi cấu trúc liên kết vòng thành cấu trúc tuyến tính về mặt logic với khả năng tự động dự phòng các kênh truyền thay thế giữa các thiết bị khi kênh truyền hoạt động gặp sự cố.

Chi tiết về hoạt động của giao thức STP trong các mạng được xây dựng trên bộ chuyển mạch Ethernet sẽ được mô tả trong chương 6.

---

4.3.4 Cấu trúc liên kết "sao"  
Cấu trúc liên kết "sao" (star) là một trong những cấu trúc liên kết phổ biến nhất của mạng máy tính. Thường được sử dụng trong các mạng cục bộ của văn phòng nhỏ hoặc mạng gia đình. Trong cấu trúc liên kết này, tất cả các nút đều được kết nối bằng đường truyền "điểm-điểm" tới một thiết bị trung tâm, trong các mạng hiện đại có thể là bộ chuyển mạch (switch), bộ định tuyến (router), hoặc điểm truy cập (access point). Việc trao đổi dữ liệu giữa các nút được thực hiện thông qua thiết bị trung tâm, thiết bị này thực hiện và kiểm soát các chức năng được triển khai trong mạng, cũng như tăng cường tín hiệu đi qua nó.

**Mạng với cấu trúc liên kết "sao"**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_28.png" alt="Hình 4.28 Mạng với cấu trúc liên kết "sao"" width="600">
</p>
<p align="center"><b>Hình 4.28 Mạng với cấu trúc liên kết "sao"</b></p>


Các ưu điểm chính của cấu trúc liên kết "sao" bao gồm:

- Đơn giản trong việc bảo trì và khắc phục sự cố mạng, cũng như dễ dàng kết nối thêm thiết bị mới.
- Tính bảo mật của mạng. Thiết bị trung tâm có thể là thiết bị mạng với các chức năng bảo mật tiên tiến, đảm bảo kiểm soát lưu lượng đi qua nó. Ngoài ra, có thể hạn chế truy cập vật lý vào thiết bị trung tâm bằng cách đặt nó ở một vị trí an toàn.
- Có thể sử dụng các loại cáp khác nhau để kết nối các nút với thiết bị trung tâm, nếu thiết bị này được trang bị các cổng có loại khác nhau (quang học, đồng).
- Có thể sử dụng thiết bị giá rẻ.

Những nhược điểm chính của cấu trúc liên kết này bao gồm:

- Tồn tại "điểm duy nhất gây lỗi". Nếu thiết bị trung tâm gặp sự cố, toàn bộ mạng sẽ ngừng hoạt động.
- Để kết nối thiết bị trong mạng có dây, cần sử dụng một lượng lớn cáp.
- Số lượng thiết bị có thể kết nối vào mạng bị giới hạn bởi số lượng cổng của thiết bị trung tâm (đối với mạng có dây) hoặc hiệu suất của điểm truy cập.

Trước khi tiếp tục xem xét các cấu trúc liên kết mạng khác, chúng ta sẽ làm một số ngoại lệ nhỏ. Các mạng nhỏ, thông thường được xây dựng trên một trong những cấu trúc liên kết cơ bản — kết nối tuyến tính, vòng hoặc sao. Đối với các mạng lớn, việc có các kết nối tùy ý giữa các nút là đặc điểm phổ biến, vì chúng thường xuyên được mở rộng và nâng cấp. Trong những mạng như vậy, có thể phân tách thành các đoạn mạng liên kết tùy ý, mỗi đoạn có một trong những cấu trúc liên kết điển hình. Vì cấu trúc liên kết của các mạng lớn là sự kết hợp của nhiều cấu trúc liên kết cơ bản, nên những mạng này được gọi là mạng có cấu trúc liên kết hỗn hợp hoặc linh hoạt.

---

## 4.3.5 Cấu trúc liên kết "cây"  
Cấu trúc liên kết "cây" (tree), còn được gọi là "sao mở rộng" (extended star), được tạo ra từ sự kết hợp của cấu trúc liên kết "sao" và kết nối tuyến tính. Cấu trúc này thực hiện phân cấp các nút. Ở cấp cao nhất của hệ thống phân cấp là thiết bị trung tâm, nó kết nối các thiết bị trung tâm của các "sao" riêng lẻ bằng các đường truyền "điểm-điểm". Cấu trúc phân cấp này có thể có nhiều cấp.

Cấu trúc liên kết "cây" là cấu trúc liên kết phổ biến nhất trong các mạng máy tính hiện đại. Nó thường được sử dụng trong mạng của các doanh nghiệp vừa và lớn, cũng như trong mạng của các nhà cung cấp dịch vụ.

**Mạng với cấu trúc liên kết "cây"**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_29.png" alt="Hình 4.29 Mạng với cấu trúc liên kết "cây"" width="600">
</p>
<p align="center"><b>Hình 4.29 Mạng với cấu trúc liên kết "cây"</b></p>


Các ưu điểm chính của cấu trúc liên kết này bao gồm:

- Khả năng mở rộng và tăng quy mô mạng.
- Có thể phân chia mạng lớn thành các đoạn mạng (các "sao" riêng lẻ), giúp đơn giản hóa việc bảo trì và quản lý mạng.
- Sự cố trong một đoạn mạng không ảnh hưởng đến hoạt động của các đoạn mạng khác.

Những nhược điểm của cấu trúc liên kết "cây" là:

- Khi số lượng đoạn mạng tăng lên, việc bảo trì và quản lý mạng trở nên phức tạp hơn, cũng như việc tìm và khắc phục sự cố.
- Chi phí thiết bị cao.
- Cần một lượng lớn cáp (trong trường hợp mạng có dây).
- Yêu cầu nhân viên có trình độ chuyên môn cao.

---

## 4.3.6 Cấu trúc liên kết dạng lưới  
Cấu trúc liên kết dạng lưới (mesh), còn được gọi là cấu trúc liên kết mạng lưới hoặc ô lưới, là một kiểu cấu trúc liên kết trong đó mỗi thiết bị được kết nối với nhiều thiết bị khác bằng các kênh truyền "điểm-điểm". Thiết bị không chỉ thu thập và xử lý dữ liệu của mình mà còn hoạt động như một bộ phát lại thông điệp cho các thiết bị khác. Cấu trúc này được đặc trưng bởi độ tin cậy cao và khả năng chống lỗi nhờ vào sự có mặt của nhiều liên kết dự phòng giữa các nút trong mạng. Sự cố của một nút hoặc đứt gãy đường truyền không ảnh hưởng đến hoạt động của mạng (khi một kênh bị đứt, có thể truyền qua các kênh khác). Để tìm ra con đường tốt nhất để truyền dữ liệu giữa các nút trong mạng lưới, các bộ định tuyến, bộ chuyển mạch, hoặc điểm truy cập được sử dụng.

Có hai loại cấu trúc liên kết dạng lưới: cấu trúc liên kết đầy đủ (full connected) và cấu trúc liên kết không đầy đủ (partially connected).

Trong cấu trúc liên kết đầy đủ, mỗi nút được kết nối trực tiếp với tất cả các nút khác trong mạng. Cấu trúc này phản ánh kiến trúc của Internet, trong đó có nhiều con đường đến bất kỳ điểm nào. Cấu trúc liên kết đầy đủ khá đắt đỏ vì trong trường hợp mạng có dây, nó yêu cầu tiêu tốn nhiều cáp và số lượng cổng kết nối lớn, nhưng đồng thời đảm bảo độ chống lỗi cao. Trên thực tế, nó hiếm khi được sử dụng và chỉ được áp dụng ở những nơi yêu cầu độ tin cậy cao và khả năng chống lỗi tối đa, ví dụ như trong việc xây dựng mạng xương sống.

**Mạng với cấu trúc liên kết dạng lưới đầy đủ**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_30.png" alt="Hình 4.30 Mạng với cấu trúc liên kết dạng lưới đầy đủ" width="600">
</p>
<p align="center"><b>Hình 4.30 Mạng với cấu trúc liên kết dạng lưới đầy đủ</b></p>

Cấu trúc liên kết không đầy đủ được tạo ra từ cấu trúc liên kết đầy đủ bằng cách loại bỏ một số liên kết có thể có. Trong cấu trúc này, số lượng kết nối của mỗi thiết bị phụ thuộc chủ yếu vào tầm quan trọng của nó trong mạng. Cấu trúc liên kết không đầy đủ ít tốn kém hơn cấu trúc đầy đủ và thường được sử dụng trong các mạng ngoại vi để kết nối với các mạng xương sống có cấu trúc liên kết đầy đủ.

**Mạng với cấu trúc liên kết dạng lưới không đầy đủ**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_31.png" alt="Hình 4.31 Mạng với cấu trúc liên kết dạng lưới không đầy đủ" width="600">
</p>
<p align="center"><b>Hình 4.31 Mạng với cấu trúc liên kết dạng lưới không đầy đủ</b></p>

Để mạng có cấu trúc liên kết dạng lưới hoạt động chính xác, cần phải cấu hình các giao thức loại bỏ những liên kết dư thừa, tránh việc tạo ra vòng lặp dữ liệu hoặc vòng lặp định tuyến.

Mặc dù có ưu điểm rõ ràng, các mạng có cấu trúc liên kết dạng lưới vẫn có những nhược điểm chính bao gồm chi phí cao, khó khăn trong việc kết nối/ngắt kết nối thiết bị mạng và cấu hình của nó. Cấu trúc liên kết dạng lưới thường được sử dụng kết hợp với các cấu trúc liên kết khác như "chuỗi", "vòng" và "sao" để tạo thành một mạng có cấu trúc liên kết hỗn hợp.

**Ví dụ về mạng có cấu trúc liên kết hỗn hợp**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_32.png" alt="Hình 4.32 Ví dụ về mạng có cấu trúc liên kết hỗn hợp" width="1000">
</p>
<p align="center"><b>Hình 4.32 Ví dụ về mạng có cấu trúc liên kết hỗn hợp</b></p>

Sau khi xem xét các cấu trúc liên kết mạng hiện có, chúng ta cần chú ý đến các yếu tố quan trọng khác ảnh hưởng đến việc lựa chọn cấu trúc liên kết mạng. Cấu trúc liên kết phải đảm bảo:

- Quản lý luồng dữ liệu thuận tiện.
- Chịu được lỗi của các nút kết nối vào mạng và đứt cáp.
- Khả năng mở rộng mạng và chuyển đổi sang các công nghệ tốc độ cao mới.
- Chi phí thấp để xây dựng và duy trì mạng.

Ngoài ra, cần cân nhắc:

- Hạ tầng cáp và thiết bị hiện có nếu mạng cần được mở rộng.
- Vị trí lắp đặt các thiết bị.
- Kích thước của mạng dự kiến.
- Khối lượng và loại thông tin để sử dụng chung.


