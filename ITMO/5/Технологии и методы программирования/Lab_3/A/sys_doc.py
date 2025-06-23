import os
import socket
import platform
import psutil
from cryptography.fernet import Fernet
import shutil

# Tạo và lưu khóa mã hóa
key = Fernet.generate_key()
cipher_suite = Fernet(key)

with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Hàm mã hóa file
def encrypt_file(filepath):
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

# Thu thập thông tin hệ thống
def gather_system_info():
    user_name = os.getlogin()
    computer_name = socket.gethostname()
    memory_info = psutil.virtual_memory().total / (1024 ** 3) 
    cpu_info = platform.processor()
    os_version = platform.platform()

    system_info = (
        f"User: {user_name}\n"
        f"Computer: {computer_name}\n"
        f"Memory: {memory_info:.2f} GB\n"
        f"CPU: {cpu_info}\n"
        f"OS: {os_version}"
    )
    return system_info

# Lưu thông tin hệ thống vào file sys.tat trong thư mục hiện tại
def save_sys_info_to_file(system_info):
    sys_tat_path = 'sys.tat'
    with open(sys_tat_path, 'w') as file:
        file.write(system_info)
    return sys_tat_path 

def main():
    # Thu thập thông tin hệ thống
    system_info = gather_system_info()
    # Lưu thông tin vào sys.tat trong thư mục hiện tại
    filepath = save_sys_info_to_file(system_info)

    # Mã hóa file sys.tat
    encrypt_file(filepath)

    # Sao chép file secur.py và key.key vào thư mục hiện tại nếu chưa tồn tại
    if not os.path.exists('./secur.py'):
        shutil.copy('secur.py', '.')

    if not os.path.exists('./key.key'):
        shutil.copy('key.key', '.')

    print("Hoàn tất. File sys.tat đã được tạo và mã hóa trong thư mục hiện tại.")

if __name__ == "__main__":
    main()

