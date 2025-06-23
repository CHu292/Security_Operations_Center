#!/bin/bash

INSTALL_DIR="$PWD"
INSTALL_FLAG="$INSTALL_DIR/installed.flag"

# Удаление файла-флага установки
if [ -f "$INSTALL_FLAG" ]; then
    rm "$INSTALL_FLAG"
    echo "Программа была удалена."
else
    echo "Программа не установлена."
    exit 1
fi

# Удаление файла user_data.txt, но сохранение limit_data.txt
if [ -f "$INSTALL_DIR/user_data.txt" ]; then
    rm "$INSTALL_DIR/user_data.txt"
    echo "Файл user_data.txt был удален."
fi

# Сохранение файла limit_data.txt для сохранения предыдущих данных лимита
if [ -f "$INSTALL_DIR/limit_data.txt" ]; then
    echo "Файл limit_data.txt сохраняется для сохранения предыдущих данных использования."
fi

