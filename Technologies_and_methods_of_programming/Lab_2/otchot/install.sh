    #!/bin/bash

    INSTALL_DIR="$PWD"
    INSTALL_FLAG="$INSTALL_DIR/installed.flag"
    LIMIT_FILE="$INSTALL_DIR/limit_data.txt"

    # Проверка, была ли программа установлена ранее
    if [ -f "$INSTALL_FLAG" ]; then
        echo "Программа уже была установлена ранее. Пожалуйста, удалите ее перед повторной установкой."
        exit 1
    fi

    # Создание файла-флага установки
    touch "$INSTALL_FLAG"

    # Создание файла `user_data.txt`, если он еще не существует
    if [ ! -f "$INSTALL_DIR/user_data.txt" ]; then
        touch "$INSTALL_DIR/user_data.txt"
        echo "Файл user_data.txt был создан."
    else
        echo "Файл user_data.txt уже существует."
    fi

    # Проверка, существует ли файл `limit_data.txt` с предыдущей установки
    if [ -f "$LIMIT_FILE" ]; then
        echo "Программа уже была установлена на этом компьютере."
        starts=$(grep "starts" "$LIMIT_FILE" | cut -d':' -f2)
        time_used=$(grep "time" "$LIMIT_FILE" | cut -d':' -f2)
        echo "Количество предыдущих запусков: $starts, Время использования ранее: $time_used секунд."
    else
        # Если файл `limit_data.txt` еще не существует, создаем файл с начальным лимитом
        echo "starts:0" > "$LIMIT_FILE"
        echo "time:0" >> "$LIMIT_FILE"
        echo "Файл limit_data.txt был создан."
    fi

    echo "Программа была успешно установлена. Чтобы запустить программу, используйте команду: './simple_program.py'."

