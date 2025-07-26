import matplotlib.pyplot as plt
import numpy as np

# Chuỗi bit cần vẽ
bit_stream = '11010000 11010100 00101001 11011111'
bits = [int(b) for b in bit_stream.replace(' ', '')]

# Số lượng bit và thời gian tương ứng với mỗi bit
n_bits = len(bits)
t = np.arange(0, n_bits + 1)

# Tín hiệu NRZ - bit "1" là 1, bit "0" là -1
signal = np.repeat([1 if bit == 1 else -1 for bit in bits], 2)

# Trục thời gian
time = np.arange(0, len(signal)) / 2

# Vẽ tín hiệu NRZ
plt.figure(figsize=(12, 4))
plt.step(time, signal, where='post', label='NRZ', color='black', linewidth=2)

# Giới hạn trục y từ -1.25 đến 1.25
plt.ylim(-1.25, 1.25)

# Vẽ đường trục x đi qua y = 0
plt.axhline(0, color='black', linewidth=1)

# Giới hạn trục x để nó khớp với tín hiệu
plt.xlim(0, len(bits))

# Vẽ các đường dọc tại **ranh giới giữa các bit**
for x in range(1, len(bits)):
    plt.axvline(x=x, color='gray', linestyle='--', linewidth=1)

# Đặt các nhãn cho từng bit, nằm ở giữa các khoảng tín hiệu
bit_labels = list(bit_stream.replace(' ', ''))  # Loại bỏ khoảng trống
plt.xticks(np.arange(0.5, len(bits) + 0.5, 1), bit_labels, fontsize=12)

# Đặt tiêu đề và nhãn trục
plt.title('NRZ Encoding', fontsize=14)
plt.xlabel('Time (bit intervals)', fontsize=12)
plt.ylabel('Signal', fontsize=12)

# Tắt lưới (grid), chỉ vẽ đường ranh giới giữa các bit
plt.grid(False)

plt.show()

