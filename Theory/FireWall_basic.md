# Mục lục

1. [Tường lửa là gì?](#tường-lửa-là-gì)
2. [Tường lửa gồm có bao nhiêu loại?](#tường-lửa-gồm-có-bao-nhiêu-loại)
   - [Tường lửa Personal](#tường-lửa-personal)
   - [Network Firewalls](#network-firewalls)
3. [Cách thức hoạt động của tường lửa như thế nào?](#cách-thức-hoạt-động-của-tường-lửa-như-thế-nào)
4. [Nhiệm vụ của tường lửa (Firewall) là gì?](#nhiệm-vụ-của-tường-lửa-firewall-là-gì)
5. [Ưu và nhược điểm của tường lửa](#ưu-và-nhược-điểm-của-tường-lửa)
   - [Ưu điểm của tường lửa](#ưu-điểm-của-tường-lửa)
   - [Nhược điểm của tường lửa](#nhược-điểm-của-tường-lửa)
6. [Những tùy chọn khi triển khai Firewall mà bạn nên biết](#những-tùy-chọn-khi-triển-khai-firewall-mà-bạn-nên-biết)
   - [Stateful firewall (Tường lửa có trạng thái)](#stateful-firewall-tường-lửa-có-trạng-thái)
   - [Next-generation firewalls – NGFW (Tường lửa thế hệ tiếp theo)](#next-generation-firewalls-ngfw-tường-lửa-thế-hệ-tiếp-theo)
   - [Proxy-based firewall (Tường lửa dựa trên proxy)](#proxy-based-firewall-tường-lửa-dựa-trên-proxy)
   - [Web application firewall – WAF (Tường lửa ứng dụng web)](#web-application-firewall-waf-tường-lửa-ứng-dụng-web)
   - [Tường lửa phần cứng](#tường-lửa-phần-cứng)
   - [Tường lửa phần mềm](#tường-lửa-phần-mềm)
   - [Kiểm tra trạng thái tường lửa](#kiểm-tra-trạng-thái-tường-lửa)
   - [Tường lửa phát hiện và diệt virus](#tường-lửa-phát-hiện-và-diệt-virus)
   - [Kiểm tra tầng ổ bảo mật SSL](#kiểm-tra-tầng-ổ-bảo-mật-ssl)
   - [Intrusion Prevention Systems – IPS (Hệ thống phòng chống xâm nhập)](#intrusion-prevention-systems-ips-hệ-thống-phòng-chống-xâm-nhập)
   - [Theo dõi lưu lượng gửi đi (DPI)](#theo-dõi-lưu-lượng-gửi-đi-dpi)
7. [Những lỗ hổng của tường lửa](#những-lỗ-hổng-của-tường-lửa)
   - [Tấn công nội bộ](#tấn-công-nội-bộ)
   - [Tấn công từ chối dịch vụ phân tán (DDos)](#tấn-công-từ-chối-dịch-vụ-phân-tán-ddos)
   - [Các phần mềm độc hại](#các-phần-mềm-độc-hại)
   - [Cấu hình tường lửa kém, thiếu cập nhật](#cấu-hình-tường-lửa-kém-thiếu-cập-nhật)

---

# Nội dung

<h1 id="tường-lửa-là-gì">Phần 1: Tường lửa là gì?</h1>

Tường lửa (firewall) là một cơ chế bảo mật mạng được sử dụng để giám sát và kiểm soát lưu lượng mạng đi qua nó. Tường lửa có thể được triển khai ở nhiều vị trí khác nhau trên mạng như trên máy tính, trên thiết bị định tuyến hoặc trên một máy chủ đặc biệt.

Tường lửa có thể cấu hình để cho phép hoặc chặn lưu lượng mạng dựa trên một số yếu tố như địa chỉ IP, cổng mạng, giao thức, ứng dụng và các luật quy định khác.

Nó có thể được sử dụng để bảo vệ mạng khỏi các cuộc tấn công từ bên ngoài, chẳng hạn như tấn công từ mạng Internet, hay để ngăn chặn các cuộc tấn công từ bên trong mạng, chẳng hạn như các cuộc tấn công từ các máy tính bị nhiễm độc.


<h1 id="tường-lửa-gồm-có-bao-nhiêu-loại">Phần 2: Tường lửa gồm có bao nhiêu loại?</h1>

Tường lửa được chia thành 2 loại, cụ thể là Personal Firewalll và Network Firewall, cụ thể như sau: 

<h2 id="tường-lửa-personal">2.1. Tường lửa Personal</h2>

Tường lửa Personal là một loại tường lửa được thiết kế để bảo vệ máy tính của người dùng khỏi các cuộc tấn công mạng từ bên ngoài.

Nó cũng tích hợp các tính năng hữu ích như theo dõi các phần mềm chống virus và phần mềm chống xâm nhập để đảm bảo an toàn cho dữ liệu

Các loại tường lửa Personal phổ biến bao gồm Microsoft Internet connection firewall, Symantec personal firewall, Cisco Security Agent và nhiều loại tường lửa khác.

Tường lửa Personal thích hợp cho cá nhân sử dụng máy tính cá nhân hoặc laptop vì thông thường họ chỉ quan tâm đến bảo vệ máy tính của mình.

Tường lửa Personal thường được tích hợp sẵn trong hệ điều hành của máy tính như Windows Firewall trên Windows hoặc được cài đặt như một phần mềm bảo mật độc lập.

<h2 id="network-firewalls">2.2. Network Firewalls</h2>

Network Firewall được thiết kế để bảo vệ các host trong mạng khỏi các cuộc tấn công từ bên ngoài. Bạn có thể tham khảo một số tường lửa bao gồm Appliance-Based network Firewalls:

Ví dụ như: Cisco PIX, Nokia firewalls, Symantec’s Enterprise Firewall, Juniper NetScreen firewall, Cisco ASA và các loại tường lửa Software-Based như Check Point’s Firewall, Linux-based IPTables, Microsoft ISA Server.

Sự khác biệt chính giữa 2 loại tường lửa này là số lượng host mà nó có nhiệm vụ bảo vệ. Personal Firewall chỉ có thể bảo vệ cho một máy tính duy nhất, trong khi Network Firewall có thể bảo vệ cho toàn bộ hệ thống mạng máy tính.

<h1 id="cách-thức-hoạt-động-của-tường-lửa-như-thế-nào">Phần 3: Cách thức hoạt động của tường lửa như thế nào?</h1>

Tường lửa hoạt động như một chiếc cổng kiểm soát lưu lượng mạng giữa hai mạng hoặc giữa một máy tính và mạng.

Nó là một thành phần quan trọng trong hệ thống bảo mật mạng và được sử dụng để bảo vệ mạng khỏi các cuộc tấn công từ bên ngoài hoặc ngăn chặn các cuộc tấn công từ bên trong mạng.

Khi lưu lượng mạng đi qua tường lửa, nó sẽ được kiểm tra và đánh giá để xác định liệu nó có phù hợp với các quy tắc bảo mật được cấu hình hay không. Nếu lưu lượng mạng không đáp ứng các quy tắc bảo mật, tường lửa sẽ chặn nó để ngăn chặn các cuộc tấn công mạng.

Tường lửa có thể kiểm soát lưu lượng mạng dựa trên một số yếu tố như địa chỉ IP, cổng mạng, giao thức và các luật quy định khác.

Nó có thể được cấu hình để cho phép hoặc chặn lưu lượng mạng dựa trên các quy tắc bảo mật được đặt ra, hoặc nó có thể được cấu hình để thông báo cho người quản trị mạng khi có một cuộc tấn công mạng xảy ra.

Tường lửa có thể được triển khai trên nhiều vị trí khác nhau trên mạng, bao gồm trên máy tính, trên thiết bị định tuyến hoặc trên một máy chủ đặc biệt.

Nó có thể được cấu hình để hoạt động theo các chế độ khác nhau như chế độ gói dữ liệu (packet filtering), chế độ đăng nhập (stateful inspection), hoặc chế độ ứng dụng (application layer).

<h1 id="nhiệm-vụ-của-tường-lửa-firewall-là-gì">Phần 4: Nhiệm vụ của tường lửa (Firewall) là gì?</h1>

Nhiệm vụ chính của tường lửa (Firewall) là bảo vệ mạng và các thiết bị trong mạng khỏi các cuộc tấn công mạng và các hoạt động độc hại.

Nó hoạt động như một bức tường ảo giữa mạng của bạn và mạng bên ngoài, kiểm soát lưu lượng mạng đi qua và quyết định cho phép hoặc chặn các gói dữ liệu dựa trên các quy tắc bảo mật được cấu hình.

Các nhiệm vụ chính của tường lửa cụ thể như sau:

Kiểm soát truy cập: Tường lửa kiểm soát truy cập vào mạng hoặc vào các thiết bị trong mạng bằng cách quản lý các quy tắc truy cập dựa trên địa chỉ IP, cổng mạng, giao thức và các luật quy định khác.

Chống tấn công: Tường lửa phát hiện và chặn các cuộc tấn công mạng từ bên ngoài hoặc từ bên trong mạng như tấn công từ chối dịch vụ (DoS), tấn công mã độc, tấn công từ bên trong mạng.

Bảo vệ dữ liệu: Tường lửa bảo vệ dữ liệu quan trọng khỏi các cuộc tấn công và lưu trữ các dữ liệu mật trong mạng một cách an toàn.

Quản lý lưu lượng mạng: Tường lửa kiểm soát và quản lý lưu lượng mạng vào và ra khỏi mạng, giúp ngăn chặn quá tải mạng và đảm bảo hiệu suất mạng tốt nhất.

Giám sát và báo cáo: Tường lửa giám sát các hoạt động trên mạng và cung cấp báo cáo cho người quản trị mạng về các hoạt động mạng và các cuộc tấn công trên không gian mạng. 

<h1 id="ưu-và-nhược-điểm-của-tường-lửa">Phần 5: Ưu và nhược điểm của tường lửa</h1>
<h2 id="ưu-điểm-của-tường-lửa">5.1. Ưu điểm của tường lửa</h2>

Tường lửa (Firewall) là một công cụ quan trọng trong hệ thống bảo mật mạng và có nhiều ưu điểm như sau:

Bảo vệ mạng và dữ liệu: Tường lửa làm nhiệm vụ bảo vệ mạng và dữ liệu trên mạng khỏi các cuộc tấn công mạng và các hoạt động độc hại.

Kiểm soát truy cập: Tường lửa giúp kiểm soát truy cập vào mạng hoặc vào các thiết bị trong mạng bằng cách quản lý các quy tắc truy cập dựa trên địa chỉ IP, cổng mạng, giao thức và các luật quy định khác.

Giám sát lưu lượng mạng: Tường lửa giúp giám sát và quản lý lưu lượng mạng vào và ra khỏi mạng, giúp ngăn chặn quá tải mạng và đảm bảo hiệu suất mạng tốt nhất.

Bảo vệ dữ liệu quan trọng: Tường lửa giúp bảo vệ dữ liệu quan trọng khỏi các cuộc tấn công và lưu trữ các dữ liệu mật trong mạng một cách an toàn.

Điều chỉnh quyền truy cập: Tường lửa giúp điều chỉnh quyền truy cập cho các máy tính và người dùng trong mạng, đảm bảo rằng chỉ những người được phép mới có thể truy cập vào các tài nguyên mạng.

Tăng cường tính năng bảo mật: Tường lửa giúp tăng cường tính năng bảo mật của các ứng dụng và các dịch vụ mạng, giúp ngăn chặn các cuộc tấn công và các lỗ hổng bảo mật.

Cung cấp báo cáo và giám sát: Tường lửa cung cấp báo cáo về các hoạt động mạng và các cuộc tấn công mạng có thể xảy ra, giúp người quản trị mạng theo dõi và đánh giá hiệu quả của hệ thống bảo mật mạng.

<h2 id="nhược-điểm-của-tường-lửa">5.2. Nhược điểm của tường lửa</h2>

Mặc dù tường lửa là một công cụ quan trọng trong hệ thống bảo mật mạng, nhưng nó cũng có một số nhược điểm như sau:

Khả năng xâm nhập: Những kẻ tấn công thông minh có thể vượt qua tường lửa bằng cách sử dụng các kỹ thuật tấn công như tấn công từ bên trong (insider attack) hoặc sử dụng các mã độc để xâm nhập vào hệ thống.

Sự cố về phần cứng hoặc phần mềm: Tường lửa có thể gặp sự cố về phần cứng hoặc phần mềm, gây ra mất mát dữ liệu và làm gián đoạn hoạt động mạng.

Gây trễ lưu lượng mạng: Tường lửa có thể làm chậm lưu lượng mạng do việc quét, phân tích mỗi gói dữ liệu đi qua, gây ra trễ trong việc truy cập mạng.

Cấu hình không chính xác: Nếu tường lửa được cấu hình không đúng cách, nó có thể chặn các kết nối hợp pháp hoặc cho phép các kết nối không hợp pháp.

Chi phí: Tường lửa có thể tốn nhiều chi phí cho việc triển khai, cấu hình và bảo trì, đặc biệt là trong các doanh nghiệp lớn có nhiều thiết bị mạng.

Không đảm bảo bảo mật tuyệt đối: Mặc dù tường lửa có thể giúp ngăn chặn các cuộc tấn công mạng, nhưng nó không đảm bảo bảo mật tuyệt đối và không thể ngăn chặn mọi cuộc tấn công.

<h1 id="những-tùy-chọn-khi-triển-khai-firewall-mà-bạn-nên-biết">Phần 6: Những tùy chọn khi triển khai Firewall mà bạn nên biết</h1>
<h2 id="stateful-firewall-tường-lửa-có-trạng-thái">6.1. Stateful firewall (Tường lửa có trạng thái)</h2>

Stateful firewall (tường lửa có trạng thái) là một loại tường lửa có khả năng theo dõi trạng thái kết nối mạng trong thời gian thực. Nó giám sát lưu lượng mạng đi qua nó và lưu trữ thông tin về các kết nối mạng đi và đến để xác định xem chúng có hợp lệ hay không.

Tường lửa stateful có thể phân biệt giữa các kết nối được thiết lập (có trạng thái) và các gói tin đơn lẻ (không có trạng thái) và áp dụng các quy tắc bảo mật khác nhau cho chúng.

Tường lửa stateful hoạt động dựa trên việc lưu trữ trạng thái của các kết nối mạng, bao gồm thông tin về địa chỉ IP nguồn và đích, cổng nguồn và đích, giao thức và trạng thái kết nối (đã thiết lập, đang giữ hoặc đã đóng).

Khi một gói tin được gửi đi hoặc nhận về, tường lửa kiểm tra trạng thái kết nối của nó để xác định xem gói tin đó có phải là một phần của một kết nối đã được thiết lập hay không. 

<h2 id="next-generation-firewalls-ngfw-tường-lửa-thế-hệ-tiếp-theo">6.2. Next-generation firewalls – NGFW (Tường lửa thế hệ tiếp theo)</h2>

Next-generation firewalls (NGFW), hay còn gọi là tường lửa thế hệ tiếp theo, là một loại tường lửa kết hợp các tính năng bảo mật mạng cơ bản với những tính năng nâng cao hơn. 

Ví dụ như có thể quản lý ứng dụng, phân tích lưu lượng mạng, phát hiện và phản ứng tấn công cũng như dùng để quản lý chính sách bảo mật.

NGFW có khả năng kiểm soát và giám sát các ứng dụng và dịch vụ mạng, giúp ngăn chặn các cuộc tấn công liên quan đến ứng dụng, như các cuộc tấn công mạng thông qua các ứng dụng web hoặc email.

Nó cũng có khả năng phát hiện và phản ứng các cuộc tấn công mạng bằng cách sử dụng các kỹ thuật như phát hiện xâm nhập (Intrusion Detection System – IDS) và phòng ngừa xâm nhập (Intrusion Prevention System – IPS).

<h2 id="proxy-based-firewall-tường-lửa-dựa-trên-proxy">6.3. Proxy-based firewall (Tường lửa dựa trên proxy)</h2>

Proxy-based firewall (tường lửa dựa trên proxy) là một loại tường lửa sử dụng máy chủ proxy để xử lý các yêu cầu kết nối vào và ra khỏi mạng.

Khi một máy tính trong mạng yêu cầu truy cập một trang web hoặc dịch vụ mạng khác, yêu cầu đó sẽ được gửi đến máy chủ proxy, và máy chủ proxy sẽ thực hiện yêu cầu này thay cho máy tính trong mạng.

Kết quả của yêu cầu sẽ được trả về cho máy chủ proxy, và máy chủ proxy sẽ chuyển kết quả này đến máy tính trong mạng.

Tường lửa dựa trên proxy hoạt động như một trung gian giữa máy tính trong mạng và Internet, giúp che giấu địa chỉ IP của các máy tính trong mạng và bảo vệ chúng khỏi các cuộc tấn công từ Internet.

Nó cũng có khả năng kiểm soát và giám sát lưu lượng mạng, bao gồm quản lý truy cập vào các trang web và các dịch vụ mạng khác.

<h2 id="web-application-firewall-waf-tường-lửa-ứng-dụng-web">6.4. Web application firewall – WAF (Tường lửa ứng dụng web)</h2>

Web Application Firewall (WAF), hay còn gọi là tường lửa ứng dụng web, là một loại tường lửa đặc biệt được thiết kế để bảo vệ các ứng dụng web khỏi các cuộc tấn công mạng.

WAF hoạt động bằng cách giám sát các yêu cầu web đến và đi từ ứng dụng web và kiểm tra chúng xem có chứa các đoạn mã độc, các lỗ hổng bảo mật hay không.

Nếu WAF phát hiện ra một yêu cầu web có chứa các đoạn mã độc hoặc các lỗ hổng bảo mật, nó sẽ chặn yêu cầu đó để bảo vệ ứng dụng web khỏi các cuộc tấn công mạng.

<h2 id="tường-lửa-phần-cứng">6.5. Tường lửa phần cứng</h2>

Tường lửa phần cứng (Hardware Firewall) là một thiết bị tường lửa được cài đặt giữa mạng nội bộ và mạng bên ngoài để giám sát và kiểm soát các lưu lượng mạng.

Thiết bị này được thiết kế để chuyên biệt và cung cấp các tính năng bảo mật mạng cao hơn so với tường lửa phần mềm trên máy tính.

Tường lửa phần cứng có thể được triển khai ở nhiều vị trí, bao gồm trên máy tính cá nhân, trên một máy chủ hoặc trên một mạng lớn. Nó có thể được cấu hình để kiểm soát và giám sát lưu lượng mạng, bao gồm cả kiểm soát truy cập vào các trang web, ứng dụng và dịch vụ mạng khác.

Nó cũng có khả năng ngăn chặn các cuộc tấn công mạng như tấn công từ chối dịch vụ (DoS), tấn công từ chối dịch vụ phân tán (DDoS), tấn công mã độc và tấn công giả mạo địa chỉ IP.

<h2 id="tường-lửa-phần-mềm">6.6. Tường lửa phần mềm</h2>

Tường lửa phần mềm (Software Firewall) là một phần mềm được cài đặt trên máy tính hoặc máy chủ để giám sát và kiểm soát các kết nối mạng đến và đi từ máy tính hoặc máy chủ đó.

Nó hoạt động bằng cách phân tích và kiểm tra các gói tin mạng, đảm bảo rằng các gói tin này tuân theo các quy tắc được cấu hình để bảo vệ máy tính hoặc máy chủ khỏi các cuộc tấn công mạng và các hoạt động độc hại trên mạng.

Tường lửa phần mềm có thể được cài đặt trực tiếp trên máy tính hoặc máy chủ, hoặc được tích hợp sẵn vào các ứng dụng mạng, hệ điều hành, phần mềm antivirus hoặc các giải pháp bảo mật khác.

Nó có thể được cấu hình để kiểm soát truy cập vào các ứng dụng, trang web và dịch vụ mạng khác trên máy tính hoặc máy chủ.

<h2 id="kiểm-tra-trạng-thái-tường-lửa">6.7. Kiểm tra trạng thái tường lửa</h2>

Để kiểm tra trạng thái của tường lửa, bạn có thể sử dụng các công cụ và lệnh cung cấp sẵn trong hệ điều hành hoặc phần mềm tường lửa đang sử dụng.

Nếu bạn đang sử dụng tường lửa phần cứng, bạn có thể truy cập giao diện quản lý của thiết bị để kiểm tra trạng thái của tường lửa.

Thông thường, giao diện quản lý sẽ cung cấp thông tin về các quy tắc bảo mật được cấu hình, các kết nối mạng đang được phép và các hoạt động bảo mật khác.

Nếu bạn đang sử dụng tường lửa phần mềm trên máy tính, bạn có thể sử dụng các lệnh và công cụ như sau:

Windows Firewall: Bạn có thể kiểm tra trạng thái của Windows Firewall bằng cách mở Control Panel, chọn Windows Defender Firewall và kiểm tra trạng thái của tường lửa.

MacOS Firewall: Bạn có thể kiểm tra trạng thái của macOS Firewall bằng cách mở System Preferences, chọn Security & Privacy và chọn tab Firewall.

Linux Firewall: Tùy thuộc vào phiên bản Linux và tường lửa được sử dụng, bạn có thể sử dụng lệnh iptables, ufw hoặc firewalld để kiểm tra trạng thái của tường lửa.

<h2 id="tường-lửa-phát-hiện-và-diệt-virus">6.8. Tường lửa phát hiện và diệt virus</h2>

Tường lửa phát hiện và diệt virus không phải là một khái niệm mới mẻ, mà thực tế nó là sự kết hợp giữa tính năng phòng chống virus của phần mềm diệt virus cùng với tính năng tường lửa phần mềm hoặc phần cứng.

<h2 id="kiểm-tra-tầng-ổ-bảo-mật-ssl">6.9. Kiểm tra tầng ổ bảo mật SSL</h2>

Kiểm tra tầng ổ bảo mật SSL (SSL/TLS Certificate Verification) là quá trình kiểm tra tính hợp lệ và độ an toàn của chứng chỉ SSL/TLS được sử dụng để bảo vệ kết nối truyền thông giữa máy khách và máy chủ trên mạng.

SSL/TLS là một công nghệ mã hóa dữ liệu đang được sử dụng rộng rãi để bảo vệ thông tin nhạy cảm trên mạng, chẳng hạn như thông tin đăng nhập, thông tin tài khoản ngân hàng, thông tin cá nhân và giao dịch trực tuyến.

<h2 id="intrusion-prevention-systems-ips-hệ-thống-phòng-chống-xâm-nhập">6.10. Intrusion Prevention Systems – IPS (Hệ thống phòng chống xâm nhập)</h2>

Intrusion Prevention Systems (IPS) hay còn gọi là Hệ thống phòng chống xâm nhập là một công nghệ bảo mật mạng được sử dụng để phát hiện và ngăn chặn các tấn công mạng từ bên ngoài vào hệ thống mạng của một tổ chức hoặc doanh nghiệp.

IPS thường được triển khai như một phần của hệ thống tường lửa (Firewall), nhưng nó có thể được triển khai như một sản phẩm riêng biệt hoặc một phần của các hệ thống bảo mật mạng khác.

<h2 id="theo-dõi-lưu-lượng-gửi-đi-dpi">6.11. Theo dõi lưu lượng gửi đi (DPI)</h2>

Theo dõi lưu lượng gửi đi (DPI – Deep Packet Inspection) là một kỹ thuật phân tích dữ liệu mạng để phân tích các luồng dữ liệu mạng trong chi tiết cực kỳ cao DPI.

Đây là tính năng thường được sử dụng trong các hệ thống bảo mật mạng và các ứng dụng quản lý mạng để xác định và kiểm soát các giao thức mạng, ứng dụng và nội dung được truyền qua mạng.

DPI hoạt động bằng cách phân tích nội dung của các gói dữ liệu mạng khi chúng đi qua thiết bị phân tích DPI. Các gói dữ liệu này được phân tích để xác định các thông tin về tầng ứng dụng và giao thức mạng được sử dụng. 

Trong đó, bao gồm các thông tin về loại nội dung, địa chỉ IP, cổng và các thông tin khác. Sau đó, các quyết định có thể được đưa ra để kiểm soát hoặc ưu tiên hóa lưu lượng mạng.

<h1 id="những-lỗ-hổng-của-tường-lửa">Phần 7: Những lỗ hổng của tường lửa</h1>

<h2 id="tấn-công-nội-bộ">7.1. Tấn công nội bộ</h2>

Tấn công nội bộ là một trong những lỗ hổng của tường lửa. Điều này đề cập đến khả năng của nhân viên bên trong tổ chức để vượt qua các biện pháp bảo mật và truy cập vào các tài nguyên mạng mà họ không được phép truy cập.

Điều này có thể xảy ra nếu nhân viên bị đánh lừa hoặc bị tấn công bởi phần mềm độc hại hoặc nếu nhân viên là kẻ phản bội.

<h2 id="tấn-công-từ-chối-dịch-vụ-phân-tán-ddos">7.2. Tấn công từ chối dịch vụ phân tán (DDos)</h2>

Tấn công DDoS là một trong những hình thức tấn công phổ biến nhất vào tường lửa. Điều này đề cập đến việc tấn công mạng bằng cách gửi một lượng lớn yêu cầu kết nối đến máy chủ mạng, gây ra tình trạng quá tải và khiến cho máy chủ không thể phản hồi các yêu cầu từ người dùng hợp lệ.

Ngoài ra còn làm ảnh hưởng đến tường lửa không thể hoạt động đúng cách và cho phép tấn công mạng xâm nhập vào hệ thống mạng.

<h2 id="các-phần-mềm-độc-hại">7.3. Các phần mềm độc hại</h2>

Các phần mềm độc hại là một trong những lỗ hổng của tường lửa. Điều này đề cập đến khả năng của phần mềm độc hại để vượt qua tường lửa và truy cập vào các tài nguyên mạng mà nó không được phép truy cập.

Điều này có thể xảy ra nếu phần mềm độc hại được thiết kế để đánh lừa tường lửa hoặc sử dụng các lỗ hổng bảo mật của tường lửa.

<h2 id="cấu-hình-tường-lửa-kém-thiếu-cập-nhật">7.4. Cấu hình tường lửa kém, thiếu cập nhật</h2>

Cấu hình tường lửa kém hoặc thiếu cập nhật là một trong những lỗ hổng của tường lửa. Điều này đề cập đến việc thiết lập tường lửa không đúng cách hoặc không cập nhật các bản vá bảo mật mới nhất.

Điều này có thể khiến cho tường lửa không thể phát hiện và ngăn chặn các cuộc tấn công mới nhất và làm tăng khả năng cho các cuộc tấn công đến hệ thống Internet. 

[Bài viết gốc ở đây](https://vinahost.vn/tuong-lua-la-gi/#ftoc-heading-1)
