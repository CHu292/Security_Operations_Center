- Cấu hình trong virtualbox:

![PC1](../img/Lab_4_setup/PC_1_1.png)

- Các công cụ cần tải:



```bash
# Cập nhật danh sách gói
sudo apt update

# Cài đặt các công cụ mạng cơ bản
sudo apt install -y net-tools iproute2 iputils-ping traceroute dnsutils curl wget

# Cài đặt công cụ đo thông lượng mạng
sudo apt install -y iperf3

# Cài đặt công cụ bắt gói tin
sudo apt install -y tcpdump

# Cài đặt máy chủ SSH
sudo apt install -y openssh-server

```

- IP configuration for PC1:

```bash
network:
 version: 2
 ethernets:
   enp0s3:
     dhcp4: no
     addresses:
       - 192.168.10.2/24
     gateway4: 192.168.10.1
     routes:
       - to: 192.168.20.0/24
         via: 192.168.10.1
```

