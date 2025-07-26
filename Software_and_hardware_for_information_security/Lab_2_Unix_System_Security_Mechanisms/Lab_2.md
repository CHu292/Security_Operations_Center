
**Mục tiêu của công việc** – làm quen với các mô-đun bảo vệ cơ bản của hệ thống Unix. Để đạt được mục tiêu này, cần phải giải quyết các nhiệm vụ sau:

- Xác định bản phân phối;
- Xác định hệ thống mà điểm cuối cần bảo vệ đang nằm trên đó;
- Xác định các yêu cầu bảo vệ thông qua cơ sở quy chuẩn;
- Thực hiện cấu hình hệ thống Unix theo các yêu cầu của cơ quan quản lý.

---

### 1. XÁC ĐỊNH BẢN PHÂN PHỐI VÀ HỆ THỐNG THÔNG TIN
**Phiên bản được chọn** – 11  
**Bản phân phối** – Debian  
**Hệ thống thông tin** – AS 2B  

#### 1.1 Debian

**Debian** là một bản phân phối Linux mã nguồn mở phổ biến và được sử dụng rộng rãi. Đây là nền tảng cho nhiều bản phân phối Linux khác, như Ubuntu và Linux Mint. Những đặc điểm chính của Debian bao gồm:

- **Hệ thống quản lý gói**: Debian sử dụng Advanced Package Tool (APT) và các gói định dạng .deb để cài đặt và quản lý phần mềm. Điều này giúp đơn giản hóa việc cài đặt, cập nhật và gỡ bỏ phần mềm chỉ với các lệnh đơn giản.

- **Phần mềm tự do và mã nguồn mở**: Debian tập trung vào việc sử dụng phần mềm tự do và mã nguồn mở, lý tưởng cho những người dùng coi trọng tự do phần mềm và tính minh bạch của mã nguồn.

- **Ổn định và đáng tin cậy**: Debian nổi tiếng với tính ổn định. Nó có ba nhánh chính: *stable* (ổn định), *testing* (kiểm thử) và *unstable* (không ổn định). Nhánh stable được kiểm tra kỹ lưỡng và được coi là sẵn sàng sử dụng trên các hệ thống sản xuất, trong khi nhánh testing và unstable có các phiên bản phần mềm mới hơn nhưng có thể kém ổn định hơn.

- **Phát triển do cộng đồng quản lý**: Debian được phát triển và duy trì bởi một cộng đồng tình nguyện viên toàn cầu. Các quyết định và cải tiến được thực hiện thông qua một quy trình dân chủ trong khuôn khổ dự án Debian.

- **Tính đa dụng**: Debian có thể được sử dụng làm hệ điều hành máy tính để bàn, hệ thống máy chủ, hoặc nhúng vào các thiết bị. Nó hỗ trợ nhiều kiến trúc phần cứng khác nhau, bao gồm x86, ARM và nhiều kiến trúc khác.

#### 1.2 Hệ thống AS 2B

**Hệ thống tự động hóa (AS)** là một hệ thống bao gồm nhân sự và tổ hợp các phương tiện tự động hóa, nhằm hỗ trợ và tối ưu hóa hoạt động của họ. Hệ thống này triển khai các công nghệ thông tin để thực hiện những chức năng xác định từ trước.

**Hệ thống tự động hóa loại 2B** có đặc điểm là tất cả người dùng đều có quyền truy cập ngang hàng đến toàn bộ thông tin được lưu trữ hoặc xử lý trong hệ thống, bất kể mức độ bảo mật của dữ liệu. Điều này có nghĩa là mỗi người dùng đều có quyền xem và thay đổi bất kỳ dữ liệu nào, bao gồm cả thông tin nhạy cảm như bí mật công vụ hoặc dữ liệu cá nhân.

### 2. YÊU CẦU BẢO VỆ HỆ THỐNG TỰ ĐỘNG HÓA LOẠI 2B
Theo tài liệu hướng dẫn của FSTEK ngày 30 tháng 3 năm 1992:

Phân loại này áp dụng cho tất cả các hệ thống tự động hóa (AS) hiện hành và đang được thiết kế tại các cơ quan, tổ chức, và doanh nghiệp xử lý thông tin bí mật.

Việc phân chia các AS thành các lớp theo điều kiện hoạt động về khía cạnh bảo vệ thông tin là cần thiết để xây dựng các biện pháp phù hợp nhằm đạt được mức độ bảo vệ thông tin yêu cầu.

