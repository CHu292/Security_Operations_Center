#!/bin/bash
limit=50  # giới hạn số lần fork để tránh sập máy
counter=0

forkbomb() {
    ((counter++))
    if [ "$counter" -lt "$limit" ]; then
        forkbomb & forkbomb &
    else
        sleep 60  # giữ tiến trình để quan sát
    fi
}

forkbomb
