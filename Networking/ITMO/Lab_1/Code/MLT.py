import numpy as np
import matplotlib.pyplot as plt

# Chuỗi bit đầu vào
bit_string = '11010111111100110010000011000010'

# Hàm mã hóa theo phương pháp MLT-3
def mlt3_encoding(bit_string):
    mlt3_signal = []
    current_state = 0
    states = [0, 1, 0, -1]  # Các trạng thái của MLT-3
    state_index = 0

    for bit in bit_string:
        if bit == '1':
            # Nếu gặp bit "1", chuyển trạng thái tiếp theo
            state_index = (state_index + 1) % len(states)
            current_state = states[state_index]
        # Nếu gặp bit "0", giữ nguyên trạng thái hiện tại
        mlt3_signal.append(current_state)
    
    # Tạo tín hiệu có dạng bước bằng cách lặp lại mỗi giá trị hai lần (giống với các tín hiệu trước)
    mlt3_signal_expanded = np.repeat(mlt3_signal, 2)
    
    return mlt3_signal_expanded

# Mã hóa chuỗi bit
mlt3_signal = mlt3_encoding(bit_string)

# Tạo trục thời gian, mỗi bit được chia thành 2 đơn vị (giống như trước)
t = np.arange(0, len(mlt3_signal))

# Vẽ biểu đồ tín hiệu MLT-3
plt.figure(figsize=(12, 3))  # Điều chỉnh kích thước đồ thị
plt.step(t, mlt3_signal, where='post', color='black', linewidth=2)  # Vẽ tín hiệu dạng bước

# Giới hạn trục y từ -1.25 đến 1.25 để hiển thị đủ ba mức tín hiệu
plt.ylim(-1.25, 1.25)

# Vẽ đường trục x đi qua 0
plt.axhline(0, color='black', linewidth=1)

# Giới hạn trục x để nó khớp với tín hiệu
plt.xlim(0, len(mlt3_signal))

# Vẽ các đường dọc tại **ranh giới giữa các bit**
for x in range(2, len(mlt3_signal) + 1, 2):
    plt.axvline(x=x, color='gray', linestyle='--', linewidth=1)

# Thêm các nhãn cho từng bit, nằm giữa nửa đầu và nửa sau của tín hiệu
plt.xticks(np.arange(1, len(mlt3_signal), 2), bit_string, fontsize=12)

# Đặt tiêu đề và nhãn trục
plt.title('MLT-3 Encoding', fontsize=14)
plt.xlabel('Time (bit intervals)', fontsize=12)
plt.ylabel('Signal', fontsize=12)

# Tắt lưới (grid), chỉ vẽ đường ranh giới giữa các bit
plt.grid(False)

plt.show()
