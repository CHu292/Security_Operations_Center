# 1.3 Các loại mạng máy tính
Mạng máy tính có thể được phân loại theo nhiều tiêu chí khác nhau:

- trên cơ sở lãnh thổ;
- theo loại phương tiện truyền dẫn;
- bởi tốc độ truyền thông tin;
- theo loại tương tác chức năng;
- theo loại cấu trúc liên kết mạng;
- theo mục đích chức năng;
- trên hệ điều hành mạng;
- theo chế độ truy cập của người dùng;
- theo vai trò trong kiến ​​trúc mạng đa cấp.

## 1.3.1 Trên cơ sở lãnh thổ
Phân loại mạng theo đặc điểm lãnh thổ là cơ bản. Tùy thuộc vào khoảng cách giữa các nút, mạng máy tính có thể được chia thành cục bộ, toàn cầu và đô thị.

### a. Mạng cục bộ - Local Area Network (LAN) 

- là một nhóm các nút được kết nối với nhau và nằm trong một khu vực nhỏ. Nhìn chung, mạng cục bộ là hệ thống truyền thông thuộc về một tổ chức. Ví dụ về mạng cục bộ bao gồm mạng gia đình, mạng văn phòng, mạng trường học và mạng doanh nghiệp. Mạng cục bộ được đặc trưng bởi tốc độ truyền dữ liệu cao. Các công nghệ phổ biến nhất cho mạng cục bộ là Ethernet và họ tiêu chuẩn IEEE 802.11 cho mạng cục bộ không dây - Wireless Local Area Network  (WLAN).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/1_Basic_concepts_of_network_technologies/image/3_Local_Area_Network.png" alt="Mạng cục bộ - LAN" width="1000">
</p>
<p align="center"><b>Mạng cục bộ - LAN</b></p>

- Các mạng cục bộ nhỏ, phạm vi giới hạn trong vài mét và được thiết kế để kết nối các thiết bị được sử dụng bởi một người (hoặc một nhóm nhỏ người) được gọi là mạng khu vực cá nhân (Personal Area Network - PAN). Thông thường, thuật ngữ này được áp dụng cho các mạng. của công nghệ không dây Bluetooth.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/1_Basic_concepts_of_network_technologies/image/3_Personal_Local_Area_Network.png" alt="Mạng cục bộ cá nhân PAN" width="1000">
</p>
<p align="center"><b>Mạng cục bộ cá nhân PAN</b></p>
  
- Mạng campus (mạng trường) có thể được coi là một loại mạng cục bộ. Mạng khu vực trường học (CAN - Campus Area Network) là mạng máy tính kết nối các mạng cục bộ trong một khu vực giới hạn về mặt địa lý, chẳng hạn như khuôn viên trường đại học, khuôn viên công ty hoặc căn cứ quân sự. Mạng trường đại học lớn hơn mạng cục bộ thông thường nhưng nhỏ hơn mạng khu vực đô thị. Thông thường, mạng trường sử dụng công nghệ Ethernet tốc độ cao. Mạng trường còn được gọi là Mạng khu vực doanh nghiệp (Corporate Area Network).

### b. Mạng toàn cầu (WAN - Wide Area Network) 
- Là mạng máy tính bao phủ các khu vực rộng lớn và bao gồm mạng của các thành phố, quốc gia và lục địa. Mạng toàn cầu phổ biến nhất là Internet. Mạng WAN được thiết kế để kết nối các mạng khác nhau để người dùng và máy tính, bất kể họ ở đâu, đều có thể tương tác với mọi người khác trên mạng toàn cầu. Một số mạng toàn cầu được xây dựng dành riêng cho một số tổ chức nhất định và mang tính riêng tư, một số mạng khác được tổ chức bởi các nhà khai thác viễn thông và là phương tiện kết nối mạng nội bộ gia đình hoặc mạng cục bộ của các tổ chức với Internet. Mạng WAN có thể được tạo bằng cách sử dụng đường truyền thuê riêng (kết nối điểm-điểm giữa hai máy tính hoặc mạng cục bộ) hoặc các phương thức dựa trên chuyển mạch mạch, gói hoặc di động. Các giao thức và công nghệ phổ biến nhất của mạng toàn cầu là SONET/SDH, MPLS, PPP, xDSL, GPON và họ Ethernet.

