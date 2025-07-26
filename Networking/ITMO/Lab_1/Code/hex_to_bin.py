def hex_to_bin(hex_code):
    # Xóa khoảng trắng khỏi chuỗi hexadecimal
    hex_code = hex_code.replace(" ", "")
    
    # Chuyển mã hexadecimal sang số nhị phân
    bin_code = bin(int(hex_code, 16))[2:]
    
    # Đảm bảo độ dài nhị phân bằng 4 lần số chữ số của mã hexadecimal
    return bin_code.zfill(len(hex_code) * 4)

# Ví dụ sử dụng
hex_code = input("Nhập mã hexadecimal: ")
bin_code = hex_to_bin(hex_code)
print(f"Mã nhị phân tương ứng: {bin_code}")