Phương pháp tiếp cận khác biệt trong việc lựa chọn các phương pháp và công cụ bảo vệ được xác định bởi tầm quan trọng của thông tin được xử lý, sự khác biệt giữa các AS về thành phần, cấu trúc, cách thức xử lý thông tin, và thành phần người dùng và nhân viên hỗ trợ.

#### 1.4. Các bước chính trong phân loại AS bao gồm:
- Phát triển và phân tích dữ liệu cơ bản;
- Xác định các đặc điểm chính của AS cần thiết cho phân loại;
- So sánh các đặc điểm được xác định của AS với các tiêu chí phân loại;
- Gán cho AS lớp bảo vệ thông tin thích hợp chống truy cập trái phép (NSD).

#### 1.5. Dữ liệu cơ bản cần thiết để phân loại AS cụ thể bao gồm:
- Danh sách các tài nguyên thông tin được bảo vệ của AS và mức độ bảo mật của chúng;
- Danh sách những người có quyền truy cập vào các phương tiện của AS, kèm theo mức độ quyền hạn của họ;
- Ma trận quyền truy cập hoặc quyền hạn của các chủ thể truy cập đối với các tài nguyên thông tin được bảo vệ của AS.

#### 1.6. Việc lựa chọn lớp của AS do khách hàng và nhà phát triển cùng thực hiện, với sự tham gia của các chuyên gia bảo vệ thông tin.

#### 1.7. Các đặc điểm xác định để phân nhóm AS thành các lớp khác nhau bao gồm:
- Sự hiện diện của thông tin với mức độ bảo mật khác nhau trong AS;
- Mức độ quyền hạn của các chủ thể truy cập AS đối với thông tin bảo mật;
- Chế độ xử lý dữ liệu trong AS – tập thể hoặc cá nhân.

#### 1.8. Có tổng cộng chín lớp bảo vệ AS khỏi NSD đối với thông tin. Mỗi lớp có một tập hợp các yêu cầu tối thiểu về bảo vệ cụ thể.

Các lớp được chia thành ba nhóm, khác nhau về cách thức xử lý thông tin trong AS. Trong mỗi nhóm, có một hệ thống phân cấp các yêu cầu bảo vệ tùy theo giá trị (mức độ bảo mật) của thông tin và do đó là hệ thống phân cấp các lớp bảo vệ của AS.

- **Nhóm thứ ba** bao gồm các AS có một người dùng duy nhất, có quyền truy cập vào tất cả thông tin của AS, được lưu trữ trên các thiết bị có cùng một mức bảo mật. Nhóm này có hai lớp – 3B và 3A.

- **Nhóm thứ hai** bao gồm các AS trong đó người dùng có quyền truy cập giống nhau (quyền hạn) đối với toàn bộ thông tin của AS, được xử lý và/hoặc lưu trữ trên các thiết bị có mức độ bảo mật khác nhau. Nhóm này có hai lớp – 2B và 2A.

- **Nhóm thứ nhất** bao gồm các AS đa người dùng, trong đó thông tin với các mức độ bảo mật khác nhau được xử lý và/hoặc lưu trữ đồng thời. Không phải tất cả người dùng đều có quyền truy cập vào toàn bộ thông tin của AS. Nhóm này có năm lớp – 1D, 1G, 1V, 1B, và 1A.



**Các mức độ bảo mật:**
- **NC**: Thông tin không bảo mật
- **C**: Thông tin bảo mật
- **CC**: Thông tin tuyệt mật
- **OB**: Thông tin đặc biệt quan trọng


### 2. Yêu cầu bảo vệ thông tin khỏi truy cập trái phép cho Hệ thống Tự động hóa (АС)

#### 2.1 Bảo vệ thông tin khỏi truy cập trái phép là một phần của vấn đề đảm bảo an toàn thông tin tổng thể. Các biện pháp bảo vệ thông tin khỏi truy cập trái phép cần được thực hiện đồng bộ với các biện pháp bảo vệ chuyên biệt cho các phương tiện máy tính chính và phụ, các phương tiện và hệ thống liên lạc khỏi các công cụ gián điệp kỹ thuật và gián điệp công nghiệp.

#### 2.2 Trong trường hợp chung, hệ thống tích hợp các phương tiện kỹ thuật và tổ chức (quy trình) để bảo vệ thông tin khỏi truy cập trái phép được thực hiện trong khuôn khổ **Hệ thống bảo vệ thông tin khỏi truy cập trái phép**, bao gồm bốn phân hệ sau:
- **Quản lý truy cập**;
- **Đăng ký và ghi nhận**;
- **Mã hóa**;
- **Đảm bảo tính toàn vẹn**.

#### 2.3 Yêu cầu đối với lớp bảo vệ 2B:

