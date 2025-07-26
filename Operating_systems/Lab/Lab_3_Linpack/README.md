# LAB 3 - LINPACK

[https://github.com/ereyes01/linpack](https://github.com/ereyes01/linpack)

**Phương án đơn giản**
Tất cả thực hiện trên một hệ điều hành

Tìm và biên dịch chương trình **linpack** để đánh giá hiệu suất tính toán của máy tính (Flops) và kiểm thử nó trong các chế độ hoạt động khác nhau của hệ điều hành:

1. Với các mức **ưu tiên nhiệm vụ khác nhau** trong bộ lập lịch
2. Có và không có **ràng buộc tiến trình với bộ xử lý** (CPU affinity)
3. Thực hiện nhiều bài kiểm thử, so sánh kết quả theo 3 sigma hoặc tiêu chí thống kê khác

---

**Phương án nâng cao**

Tương tự như trên, **cộng thêm thay đổi các tham số ở cấp độ nhân hệ điều hành** (chọn một trong các mục sau):

1. **Chặn thực thi tất cả các luồng** ngoại trừ luồng được kiểm thử (bằng cách **chặn ngắt**, gọi là *cli sti*)
2. **Tìm và sử dụng bộ lập lịch khác** cho tiến trình trong Linux và so sánh kết quả xử lý tính toán
3. **Điều chỉnh cấu hình** của bộ lập lịch hiện tại
4. **Can thiệp trực tiếp** vào hoạt động của bộ lập lịch ở cấp độ nhân

---

**Hệ thống tệp (FS)**

* [FAT](http://pascal.net.ru/book/fat.pdf)

* [ext2](http://samag.ru/archive/article/203)

---

