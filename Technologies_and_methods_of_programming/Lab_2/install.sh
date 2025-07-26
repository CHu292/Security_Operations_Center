#!/bin/bash

INSTALL_DIR="$PWD"
INSTALL_FLAG="$INSTALL_DIR/installed.flag"
LIMIT_FILE="$INSTALL_DIR/limit_data.txt"

# Kiểm tra xem chương trình đã được cài đặt trước đó chưa
if [ -f "$INSTALL_FLAG" ]; then
    echo "Chương trình đã được cài đặt trước đó. Vui lòng gỡ cài đặt trước khi cài đặt lại."
    exit 1
fi

# Tạo file đánh dấu cài đặt
touch "$INSTALL_FLAG"

# Tạo file `user_data.txt` nếu chưa tồn tại
if [ ! -f "$INSTALL_DIR/user_data.txt" ]; then
    touch "$INSTALL_DIR/user_data.txt"
    echo "File user_data.txt đã được tạo."
else
    echo "File user_data.txt đã tồn tại."
fi

# Kiểm tra nếu file `limit_data.txt` tồn tại từ lần cài đặt trước
if [ -f "$LIMIT_FILE" ]; then
    echo "Chương trình đã từng được cài đặt trước trên máy tính này."
    starts=$(grep "starts" "$LIMIT_FILE" | cut -d':' -f2)
    time_used=$(grep "time" "$LIMIT_FILE" | cut -d':' -f2)
    echo "Số lần sử dụng trước đó: $starts, Thời gian sử dụng trước đó: $time_used giây."

    # Kiểm tra nếu giới hạn đã đạt
    MAX_STARTS=5
    TIME_LIMIT=30
    if (( starts >= MAX_STARTS || time_used >= TIME_LIMIT )); then
        echo "Giới hạn sử dụng đã đạt từ trước. Vui lòng mua phiên bản đầy đủ hoặc gỡ cài đặt."
        exit 1
    fi
else
    # Nếu file `limit_data.txt` chưa tồn tại, tạo file với giới hạn ban đầu
    echo "starts:0" > "$LIMIT_FILE"
    echo "time:0" >> "$LIMIT_FILE"
    echo "File limit_data.txt đã được tạo."
fi

echo "Chương trình đã được cài đặt thành công. Để khởi động chương trình, hãy dùng lệnh: './simple_program.py'."