- **Phân hệ quản lý truy cập**: Phải thực hiện nhận dạng và xác thực các chủ thể truy cập khi đăng nhập vào hệ thống bằng mã nhận dạng và mật khẩu có độ dài tối thiểu sáu ký tự chữ và số.

- **Phân hệ đăng ký và ghi nhận**: Phải thực hiện đăng ký việc truy cập (đăng nhập/đăng xuất) của các chủ thể truy cập vào/ra khỏi hệ thống, hoặc đăng ký việc khởi động và khởi tạo hệ điều hành và dừng hoạt động của hệ thống. Việc đăng ký đăng xuất hoặc dừng hệ thống không thực hiện khi hệ thống bị tắt nguồn. Các thông tin đăng ký bao gồm:
  - Ngày và giờ đăng nhập (đăng xuất) của chủ thể truy cập hoặc khởi động (dừng) hệ thống;
  - Kết quả thử đăng nhập: thành công hoặc không thành công (khi có truy cập trái phép);
  - Phải theo dõi tất cả các phương tiện lưu trữ thông tin được bảo vệ bằng cách đánh dấu chúng và ghi dữ liệu đăng ký vào sổ theo dõi (hoặc thẻ đăng ký).

- **Phân hệ đảm bảo tính toàn vẹn**: Phải đảm bảo tính toàn vẹn của phần mềm trong Hệ thống bảo vệ thông tin khỏi truy cập trái phép, thông tin được xử lý, và tính bất biến của môi trường phần mềm. Cụ thể:
  - Kiểm tra tính toàn vẹn của Hệ thống bảo vệ thông tin khỏi truy cập trái phép khi hệ thống khởi động bằng cách xác minh tên (nhận dạng) của các thành phần hệ thống bảo vệ;
  - Tính toàn vẹn của môi trường phần mềm được đảm bảo bằng việc không có công cụ phát triển và gỡ lỗi phần mềm trong hệ thống trong khi xử lý hoặc lưu trữ thông tin được bảo vệ;
  - Phải thực hiện bảo vệ vật lý đối với các thiết bị và phương tiện lưu trữ thông tin, bao gồm kiểm soát truy cập vào khu vực hệ thống và sự hiện diện của các rào cản đáng tin cậy để ngăn chặn truy cập trái phép vào các khu vực này, đặc biệt là ngoài giờ làm việc;
  - Thực hiện kiểm tra định kỳ các chức năng của Hệ thống bảo vệ thông tin khỏi truy cập trái phép khi có thay đổi trong môi trường phần mềm và nhân sự của hệ thống thông qua các chương trình kiểm tra mô phỏng các nỗ lực truy cập trái phép;
  - Phải có phương tiện phục hồi Hệ thống bảo vệ thông tin khỏi truy cập trái phép, bao gồm duy trì hai bản sao phần mềm của hệ thống và định kỳ cập nhật, kiểm tra khả năng hoạt động của chúng.

### 3. Cấu hình Debian theo yêu cầu của cơ quan quản lý

#### 3.1 Cấu hình phân hệ quản lý truy cập

Đầu tiên, chúng ta tạo một người dùng mới (Hình 2).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/2.png" alt="" width="1000">
</p>
<p align="center"><b>Hình 2 – Tạo người dùng mới</b></p>


Sau đó, thực hiện nhận dạng và xác thực các chủ thể truy cập khi đăng nhập vào hệ thống bằng mã nhận dạng và mật khẩu cố định, gồm ít nhất 8 ký tự và bao gồm ít nhất 3 loại ký tự khác nhau (Hình 3).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/3.png" alt="" width="800">
</p>
<p align="center"><b></b></p>

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/3.1.png" alt="" width="800">
</p>
<p align="center"><b>Hình 3 – Quy tắc đặt mật khẩu</b></p>

Tiếp theo, kiểm tra các quy tắc đặt mật khẩu. Chúng ta thấy rằng nếu mật khẩu có ít hơn 12 ký tự hoặc bao gồm ít hơn 3 loại ký tự, thì mật khẩu được coi là không hợp lệ và chúng ta không thể thay đổi mật khẩu (Hình 4).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/4.png" alt="" width="800">
</p>
<p align="center"><b>Hình 4 – Kiểm tra quy tắc đặt mật khẩu</b></p>


### 3.2 Cấu hình hệ thống ghi nhật ký và kiểm toán

Tất cả các tệp nhật ký có thể được phân loại vào một trong các nhóm sau:
- ứng dụng;
- sự kiện;
- dịch vụ;
- hệ thống.

