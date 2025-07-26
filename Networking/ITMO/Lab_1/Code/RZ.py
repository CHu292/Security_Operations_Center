import numpy as np
import matplotlib.pyplot as plt

# Chuỗi bit đầu vào
bit_string = '11010111111100110010000011000010'

# Hàm mã hóa theo phương pháp RZ
def rz_encoding_custom(bit_string):
    rz_signal = []
    
    for bit in bit_string:
        if bit == '1':
            rz_signal.extend([1, 0])  # Tín hiệu 1: nửa đầu lên 1, nửa sau về 0
        else:
            rz_signal.extend([-1, 0])  # Tín hiệu 0: nửa đầu xuống -1, nửa sau về 0
    
    return rz_signal

# Mã hóa chuỗi bit
rz_signal = rz_encoding_custom(bit_string)

# Tạo trục thời gian, mỗi bit được chia thành 2 đơn vị (nửa đầu và nửa sau)
t = np.arange(0, len(rz_signal))

# Vẽ biểu đồ tín hiệu RZ
plt.figure(figsize=(12, 3))  # Điều chỉnh kích thước đồ thị
plt.step(t, rz_signal, where='post', color='black', linewidth=2)  # Vẽ tín hiệu dạng bước

# Giới hạn trục y từ -1.25 đến 1.25
plt.ylim(-1.25, 1.25)

# Vẽ đường trục x đi qua 0
plt.axhline(0, color='black', linewidth=1)

# Giới hạn trục x để nó khớp với tín hiệu
plt.xlim(0, len(rz_signal))

# Vẽ các đường dọc tại **ranh giới giữa các bit**
for x in range(2, len(rz_signal) + 1, 2):
    plt.axvline(x=x, color='gray', linestyle='--', linewidth=1)

# Thêm các nhãn cho từng bit, nằm giữa nửa đầu và nửa sau của tín hiệu
plt.xticks(np.arange(1, len(rz_signal), 2), bit_string, fontsize=12)

# Đặt tiêu đề và nhãn trục
plt.title('RZ Encoding', fontsize=14)
plt.xlabel('Time (bit intervals)', fontsize=12)
plt.ylabel('Signal', fontsize=12)

# Tắt lưới (grid), chỉ vẽ đường ranh giới giữa các bit
plt.grid(False)

plt.show()

