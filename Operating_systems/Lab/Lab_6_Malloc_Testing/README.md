# LAB 6 - MALLOC TESTING

Kiểm thử hàm **malloc/free** và xây dựng biểu đồ thể hiện **sự phụ thuộc của thời gian cấp phát bộ nhớ vào kích thước bộ nhớ yêu cầu**.

Hệ điều hành: Windows hoặc Linux.

---

### **Phiên bản nâng cao (hoặc)**

1. So sánh với các **trình malloc khác**
2. Kiểm thử trên **tiến trình đang chạy thực tế**

---

### **Lệnh tham khảo để đo đạc bằng perf (Linux):**

```bash
sudo perf record -ag -e syscalls:sys_enter_mmap -- sleep 30
sudo perf script --header
```

---