Hầu hết các tệp nhật ký đều nằm trong thư mục `/var/log`:
- `/var/log/syslog` hoặc `/var/log/messages` — chứa nhật ký hệ thống toàn cục, ghi lại các thông báo từ lúc hệ thống khởi động, bao gồm thông tin từ kernel của Linux, các dịch vụ khác nhau, thiết bị được phát hiện, các giao diện mạng, và nhiều thông tin khác.
- `/var/log/auth.log` hoặc `/var/log/secure` — chứa thông tin về việc xác thực người dùng, bao gồm các lần đăng nhập thành công và thất bại, cùng các cơ chế xác thực được sử dụng.
- `/var/log/dmesg` — chứa nhật ký của các trình điều khiển thiết bị. Có thể sử dụng lệnh cùng tên để xem nội dung của tệp này. Dung lượng của nhật ký có giới hạn; khi tệp đạt đến mức tối đa, các thông báo cũ sẽ bị ghi đè bởi các thông báo mới. Thêm tùy chọn `--level=` để lọc đầu ra theo mức độ quan trọng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/5.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 5** – Danh sách các bản ghi về các sự kiện hệ thống và ứng dụng khác nhau </b></p>



<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/6.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 6** – Nhật ký đăng nhập và đăng xuất của người dùng  </b></p>


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/7.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 7** – Nhật ký các lần đăng nhập không thành công  </b></p>

Lệnh `dmesg` được sử dụng để hiển thị các thông báo của kernel trong các hệ điều hành tương tự Unix, bao gồm Debian. Để tìm kiếm thông tin liên quan đến một thiết bị cụ thể, chẳng hạn như ổ đĩa cứng được xác định là "sda", chúng ta có thể sử dụng lệnh `dmesg` kết hợp với `grep`.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/8.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 8** – Nhật ký phương tiện thông tin  </b></p>

### 3.3 Cấu hình hệ thống bảo đảm tính toàn vẹn

Chúng tôi đã chọn phần mềm chống virus miễn phí ClamAV làm hệ thống bảo đảm an ninh thông tin (СЗИ). Các tệp cấu hình của ClamAV nằm trong đường dẫn `/etc/clamav/clamd.conf` và `/etc/clamav/freshclam.conf`. Để kiểm tra tính toàn vẹn của các tệp cấu hình, chúng tôi sử dụng hàm băm `sha256`. Giá trị của hàm băm được hiển thị ở **Hình 9**.

Cài đặt clamav:
```bash
sudo apt install clamav clamav-daemon
```
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/9.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 9** – Kiểm tra tính toàn vẹn của tệp trước khi thay đổi</b></p>


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/10.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 10** – Bash script để tạo giá trị băm</b></p>

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/11.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 11** – Bash script để so sánh giá trị băm tính toán với giá trị mong đợi</b></p>



<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/12.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 12** – Kiểm tra hoạt động của script</b></p>

Để thêm script vào crontab ta thực hiện như sau:

```bash
crontab -e
```
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/13.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 13** – Thêm script vào crontab</b></p>



Tệp `/home/debian/check_hash.sh` thực hiện việc khởi chạy script bash. Giờ đây, sau khi lưu tệp và khởi động lại thiết bị, script bash sẽ tự động chạy.

Sau đó, chúng tôi sử dụng ứng dụng “Backintime” để tạo bản sao lưu. Chúng ta có thể lưu bản sao lưu trên máy cục bộ hoặc thông qua SSH để kết nối từ xa. Ngoài ra, chúng ta có thể lập lịch sao lưu trong phần “Schedule” (**Hình 14**).

Đầu tiên chúng ta cần tải Back In Time
```bash
sudo apt update
sudo apt install backintime-qt
```
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/14.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 14** – Ứng dụng “Backintime”</b></p>


Tùy chọn “Include” cho phép chỉ định các tệp và thư mục để sao lưu, trong khi “Exclude” cho phép loại trừ các thư mục không cần thiết. Khi khởi chạy ứng dụng, cấu hình khá đơn giản. Trên màn hình chính, tất cả các bản sao lưu được liệt kê (Backintime gọi chúng là "snapshot").

---
Để cấu hình và sử dụng **Back In Time** nhằm sao lưu các tệp và thư mục mong muốn, bạn có thể thực hiện theo các bước sau:

### Bước 1: Khởi chạy Back In Time
- Mở **Back In Time** bằng cách chạy lệnh sau trên terminal:
  ```bash
  backintime-qt
  ```
- Nếu cần quyền root, chạy:
  ```bash
  sudo backintime-qt
  ```

