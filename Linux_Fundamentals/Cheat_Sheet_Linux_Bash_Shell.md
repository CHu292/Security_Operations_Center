### Cheat Sheet: Linux Bash Shell 

#### **1. Giới thiệu**
- **Bash Shell Cheat Sheet** cung cấp các lệnh cơ bản để làm việc hiệu quả trên Linux.
- **Chú thích:**
  - Mọi thứ trong `< >` cần được thay thế, ví dụ: `<fileName>` → `iLovePeanuts.txt`.
  - Không bao gồm dấu `=` trong các lệnh.
  - `..` nghĩa là nhiều tệp có thể bị ảnh hưởng bởi một lệnh duy nhất (ví dụ: `rm file1 file2 ...`).

---

### **2. Các phím tắt cơ bản (Basic Terminal Shortcuts)**
| **Phím tắt**             | **Mô tả**                                                                 |
|---------------------------|---------------------------------------------------------------------------|
| `CTRL + L`                | Xóa màn hình Terminal.                                                   |
| `CTRL + D`                | Thoát khỏi Terminal.                                                     |
| `CTRL + A`                | Di chuyển con trỏ về đầu dòng lệnh.                                      |
| `CTRL + E`                | Di chuyển con trỏ về cuối dòng lệnh.                                     |
| `CTRL + U`                | Xóa từ con trỏ đến đầu dòng.                                             |
| `CTRL + K`                | Xóa từ con trỏ đến cuối dòng.                                            |
| `CTRL + W`                | Xóa một từ bên trái con trỏ.                                             |
| `CTRL + Y`                | Dán nội dung đã xóa.                                                    |
| `CTRL + R`                | Tìm kiếm ngược trong lịch sử lệnh.                                       |
| `!!`                      | Thực thi lại lệnh cuối cùng.                                             |
| `CTRL + Z`                | Dừng tạm thời một lệnh (resume với `fg` hoặc `bg`).                      |
| `TAB`                     | Tự động hoàn thành tệp hoặc lệnh.                                        |

---

### **3. Điều hướng cơ bản trong Terminal**
| **Lệnh**                     | **Mô tả**                                                                              |
|-------------------------------|----------------------------------------------------------------------------------------|
| `ls -a`                      | Liệt kê tất cả tệp và thư mục, bao gồm tệp ẩn.                                          |
| `ls <folderName>`            | Hiển thị nội dung của thư mục cụ thể.                                                  |
| `ls -lh`                     | Hiển thị danh sách chi tiết (đọc dễ hơn).                                              |
| `cd /`                       | Di chuyển đến thư mục gốc.                                                             |
| `cd ..`                      | Lùi về một thư mục.                                                                    |
| `pwd`                        | Hiển thị thư mục hiện tại.                                                             |
| `man <command>`              | Hiển thị tài liệu hướng dẫn về lệnh.                                                   |
| `du -h`                      | Kiểm tra dung lượng thư mục (đọc dễ hơn).                                              |

---

### **4. Quản lý tệp (File Manipulation)**
| **Lệnh**                     | **Mô tả**                                                                              |
|-------------------------------|----------------------------------------------------------------------------------------|
| `cat <fileName>`             | Hiển thị nội dung của tệp.                                                             |
| `head -n <lines> <fileName>` | Hiển thị `n` dòng đầu tiên của tệp.                                                    |
| `tail -n <lines> <fileName>` | Hiển thị `n` dòng cuối cùng của tệp.                                                   |
| `mkdir <folderName>`         | Tạo thư mục mới.                                                                       |
| `cp <src> <dest>`            | Sao chép tệp/thư mục.                                                                 |
| `mv <src> <dest>`            | Di chuyển hoặc đổi tên tệp/thư mục.                                                   |
| `rm <fileName>`              | Xóa tệp.                                                                              |
| `rm -r <folderName>`         | Xóa thư mục và tất cả nội dung bên trong.                                              |
| `touch <fileName>`           | Tạo tệp rỗng mới hoặc cập nhật thời gian sửa đổi của tệp.                              |

---

### **5. Tìm kiếm tệp (Researching Files)**
| **Lệnh**                          | **Mô tả**                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------|
| `locate <text>`                   | Tìm kiếm nội dung của tệp.                                                                         |
| `find <path> -name <fileName>`    | Tìm tệp theo tên trong thư mục.                                                                    |
| `find <path> -type d`             | Tìm kiếm thư mục trong đường dẫn cụ thể.                                                           |
| `find <path> -size +10M`          | Tìm tệp có dung lượng lớn hơn 10MB.                                                                |

---

### **6. Chuyển hướng luồng dữ liệu (Flow Redirection)**
| **Lệnh**                          | **Mô tả**                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------|
| `command > file.txt`              | Ghi kết quả lệnh vào tệp (ghi đè).                                                                 |
| `command >> file.txt`             | Ghi kết quả lệnh vào tệp (thêm vào cuối tệp).                                                      |
| `command 2> error.log`            | Ghi lỗi của lệnh vào tệp log lỗi.                                                                  |
| `command \| another_command`       | Chuyển kết quả lệnh đầu tiên làm đầu vào cho lệnh thứ hai.                                          |

---

### **7. Quyền tệp và người dùng**
| **Lệnh**                          | **Mô tả**                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------|
| `chmod +x <fileName>`             | Gán quyền thực thi cho tệp.                                                                        |
| `chown user:group <fileName>`     | Thay đổi chủ sở hữu của tệp.                                                                       |
| `sudo adduser <userName>`         | Tạo người dùng mới.                                                                                |
| `sudo passwd <userName>`          | Đặt lại mật khẩu cho người dùng.                                                                   |
| `sudo deluser <userName>`         | Xóa người dùng khỏi hệ thống.                                                                      |

---

### **8. Lập lịch thực thi (Scheduling Commands)**
| **Lệnh**                          | **Mô tả**                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------|
| `crontab -e`                      | Sửa lịch thực thi định kỳ.                                                                         |
| `at <time>`                       | Thực thi lệnh tại một thời gian cụ thể.                                                            |
| `nohup <command>`                 | Chạy lệnh trong nền, không bị dừng khi thoát khỏi terminal.                                        |

---

### **9. Nén và giải nén (Archiving and Compressing Data)**
| **Lệnh**                          | **Mô tả**                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------|
| `tar -cvf archive.tar folder/`    | Nén thư mục thành tệp `.tar`.                                                                      |
| `tar -xvf archive.tar`            | Giải nén tệp `.tar`.                                                                               |
| `gzip file.txt`                   | Nén tệp thành `.gz`.                                                                              |
| `gunzip file.txt.gz`              | Giải nén tệp `.gz`.                                                                               |

---
