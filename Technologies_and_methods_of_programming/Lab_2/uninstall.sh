#!/bin/bash

# Thư mục cài đặt là thư mục hiện tại
INSTALL_DIR="$PWD"
INSTALL_FLAG="$INSTALL_DIR/installed.flag"

# Xóa tệp cờ cài đặt
if [ -f "$INSTALL_FLAG" ]; then
    rm "$INSTALL_FLAG"
    echo "Chương trình đã được gỡ cài đặt."
else
    echo "Chương trình không được cài đặt."
    exit 1
fi

# Xóa tệp chương trình
if [ -f "$INSTALL_DIR/user_data.txt" ]; then
    rm "$INSTALL_DIR/user_data.txt"
    echo "Tệp user_data.txt đã bị xóa."
fi

# Giữ lại tệp limit_data.txt để bảo lưu dữ liệu giới hạn
if [ -f "$INSTALL_DIR/limit_data.txt" ]; then
    echo "Tệp limit_data.txt được giữ lại để bảo lưu giới hạn sử dụng trước đó."
fi

