import numpy as np
import matplotlib.pyplot as plt

# Chuỗi bit đầu vào
bit_string = '11010111111100110010000011000010'

# Hàm mã hóa theo phương pháp PAM-5
def pam5_encoding(bit_string):
    pam5_signal = []
    
    # Chia chuỗi bit thành các cặp bit
    bit_pairs = [bit_string[i:i+2] for i in range(0, len(bit_string), 2)]
    
    # Ánh xạ mỗi cặp bit thành mức PAM-5
    for pair in bit_pairs:
        if pair == '00':
            pam5_signal.append(-2)
        elif pair == '01':
            pam5_signal.append(-1)
        elif pair == '10':
            pam5_signal.append(2)
        elif pair == '11':
            pam5_signal.append(1)
    
    return pam5_signal

# Mã hóa chuỗi bit
pam5_signal = pam5_encoding(bit_string)

# Tạo trục thời gian, mỗi tín hiệu ứng với 2 bit (thời gian vẫn chia đơn vị theo từng bit)
t = np.arange(0, 2 * len(pam5_signal))

# Mở rộng tín hiệu để tương ứng với từng bit (mỗi giá trị tín hiệu được lặp lại 2 lần)
expanded_signal = np.repeat(pam5_signal, 2)

# Vẽ biểu đồ tín hiệu PAM-5
plt.figure(figsize=(12, 3))  # Điều chỉnh kích thước đồ thị
plt.step(t, expanded_signal, where='post', color='black', linewidth=2)  # Vẽ tín hiệu dạng bước

# Giới hạn trục y từ -2.5 đến 2.5
plt.ylim(-2.5, 2.5)

# Vẽ đường trục x đi qua 0
plt.axhline(0, color='black', linewidth=1)

# Giới hạn trục x để nó khớp với tín hiệu
plt.xlim(0, len(expanded_signal) - 1)

# Vẽ các đường dọc tại **ranh giới giữa các bit**
for x in range(1, len(expanded_signal)):
    plt.axvline(x=x, color='gray', linestyle='--', linewidth=1)

# Thêm các nhãn cho từng bit trên trục x, đặt ở giữa mỗi nửa tín hiệu
plt.xticks(np.arange(0.5, len(expanded_signal), 1), list(bit_string), fontsize=12)

# Đặt tiêu đề và nhãn trục
plt.title('PAM-5 Encoding', fontsize=14)
plt.xlabel('Time (bit intervals)', fontsize=12)
plt.ylabel('Signal', fontsize=12)
plt.grid(False)  # Tắt lưới, chỉ vẽ đường chia ranh giới

plt.show()
