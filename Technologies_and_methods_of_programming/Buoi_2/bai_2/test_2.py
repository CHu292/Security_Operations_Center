def max_product_with_gap(arr):
    N = len(arr)
    max_so_far = arr[0]
    max_product = 0

    for i in range(8, N):
        max_product = max(max_product, arr[i] * max_so_far)
        max_so_far = max(max_so_far, arr[i - 7])  # Cập nhật giá trị tối đa cho cửa sổ

    return max_product

# Hàm đọc dữ liệu từ tệp và tính toán kết quả
def process_file(filename):
    with open(filename, 'r') as file:
        N = int(file.readline().strip())  # Đọc số lượng phần tử
        arr = [int(file.readline().strip()) for _ in range(N)]  # Đọc các phần tử vào mảng

    return max_product_with_gap(arr)

# Xử lý tệp A.txt và B.txt
result_A = process_file('A.txt')
result_B = process_file('B.txt')

# In kết quả
print(f"Giá trị sản phẩm lớn nhất từ file A: {result_A}")
print(f"Giá trị sản phẩm lớn nhất từ file B: {result_B}")
