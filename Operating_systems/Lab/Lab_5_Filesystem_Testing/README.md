# LAB 5 - Filesystem Testing 

>Kiểm tra Hệ thống Tập tin (Filesystem - FS)

Chọn **3 (hoặc nhiều hơn)** hệ thống tập tin, chọn phương pháp kiểm tra và tìm ra hệ thống tốt nhất trong số đó.

---

### **Biến thể nâng cao**

* Hệ thống tập tin “dị”
* Hoặc phương pháp kiểm tra “dị”

---

### **Bài tập tại lớp**

1. **Tạo đĩa bằng lệnh `dd`:**

```bash
dd if=/dev/zero of=123.bin bs=1M count=64
```

2. **Tạo hệ thống tập tin bằng `mkfs`:**

```bash
mkfs -t ntfs -F 123.bin
```

3. **Gắn hệ thống tập tin vào thư mục:**

```bash
mount 123.bin mymount/
echo dfg > mymount/123.txt
umount 123.bin
```

---

4. **Dùng `losetup` với tập tin ảnh đĩa:**

```bash
losetup /dev/loop0 disk.img
```

5. **Phân vùng với `fdisk`:**

```bash
fdisk disk.img
```

6. **Tạo 2 đĩa và sử dụng `kpartx`:**

```bash
kpartx -a 123.bin     # tạo ánh xạ phân vùng
# gắn hệ thống tập tin, tạo file, thử nghiệm, tháo gỡ
kpartx -d 123.bin     # xóa ánh xạ phân vùng
```

---

### **7. Quản lý ổ đĩa logic (LVM)**

**Tạo ổ đĩa từ hai tập tin:**

```bash
dd if=/dev/zero of=./d01 count=1 bs=1M    # tạo file giả lập dữ liệu
losetup --show ./d01                      # gắn file như thiết bị
```

```bash
pvcreate /dev/...                         # khởi tạo vùng vật lý
Pvmove                                    # giải phóng dữ liệu khỏi ổ
```

---

### **Nhóm ổ đĩa:**

```bash
vgscan                       # xem các nhóm hiện có
vgcreate -s 32M [tên] disks  # tạo nhóm ổ đĩa
vgextend, vgreduce           # thêm / xóa đĩa khỏi nhóm
```

---

### **Ổ đĩa logic:**

```bash
lvcreate -n first -L 2G vg       # tạo volume logic
lvresize -L 40G vg1/lv2          # thay đổi kích thước volume
lvremove                        # xóa volume
```

---

### **Tài liệu tham khảo về quản lý bộ nhớ (Memory Management):**

* [https://www.kernel.org/doc/gorman/html/understand/understand009.html](https://www.kernel.org/doc/gorman/html/understand/understand009.html)
* [https://blog.holbertonschool.com/hack-the-virtual-memory-malloc-the-heap-the-program-break/](https://blog.holbertonschool.com/hack-the-virtual-memory-malloc-the-heap-the-program-break/)
* [http://goog-perftools.sourceforge.net/doc/tcmalloc.html](http://goog-perftools.sourceforge.net/doc/tcmalloc.html)
* [https://codearcana.com/posts/2016/07/11/arena-leak-in-glibc.html](https://codearcana.com/posts/2016/07/11/arena-leak-in-glibc.html) – thống kê bộ nhớ

---

