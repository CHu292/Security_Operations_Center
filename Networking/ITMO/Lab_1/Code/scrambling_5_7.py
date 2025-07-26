def scrambling(input_bits):
    n = len(input_bits)
    
    # Tạo một danh sách chứa các bit B_i, ban đầu khởi tạo tất cả bằng 0
    B = [0] * n

    # Quy ước ban đầu: các bit B trước khi tính toán (B_0, ..., B_6) là 0
    for i in range(n):
        # Lấy bit A_i từ chuỗi nhập vào
        A_i = int(input_bits[i])
        
        # Tính toán B_i theo công thức B_i = A_i XOR B_{i-5} XOR B_{i-7}
        B_i_minus_5 = B[i - 5] if i >= 5 else 0
        B_i_minus_7 = B[i - 7] if i >= 7 else 0
        
        # Tính giá trị của B_i
        B[i] = A_i ^ B_i_minus_5 ^ B_i_minus_7
    
    # Trả về dãy bit sau khi thực hiện scrambling
    return ''.join(map(str, B))

# Nhập chuỗi bit từ người dùng
input_bits = input("Nhập chuỗi bit: ")

# Kiểm tra đầu vào là dãy bit hợp lệ
if all(bit in '01' for bit in input_bits):
    # Gọi hàm scrambling và in kết quả
    result = scrambling(input_bits)
    print(f"Chuỗi bit sau khi thực hiện scrambling: {result}")
else:
    print("Chuỗi nhập vào không hợp lệ. Vui lòng chỉ nhập các bit 0 và 1.")