### Bước 2: Thiết lập cấu hình sao lưu
Khi khởi chạy lần đầu, **Back In Time** sẽ yêu cầu bạn thiết lập cấu hình cho các bản sao lưu. Các bước cụ thể như sau:

1. **Chọn thư mục sao lưu**:
   - Trong tab **General** (Tổng quát), chọn thư mục **Where to save snapshots** (Nơi lưu trữ các bản snapshot). Đây là nơi các bản sao lưu sẽ được lưu trữ (có thể là ổ đĩa ngoài, thư mục cụ thể trên hệ thống, v.v.).
   
2. **Thiết lập thời gian sao lưu tự động (tùy chọn)**:
   - Trong phần **Schedule** (Lịch trình), bạn có thể chọn thời gian sao lưu tự động (hàng giờ, hàng ngày, hàng tuần, hoặc theo ý muốn).

### Bước 3: Cấu hình tệp và thư mục để sao lưu và loại trừ
Để chỉ định các thư mục và tệp bạn muốn sao lưu hoặc loại trừ, chuyển đến tab **Include/Exclude** và làm như sau:

1. **Thêm các thư mục và tệp cần sao lưu**:
   - Trong phần **Include** (Bao gồm), nhấp vào nút **Add** để thêm các thư mục hoặc tệp mà bạn muốn sao lưu. Bạn có thể thêm nhiều thư mục và tệp tùy ý.

2. **Loại trừ các thư mục và tệp không cần thiết**:
   - Trong phần **Exclude** (Loại trừ), nhấp vào nút **Add** để loại trừ các thư mục hoặc tệp mà bạn không muốn sao lưu (như thư mục tạm thời, thư mục cache, v.v.).
   - Back In Time cũng cho phép bạn thiết lập các quy tắc loại trừ dựa trên kiểu tệp hoặc tên tệp. Bạn có thể loại trừ dựa trên ký tự đại diện hoặc biểu thức (như `*.tmp` để loại trừ tất cả các tệp có đuôi `.tmp`).

### Bước 4: Thực hiện sao lưu lần đầu
- Sau khi hoàn tất cấu hình, quay lại màn hình chính và nhấp vào **Take Snapshot** (Chụp snapshot) để thực hiện sao lưu lần đầu.
- Tất cả các bản sao lưu sẽ xuất hiện trên màn hình chính của ứng dụng dưới dạng các "snapshot" được liệt kê theo thời gian.

### Bước 5: Khôi phục dữ liệu từ snapshot (nếu cần)
- Để khôi phục dữ liệu từ snapshot, chỉ cần chọn snapshot trong danh sách và nhấp vào nút **Restore** (Khôi phục).
- Bạn có thể chọn khôi phục toàn bộ snapshot hoặc chỉ những tệp và thư mục cụ thể.

Với các bước này, bạn sẽ có một bản sao lưu được cấu hình và quản lý dễ dàng thông qua giao diện của **Back In Time**.
--- 

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/15.png" alt="" width="800">
</p>
<p align="center"><b>**Hình 15** – Giao diện chương trình</b></p>


Ở đây bạn có thể thao tác với tất cả các bản sao lưu: khôi phục, xóa, so sánh, v.v. Chọn bản sao lưu cần thiết và nhấn nút “Khôi phục”. Sau khi hoàn tất, tất cả dữ liệu sẽ được khôi phục.

Để kiểm tra định kỳ chức năng của hệ thống bảo đảm an ninh thông tin (СЗИ), chúng tôi đã chọn Vulners Agent, một chương trình kiểm tra tương thích với Debian 12. Agent này thu thập thông tin về hệ điều hành, phiên bản và các gói đã cài đặt. Sau đó, thông tin này được gửi đến Vulners API để xác định phần mềm nào có lỗ hổng bảo mật.

#### Cách tải Vulners Agent

Adding the Public Key

First, add vulners.com pubkey:

```bash
wget -O- https://repo.vulners.com/pubkey.txt | apt-key add -
echo "deb http://repo.vulners.com/debian focal main" | tee /etc/apt/sources.list.d/vulners.list
apt-get update && apt-get install vulners-agent
```
[chi tiết tại đây](https://vulners.com/docs/manuals/vulners_agent/#debian)

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/image/16.png" alt="" width="800">
</p>
<p align="center"><b>****Hình 17** – Thêm api-key để sử dụng Vulners Agent</b></p>



**Hình 18** – Khởi chạy máy quét

**Hình 19** – Kết quả quét

СЗИ ClamAV không cho phép các loại virus và phần mềm độc hại xâm nhập.

