# Hàm chuyển một số từ hệ thập phân sang hệ tam phân
def to_base_3(n):
    digits = []
    while n > 0:
        digits.append(n % 3)
        n //= 3
    return digits[::-1]  # Trả về danh sách các chữ số theo thứ tự đúng

# Hàm kiểm tra tổng các chữ số của số trong hệ tam phân
def sum_base_3_digits(n):
    base_3_digits = to_base_3(n)
    sum = 0
    for i in base_3_digits:
        sum += i
    return sum

# Hàm kiểm tra điều kiện cho một số thỏa mãn yêu cầu
def check_number(n):
    if n % 7 == 0 and n % 5 != 0:
        if sum_base_3_digits(n) == 10:
            return True
    return False

# Tổng các số thỏa mãn điều kiện
def sum_special_numbers():
    total_sum = 0
    for decimal_num in range(4096, 32768):  # Duyệt qua các số có 5 chữ số trong hệ bát phân
        if check_number(decimal_num):
            total_sum += decimal_num
    return total_sum

# Gọi hàm tính tổng
result = sum_special_numbers()
print(result)
