import os
import socket
import platform
import psutil
from cryptography.fernet import Fernet
import shutil

# Создание и сохранение ключа шифрования
key = Fernet.generate_key()
cipher_suite = Fernet(key)

with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Функция для шифрования файла
def encrypt_file(filepath):
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

# Сбор информации о системе
def gather_system_info():
    user_name = os.getlogin()
    computer_name = socket.gethostname()
    memory_info = psutil.virtual_memory().total / (1024 ** 3) 
    cpu_info = platform.processor()
    os_version = platform.platform()

    system_info = (
        f"Пользователь: {user_name}\n"
        f"Компьютер: {computer_name}\n"
        f"Память: {memory_info:.2f} ГБ\n"
        f"ЦП: {cpu_info}\n"
        f"ОС: {os_version}"
    )
    return system_info

# Сохранение информации о системе в файл sys.tat в текущем каталоге
def save_sys_info_to_file(system_info):
    sys_tat_path = 'sys.tat'
    with open(sys_tat_path, 'w') as file:
        file.write(system_info)
    return sys_tat_path 

def main():
    # Сбор информации о системе
    system_info = gather_system_info()
    # Сохранение информации в sys.tat в текущем каталоге
    filepath = save_sys_info_to_file(system_info)

    # Шифрование файла sys.tat
    encrypt_file(filepath)

    # Копирование файла secur.py и key.key в текущий каталог, если они не существуют
    if not os.path.exists('./secur.py'):
        shutil.copy('secur.py', '.')

    if not os.path.exists('./key.key'):
        shutil.copy('key.key', '.')

    print("Завершено. Файл sys.tat был создан и зашифрован в текущем каталоге.")

if __name__ == "__main__":
    main()

