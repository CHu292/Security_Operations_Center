import os
import re
import time
from datetime import datetime

MONITORED_DIR = os.path.expanduser("~/Desktop/Task_1/dlp_test")
LOG_FILE = os.path.expanduser("~/Desktop/Task_1/dlp_alerts.log")

PATTERNS = {
    "Credit Card": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
    "Passport Number": re.compile(r"\b[A-Z]{2}\d{7}\b")
}

def write_log(message):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as logf:
            logf.write(message + "\n")
        print(f"[LOG] {message}")
    except Exception as e:
        print(f"[ERROR] Failed to write log: {e}")

def scan_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            for label, pattern in PATTERNS.items():
                if pattern.search(content):
                    log = f"[{datetime.now()}] {label} detected in {filepath}"
                    write_log(log)
    except Exception as e:
        print(f"[ERROR] Cannot read file {filepath}: {e}")

def monitor():
    print(f"Monitoring folder: {MONITORED_DIR}")
    while True:
        for root, _, files in os.walk(MONITORED_DIR):
            for name in files:
                path = os.path.join(root, name)
                scan_file(path)
        time.sleep(3)

if __name__ == "__main__":
    if not os.path.exists(MONITORED_DIR):
        os.makedirs(MONITORED_DIR)
        print(f"Created folder: {MONITORED_DIR}")
    monitor()
