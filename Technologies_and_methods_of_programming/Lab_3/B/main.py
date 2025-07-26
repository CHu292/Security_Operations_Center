from fastapi import FastAPI, Request
import psutil
import socket
import platform
import os

app = FastAPI()

def write_info_to_network_disk(data, identifier):
    # Đường dẫn đến thư mục trên Linux
    network_path = f"/home/chu/Documents/SOC/Technologies_and_methods_of_programming/Lab_3/B/{identifier}"
    os.makedirs(network_path, exist_ok=True)
    
    # Ghi thông tin vào tệp
    with open(f"{network_path}/system_info.txt", "a") as f:  # Sử dụng "a" để thêm thông tin
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")  # Thêm dòng trống giữa các lần ghi

@app.get("/")
def read_root():
    return {"message": "Welcome! Please visit /system-info to collect system information."}

@app.get("/system-info")
async def get_system_info(request: Request):
    # Lấy địa chỉ IP của máy khách
    ip_address = request.client.host

    # Lấy tên người dùng và tên máy tính
    user_name = os.environ.get('USER')  # Lấy tên người dùng
    computer_name = socket.gethostname()

    # Lấy thông tin về CPU và bộ nhớ RAM
    cpu_info = psutil.cpu_percent(interval=1)
    ram_info = psutil.virtual_memory().total / (1024 ** 3)  # Chuyển đổi sang GB

    # Lấy phiên bản hệ điều hành
    os_version = platform.platform()

    # Thu thập thông tin
    system_info = {
        "user_name": user_name,
        "computer_name": computer_name,
        "cpu_usage_percent": cpu_info,
        "ram_total_gb": ram_info,
        "os_version": os_version,
        "ip_address": ip_address
    }

    # Ghi thông tin vào đĩa mạng
    write_info_to_network_disk(system_info, ip_address)

    return system_info  # Trả thông tin hệ thống về client

