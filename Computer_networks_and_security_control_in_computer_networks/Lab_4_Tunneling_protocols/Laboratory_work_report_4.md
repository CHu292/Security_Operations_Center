

## 🧱 PHẦN 1: CHUẨN BỊ MÔ HÌNH TRONG GNS3

### 🎯 **Sơ đồ mục tiêu**
```
PC1 -- pfSense -- R1 -- Cisco -- PC2
```

### 🔧 **Thiết bị cần thiết**
| Loại | Thiết bị | Chức năng |
|------|----------|-----------|
| Host | PC1, PC2 | Kiểm tra iperf3 |
| Gateway 1 | pfSense | VPN Gateway 1 |
| Gateway 2 | Cisco Router (c7200) | VPN Gateway 2 |
| Router trung gian | R1 | Giả lập WAN |
| Switch | Ethernet Switch (nếu cần) | Kết nối LAN |

---

## ⚙️ PHẦN 2: CẤU HÌNH MẠNG

### 🖥️ **Cấu hình địa chỉ IP**

| Thiết bị         | Interface | Địa chỉ IP         | Vai trò |
|------------------|-----------|---------------------|---------|
| PC1              | e0        | 192.168.10.2/24     | LAN bên trái |
| pfSense          | em0       | 192.168.10.1/24     | LAN |
| pfSense          | em1       | 10.10.10.2/30       | WAN (về R1) |
| R1               | f0/1      | 10.10.10.1/30       | ↔ pfSense |
| R1               | f0/0      | 10.10.20.1/30       | ↔ Cisco |
| Cisco Router     | f0/1      | 10.10.20.2/30       | WAN |
| Cisco Router     | f0/0      | 192.168.20.1/24     | LAN |
| PC2              | e0        | 192.168.20.2/24     | LAN bên phải |

---

## 🧪 PHẦN 3: CẤU HÌNH PC1, PC2

### **PC1 (VPCS)**:
```bash
ip 192.168.10.2 255.255.255.0 192.168.10.1
```

### **PC2 (VPCS)**:
```bash
ip 192.168.20.2 255.255.255.0 192.168.20.1
```

---

## 🌐 PHẦN 4: CẤU HÌNH pfSENSE (VPN GATEWAY 1)

### ✅ Bước 1: Import pfSense ISO vào GNS3 (chạy bằng QEMU)
1. Tải bản ISO pfSense từ: https://www.pfsense.org/download/
2. GNS3 → `File > Import Appliance` → Tạo QEMU VM mới từ ISO

### ✅ Bước 2: Cấu hình ban đầu từ console
Khi khởi động lần đầu:
- Gán `em1` = WAN (10.10.10.2)
- Gán `em0` = LAN (192.168.10.1)

Sau đó truy cập giao diện web từ PC1:  
`http://192.168.10.1` → Đăng nhập:
- **User:** `admin`
- **Password:** `pfsense`

### ✅ Bước 3: Thiết lập IPsec

**Vào:** `VPN > IPsec > Add P1`

#### Phase 1:
- Remote Gateway: `10.10.20.2`
- Authentication Method: Pre-Shared Key
- PSK: `"mypresharedkey"`
- Encryption: AES-256-CTR
- Hash: SHA-256
- DH Group: 2
- Lifetime: 86400
- Key Exchange: IKEv2

**Add Phase 2:**
- Local Network: `192.168.10.0/24`
- Remote Network: `192.168.20.0/24`
- Protocol: ESP
- Encryption: AES-256-CTR
- Auth: SHA-256
- PFS: group 5
- Lifetime: 3600

---

## 🧮 PHẦN 5: CẤU HÌNH CISCO ROUTER

### ✅ Bước 1: Địa chỉ IP
```cisco
interface FastEthernet0/0
 ip address 192.168.20.1 255.255.255.0
 no shutdown

interface FastEthernet0/1
 ip address 10.10.20.2 255.255.255.252
 no shutdown

ip route 192.168.10.0 255.255.255.0 10.10.20.1
```

### ✅ Bước 2: Cấu hình IPsec site-to-site

```cisco
crypto isakmp policy 10
 encr aes 256
 hash sha256
 authentication pre-share
 group 2
 lifetime 86400

crypto isakmp key mypresharedkey address 10.10.10.2

crypto ipsec transform-set MYSET esp-aes 256 esp-sha256-hmac mode tunnel

crypto map MYMAP 10 ipsec-isakmp
 set peer 10.10.10.2
 set transform-set MYSET
 match address 101

interface FastEthernet0/1
 crypto map MYMAP

access-list 101 permit ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255
```

---

## 📶 PHẦN 6: KIỂM TRA TUNNEL

1. Ping từ PC1 đến PC2:
```bash
ping 192.168.20.2
```

2. Trên pfSense:  
`Status > IPsec > SA` → xem trạng thái kết nối

3. Trên Cisco:
```cisco
show crypto isakmp sa
show crypto ipsec sa
```

---

## 📊 PHẦN 7: ĐO TỐC ĐỘ TRUYỀN DỮ LIỆU

### ✅ Trên PC2:
```bash
iperf3 -s
```

### ✅ Trên PC1:
```bash
iperf3 -c 192.168.20.2
```

- Thực hiện đo **có tunnel** và **tắt IPsec tunnel** để so sánh

---

## 📑 PHẦN 8: GHI NHẬN KẾT QUẢ

| Trạng thái kết nối   | Tốc độ (Mbps) |
|----------------------|----------------|
| Không IPsec (NAT)    | xxx Mbps       |
| Qua IPsec Tunnel     | xxx Mbps       |

---
