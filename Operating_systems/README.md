
[1. LAB 1 - ForkBomb](./Lab/Lab_1_Forkbomb/)

1. Viết fork bomb đơn giản cho Linux và Windows.
2. Theo dõi và vẽ biểu đồ số tiến trình theo thời gian.
3. Phân tích phản ứng của hệ điều hành (OS).

---

[2. LAB 2 - MemBomb](./Lab/Lab_2_Membomb/)

1. Viết một chương trình cấp phát bộ nhớ và điền nó bằng số 0
   với bước nhảy bằng kích thước của một trang bộ nhớ (sử dụng `mmap`, `VirtualAlloc`)
2. Vẽ biểu đồ bộ nhớ trống
3. Tìm hiểu cách hoạt động của daemon OOM Killer trong Linux
4. Nhận được thông báo không thể cấp phát thêm bộ nhớ trong Windows

---

[3. LAB 3 - LINPACK](./Lab/Lab_3_Linpack/)

1. **Phương án đơn giản**

Tất cả thực hiện trên một hệ điều hành

Tìm và biên dịch chương trình **linpack** để đánh giá hiệu suất tính toán của máy tính (Flops) và kiểm thử nó trong các chế độ hoạt động khác nhau của hệ điều hành:

1. Với các mức **ưu tiên nhiệm vụ khác nhau** trong bộ lập lịch
2. Có và không có **ràng buộc tiến trình với bộ xử lý** (CPU affinity)
3. Thực hiện nhiều bài kiểm thử, so sánh kết quả theo 3 sigma hoặc tiêu chí thống kê khác

2. **Phương án nâng cao**

Tương tự như trên, **cộng thêm thay đổi các tham số ở cấp độ nhân hệ điều hành** (chọn một trong các mục sau):

1. **Chặn thực thi tất cả các luồng** ngoại trừ luồng được kiểm thử (bằng cách **chặn ngắt**, gọi là *cli sti*)
2. **Tìm và sử dụng bộ lập lịch khác** cho tiến trình trong Linux và so sánh kết quả xử lý tính toán
3. **Điều chỉnh cấu hình** của bộ lập lịch hiện tại
4. **Can thiệp trực tiếp** vào hoạt động của bộ lập lịch ở cấp độ nhân

---

[4. LAB 4 - Scheduler](./Lab/Lab_4_Scheduler/)

1. **Nhiệm vụ:**

Thực hiện kiểm thử và tìm ra **bộ lập lịch I/O (nhập/xuất) tốt nhất** trong số các lựa chọn.

2. **Lựa chọn nâng cao:**

Chỉnh sửa bộ lập lịch hiện có ở cấp độ nhân hệ điều hành

---

[5. LAB 5 - Filesystem Testing](./Lab/Lab_5_Filesystem_Testing/)

1. **Phương án cơ bản**

Chọn **3 (hoặc nhiều hơn)** hệ thống tập tin, chọn phương pháp kiểm tra và tìm ra hệ thống tốt nhất trong số đó.

2. **Phương án nâng cao**

* Hệ thống tập tin “dị”
* Hoặc phương pháp kiểm tra “dị”

---

[6. LAB 6 - Malloc Testing](./Lab/Lab_6_Malloc_Testing/)

1. Phương án cơ bản

Kiểm thử hàm **malloc/free** và xây dựng biểu đồ thể hiện **sự phụ thuộc của thời gian cấp phát bộ nhớ vào kích thước bộ nhớ yêu cầu**.

Hệ điều hành: Windows hoặc Linux.


2.  **Phiên bản nâng cao**

* So sánh với các **trình malloc khác**
* Kiểm thử trên **tiến trình đang chạy thực tế**

[7. LAB 7 - Virtual Machine](./Lab/Lab_7_Virtual_Machine/)

1. Phương án cơ bản

**Liệt kê tất cả các cách mà bạn biết để phát hiện hệ thống đang chạy trong máy ảo.**
(Yêu cầu ít nhất **5 cách** trở lên)

2. **Phiên bản nâng cao (hoặc):**

* Chỉ ra cách **thoát khỏi máy ảo**
* Thực hiện bằng **ngôn ngữ hợp ngữ (assembly)**

---

[8. LAB 8 - AppArmor and SELinux](./Lab/Lab_8_AppArmor_and_SELinux/)

1. Phương án cơ bản

**Thực hiện cả hai nhiệm vụ sau:**

* **Cấu hình AppArmor** để giám sát một ứng dụng phức tạp và trình diễn cách ứng dụng đó hoạt động với **quyền hạn chế** (ứng dụng giao diện hoặc web server).
* **Cấu hình SELinux** trong chế độ kiểm soát truy cập bắt buộc (Mandatory Access Control, như trong CentOS, v.v.) và trình diễn hoạt động trong **mô hình hai tầng**.

2. **Phiên bản nâng cao (hoặc):**

* Tự nghĩ và viết **một mô-đun LSM** (Linux Security Module) riêng – với **ủy quyền hành động phức tạp**.
* Tự nghĩ và viết **một mô-đun PAM** riêng – cũng với **ủy quyền hành động phức tạp**.
* Tạo **bộ lọc Seccomp** phức tạp riêng.

---

[9. LAB 9 - Network Programming and Packet Filtering](./Lab/Lab_9_Network_Programming_and_Packet_Filtering/)

1. Phương án cơ bản

**Chọn một trong hai:**

* Viết **bộ lọc gói mạng** dựa trên **nfqueue** và **iptables**, sau đó kiểm thử tốc độ hoạt động
* Kiểm thử hoạt động của **socket TCP** với các cấu hình khác nhau của **setsockopt**

2. **Phiên bản nâng cao** (chọn một):

* Viết **bộ lọc gói** dựa trên giao diện **netfilter** trong nhân Linux
* Xây dựng **chương trình RPC** cho Linux có hỗ trợ xác thực (dùng `rpcinfo`, `rpcbind`)