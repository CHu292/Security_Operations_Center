from fastapi import FastAPI, Request
import psutil
import socket
import platform
import os

app = FastAPI()

def write_info_to_network_disk(data, identifier):
    # Путь к директории в Linux
    network_path = f"/home/chu/Documents/Technologies_and_methods_of_programming/Lab_3/B/{identifier}"
    os.makedirs(network_path, exist_ok=True)
    
    # Запись информации в файл
    with open(f"{network_path}/system_info.txt", "a") as f:  # Используем "a" для добавления информации
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")  # Добавляем пустую строку между записями

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать! Пожалуйста, посетите /system-info для сбора информации о системе."}

@app.get("/system-info")
async def get_system_info(request: Request):
    # Получение IP-адреса клиента
    ip_address = request.client.host

    # Получение имени пользователя и имени компьютера
    user_name = os.environ.get('USER')  # Получаем имя пользователя
    computer_name = socket.gethostname()

    # Получение информации о ЦП и оперативной памяти
    cpu_info = psutil.cpu_percent(interval=1)
    ram_info = psutil.virtual_memory().total / (1024 ** 3)  # Преобразуем в ГБ

    # Получение версии операционной системы
    os_version = platform.platform()

    # Сбор информации
    system_info = {
        "user_name": user_name,
        "computer_name": computer_name,
        "cpu_usage_percent": cpu_info,
        "ram_total_gb": ram_info,
        "os_version": os_version,
        "ip_address": ip_address
    }

    # Запись информации на сетевой диск
    write_info_to_network_disk(system_info, ip_address)

    return system_info  # Возвращаем информацию о системе клиенту

