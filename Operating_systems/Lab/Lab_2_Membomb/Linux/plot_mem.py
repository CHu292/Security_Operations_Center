import matplotlib.pyplot as plt

with open("membomb.txt") as f:
    lines = f.readlines()

free_list = []
avail_list = []
time_list = []

for i, line in enumerate(lines):
    if line.startswith("Mem:"):
        parts = line.split()
        free_mem = int(parts[3])
        avail_mem = int(parts[6])
        free_list.append(free_mem)
        avail_list.append(avail_mem)
        time_list.append(len(free_list))

plt.figure(figsize=(12, 6))
plt.plot(time_list, free_list, label="RAM trống (free)", marker='o', linewidth=2)
plt.plot(time_list, avail_list, label="RAM khả dụng (available)", marker='x', linewidth=2, linestyle='--')

plt.xlabel("Thời điểm (lần log)", fontsize=12)
plt.ylabel("Dung lượng RAM (MB)", fontsize=12)
plt.title("Biểu đồ suy giảm bộ nhớ khi thực thi membomb", fontsize=14, weight='bold')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig("membomb_chart.png")  # lưu ảnh nếu cần
plt.show()
