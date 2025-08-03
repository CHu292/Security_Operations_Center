# Tcpdump: The Basics

## Mục lục

1. [Task 1: Introduction](#task-1-introduction)
2. [Task 2: Basic Packet Capture](#task-2-basic-packet-capture)
3. [Task 3: Filtering Expressions](#task-3-filtering-expressions)
4. [Task 4: Advanced Filtering](#task-4-advanced-filtering)
5. [Task 5: Displaying Packets](#task-5-displaying-packets)

## Nội dung

# Task 1: Introduction

**Giới thiệu**

Thách thức chính khi nghiên cứu các giao thức mạng là chúng ta không có cơ hội để thấy các “cuộc hội thoại” giao thức diễn ra. Tất cả các phức tạp kỹ thuật đều bị ẩn sau giao diện người dùng thân thiện và thanh lịch. Bạn truy cập tài nguyên trên mạng cục bộ của mình mà không bao giờ thấy một truy vấn ARP. Tương tự, bạn có thể truy cập các dịch vụ Internet trong nhiều năm mà không thấy một cái bắt tay ba bước nào cho đến khi bạn kiểm tra một cuốn sách mạng hoặc kiểm tra một bản ghi lưu lượng mạng. Công cụ học tập tốt nhất là ghi lại lưu lượng mạng và xem xét kỹ hơn các giao thức khác nhau; điều này giúp chúng ta hiểu rõ hơn cách mạng hoạt động.

Phòng này giới thiệu một số đối số dòng lệnh cơ bản để sử dụng Tcpdump. Công cụ Tcpdump và thư viện `libpcap` được viết bằng C và C++ và được phát hành cho các hệ thống giống Unix vào cuối những năm 1980 hoặc đầu những năm 1990. Do đó, chúng rất ổn định và cung cấp tốc độ tối ưu. Thư viện `libpcap` là nền tảng cho nhiều công cụ mạng khác hiện nay. Hơn nữa, nó đã được chuyển sang hệ điều hành MS Windows dưới tên `winpcap`.

**Mục tiêu học tập**

Phòng này nhằm cung cấp cho bạn những kiến thức cơ bản cần thiết để sử dụng `tcpdump`. Cụ thể, bạn sẽ học cách:

* Ghi lại các gói tin và lưu chúng vào một tệp
* Thiết lập bộ lọc trên các gói tin đã ghi lại
* Kiểm soát cách hiển thị các gói tin đã ghi lại

---

# Task 2: Basic Packet Capture
**Ghi lại gói tin cơ bản**

**Tcpdump** là một công cụ để ghi lại các gói tin mạng. Một số lệnh cơ bản để ghi lại các gói tin:

* `tcpdump -i INTERFACE`: Ghi lại các gói tin trên một giao diện mạng được chỉ định (ví dụ: `-i eth0` cho Ethernet hoặc `-i any` cho tất cả các giao diện).

* `tcpdump -w FILE`: Lưu các gói tin đã ghi vào một tệp, thường có phần mở rộng là `.pcap`, để phân tích sau.

* `tcpdump -r FILE`: Đọc và hiển thị các gói tin từ một tệp đã lưu.

* `tcpdump -c COUNT`: Giới hạn việc ghi lại đến một số lượng gói tin nhất định.

* `tcpdump -n` / `-nn`: Tránh phân giải địa chỉ IP và cổng thành tên miền và tên giao thức, giúp đầu ra nhanh hơn và dễ hiểu hơn.

- Ví dụ:

```bash
user@TryHackMe$ sudo tcpdump -i ens5 -c 5 -n
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens5, link-type EN10MB (Ethernet), capture size 262144 bytes
08:55:18.989213 IP 10.10.117.2.22 > 10.11.81.126.53378: Flags [P.], seq 2888580014:2888580210, ack 771262362, win 922, options [nop,nop,TS val 3216251159 ecr 33295823], length 196
08:55:18.989446 IP 10.10.117.2.22 > 10.11.81.126.53378: Flags [P.], seq 196:424, ack 1, win 922, options [nop,nop,TS val 3216251159 ecr 33295823], length 228
08:55:18.989576 IP 10.10.117.2.22 > 10.11.81.126.53378: Flags [P.], seq 424:620, ack 1, win 922, options [nop,nop,TS val 3216251159 ecr 33295823], length 196
08:55:18.989839 IP 10.10.117.2.22 > 10.11.81.126.53378: Flags [P.], seq 620:816, ack 1, win 922, options [nop,nop,TS val 3216251159 ecr 33295823], length 196
08:55:18.989958 IP 10.10.117.2.22 > 10.11.81.126.53378: Flags [P.], seq 816:1012, ack 1, win 922, options [nop,nop,TS val 3216251159 ecr 33295823], length 196
5 packets captured
6 packets received by filter
0 packets dropped by kernel
```

**Xem các ví dụ sau:**

* `tcpdump -i eth0 -c 50 -v` ghi lại và hiển thị 50 gói tin bằng cách lắng nghe trên giao diện `eth0`, là giao diện Ethernet có dây, và hiển thị chi tiết.

* `tcpdump -i wlo1 -w data.pcap` ghi lại các gói tin bằng cách lắng nghe trên giao diện `wlo1` (giao diện WiFi) và ghi các gói tin vào tệp `data.pcap`. Quá trình này sẽ tiếp tục cho đến khi người dùng dừng lại bằng cách nhấn CTRL-C.

* `tcpdump -i any -nn` ghi lại các gói tin trên tất cả các giao diện và hiển thị chúng lên màn hình mà không phân giải tên miền hoặc tên giao thức.


### **Trả lời câu hỏi sau**

**Câu hỏi:**
*Tùy chọn nào bạn có thể thêm vào lệnh để hiển thị địa chỉ chỉ ở định dạng số?*

**Trả lời:** `-n`

---

# Task 3: Filtering Expressions
**Biểu thức lọc**

Để lọc các gói tin dựa trên các tiêu chí như máy chủ, cổng hoặc giao thức:

### **Lọc theo máy chủ (Host Filtering):**

  `tcpdump host HOSTNAME` ghi lại các gói tin có liên quan đến một máy chủ cụ thể.
  Sử dụng `src host HOST` hoặc `dst host HOST` để lọc các gói tin chỉ từ nguồn hoặc chỉ đến đích.

```bash
user@TryHackMe$ sudo tcpdump host example.com -w http.pcap
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
16:49:02.482295 IP 192.168.139.132.49480 > 93.184.215.14.http: Flags [S], seq 3330895816, win 32120, options [mss 1460,sackOK,TS val 621343956 ecr 0,nop,wscale 7], length 0
16:49:02.635087 IP 93.184.215.14.http > 192.168.139.132.49480: Flags [S.], seq 2231582859, ack 3330895817, win 64240, options [mss 1460], length 0
16:49:02.635125 IP 192.168.139.132.49480 > 93.184.215.14.http: Flags [.], ack 1, win 32120, length 0
16:49:02.635491 IP 192.168.139.132.49480 > 93.184.215.14.http: Flags [P.], seq 1:131, ack 1, win 32120, length 130: HTTP: GET / HTTP/1.1
16:49:02.635580 IP 93.184.215.14.http > 192.168.139.132.49480: Flags [.], ack 131, win 64240, length 0
[...]
^C
13 packets captured
25 packets received by filter
0 packets dropped by kernel
```

### **Lọc theo cổng (Port Filtering):**
  `tcpdump port PORT_NUMBER` ghi lại các gói tin trên một cổng cụ thể.
  Sử dụng `src port` hoặc `dst port` để lọc chi tiết hơn theo nguồn hoặc đích.

```bash
user@TryHackMe$ sudo tcpdump -i ens5 port 53 -n
[sudo] password for strategos: 
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
17:26:33.591670 IP 192.168.139.132.47902 > 192.168.139.2.53: 47108+ A? example.org. (29)
17:26:33.591717 IP 192.168.139.132.47902 > 192.168.139.2.53: 5+ AAAA? example.org. (29)
17:26:33.593324 IP 192.168.139.2.53 > 192.168.139.132.47902: 47108 1/0/0 A 93.184.215.14 (45)
17:26:33.593325 IP 192.168.139.2.53 > 192.168.139.132.47902: 5 1/0/0 AAAA 2606:2800:21f:cb07:6820:80da:af6b:8b2c (57)
[...]
^C
12 packets captured
12 packets received by filter
0 packets dropped by kernel
```

### **Lọc theo giao thức (Protocol Filtering):**
  `tcpdump PROTOCOL` lọc các gói tin theo giao thức, như `tcp`, `udp`, `icmp`, v.v.

```bash
user@TryHackMe$ sudo tcpdump -i ens5 icmp -n
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
18:11:00.624681 IP 192.168.139.132 > 93.184.215.14: ICMP echo request, id 47038, seq 1, length 64
18:11:00.781482 IP 93.184.215.14 > 192.168.139.132: ICMP echo reply, id 47038, seq 1, length 64
18:11:04.168792 IP 192.168.139.2 > 192.168.139.132: ICMP time exceeded in-transit, length 68
18:11:04.168815 IP 192.168.139.2 > 192.168.139.132: ICMP time exceeded in-transit, length 68
[...]
18:11:14.857188 IP 93.184.215.14 > 192.168.139.132: ICMP 93.184.215.14 udp port 33495 unreachable, length 68
^C
52 packets captured
52 packets received by filter
0 packets dropped by kernel
```

### **Toán tử logic trong Tcpdump:**

* **and** (`tcpdump host 1.1.1.1 and tcp`): Ghi lại các gói tin khớp với cả hai điều kiện.
* **or** (`tcpdump udp or icmp`): Ghi lại các gói tin khớp với một trong hai điều kiện.
* **not** (`tcpdump not tcp`): Ghi lại tất cả các gói tin ngoại trừ những gói khớp với điều kiện đó.

---

**Xem các ví dụ sau:**

* `tcpdump -i any tcp port 22` lắng nghe trên tất cả giao diện và ghi lại các gói `tcp` từ hoặc đến `port 22`, tức là lưu lượng SSH.

* `tcpdump -i wlo1 udp port 123` lắng nghe trên card mạng WiFi và lọc lưu lượng `udp` đến `port 123`, là giao thức NTP (Network Time Protocol).

* `tcpdump -i eth0 host example.com and tcp port 443 -w https.pcap` sẽ lắng nghe trên `eth0`, giao diện Ethernet có dây, và lọc lưu lượng trao đổi với `example.com` sử dụng `tcp` và `port 443`. Nói cách khác, lệnh này lọc lưu lượng HTTPS liên quan đến `example.com`.

---

### **Lưu ý khi đọc tệp gói tin:**

Chúng ta sẽ đọc các gói tin đã ghi từ tệp `traffic.pcap`. Như đã nói trước đó, dùng tùy chọn `-r FILE` để đọc từ một tệp ghi gói.

Ví dụ để kiểm tra:

```
tcpdump -r traffic.pcap -c 5 -n
```

Câu lệnh này sẽ hiển thị 5 gói đầu tiên trong tệp mà không tra cứu địa chỉ IP.

---

**Mẹo đếm số gói tin:**

Bạn có thể đếm số dòng bằng cách chuyển kết quả qua lệnh `wc`. Trong ví dụ bên dưới, có 910 gói với địa chỉ IP nguồn được đặt là `192.168.124.1`.

Lưu ý cần thêm `-n` để tránh chậm trễ do cố gắng phân giải địa chỉ IP. Trong ví dụ, không dùng `sudo` vì việc đọc tệp `.pcap` không yêu cầu quyền `root`.

```bash
user@TryHackMe$ tcpdump -r traffic.pcap src host 192.168.124.1 -n | wc
reading from file traffic.pcap, link-type EN10MB (Ethernet)
    910   17415  140616
```

### **Trả lời các câu hỏi dưới đây**

---

**Câu hỏi:**

*Có bao nhiêu gói tin trong tệp `traffic.pcap` sử dụng giao thức ICMP?*

**Trả lời:** `26`

```bash
user@ip-10-10-218-40:~$ sudo tcpdump -r traffic.pcap icmp -n | wc
reading from file traffic.pcap, link-type EN10MB (Ethernet)
     26     358    2722
```

---

**Câu hỏi:**

*Địa chỉ IP của máy yêu cầu địa chỉ MAC của 192.168.124.137 là gì?*

**Trả lời:** `192.168.124.148`

```bash
user@ip-10-10-218-40:~$ sudo tcpdump -r traffic.pcap arp and host 192.168.124.137
reading from file traffic.pcap, link-type EN10MB (Ethernet)
07:18:29.940761 ARP, Request who-has ip-192-168-124-137.eu-west-1.compute.internal tell ip-192-168-124-148.eu-west-1.compute.internal, length 28
07:18:29.940776 ARP, Reply ip-192-168-124-137.eu-west-1.compute.internal is-at 52:54:00:23:60:2b (oui Unknown), length 28
```

---

**Câu hỏi:**

*Tên máy chủ (subdomain) nào xuất hiện trong truy vấn DNS đầu tiên?*

**Trả lời:** `mirrors.rockylinux.org`

```bash
user@ip-10-10-218-40:~$ sudo tcpdump -r traffic.pcap port 53 -A
reading from file traffic.pcap, link-type EN10MB (Ethernet)
07:18:24.058626 IP ip-192-168-124-137.eu-west-1.compute.internal.33672 > ip-192-168-124-1.eu-west-1.compute.internal.domain: 39913+ A? mirrors.rockylinux.org. (40)
E..D..@.@.'...|...|....5.0z..............mirrors
rockylinux.org.....
```

# Task 4: Advanced Filtering
**Lọc nâng cao (Advanced Filtering)**

Lọc nâng cao sử dụng các điều kiện để phục vụ các nhu cầu cụ thể hơn:

* **Độ dài gói tin (Packet Length):**
  Sử dụng `greater LENGTH` hoặc `less LENGTH` để ghi lại các gói có độ dài lớn hơn hoặc nhỏ hơn một giá trị xác định.

* **Phép toán nhị phân (Binary Operations):**
  Có thể định nghĩa bộ lọc bằng cách sử dụng các toán tử nhị phân trên tiêu đề giao thức.
  **Ví dụ:**

  * `tcp[tcpflags] == tcp-syn`: Ghi lại các gói chỉ có cờ SYN được bật.
  * `tcp[tcpflags] & tcp-ack != 0`: Ghi lại các gói có ít nhất cờ ACK được bật.

---

Trước khi tiếp tục, bạn nên hiểu về các phép toán nhị phân. Một phép toán nhị phân hoạt động trên các bit – tức là các số 0 và 1. Phép toán có thể lấy một hoặc hai bit làm đầu vào và trả về một bit đầu ra. Dưới đây là ba phép toán nhị phân phổ biến:

* `&` (AND): Trả về 1 chỉ khi cả hai đầu vào đều là 1.
* `|` (OR): Trả về 1 nếu ít nhất một đầu vào là 1.
* `!` (NOT): Đảo ngược giá trị bit (0 thành 1, 1 thành 0).

### **Toán tử nhị phân: & (AND)**

Toán tử `&` nhận hai bit và trả về `0` trừ khi cả hai đầu vào đều là `1`. Bảng dưới minh họa:

| Input 1 | Input 2 | Input 1 & Input 2 |
| ------- | ------- | ----------------- |
| 0       | 0       | 0                 |
| 0       | 1       | 0                 |
| 1       | 0       | 0                 |
| 1       | 1       | 1                 |

---

### **Toán tử nhị phân: | (OR)**

Toán tử `|` nhận hai bit và trả về `1` trừ khi cả hai đầu vào đều là `0`. Bảng dưới minh họa:

| Input 1 | Input 2 | Input 1 \| Input 2 |
| ------- | ------- | ------------------ |
| 0       | 0       | 0                  |
| 0       | 1       | 1                  |
| 1       | 0       | 1                  |
| 1       | 1       | 1                  |


### **Toán tử nhị phân: `!` (NOT)**

Toán tử `!` nhận một bit và đảo ngược nó:

* Nếu đầu vào là `1` → trả về `0`
* Nếu đầu vào là `0` → trả về `1`

Bảng minh họa:

| Input 1 | ! Input 1 |
| ------- | --------- |
| 0       | 1         |
| 1       | 0         |


### **Byte tiêu đề (Header Bytes)**

Mục đích của phần này là để lọc các gói tin dựa trên nội dung của một byte trong phần tiêu đề. Ví dụ: ARP, Ethernet, ICMP, IP, TCP và UDP. Chúng ta sẽ tập trung vào cờ TCP.

---

**Cú pháp bộ lọc trong tcpdump:**

```
proto[expr:size]
```

Giải thích:

* `proto`: chỉ giao thức (ví dụ: `arp`, `ether`, `icmp`, `ip`, `ip6`, `tcp`, `udp`)
* `expr`: vị trí byte (byte offset), bắt đầu từ `0`
* `size`: số byte quan tâm (1, 2 hoặc 4). Có thể bỏ qua, mặc định là 1.

---

**Ví dụ minh họa:**

1. `ether[0] & 1 != 0`:

   * Lấy byte đầu tiên của header Ethernet.
   * So sánh với số 1 (`0000 0001` nhị phân) bằng phép `&` (AND).
   * Nếu kết quả khác 0 → là địa chỉ multicast.
   * Mục đích: hiển thị các gói tin gửi đến địa chỉ multicast.

2. `ip[0] & 0xf != 5`:

   * Lấy byte đầu tiên trong header IP.
   * Áp dụng `&` với `0xf` (hex, tương đương `0000 1111` nhị phân).
   * Kiểm tra nếu kết quả khác `5` (`0000 0101` nhị phân).
   * Mục đích: lọc tất cả các gói IP có chứa tuỳ chọn (options).

Đừng lo nếu bạn thấy hai ví dụ trước đó phức tạp — chúng chỉ nhằm minh họa những gì bạn *có thể* làm. Tuy nhiên, bạn không cần hiểu hoàn toàn chúng để hoàn thành nhiệm vụ. Ở đây, chúng ta sẽ tập trung vào việc lọc các gói TCP dựa trên các cờ (flag) TCP được thiết lập.

Bạn có thể sử dụng `tcp[tcpflags]` để tham chiếu đến trường cờ TCP. Các cờ TCP phổ biến có thể dùng để so sánh bao gồm:

* `tcp-syn`: TCP SYN (Đồng bộ hóa kết nối)
* `tcp-ack`: TCP ACK (Xác nhận)
* `tcp-fin`: TCP FIN (Kết thúc kết nối)
* `tcp-rst`: TCP RST (Thiết lập lại kết nối)
* `tcp-push`: TCP Push (Gửi ngay dữ liệu)

---

**Dựa vào các cờ trên, ta có thể viết:**

* `tcpdump "tcp[tcpflags] == tcp-syn"`
  → Ghi lại các gói TCP chỉ có cờ SYN được bật (tức là thiết lập kết nối), trong khi các cờ khác chưa được bật.

* `tcpdump "tcp[tcpflags] & tcp-syn != 0"`
  → Ghi lại các gói TCP có ít nhất cờ SYN được bật.

* `tcpdump "tcp[tcpflags] & (tcp-syn|tcp-ack) != 0"`
  → Ghi lại các gói TCP có ít nhất một trong hai cờ SYN **hoặc** ACK được bật.

Bạn có thể viết bộ lọc riêng của mình tùy thuộc vào mục đích tìm kiếm.

### **Trả lời các câu hỏi dưới đây**

---

**Câu hỏi:**

*Có bao nhiêu gói tin chỉ có cờ TCP Reset (RST) được bật?*

**Trả lời:** `57`

```bash
user@ip-10-10-218-40:~$ sudo tcpdump -r traffic.pcap 'tcp[tcpflags] == tcp-rst' | wc -l
reading from file traffic.pcap, link-type EN10MB (Ethernet)
57
```

---

**Câu hỏi:**

*Địa chỉ IP của máy đã gửi các gói tin lớn hơn 15000 byte là gì?*

**Trả lời:** `185.117.80.53`

```bash
user@ip-10-10-218-40:~$ sudo tcpdump -r traffic.pcap 'greater 15000' -n
reading from file traffic.pcap, link-type EN10MB (Ethernet)
07:18:24.967023 IP 185.117.80.53.80 > 192.168.124.137.60518: Flags [.], seq 2140876081:2140896901, ack 741991605, win 235, options [nop,nop,TS val 2226566282 ecr 3054280184], length 20820: H
TTP
07:18:25.778012 IP 185.117.80.53.80 > 192.168.124.137.60518: Flags [.], seq 1293616:1308884, ack 1, win 235, options [nop,nop,TS val 2226567095 ecr 3054280994], length 15268: HTTP
07:18:25.861724 IP 185.117.80.53.80 > 192.168.124.137.60518: Flags [.], seq 1378284:1397716, ack 1, win 235, options [nop,nop,TS val 2226567176 ecr 3054281078], length 19432: HTTP
07:18:26.457422 IP 185.117.80.53.80 > 192.168.124.137.60518: Flags [.], seq 2356824:2373480, ack 1, win 235, options [nop,nop,TS val 2226567777 ecr 3054281682], length 16656: HTTP
07:18:26.746414 IP 185.117.80.53.80 > 192.168.124.137.60492: Flags [.], seq 964376218:964395650, ack 1034282473, win 235, options [nop,nop,TS val 2226568063 ecr 3054281963], length 19432: HT
TP
07:18:26.978560 IP 185.117.80.53.80 > 192.168.124.137.60502: Flags [.], seq 3786023752:3786039020, ack 3169565691, win 235, options [nop,nop,TS val 2226568298 ecr 3054282201], length 15268: 
HTTP
07:18:27.195761 IP 185.117.80.53.80 > 192.168.124.137.60492: Flags [.], seq 570468:589900, ack 1, win 235, options [nop,nop,TS val 2226568513 ecr 3054282418], length 19432: HTTP
07:18:27.391916 IP 185.117.80.53.80 > 192.168.124.137.60492: Flags [.], seq 831412:848068, ack 1, win 235, options [nop,nop,TS val 2226568707 ecr 3054282611], length 16656: HTTP
```

# Task 5: Displaying Packets

**Hiển thị gói tin (Displaying Packets)**

Tuỳ chỉnh cách Tcpdump hiển thị gói tin giúp việc phân tích dễ dàng hơn:

* `tcpdump -q`: Hiển thị nhanh với thông tin ngắn gọn.
* `tcpdump -e`: Hiển thị địa chỉ MAC.
* `tcpdump -A`: Hiển thị nội dung gói ở dạng ký tự ASCII.
* `tcpdump -xx`: Hiển thị dữ liệu gói ở định dạng hexa.
* `tcpdump -X`: Hiển thị cả hexa và ASCII.

- Ví dụ:

```bash
user@TryHackMe$ tcpdump -r TwoPackets.pcap -X
reading from file TwoPackets.pcap, link-type EN10MB (Ethernet), snapshot length 262144
18:59:59.979771 IP 104.18.12.149.https > g5000.45248: Flags [P.], seq 2695955324:2695955349, ack 2856007037, win 16, options [nop,nop,TS val 412758285 ecr 3959057198], length 25
        0x0000:  4500 004d fbd8 4000 3506 d229 6812 0c95  E..M..@.5..)h...
        0x0010:  c0a8 4259 01bb b0c0 a0b1 037c aa3b 357d  ..BY.......|.;5}
        0x0020:  8018 0010 f905 0000 0101 080a 189a 310d  ..............1.
        0x0030:  ebfa 6b2e 1703 0300 146a 8f33 1832 e6a2  ..k......j.3.2..
        0x0040:  fb99 eb26 3961 dad4 1611 152d 4c         ...&9a.....-L
18:59:59.980574 IP g5000.45248 > 104.18.12.149.https: Flags [P.], seq 1:30, ack 25, win 2175, options [nop,nop,TS val 3959057384 ecr 412758285], length 29
        0x0000:  4500 0051 6ca8 4000 4006 5656 c0a8 4259  E..Ql.@.@.VV..BY
        0x0010:  6812 0c95 b0c0 01bb aa3b 357d a0b1 0395  h........;5}....
        0x0020:  8018 087f 17e0 0000 0101 080a ebfa 6be8  ..............k.
        0x0030:  189a 310d 1703 0300 18f4 31fa 798d 2656  ..1.......1.y.&V
        0x0040:  433c 2389 5f4a 24c2 fa7a 1496 8444 238e  C<#._J$..z...D#.
        0x0050:  60
```

---

**Trả lời câu hỏi:**

**Câu hỏi:**
*Địa chỉ MAC của máy đã gửi yêu cầu ARP là gì?*
**Trả lời:** `52:54:00:7c:d3:5b`

```bash
user@ip-10-10-218-40:~$ sudo tcpdump -r traffic.pcap arp -e
reading from file traffic.pcap, link-type EN10MB (Ethernet)
07:18:29.940761 52:54:00:7c:d3:5b (oui Unknown) > Broadcast, ethertype ARP (0x0806), length 42: Request who-has ip-192-168-124-137.eu-west-1.compute.internal tell ip-192-168-124-148.eu-west-
1.compute.internal, length 28
07:18:29.940776 52:54:00:23:60:2b (oui Unknown) > 52:54:00:7c:d3:5b (oui Unknown), ethertype ARP (0x0806), length 42: Reply ip-192-168-124-137.eu-west-1.compute.internal is-at 52:54:00:23:60
:2b (oui Unknown), length 28
```

