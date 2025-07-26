# LAB 9 - Network Programming and Packet Filtering

---

**Chọn một trong hai:**

1. Viết **bộ lọc gói mạng** dựa trên **nfqueue** và **iptables**, sau đó kiểm thử tốc độ hoạt động
2. Kiểm thử hoạt động của **socket TCP** với các cấu hình khác nhau của **setsockopt**

---

### **Phiên bản nâng cao** (chọn một):

1. Viết **bộ lọc gói** dựa trên giao diện **netfilter** trong nhân Linux
2. Xây dựng **chương trình RPC** cho Linux có hỗ trợ xác thực (dùng `rpcinfo`, `rpcbind`)

---

### **Tài liệu tham khảo:**

* [https://it.wikireading.ru/7079](https://it.wikireading.ru/7079) – các tùy chọn socket
* [https://www.ibm.com/developerworks/ru/library/l-hisock/index.html](https://www.ibm.com/developerworks/ru/library/l-hisock/index.html) – tối ưu hóa TCP
* [https://mathcs.clarku.edu/\~jbreecher/cs280/UNIX%20Network%20Programming(Volume1,3rd).pdf](https://mathcs.clarku.edu/~jbreecher/cs280/UNIX%20Network%20Programming%28Volume1,3rd%29.pdf) – Lập trình mạng trong UNIX (sách PDF)
* [http://tharikashblogs.blogspot.com/p/how-to-write-simple-rpc-programme.html](http://tharikashblogs.blogspot.com/p/how-to-write-simple-rpc-programme.html) – viết RPC đơn giản trên Linux
* ftp\://ftp.tmao.kiev.ua/pub/docs\_books/Linux/... – Tài liệu tiếng Nga về Linux và socket (PDF)

---

### **Thực hành**

1. Viết chương trình **client-server** bằng ngôn ngữ C sử dụng **giao thức TCP** (cả server và client)
    Thực hiện trong 10–15 phút, từ 12:00

2. Thực hiện truyền dữ liệu **không chặn luồng nhập từ socket và bàn phím**, sử dụng **select**

---

