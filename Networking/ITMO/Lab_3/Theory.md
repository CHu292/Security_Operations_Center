# Nhiệm vụ 4. Cơ bản về quản trị mạng máy tính có định tuyến

## 4.1. Mục tiêu và đặc điểm ngắn gọn của nhiệm vụ

Mục tiêu của nhiệm vụ là nghiên cứu các phương pháp cơ bản để cấu hình mạng máy tính có định tuyến thông qua ví dụ về một mạng gồm các máy tính chạy hệ điều hành Linux.

Trong quá trình thực hiện nhiệm vụ, sẽ nghiên cứu tầng mạng của mô hình OSI. Thực hiện cấu hình cơ bản kết nối trong mạng, quản lý các bảng định tuyến và các quy tắc chuyển đổi địa chỉ mạng. Sử dụng tiện ích *tcpdump* để theo dõi quá trình truyền tải lưu lượng qua các kênh kết nối trong mạng máy tính có định tuyến. 

Việc sử dụng tiện ích *tcpdump* cho phép theo dõi trực tiếp trong terminal (đây là phương pháp quản lý thiết bị mạng cơ bản) các gói dữ liệu đi qua giao diện mạng của máy tính và nghiên cứu lưu lượng nội bộ của mạng.

Trong nhiệm vụ này, sẽ nghiên cứu các phương pháp định tuyến trong các mạng IPv4 và IPv6, cũng như công nghệ NAT vốn phổ biến rộng rãi trong các mạng máy tính.


---

## 4.2. Tham khảo lý thuyết

Quá trình định tuyến gói tin tại mỗi nút mạng máy tính là một quá trình nhiều giai đoạn. Ở mỗi giai đoạn, các điều kiện khác nhau được kiểm tra để xác định các hành động tiếp theo với gói tin được định tuyến.

Trong Linux, quá trình định tuyến được chia thành các giai đoạn sau:
1. **Lọc và xử lý ban đầu** các gói tin được gửi đến bộ định tuyến.
2. **Xác định bảng định tuyến**, nơi sẽ tìm kiếm tuyến đường phù hợp cho gói tin.
3. **Tìm kiếm trong bảng định tuyến** và quyết định cách xử lý gói tin.
4. **Lọc và thay đổi gói tin được định tuyến**, dựa trên thông tin về việc di chuyển gói tin.

Chúng ta sẽ xem xét chi tiết từng giai đoạn này.

---

Mặc định trong Linux tồn tại 3 bảng định tuyến: `local`, `main`, và `default`. Đối với mỗi gói tin, việc tìm kiếm tuyến đường sẽ được thực hiện lần lượt trong từng bảng định tuyến cho đến khi tìm được tuyến đường phù hợp hoặc tất cả các tuyến đường đã được kiểm tra.

- **Bảng `local`** chứa các tuyến đường thuộc về giao diện mạng của bộ định tuyến (ví dụ: địa chỉ multicast, địa chỉ của các mạng con kết nối, hoặc địa chỉ gán cho giao diện của bộ định tuyến). Nếu gói tin phù hợp với một tuyến trong bảng này, nó sẽ được xử lý ở tầng giao thức tiếp theo.

- **Bảng `main`** chứa các tuyến đường chính, được sử dụng để thực hiện định tuyến trên máy tính. Nếu tìm thấy một quy tắc phù hợp, gói tin sẽ được chuyển tiếp qua giao diện mạng tương ứng.

- **Bảng `default`** được sử dụng để chỉ định tuyến đường cho các gói tin không được xử lý trong hai bảng trước đó. Thông thường, bảng này trống.

Nếu không tìm thấy tuyến đường trong bất kỳ bảng nào, gói tin sẽ bị loại bỏ. Trong trường hợp này, một thông báo ICMP về lỗi “Destination host unreachable” sẽ được gửi đến địa chỉ nguồn của gói tin.

