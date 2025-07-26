# LAB 8 - AppArmor và SELinux

---

**Thực hiện cả hai nhiệm vụ sau:**

1. **Cấu hình AppArmor** để giám sát một ứng dụng phức tạp và trình diễn cách ứng dụng đó hoạt động với **quyền hạn chế** (ứng dụng giao diện hoặc web server).
2. **Cấu hình SELinux** trong chế độ kiểm soát truy cập bắt buộc (Mandatory Access Control, như trong CentOS, v.v.) và trình diễn hoạt động trong **mô hình hai tầng**.

---

### **Phiên bản nâng cao (hoặc):**

1. Tự nghĩ và viết **một mô-đun LSM** (Linux Security Module) riêng – với **ủy quyền hành động phức tạp**.
2. Tự nghĩ và viết **một mô-đun PAM** riêng – cũng với **ủy quyền hành động phức tạp**.
   3\*. Tạo **bộ lọc Seccomp** phức tạp riêng.

---

### **Bài tập:**

Sử dụng các công cụ sau:

* `apparmor-profiles`
* `apparmor-utils`

Lệnh hữu ích:

* `aa-status` – kiểm tra trạng thái AppArmor
* `aa-complain` – bật **chế độ giám sát**
* `aa-enforce` – bật **chế độ bảo vệ**
* `aa-autodep` – tạo **hồ sơ mới**
* `aa-genprof` – cập nhật hồ sơ hiện có

---

**Yêu cầu:**
Sinh hồ sơ AppArmor của riêng bạn cho chương trình **ncat**.

---



