# Hàm kiểm tra xem một chuỗi có phải là dãy không giảm không
def is_non_decreasing(oct_str):
    # So sánh từng chữ số với chữ số trước nó
    for i in range(len(oct_str) - 1):
        if oct_str[i] > oct_str[i + 1]:
            return False
    return True

def decimal_to_octal(n):
    if n == 0:
        return "0"
    
    octal_digits = []
    
    # Lặp lại cho đến khi n = 0
    while n > 0:
        remainder = n % 8  # Lấy phần dư khi chia cho 8
        octal_digits.append(str(remainder))  # Lưu lại phần dư
        n = n // 8  # Chia lấy phần nguyên
    
    # Đảo ngược danh sách vì các phần dư được tính từ hàng đơn vị trở lên
    octal_digits.reverse()
    
    # Ghép các chữ số lại thành chuỗi
    return ''.join(octal_digits)

# Đếm các số lẻ thỏa mãn điều kiện
def count_odd_non_decreasing_numbers():
    count = 0
    # Duyệt qua các số từ 100 đến 9999
    for num in range(100, 10000):
        if num % 2 == 1:  # Chỉ xét các số lẻ
            oct_str = decimal_to_octal(num)  
            if is_non_decreasing(oct_str):  # Kiểm tra dãy không giảm
                count += 1
    return count

# Gọi hàm và in kết quả
result = count_odd_non_decreasing_numbers()
print("Число удовлетворяющих нечетным числам равно:", result)
