
## ⚠️ Cảnh báo:

**Chỉ thực hiện trong môi trường ảo hoá có giới hạn tài nguyên. Không chạy trên máy thật!**

---

## Mục tiêu lab:

1. **Viết fork bomb đơn giản** cho Linux và Windows.
2. **Theo dõi và vẽ biểu đồ số tiến trình theo thời gian**.
3. **Phân tích phản ứng của hệ điều hành (OС)**.

---

## 1. Viết Fork Bomb

### Linux – Fork Bomb bằng Bash (dạng đơn giản, có kiểm soát):

Tạo file `safe_forkbomb.sh`:

```bash
#!/bin/bash
limit=50  # giới hạn số lần fork để tránh sập máy
counter=0

forkbomb() {
    ((counter++))
    if [ "$counter" -lt "$limit" ]; then
        forkbomb & forkbomb &
    else
        sleep 60  # giữ tiến trình để quan sát
    fi
}

forkbomb
```

Cấp quyền:

```bash
chmod +x safe_forkbomb.sh
```

> Dừng bằng: `killall bash` hoặc `pkill -f safe_forkbomb.sh`

Chương trình trên là một **phiên bản an toàn của fork bomb** viết bằng Bash, có **giới hạn số lần fork** để tránh làm sập hệ thống.

---

### Giải thích

```bash
#!/bin/bash
```

* Khai báo đây là một script Bash.

---

```bash
limit=50  # giới hạn số lần fork để tránh sập máy
counter=0
```

* Biến `limit`: số lần tối đa được phép gọi đệ quy (tức là tạo tiến trình con).
* Biến `counter`: đếm số lần gọi hàm `forkbomb`.

---

```bash
forkbomb() {
    ((counter++))
```

* Định nghĩa hàm `forkbomb`.
* Mỗi lần hàm được gọi, biến `counter` tăng thêm 1.

---

```bash
    if [ "$counter" -lt "$limit" ]; then
        forkbomb & forkbomb &
```

* Nếu số lần gọi nhỏ hơn giới hạn (`limit = 50`):

  * Hàm sẽ tự gọi lại **2 lần** trong **nền** (dùng `&`).
  * Tức là tạo ra **2 tiến trình con** mới từ mỗi lần gọi.

→ Hiệu ứng là **tăng số tiến trình theo cấp số nhân** (giống fork bomb thật), **nhưng có kiểm soát**.

---

```bash
    else
        sleep 60  # giữ tiến trình để quan sát
    fi
```

* Khi đã đến giới hạn (50 lần), các tiến trình sẽ **dừng đệ quy** và ngủ 60 giây.
* Việc này giúp bạn quan sát chúng bằng lệnh như `ps`, `top`, v.v.

---

```bash
forkbomb
```

* Gọi hàm lần đầu để bắt đầu quá trình fork.

---

### **Lưu ý**

* **Đây không phải là fork bomb thực sự nguy hiểm** vì có giới hạn (`limit=50`).
* Fork bomb thật sẽ không có giới hạn và sẽ khiến hệ thống **hết PID/process**, dẫn đến treo máy.

---


### Windows – Fork Bomb bằng Python:

Tạo file `safe_forkbomb_win.py`:

```python
import multiprocessing
import time

def bomb():
    while True:
        time.sleep(60)

if __name__ == '__main__':
    processes = []
    for _ in range(50):  # giới hạn tiến trình để không làm sập Windows
        p = multiprocessing.Process(target=bomb)
        p.start()
        processes.append(p)
```

Chạy bằng:

```bash
python safe_forkbomb_win.py
```

---

## 📈 2. Ghi lại và vẽ biểu đồ số tiến trình

### Linux: Sử dụng script ghi log:

```bash
#!/bin/bash
> process_log.txt
for i in {1..60}; do
    echo "$(date +%s) $(ps -e | wc -l)" >> process_log.txt
    sleep 1
done
```

Sau đó vẽ bằng Python:

```python
import matplotlib.pyplot as plt

times, processes = [], []
with open('process_log.txt') as f:
    for line in f:
        t, p = line.strip().split()
        times.append(int(t))
        processes.append(int(p))

plt.plot(times, processes)
plt.xlabel('Unix Time')
plt.ylabel('Number of Processes')
plt.title('Process Count Over Time')
plt.grid()
plt.show()
```

---

## 🧠 3. Phân tích phản ứng của hệ điều hành

**Ghi chú trong báo cáo:**

* **Giai đoạn đầu**: hệ thống cho phép tạo tiến trình mới.
* **Khi gần đến giới hạn** (Linux mặc định `ulimit -u` \~4096): người dùng không thể mở terminal, GUI treo.
* **Hệ thống có thể giết tiến trình** bằng `OOM Killer` (Linux).
* **Windows** thường chậm dần, và hiển thị lỗi "Không thể tạo tiến trình mới".

---


