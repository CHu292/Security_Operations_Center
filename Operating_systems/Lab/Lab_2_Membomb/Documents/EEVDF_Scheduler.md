# EEVDF Scheduler

[Bài viết gốc](https://www.kernel.org/doc/html/latest/scheduler/sched-eevdf.html)
---

### **Bộ lập lịch EEVDF**

**EEVDF** (Earliest Eligible Virtual Deadline First – Hạn chót ảo đủ điều kiện sớm nhất) lần đầu tiên được giới thiệu trong một bài báo khoa học vào năm **1995** \[1].

Linux kernel bắt đầu chuyển sang EEVDF từ phiên bản **6.6** (tùy chọn mới trong năm **2024**), thay thế dần cho bộ lập lịch **Completely Fair Scheduler (CFS)**, với phiên bản EEVDF do **Peter Zijlstra** đề xuất vào năm **2023** \[2–4].
Thông tin thêm về CFS có thể xem tại [CFS Scheduler](./CFS_Scheduler.md).

---

Tương tự như CFS, **EEVDF** nhắm tới việc phân phối thời gian CPU **một cách công bằng** cho tất cả các tiến trình có thể chạy và có cùng mức ưu tiên.
Để làm được điều đó, nó gán **thời gian chạy ảo (virtual run time)** cho mỗi tiến trình và tính ra một **độ trễ (lag)** để xác định xem một tiến trình đã được cấp đúng phần CPU hay chưa.

* Nếu **lag > 0** → tiến trình đang **nợ thời gian CPU**
* Nếu **lag < 0** → tiến trình đã **dùng quá phần** thời gian được phân

Sau đó, EEVDF chọn tiến trình có **hạn chót ảo (Virtual Deadline – VD)** sớm nhất để thực thi tiếp theo.
Việc này đặc biệt **có lợi cho các ứng dụng yêu cầu độ trễ thấp** vì những tiến trình đó có thể được ưu tiên nhờ thời lượng thực thi ngắn hơn.

---

Hiện tại đang có các nghiên cứu liên quan đến cách xử lý lag cho các tiến trình ngủ.
EEVDF sử dụng cơ chế **"suy giảm (decaying)" dựa trên thời gian chạy ảo (VRT – Virtual Runtime)**.
→ Điều này giúp tránh việc các tiến trình ngủ **lợi dụng** hệ thống bằng cách reset lag một cách nhanh chóng.

Cụ thể:

* Khi một tiến trình đi vào trạng thái ngủ, nó vẫn được giữ trong hàng đợi, nhưng được đánh dấu là "trì hoãn đưa ra hàng đợi" (deferred dequeue).
* Lag sẽ **tự động giảm dần theo VRT**.
  → Do đó, các tiến trình ngủ lâu vẫn có thể reset lag về sau một cách tự nhiên.

Cuối cùng, các tiến trình có thể **giành quyền thực thi sớm hơn** nếu **VD** của chúng sớm hơn và có thể **yêu cầu kích thước lát thời gian (timeslice)** cụ thể thông qua syscall `sched_setattr()`, giúp hỗ trợ tốt hơn cho các ứng dụng nhạy cảm với độ trễ.

---

### **Tài liệu tham khảo**

1. \[Bài báo gốc về EEVDF (1995)]\([https://citeseerx.ist.psu.edu/document?repid=rep1\&type=pdf\&doi=80](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=80) 5acf7726282721504c8f00575d91ebfd750564)
2. [Bài viết kernel: chuyển sang EEVDF (2023)](https://lore.kernel.org/lkml/a79014e6-ea83-b316-le12-2ae056bda6fa@linux.vnet.ibm.com/)
3. [LWN: Giới thiệu EEVDF (1)](https://lwn.net/Articles/969062/)
4. [LWN: Giới thiệu EEVDF (2)](https://lwn.net/Articles/925371/)

---