### c. Mạng thành phố hoặc mạng khu vực đô thị (MAN - Metropolitan Area Network) 
- Là mạng máy tính kết nối nhiều mạng cục bộ trong lãnh thổ của một thành phố. Mạng đô thị kết hợp các tính năng của cả mạng cục bộ và mạng toàn cầu. Nó được đặc trưng bởi mật độ kết nối cao của các thuê bao cuối, đường truyền tốc độ cao và các kênh liên lạc có độ dài lớn. Ví dụ về mạng đô thị bao gồm mạng lõi và mạng truyền hình cáp của nhà cung cấp. - - -- Trong hầu hết các trường hợp, mạng đô thị sử dụng các đường dây và công nghệ truyền thông quang thuộc họ Ethernet (tức là Metro Ethernet). Tuy nhiên, các kênh liên lạc giữa các mạng cục bộ có thể được tổ chức mà không cần sử dụng dây cáp. Sự phát triển liên quan đến truy cập Internet không dây tốc độ cao đã dẫn đến việc tạo ra các MAN không dây (Mạng khu vực đô thị không dây, WMAN - Wireless Metropolitan Area Networks).
Sự kết hợp giữa các mạng toàn cầu, đô thị và cục bộ giúp tạo ra các hệ thống phân cấp đa cấp, là những công cụ mạnh mẽ để xử lý lượng lớn dữ liệu và truy cập các nguồn thông tin hầu như không giới hạn.

## 1.3.2 Theo loại tương tác chức năng

- Một ví dụ về sự tương tác giữa mạng cục bộ và mạng diện rộng là mạng riêng ảo (VPN - Virtual Private Network) - kết nối an toàn qua các kênh công cộng của mạng diện rộng (ví dụ: Internet) giữa hai hoặc nhiều điểm cuối nằm trên các mạng cục bộ khác nhau.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/1_Basic_concepts_of_network_technologies/image/3_Virtual_Private_Network.png" alt="Mạng riêng ảo - VPN" width="1000">
</p>
<p align="center"><b>Mạng riêng ảo - VPN</b></p>

---
- Nói cách khác, một mạng lớn có thể được mô tả như một cấu trúc bao gồm nhiều mạng nhỏ hơn hoặc các phần của chúng được kết nối với nhau. Khái niệm này rất quan trọng để hiểu các công nghệ mạng vì một số trong số chúng có thể được giải thích tốt nhất bằng cách xem xét toàn bộ mạng lớn hơn ở cấp cao nhất của hệ thống phân cấp, trong khi việc giải thích các công nghệ khác yêu cầu cái nhìn chi tiết về hoạt động của các bộ phận của nó.
- Cần phải đi vòng qua một chút ở đây để làm quen với các thuật ngữ là những khái niệm quan trọng trong thiết kế mạng và được sử dụng để mô tả kích thước tương đối của mạng và các bộ phận của chúng.
- Những thuật ngữ được sử dụng phổ biến nhất là:
  - **Mạng (Network)** là một thuật ngữ chung thường được dùng để chỉ nhiều khái niệm khác nhau. Một mạng có thể có hầu như bất kỳ kích thước nào, từ hai thiết bị đến hàng nghìn. Khi một mạng lớn và bao gồm nhiều mạng nhỏ hơn được kết nối với nhau, thì nó đã được gọi là mạng tổng hợp (Internetwork). Tuy nhiên, mặc dù vậy, bạn vẫn thường nghe thấy, ví dụ, "Mạng doanh nghiệp D-Link", mặc dù rõ ràng là nó bao gồm ít nhất một nghìn máy tính.
  - **Mạng con (Subnetwork, subnet).** Thuật ngữ này có một số ý nghĩa. Mạng con là một phần của mạng hoặc mạng là một phần của mạng tổng hợp lớn hơn. Ngoài ra, thuật ngữ "mạng con" có ý nghĩa đặc biệt trong bối cảnh địa chỉ IP.
  - **Phân đoạn (Phân đoạn mạng, phân khúc, phân khúc mạng - segment, network segment).** Thuật ngữ này, giống như thuật ngữ "mạng con", có nhiều ý nghĩa. Một phân đoạn có thể được định nghĩa là một phần nhỏ của mạng; trong một số ngữ cảnh, phân đoạn đề cập đến "mạng con" và các thuật ngữ được sử dụng thay thế cho nhau. Tuy nhiên, thông thường thuật ngữ “phân đoạn” được hiểu là một phần riêng biệt của mạng, nhỏ hơn mạng con. Mạng thường được thiết kế sao cho các máy tính được kết nối với nhau hoặc được sử dụng bởi cùng một nhóm người được đặt trên cùng một phân đoạn mạng.
    - Có vấn đề với việc sử dụng kép thuật ngữ "phân đoạn" trong công nghệ Ethernet. Các thông số kỹ thuật của lớp vật lý Ethernet đầu tiên sử dụng cáp đồng trục, bản thân cáp này được gọi là "phân đoạn". Phân đoạn này được chia sẻ bởi tất cả các thiết bị kết nối với nó và được gọi là “miền xung đột - collision domain” của mạng.
    - Đối với mỗi lớp vật lý của công nghệ Ethernet, các quy tắc được xác định để điều chỉnh số lượng thiết bị trong một phân đoạn, độ dài của phân đoạn, cách các phân đoạn được kết nối với nhau, tùy thuộc vào thiết bị mạng được sử dụng. Ví dụ, các thiết bị như bộ lặp và bộ chia làm tăng miền xung đột (collision domain), trong khi các bộ chuyển mạch chia một miền va chạm lớn thành nhiều collision domain nhỏ hơn. Theo thời gian, các thuật ngữ "miền xung đột - collision domain" và "phân đoạn - segment" trở nên có thể hoán đổi cho nhau. Do đó, ngày nay trong công nghệ Ethernet, thuật ngữ "phân đoạn - segment" được sử dụng để chỉ cả một phần cáp và cáp được kết nối điện biểu thị một collision domain duy nhất.
    - Một ý nghĩa khác của thuật ngữ "phân đoạn - segment" có liên quan đến giao thức TCP. Một phân đoạn là một tin nhắn được gửi bởi giao thức này
