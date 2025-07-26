def max_product_from_file(file_name):
    # Đọc dữ liệu từ file
    with open(file_name, 'r') as f:
        N = int(f.readline().strip())
        sequence = [int(f.readline().strip()) for _ in range(N)]
    
    if N <= 8:
        return "Lỗi: Dữ liệu trong file quá ít phần tử để tính toán."

    # Danh sách lưu giá trị lớn nhất từ chỉ số hiện tại đến hết danh sách
    max_from_right = [0] * N

    # Tính giá trị lớn nhất từ chỉ số hiện tại đến hết danh sách
    max_from_right[-1] = sequence[-1]
    for i in range(N - 2, -1, -1):
        max_from_right[i] = max(sequence[i], max_from_right[i + 1])
    
    max_product_value = float('-inf')  # Khởi tạo với giá trị nhỏ nhất có thể

    # Duyệt tất cả các chỉ số i và j sao cho j >= i + 8
    for i in range(N - 8):
        product = sequence[i] * max_from_right[i + 8]
        if product > max_product_value:
            max_product_value = product
    
    return max_product_value

# Tính toán cho file A.txt và B.txt
result_A = max_product_from_file('A.txt')
result_B = max_product_from_file('B.txt')

# In kết quả
print(f"MAX A: {result_A}")
print(f"MAX B: {result_B}")
