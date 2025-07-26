# LAB 7 - Virtual Machine

---

**Liệt kê tất cả các cách mà bạn biết để phát hiện hệ thống đang chạy trong máy ảo.**
(Yêu cầu ít nhất **5 cách** trở lên)

---

### **Phiên bản nâng cao (hoặc):**

* Chỉ ra cách **thoát khỏi máy ảo**
* Thực hiện bằng **ngôn ngữ hợp ngữ (assembly)**

---

### **Thực hành**

**Cài đặt Docker**
[Hướng dẫn chính thức](https://docs.docker.com/engine/install)

**Chạy Ubuntu, ánh xạ cổng 8000, khởi chạy Python HTTP Server, ánh xạ thư mục vào container và cấp quyền truy cập thư mục:**

---

### **Các lệnh Docker hữu ích**

1.

```bash
sudo docker run -ti ubuntu /bin/bash
```

Chạy container và vào chế độ tương tác

2.

Nhấn `CTRL + P + Q` – **Thoát khỏi container mà không tắt nó**

3.

```bash
docker ps -a
```

Xem danh sách container đang chạy (và đã dừng)

4.

```bash
docker commit <id> <name>
```

Lưu container hiện tại thành image với tên đã đặt

5.

```bash
docker images
```

Hiển thị danh sách các image hiện có

```bash
docker search <tên>
docker pull <tên image>
```

Tìm và tải image

6.

```bash
docker attach <id>
```

Gắn vào container đang chạy

7.

```bash
docker run <các tùy chọn> -ti ubuntu /bin/bash
```

Chạy container và ánh xạ **giao diện mạng của host**
Tất cả cổng mở trong container sẽ mở ngoài host
(Thoát: `CTRL + P + Q`)

```bash
docker ps -a
docker attach <id_container>
docker exec -ti <id_container> /bin/bash
docker run --net="host" -ti ubuntu /bin/bash
```

Ánh xạ cổng:

```bash
-p <CỔNG_HOST>:<CỔNG_CONTAINER>
```

8.

```bash
docker run -v /đường/dẫn/trên/host:/đường/dẫn/trong/container
```

Ánh xạ thư mục vào container

9.

```bash
docker export <id> > name.tar
```

Xuất container

10.

```bash
cat name.tar | docker import - <tên>
```

Nhập container từ file tar

---

### **Dockerfile – tệp cấu hình tạo image:**

```Dockerfile
FROM ubuntu
RUN apt update
RUN apt install -y python3
WORKDIR /home/test
ENTRYPOINT python3 -m http.server 2000
```

Tạo image:

```bash
docker build -t mycont .
```

---

### **docker-compose.yml** – chỉ định container, ánh xạ thư mục & cổng

```yaml
version: "2.0"
services:
  my_container:
    build: .
    volumes:
      - /tmp/test/shared:/home/test
    ports:
      - 8011:2000
```

Chạy:

```bash
docker-compose up --build -d
```

---

## **PAM (Pluggable Authentication Modules)**

[https://www.opennet.ru/base/dev/pam\_linux.txt.html](https://www.opennet.ru/base/dev/pam_linux.txt.html)

---

## **SELinux (Security-Enhanced Linux)**

* [https://habr.com/ru/company/kingservers/blog/209644/](https://habr.com/ru/company/kingservers/blog/209644/)
* [https://defcon.ru/os-security/1264/](https://defcon.ru/os-security/1264/)

---

## **AppArmor**

* [https://help.ubuntu.ru/wiki/руководство\_по\_ubuntu\_server/безопасность/apparmor](https://help.ubuntu.ru/wiki/руководство_по_ubuntu_server/безопасность/apparmor)
* [https://losst.ru/nastrojka-apparmor-v-ubuntu-16-04](https://losst.ru/nastrojka-apparmor-v-ubuntu-16-04)
* [https://manpages.ubuntu.com/manpages/bionic/en/man5/apparmor.d.5.html](https://manpages.ubuntu.com/manpages/bionic/en/man5/apparmor.d.5.html)
* [https://defcon.ru/os-security/1544/](https://defcon.ru/os-security/1544/) – lịch sử
* [https://ru.bmstu.wiki/AppArmor](https://ru.bmstu.wiki/AppArmor) – quy tắc

---

## **LSM (Linux Security Modules)**

[https://habr.com/ru/company/pt/blog/144014/](https://habr.com/ru/company/pt/blog/144014/)

---

## **Windows**

* **Sách**: Руссинович – *Cấu trúc bên trong của Windows*, trang 510
* **Mã truy cập (Access Token)**: [https://ru.bmstu.wiki/Access\_Token](https://ru.bmstu.wiki/Access_Token)
* **Bộ mô tả bảo mật (Security Descriptor)**: [https://intuit.ru/studies/courses/10471/1078/lecture/16581?page=2](https://intuit.ru/studies/courses/10471/1078/lecture/16581?page=2)
* [https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-security\_descriptor?redirectedfrom=MSDN](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-security_descriptor?redirectedfrom=MSDN)
* **Ký số Driver**: [https://docs.microsoft.com/en-us/windows-hardware/drivers/install/kernel-mode-code-signing-policy--windows-vista-and-later-](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/kernel-mode-code-signing-policy--windows-vista-and-later-)
* **ELAM (Early Launch AntiMalware)**: [https://docs.microsoft.com/en-us/windows-hardware/drivers/install/early-launch-antimalware](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/early-launch-antimalware)
* **Kernel Patch Protector**: [https://xakep.ru/2019/11/25/byepg/](https://xakep.ru/2019/11/25/byepg/)
* **EWT – Event Tracing for Windows**: [https://docs.microsoft.com/en-us/windows/win32/etw/event-tracing-portal](https://docs.microsoft.com/en-us/windows/win32/etw/event-tracing-portal)
* **HVCI – Hypervisor-protected Code Integrity**: [https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/enable-virtualization-based-protection-of-code-integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/enable-virtualization-based-protection-of-code-integrity)
* **UAC – Kiểm soát tài khoản người dùng**: [https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works)

---

