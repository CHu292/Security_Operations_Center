#!/usr/bin/env python3
import os
import time
import hashlib
import threading
import sys

INSTALL_DIR = os.getcwd()
USER_FILE = os.path.join(INSTALL_DIR, "user_data.txt")
LIMIT_FILE = os.path.join(INSTALL_DIR, "limit_data.txt")
INSTALL_FLAG = os.path.join(INSTALL_DIR, "installed.flag")
MAX_STARTS = 5
TIME_LIMIT = 30  # Ограничение времени использования (в секундах)

def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()

def check_user_exists(full_name):
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                if hash_string(full_name) in line:
                    return True
    return False

def add_user(full_name):
    with open(USER_FILE, "a") as file:
        file.write(hash_string(full_name) + "\n")

def check_limits():
    """Проверка лимитов доступа и времени."""
    if not os.path.exists(LIMIT_FILE):
        with open(LIMIT_FILE, "w") as file:
            file.write(f"starts:0\ntime:0\n")

    with open(LIMIT_FILE, "r") as file:
        data = file.readlines()
        starts = int(data[0].split(":")[1].strip())
        used_time = int(data[1].split(":")[1].strip())

    if starts >= MAX_STARTS:
        return False, "Вы достигли лимита количества запусков. Пожалуйста, купите полную версию или удалите программу."
    if used_time >= TIME_LIMIT:
        return False, "Вы достигли лимита времени использования. Пожалуйста, купите полную версию или удалите программу."

    return True, ""

def update_limits(start_time):
    """Обновление количества запусков и времени использования."""
    with open(LIMIT_FILE, "r") as file:
        data = file.readlines()
        starts = int(data[0].split(":")[1].strip()) + 1
        used_time = int(data[1].split(":")[1].strip()) + int(time.time() - start_time)

    with open(LIMIT_FILE, "w") as file:
        file.write(f"starts:{starts}\ntime:{used_time}\n")

    return starts, used_time

def countdown_timer(remaining_time, program_running):
    """Обратный отсчет времени использования."""
    while remaining_time > 0 and program_running.is_set():
        time.sleep(1)
        remaining_time -= 1
    if remaining_time <= 0:
        program_running.clear()

def check_installation():
    """Проверка, установлена ли программа."""
    if not os.path.exists(INSTALL_FLAG):
        print("Программа не установлена. Пожалуйста, установите ее перед запуском.")
        sys.exit(1)

def main():
    check_installation()
    allowed, message = check_limits()
    if not allowed:
        print(message)
        sys.exit(1)

    start_time = time.time()
    program_running = threading.Event()
    program_running.set()
    remaining_time = TIME_LIMIT
    timer_thread = threading.Thread(target=countdown_timer, args=(remaining_time, program_running))
    timer_thread.start()

    try:
        full_name = input("Введите ваше полное имя: ")
        if not program_running.is_set():
            print("\nВремя использования истекло.")
            sys.exit(1)

        if check_user_exists(full_name):
            print("Ваше имя уже сохранено в системе.")
        else:
            add_user(full_name)
            print("Ваша информация была сохранена.")

        action = input("Введите 'show', чтобы увидеть оставшиеся лимиты, или нажмите Enter, чтобы выйти: ")
        if action == "show":
            starts, used_time = update_limits(start_time)
            remaining_starts = MAX_STARTS - starts
            remaining_time_overall = TIME_LIMIT - used_time
            remaining_minutes = remaining_time_overall // 60
            remaining_seconds = remaining_time_overall % 60
            print(f"Осталось запусков: {remaining_starts}, Время: {remaining_minutes} минут {remaining_seconds} секунд.")
        
        program_running.clear()
    except KeyboardInterrupt:
        print("\nПрограмма была остановлена.")
        program_running.clear()

    timer_thread.join()

    starts, used_time = update_limits(start_time)
    if used_time >= TIME_LIMIT or starts >= MAX_STARTS:
        print("Достигнут лимит. Пожалуйста, купите полную версию или удалите программу.")
        sys.exit(1)

if __name__ == "__main__":
    main()

