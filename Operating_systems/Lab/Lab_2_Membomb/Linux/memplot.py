import psutil
import matplotlib.pyplot as plt
import time

mem_used = []
timestamps = []

for i in range(60):  # 60 giây theo dõi
    mem = psutil.virtual_memory()
    mem_used.append(mem.available / (1024 * 1024))  # MB
    timestamps.append(i)
    print(f"Time {i}s - Available RAM: {mem.available / (1024*1024):.2f} MB")
    time.sleep(1)

plt.plot(timestamps, mem_used, label='RAM trống (MB)')
plt.xlabel('Thời gian (giây)')
plt.ylabel('RAM trống (MB)')
plt.title('Biểu đồ RAM theo thời gian')
plt.grid(True)
plt.legend()
plt.show()