Danh sách kiểm tra bảng định tuyến được định nghĩa bằng một tập hợp các quy tắc. Mặc định, tập hợp này trông như sau (lệnh `ip rule list`):
```
0:    from all lookup local
32766: from all lookup main
32767: from all lookup default
```
Tất cả các quy tắc được xử lý theo thứ tự tăng dần của chỉ số. Sau ký hiệu `:` là quy tắc chỉ định hành động cần thực hiện cho gói tin hiện tại. Sau từ khóa `lookup` là bảng định tuyến mà sẽ được tìm kiếm tuyến đường phù hợp cho gói tin hiện tại.

Ví dụ, quy tắc đầu tiên (`from all`) có nghĩa là tất cả các gói tin từ bất kỳ nguồn nào đều được xử lý.

---

Trong quá trình xử lý gói tin qua bộ định tuyến, các bước kiểm tra gói tin được thực hiện tại các giai đoạn khác nhau (định tuyến, chuyển đổi trường dữ liệu, hoặc NAT). Trong thuật ngữ của Linux, các giai đoạn này tương ứng với các bảng sau:

- **Mangle**: Thay đổi các trường như ToS, TTL, hoặc thêm nhãn đặc biệt vào gói tin để sử dụng ở các bảng khác.
- **NAT**: Thực hiện chuyển đổi địa chỉ IP và cổng UDP/TCP.
- **Filter**: Lọc các gói tin (tính năng chính của firewall) để ngăn chặn các gói không mong muốn.
- **Raw** và **Security**: Các bảng này được sử dụng trong các trường hợp cụ thể, không được xem xét ở đây.

---

Trong mỗi bảng, có các chuỗi quy tắc được kích hoạt ở các giai đoạn xử lý gói tin (PREROUTING, INPUT, FORWARD, OUTPUT, POSTROUTING). Theo mặc định, tất cả các bảng đều rỗng, nên cần phải cấu hình các quy tắc để thực hiện hành động cụ thể.

---

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/ITMO/Lab_3/img/4_1.png" alt="Hình 4.1. Sơ đồ đơn giản hóa về quá trình xử lý gói tin qua các chuỗi trong bảng của tường lửa Linux." width="800">
</p>

<p align="center"><b>Hình 4.1. Sơ đồ đơn giản hóa về quá trình xử lý gói tin qua các chuỗi trong bảng của tường lửa Linux.</b></p>

Có thể dường như việc một số bảng (ví dụ: *mangle*) xuất hiện đồng thời trong nhiều chuỗi là dư thừa. Tuy nhiên, sự dư thừa này cho phép linh hoạt đặt quy tắc xử lý gói tin. Ví dụ: nếu thêm quy tắc vào bảng *mangle* trong chuỗi *FORWARD*, quy tắc này sẽ chỉ áp dụng cho các gói tin được chuyển tiếp trong kịch bản 2, nhưng không áp dụng cho các gói tin trong kịch bản 1 và 3. Ngược lại, nếu thêm quy tắc vào chuỗi *POSTROUTING* trong cùng bảng *mangle*, quy tắc đó sẽ được áp dụng cho tất cả gói tin trong kịch bản 2 và 3, nhưng không áp dụng cho kịch bản 1 (điều này được minh họa bằng đường nét đứt trong Hình 4.1). 

Lưu ý rằng trong mỗi kịch bản đều có một chuỗi riêng biệt mà không có ở các chuỗi khác. Điều này cho phép thực hiện logic xử lý độc lập đối với bất kỳ loại gói tin nào trong mỗi kịch bản.

Chữ cái "d" trong ngoặc trước bảng *nat* chỉ ra rằng trong chuỗi tương ứng trong khuôn khổ công nghệ NAT, việc thay đổi chỉ áp dụng cho địa chỉ đích (*destination*). Điều này được giải thích bởi thực tế là thay đổi địa chỉ đích là cần thiết để tìm tuyến đường trong quá trình truyền tải (tên chuỗi *PREROUTING* được hiểu theo nghĩa đen là "trước định tuyến"). Tương tự, chữ "s" trong ngoặc chỉ ra rằng trong bảng tương ứng, chỉ cần thay đổi địa chỉ nguồn (*source*).


---

