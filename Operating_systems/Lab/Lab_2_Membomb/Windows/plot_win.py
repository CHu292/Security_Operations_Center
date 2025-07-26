import matplotlib.pyplot as plt

times = []
available = []

with open("win_membomb.txt") as f:
    lines = f.readlines()[1:]  # bỏ dòng tiêu đề
    for line in lines:
        time, avail = line.strip().split()
        times.append(int(time))
        available.append(int(avail))

plt.figure(figsize=(10, 5))
plt.plot(times, available, marker='o', linestyle='-', color='blue', label='RAM khả dụng (MB)')
plt.xlabel('Thời điểm (block số)')
plt.ylabel('Dung lượng RAM khả dụng (MB)')
plt.title('Biểu đồ RAM khả dụng khi thực thi membomb trên Windows')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("win_membomb_chart.png")
plt.show()
