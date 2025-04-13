# 🧱 PHẦN 1 – CHUẨN BỊ

# Cài đặt pfSense 

- Tải file iso của pfSense [tại đây](https://github.com/CloudSentralDotNet/iso_pfsense/releases)

## ✅ **Bước 1: Tạo máy ảo pfSense trong VirtualBox**

1. **Mở VirtualBox** → Bấm `New` (Tạo máy ảo mới)
2. Nhập thông tin:
   - **Name:** pfSenseGW
   - **Type:** BSD
   - **Version:** FreeBSD (64-bit)

3. **Memory size:** Chọn ít nhất **1024 MB**, tốt nhất là **2048 MB**

4. **Hard disk:**
   - Chọn “Create a virtual hard disk now” → Next
   - Loại: VDI → Next
   - Storage: Dynamically allocated → Next
   - Kích thước: Tối thiểu **10 GB** → Create

---

## ✅ **Bước 2: Gắn file ISO và cấu hình mạng**

1. Chọn máy `pfSenseGW` → bấm `Settings`

### ➤ **Tab System:**
- Bỏ chọn “Floppy” trong Boot Order (giữ lại Optical & Hard Disk)

### ➤ **Tab Storage:**
- Click vào “Empty” dưới "Controller: IDE"
- Click biểu tượng đĩa bên phải → `Choose a disk file...` → chọn `pfSense-CE-2.5.2-RELEASE-amd64.iso`
- Chọn OK

### ➤ **Tab Network:**
- **Adapter 1 (WAN):**
  - Enable → Attached to: **Internal Network**
  - Name: `net-WAN` *(bạn có thể đặt tên tùy ý)*

- **Adapter 2 (LAN):**
  - Enable → Attached to: **Internal Network**
  - Name: `net-LAN1`

> ⚠️ Nếu bạn chưa tạo Internal Network, bạn có thể vào `File > Preferences > Network` để thêm chúng (hoặc trong Adapter, gõ tên mạng là đủ).

---

## ✅ **Bước 3: Khởi động và cài đặt pfSense**

1. Bấm `Start` để khởi động máy ảo.
2. Giao diện cài đặt pfSense sẽ hiện lên:
   - Chọn `[Accept]` để chấp nhận License
   - Chọn `Install pfSense` → Enter

![](./img/huongdancaidat_pfSense/1.png)

3. Chọn kiểu bàn phím:

- nên chọn dòng đầu

![](./img/huongdancaidat_pfSense/2.png)

4. Chọn phân vùng ổ đĩa
- Chọn Auto (ZFS)

![](./img/huongdancaidat_pfSense/3.png)

- Di chuyển xuống dòng Disk info

![](./img/huongdancaidat_pfSense/4.png)

- Tìm ổ nhớ khả dụng

![](./img/huongdancaidat_pfSense/5.png)

- Quay trở lại chọn Pool Type/Disks:
- Chọn stripe

![](./img/huongdancaidat_pfSense/6.png)

- Nhấn phím cách để chọn ổ nhớ và nhấn ok

![](./img/huongdancaidat_pfSense/7.png)

- sau đó nhấn ok để cài đặt


# 🏗️ PHẦN 2 – TẠO MÔ HÌNH TRONG GNS3

## ✅ Bước 2.1: Kéo thiết bị vào
1. Mở GNS3, tạo project mới: `IPsec_Site2Site`
2. Kéo vào các thiết bị sau:
   - 1 × pfSense (dưới tab "QEMU VMs")
   - 1 × Cisco c7200 Router
   - 1 × Router trung gian (R1, có thể là Cisco c3725 hoặc IOU)
   - 2 × VPCS (PC1 và PC2)

## ✅ Bước 2.2: Kết nối dây như sơ đồ
```
PC1 -- pfSense(em0/em1) -- R1 -- Cisco -- PC2
```

| Kết nối       | Interface             |
|---------------|------------------------|
| PC1 → pfSense | VPCS e0 ↔ pfSense em0 |
| pfSense ↔ R1  | pfSense em1 ↔ R1 f0/1 |
| R1 ↔ Cisco    | R1 f0/0 ↔ Cisco f0/1  |
| Cisco → PC2   | Cisco f0/0 ↔ VPCS e0  |

---

# ⚙️ PHẦN 3 – CẤU HÌNH MẠNG

## ✅ Bước 3.1: IP các thiết bị

| Thiết bị         | Interface | IP Address        |
|------------------|-----------|-------------------|
| PC1              | e0        | `192.168.10.2/24` |
| pfSense LAN      | em0       | `192.168.10.1/24` |
| pfSense WAN      | em1       | `10.10.10.2/30`   |
| R1 f0/1          |           | `10.10.10.1/30`   |
| R1 f0/0          |           | `10.10.20.1/30`   |
| Cisco f0/1       |           | `10.10.20.2/30`   |
| Cisco f0/0       |           | `192.168.20.1/24` |
| PC2              | e0        | `192.168.20.2/24` |

---

# 🛠️ PHẦN 4 – CẤU HÌNH PC1 & PC2 (VPCS)

## ✅ PC1:
```bash
ip 192.168.10.2 255.255.255.0 192.168.10.1
```

## ✅ PC2:
```bash
ip 192.168.20.2 255.255.255.0 192.168.20.1
```

---

# 🧱 PHẦN 5 – CẤU HÌNH pfSENSE

## ✅ Bước 5.1: Khởi động pfSense

1. Khi boot lần đầu → hỏi gán interface:
   - **WAN (em1)**: 10.10.10.2/30
   - **LAN (em0)**: 192.168.10.1/24

2. Sau khi cấu hình IP xong, từ PC1 mở browser:
   - Truy cập: `http://192.168.10.1`
   - Login: `admin / pfsense`

## ✅ Bước 5.2: Vào giao diện cấu hình VPN

### ➤ `VPN > IPsec` → Add Phase 1

| Thông số | Giá trị |
|----------|--------|
| Remote Gateway | `10.10.20.2` |
| Authentication | Pre-Shared Key |
| PSK | `mypresharedkey` |
| Key Exchange | IKEv2 |
| Encryption | AES-256-CTR |
| Hash | SHA-256 |
| DH Group | 2 |
| Lifetime | 86400 |

### ➤ Thêm Phase 2 (trong Phase 1)
| Thông số | Giá trị |
|----------|---------|
| Local Subnet | `192.168.10.0/24` |
| Remote Subnet | `192.168.20.0/24` |
| Encryption | AES-256-CTR |
| Auth | SHA-256 |
| PFS | Group 5 |
| Lifetime | 3600 |

✅ Nhấn Save và Apply Changes

---

# 🔧 PHẦN 6 – CẤU HÌNH R1 (TRUNG GIAN)

## R1 (ví dụ dùng Cisco)
```cisco
interface FastEthernet0/0
 ip address 10.10.20.1 255.255.255.252
 no shutdown
interface FastEthernet0/1
 ip address 10.10.10.1 255.255.255.252
 no shutdown
```

---

# 🔒 PHẦN 7 – CẤU HÌNH CISCO VPN GATEWAY

### ✅ Interface và routing
```cisco
interface FastEthernet0/0
 ip address 192.168.20.1 255.255.255.0
 no shutdown
interface FastEthernet0/1
 ip address 10.10.20.2 255.255.255.252
 no shutdown
ip route 192.168.10.0 255.255.255.0 10.10.20.1
```

### ✅ IPsec configuration
```cisco
crypto isakmp policy 10
 encr aes 256
 hash sha256
 authentication pre-share
 group 2
 lifetime 86400

crypto isakmp key mypresharedkey address 10.10.10.2

crypto ipsec transform-set MYSET esp-aes 256 esp-sha256-hmac
 mode tunnel

crypto map MYMAP 10 ipsec-isakmp
 set peer 10.10.10.2
 set transform-set MYSET
 match address 101

interface FastEthernet0/1
 crypto map MYMAP

access-list 101 permit ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255
```

---

# 🧪 PHẦN 8 – KIỂM TRA HOẠT ĐỘNG

## ✅ Kiểm tra ping
Từ **PC1**:
```bash
ping 192.168.20.2
```

Từ **Cisco**:
```bash
show crypto isakmp sa
show crypto ipsec sa
```

Từ **pfSense**:
- `Status > IPsec` → kiểm tra SA

---

# 📊 PHẦN 9 – ĐO THÔNG LƯỢNG (IPERF3)

### ✅ Trên PC2:
```bash
iperf3 -s
```

### ✅ Trên PC1:
```bash
iperf3 -c 192.168.20.2
```

- Ghi lại kết quả **khi có tunnel**
- Sau đó **disable tunnel**, đo lại → so sánh

---

# 📝 PHẦN 10 – GHI NHẬN KẾT QUẢ

| Trạng thái        | Tốc độ (Mbps) |
|-------------------|---------------|
| Không dùng IPsec  | XXX           |
| Qua IPsec tunnel  | XXX           |

---