Dưới đây là bản dịch chính xác và đầy đủ nội dung từ hình ảnh:

---

## 4.3. Các giai đoạn thực hiện công việc

### Giai đoạn 1. Cấu hình máy ảo

Để thực hiện bài tập, cần cài đặt chương trình miễn phí **Oracle VirtualBox** trên máy tính. Đây là một môi trường ảo hóa cho phép khởi chạy các máy ảo và kết nối chúng trong các mạng máy tính cách ly. Bạn có thể tải VirtualBox từ trang web chính thức:  
[https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads).

Trong công việc này, hệ điều hành Linux được khuyến nghị là **Ubuntu 14.04.5 Server**, có thể tải từ liên kết:  
[http://mirror.yandex.ru/ubuntu-releases/14.04.5/ubuntu-14.04.5-server-amd64.iso](http://mirror.yandex.ru/ubuntu-releases/14.04.5/ubuntu-14.04.5-server-amd64.iso)  
(hoặc sử dụng liên kết rút gọn: [https://goo.gl/y3ueas](https://goo.gl/y3ueas)).

Khi cấu hình từng máy ảo, cần phân bổ ít nhất 400 MB bộ nhớ RAM và 8 GB không gian đĩa.

Cần tạo số lượng máy ảo đủ để thực hiện bài tập theo yêu cầu. Kết nối giữa các máy ảo trong mạng cục bộ theo đúng mô hình được chỉ định sẽ được thực hiện bằng cách sử dụng bộ điều hợp mạng bên trong (Hình 4.2).

Nếu theo mô hình, các máy ảo cần được kết nối với mạng bên ngoài (Internet), thì cần phải gán các bộ điều hợp mạng phù hợp (như được chỉ định trong Hình 4.2) và thực hiện cấu hình tương ứng với các địa chỉ IP, mặt nạ mạng, và địa chỉ MAC trong phạm vi bài tập.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/ITMO/Lab_3/img/4_2.png" alt="Hình 4.2. Cấu hình mạng nội bộ cho bộ điều hợp mạng." width="800">
</p>

<p align="center"><b>Hình 4.2. Cấu hình mạng nội bộ cho bộ điều hợp mạng.</b></p>



### Giai đoạn 2. Làm quen với các lệnh Linux được sử dụng

Dưới đây là các lệnh Linux có thể hữu ích cho nhiệm vụ. Các lệnh được đánh dấu bằng `>` thực hiện trong dòng lệnh, còn `#` là chú thích giải thích ý nghĩa lệnh. Một số lệnh yêu cầu quyền quản trị (root).

- Hiển thị danh sách giao diện và địa chỉ IP:
  ```
  > ip a  # hiển thị danh sách giao diện và địa chỉ
  ```

- Bật/tắt giao diện mạng:
  ```
  > ip link set <tên_giao_diện> up  # bật giao diện
  > ip link set <tên_giao_diện> down  # tắt giao diện
  ```

Ở đây, `<tên_giao_diện>` là chuỗi như "ethN", trong đó `N` là số nguyên (bao gồm cả 0). Ví dụ các giao diện `eth1`, `eth2` được minh họa trong Hình 4.3.

Giao diện có tên `lo` (vòng lặp cục bộ) dùng để gán địa chỉ IP duy nhất cho một máy tính để nhận dạng. Nếu một máy tính có nhiều giao diện, địa chỉ IP gán cho vòng lặp cục bộ có thể được sử dụng như một địa chỉ chung để truy cập từ các mạng con khác nhau.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/ITMO/Lab_3/img/4_3.png" alt="Hình 4.3. Ví dụ về đầu ra của lệnh ip a" width="800">
</p>

<p align="center"><b>Hình 4.3. Ví dụ về đầu ra của lệnh ip a</b></p>

---

#### **Gán và xóa địa chỉ IP**

- Gán địa chỉ IP với mặt nạ cho giao diện:
  ```
  > ip a add <ip-address/mask> dev <tên_giao_diện>  # gán địa chỉ IP với mặt nạ
  ```

- Xóa địa chỉ IP khỏi giao diện:
  ```
  > ip a del <ip-address/mask> dev <tên_giao_diện>  # xóa địa chỉ IP khỏi giao diện
  ```

- Hiển thị bảng định tuyến:
  ```
  > ip ro  # hiển thị bảng định tuyến
  ```

Khi một địa chỉ IP được gán cho giao diện, tuyến đường tương ứng tự động được thêm vào bảng định tuyến (Hình 4.4).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/ITMO/Lab_3/img/4_4.png" alt="Hình 4.4. Ví dụ về đầu ra của lệnh ip ro" width="800">
</p>

<p align="center"><b>Hình 4.4. Ví dụ về đầu ra của lệnh ip ro</b></p>

---

 **Cấu hình bảng định tuyến**

- Thêm tuyến đường đến mạng/host qua gateway:
  ```
  > ip ro add <dest_ip/mask> via <gateway_ip>  # thêm tuyến đường
  ```

- Xóa tuyến đường:
  ```
  > ip ro del <dest_ip/mask> via <gateway_ip>  # xóa tuyến đường
  ```

- Thêm tuyến đường vào bảng cụ thể:
  ```
  > ip ro add <dest_ip/mask> via <gateway_ip> table <số_bảng>
  ```

- Hiển thị bảng định tuyến với số bảng cụ thể:
  ```
  > ip ro list table <số_bảng>  # hiển thị bảng định tuyến
  ```

- Định tuyến cân bằng tải:
  ```
  > ip ro add <dest_ip/mask> nexthop via <gateway_ip1> weight <weight_1> nexthop via <gateway_ip2> weight <weight_2> nexthop via <gateway_ip3> weight <weight_3>
  ```

Ở đây, `gateway_ip_1`, `gateway_ip_2`, `gateway_ip_3` là các địa chỉ IP của gateway; `weight_1`, `weight_2`, `weight_3` là trọng số tương ứng với từng gateway: trọng số càng lớn, xác suất chọn gateway cụ thể để chuyển tiếp gói tin càng cao. 

Trong ví dụ này, xác suất chọn `gateway_ip_1` sẽ bằng:

```
weight_1 / (weight_1 + weight_2 + weight_3)
```


---

- **Hiển thị các quy tắc lựa chọn bảng định tuyến**:  
  ```
  > ip rule # hiển thị các quy tắc lựa chọn bảng định tuyến
  ```

- **Thêm quy tắc định tuyến**:  
  ```
  > ip rule add prio <rule_number> from <src_ip/mask> lookup <table_number>
  ```  
  Lệnh này thêm quy tắc, trong đó việc lựa chọn bảng định tuyến cho gói tin được xác định dựa trên địa chỉ nguồn. Phương pháp này gọi là *Policy-Based Routing* (PBR), khác với định tuyến thông thường chỉ sử dụng địa chỉ đích để đưa ra quyết định.

  Ở đây:  
  - `rule_number`: số thứ tự của quy tắc trong danh sách.  
  - `src_ip/mask`: địa chỉ mạng nguồn của gói tin.  
  - `table_number`: số hiệu của bảng định tuyến mà gói tin sẽ được tìm kiếm nếu thuộc phạm vi `src_ip/mask`.

---

- **Kiểm tra kết nối với IPv6 bằng ICMP Echo Request**:  
  Để kiểm tra kết nối IPv6, sử dụng lệnh `ping6`. Ví dụ:  
  ```
  > ping6 -I 192.168.1.101
  ```  
  Trong lệnh trên, tham số `-I` yêu cầu chỉ định địa chỉ nguồn trong gói tin ICMP.

---

- **Cấu hình địa chỉ IPv6**:  
  Để gán địa chỉ IPv6 và định tuyến, thêm tham số `-6` vào lệnh. Ví dụ:  
  ```
  > ip -6 a add 2000::1/64 dev eth0
  > ip -6 ro add 2001::/64 via 2000::2
  ```


Tiếp theo là tập hợp các lệnh để quản lý tường lửa netfilter trong hệ điều hành Linux bằng tiện ích `iptables`:

- **Hiển thị các quy tắc trong bảng lọc (filter):**
  ```
  > iptables -nvL  # hiển thị các quy tắc trong bảng lọc
  ```

- **Hiển thị các quy tắc trong bảng NAT:**
  ```
  > iptables -nvL -t nat  # hiển thị các quy tắc trong bảng NAT
  ```

- **Hiển thị các quy tắc lọc với số thứ tự:**
  ```
  > iptables -nvL --line-numbers  # hiển thị các quy tắc với số thứ tự
  ```

- **Thêm quy tắc vào chuỗi trong bảng lọc:**
  ```
  > iptables -A <tên_chuỗi> <tham_số_lọc> -j <hành_động>
  ```

- **Thêm quy tắc vào bảng NAT:**
  ```
  > iptables -t nat -A <tên_chuỗi> <tham_số_lọc> -j <hành_động>
  ```

Trong đó:
- `<tên_chuỗi>`:
  - Đối với bảng `filter`, có thể là `INPUT`, `OUTPUT`, `FORWARD`.
  - Đối với bảng `nat`, có thể là `PREROUTING`, `INPUT`, `OUTPUT`, `POSTROUTING`.

- `<tham_số_lọc>`: Xác định tập hợp các điều kiện để kiểm tra gói tin.

- `<hành_động>`: Quy định hành động cần thực hiện với các gói tin phù hợp với quy tắc.

---

Dưới đây là phần dịch chính xác nội dung từ ảnh:

---

**Lưu ý 1.**  
Mặc định trong Linux, tính năng định tuyến gói tin bị tắt. Do đó, để cho phép gói tin đi qua máy tính trong mạng (chuyển tiếp gói tin), cần bật chế độ định tuyến.  

Đối với IPv4, bạn có thể thực hiện điều này bằng cách chạy một trong hai lệnh sau:  
```
> sysctl -w net.ipv4.ip_forward=1
```
Hoặc:  
```
> echo 1 > /proc/sys/net/ipv4/ip_forward
```


---

**Lưu ý 2.**  
Một số loại tấn công mạng dựa trên việc giả mạo địa chỉ nguồn trong gói tin. Do đó, mặc định trong Linux, các gói tin có địa chỉ nguồn không hợp lệ qua giao diện mà gói tin đến sẽ bị loại bỏ. Để kiểm tra tính hợp lệ của địa chỉ, bảng định tuyến được sử dụng.

Trong một số phiên bản Linux, quy tắc này có thể được nới lỏng: gói tin sẽ không bị loại bỏ nếu địa chỉ nguồn hợp lệ qua bất kỳ giao diện nào của máy tính (không chỉ qua giao diện mà gói tin đến).

Để thực hiện một số bài tập, cần tắt tính năng bảo vệ này trong Linux. Đối với IPv4, bạn có thể thực hiện bằng các lệnh sau:  
```
sysctl -w net.ipv4.conf.all.rp_filter=0
```
Hoặc:  
```
echo 0 > /proc/sys/net/ipv4/conf/all/rp_filter
```

---


### **Giai đoạn 3. Thực hiện phần chung của nhiệm vụ**

Bật chế độ định tuyến trên mỗi máy tính trong mạng. Cấu hình các giao diện mạng của tất cả các máy tính trong mạng. Cấu hình bảng định tuyến sao cho mỗi máy tính có thể giao tiếp với bất kỳ máy tính nào khác.  

Mô hình mạng cần được lựa chọn theo kịch bản V1 (công thức tính cho V1 được đưa ra ở Mục 4.4). Sự tương tác giữa các máy tính cần được thực hiện phù hợp với định tuyến của kịch bản này.  

Thiết lập các quy tắc lọc đơn giản để chặn các gói tin không mong muốn. Kiểm tra kết nối giữa các thiết bị bằng cách sử dụng tiện ích `ping`, và kiểm tra tính chính xác của định tuyến bằng công cụ `tracert`.

---

### **Giai đoạn 4. Thực hiện nhiệm vụ theo kịch bản**

Thực hiện phần chung của nhiệm vụ sẽ giúp đạt được điểm 3E. Để đạt điểm cao hơn (từ 3D đến 5A), cần hoàn thành thêm một nhiệm vụ cá nhân theo bảng 4.1.  

Công thức tính cho kịch bản V1 và V2 được đưa ra trong Mục 4.4. Cần đảm bảo rằng hệ thống hoạt động theo sơ đồ được mô tả trong kịch bản bài tập.

---
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/ITMO/Lab_3/img/4_5.png" alt="bảng 4.1" width="800">
</p>

<p align="center"><b>Bảng 4.1</b></p>


---

### **4.4. Trình tự thực hiện nhiệm vụ**

1. **Chọn kịch bản thực hiện nhiệm vụ theo công thức**:
   - V1 = 1 + (N mod 5), V2 = 6 + (N mod 5),  
   trong đó V1 và V2 là số của kịch bản; N = tổng số chữ cái trong họ và tên của sinh viên; mod = phép lấy phần dư khi chia.

2. **Cấu hình địa chỉ IP và IPv6 (nếu cần)**:  
   Trên tất cả các giao diện của các máy tính trong mô hình được chỉ định, thiết lập địa chỉ IP theo định dạng:  
   ```
   A.B.X.Y/M
   ```
   trong đó:  
   - `A` = số chữ cái trong tên;  
   - `B` = số chữ cái trong họ;  
   - `X, Y` = các số do sinh viên tự chọn;  
   - `M` = mặt nạ mạng (chọn mặt nạ tối đa để đảm bảo kết nối).  

   Địa chỉ IPv6 được tạo từ địa chỉ IPv4 theo ký hiệu chuyển đổi IPv4 sang IPv6. Ví dụ:  
   - IPv4: 10.10.12.11  
   - IPv6: 0:0:0:0:0:ffff:0a0c:b (hoặc viết tắt: `::ffff:10.10.12.11`).

3. **Cấu hình bảng định tuyến**:  
   Trên tất cả các máy tính, thiết lập bảng định tuyến sao cho đảm bảo mạng hoàn toàn khả dụng (mỗi máy tính phải có khả năng `ping` được bất kỳ máy tính nào khác).

4. **Nghiên cứu tiện ích Linux `nc` (hoặc các tương tự như: netcat, ncat, pnetcat)**:  
   - Khởi chạy tiện ích ở chế độ máy khách trên máy tính A và ở chế độ máy chủ trên máy tính B, sử dụng cổng bất kỳ (hai máy tính A và B phải ở cách xa nhau nhất có thể).  
   - Truyền một thông điệp dạng văn bản ghi tên mình từ máy tính B đến máy tính A.

5. **Thiết lập các quy tắc lọc với tiện ích iptables**:
   - Cấm chuyển tiếp các gói tin TCP chỉ định cổng trong cấu hình tiện ích `nc`.  
   - Cấm nhận các gói tin UDP gửi đến từ cổng được chỉ định.  
   - Cấm chuyển tiếp các gói tin được gửi từ địa chỉ IP của máy tính A.  
   - Cấm nhận các gói tin được gửi đến địa chỉ IP của máy tính B.  
   - Cấm nhận và gửi các gói ICMP có kích thước lớn hơn 1000 byte, với trường TTL nhỏ hơn 10.

6. **Kiểm tra hoạt động của các quy tắc lọc**:  
   Sử dụng các lệnh `ping`, `traceroute`, hoặc `nc` để đảm bảo rằng các quy tắc lọc được cấu hình trong iptables hoạt động đúng cách. Thử gửi gói tin bị cấm trước, sau đó gửi gói tin được phép.

7. **Hoàn thành các bước từ 1 đến 6 để đạt được điểm 3E**:  
   Để đạt được điểm cao hơn, cần thực hiện thêm các nhiệm vụ bổ sung theo các kịch bản V1 và V2 (xem Bảng 4.1). Các nhiệm vụ bổ sung có thể yêu cầu thay đổi cấu hình được thực hiện ở các bước từ 2 đến 6.

---

