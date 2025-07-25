import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Đọc dữ liệu từ CSV
df = pd.read_csv("process_monitor.csv")

# Chuyển cột Time (định dạng HH:mm:ss) sang datetime
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')

# Tính thời gian tương đối (giây từ thời điểm đầu tiên)
t0 = df['Time'][0]
df['RelativeTime'] = (df['Time'] - t0).dt.total_seconds()

# Vẽ biểu đồ
plt.plot(df['RelativeTime'], df['Count'], marker='o')
plt.title("Số lượng tiến trình theo thời gian")
plt.xlabel("Thời gian (giây từ lúc bắt đầu)")
plt.ylabel("Số lượng tiến trình")
plt.grid(True)
plt.tight_layout()
plt.show()