---
- **Mạng tổng hợp (Internetwork, Internet).** Ý nghĩa của thuật ngữ này có thể chung chung hoặc cụ thể, tùy thuộc vào ngữ cảnh. Một số công nghệ sử dụng "internetwork" để chỉ cấu trúc mạng lớn được tạo thành từ nhiều mạng nhỏ hơn. Ở những nơi khác, đó là một mạng được tách biệt khỏi mạng tổng hợp dựa trên cách kết nối các thiết bị. Ví dụ: mạng thường có nghĩa là một nhóm nút được kết nối ở cấp liên kết dữ liệu của mô hình OSI - (Open Systems Interconnection Reference Model) (Mô hình tham chiếu kết nối hệ thống mở) thông qua công nghệ Ethernet sử dụng bộ chuyển mạch. Mạng tổng hợp được hình thành khi các mạng này được kết nối với nhau ở lớp thứ ba của mô hình OSI bằng bộ định tuyến.

## 1.3.3 Theo vai trò trong kiến ​​trúc mạng đa cấp

- Dựa trên vai trò của chúng trong kiến ​​trúc đa cấp, mạng có thể được chia thành:
  - **mạng truy cập (access network);**
  - **mạng đường trục  - mạng lõi(backbone, backbone network).**
- **Mạng truy nhập - access network:** được hiểu là mạng cục bộ cần thiết để kết nối thiết bị đầu cuối thuê bao với các nút của mạng đường trục của một doanh nghiệp hoặc nhà khai thác viễn thông.
- **Mạng đường trục  - mạng lõi (Backbone Network)** được hiểu là mạng phân tán về mặt địa lý, thực hiện chức năng truyền (truyền - transporting) các luồng thông báo từ mạng truy cập này sang mạng truy cập khác. Các nút mạng đường trục (bộ chuyển mạch - switches, bộ định tuyến - routers) thường được kết nối bằng các kênh liên lạc tốc độ cao và đáng tin cậy (quang hoặc vệ tinh).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/1_Basic_concepts_of_network_technologies/image/3_Connecting_access_networks_to_the_backbone_network.png" alt="Kết nối mạng truy cập với mạng đường trục" width="1000">
</p>
<p align="center"><b>Kết nối mạng truy cập với mạng đường trục</b></p>

## 1.3.4 theo chế độ truy cập của người dùng
- Theo chế độ truy cập của người dùng, tất cả các mạng hiện có được chia thành: mạng công cộng (public) và mạng riêng (private). Mạng công cộng là mạng mà bất kỳ người dùng nào cũng có thể truy cập. Mạng truyền thông công cộng bao gồm Internet, mạng điện thoại công cộng, mạng truyền hình và phát thanh. Chỉ một nhóm người hạn chế có thể truy cập vào mạng riêng, thường là người dùng gia đình, nhân viên của các công ty và doanh nghiệp. Mạng riêng bao gồm mạng gia đình, mạng doanh nghiệp, mạng chuyên nghiệp, mạng công nghiệp và công nghệ.

## 1.3.5 Theo loại phương tiện truyền dẫn
- Dựa trên loại phương tiện truyền dẫn, mạng máy tính có thể được chia thành có dây và không dây.
  - Mạng có dây sử dụng cáp điện (đồng trục, cáp xoắn đôi) hoặc cáp quang để truyền dữ liệu.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/1_Basic_concepts_of_network_technologies/image/3_Wired_network.png" alt="Mạng có dây" width="1000">
</p>
<p align="center"><b>Mạng có dây</b></p>

  - Trong mạng không dây, thông tin được truyền bằng sóng điện từ ở một dải tần số nhất định.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/1_Basic_concepts_of_network_technologies/image/3_Wireless_network.png" alt="Mạng không dây" width="1000">
</p>
<p align="center"><b>Mạng không dây</b></p>
