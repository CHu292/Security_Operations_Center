import random

def generate_random_numbers(filename, N, max_value=50):
    # Tạo một tập hợp các số ngẫu nhiên không trùng nhau
    random_numbers = random.sample(range(1, max_value + 1), N)
    
    # Ghi vào file
    with open(filename, 'w') as f:
        f.write(f"{N}\n")  # Ghi số lượng N
        for num in random_numbers:
            f.write(f"{num}\n")  # Ghi các số ngẫu nhiên


# Hàm tìm tổng lớn nhất của 3 số chia hết cho 3
def max_sum_divisible_by_3(filename):
    # Đọc file và lấy dãy số
    with open(filename, 'r') as f:
        N = int(f.readline())  # Số lượng phần tử
        numbers = [int(f.readline()) for _ in range(N)]  # Các số tự nhiên

    # Chia các số theo phần dư khi chia cho 3
    mod_0 = []  # Các số có phần dư 0
    mod_1 = []  # Các số có phần dư 1
    mod_2 = []  # Các số có phần dư 2

    for num in numbers:
        if num % 3 == 0:
            mod_0.append(num)
        elif num % 3 == 1:
            mod_1.append(num)
        else:
            mod_2.append(num)

    # Sắp xếp các nhóm số để dễ chọn ra các số lớn nhất
    mod_0.sort(reverse=True)
    mod_1.sort(reverse=True)
    mod_2.sort(reverse=True)

    # Khởi tạo các tổ hợp có thể
    candidates = []

    # 1. Chọn 3 số từ nhóm mod_0
    if len(mod_0) >= 3:
        candidates.append(sum(mod_0[:3]))

    # 2. Chọn 3 số từ nhóm mod_1
    if len(mod_1) >= 3:
        candidates.append(sum(mod_1[:3]))

    # 3. Chọn 3 số từ nhóm mod_2
    if len(mod_2) >= 3:
        candidates.append(sum(mod_2[:3]))

    # 4. Chọn 1 số từ mỗi nhóm
    if len(mod_0) >= 1 and len(mod_1) >= 1 and len(mod_2) >= 1:
        candidates.append(mod_0[0] + mod_1[0] + mod_2[0])

    # Trả về tổng lớn nhất chia hết cho 3
    if candidates:
        return max(candidates)
    else:
        return 0


# Sử dụng hàm để tạo file A và B với số lượng số ngẫu nhiên khác nhau
N_A = int(input("Enter n_a: ")) # Số lượng ngẫu nhiên cho file A
N_B = int(input("Enter n_b: "))  # Số lượng ngẫu nhiên cho file B

generate_random_numbers('A.txt', N_A)
generate_random_numbers('B.txt', N_B)

# Tính toán kết quả cho file A và B
result_A = max_sum_divisible_by_3('A.txt')
result_B = max_sum_divisible_by_3('B.txt')

# In ra kết quả
print("Result of file A:", result_A)
print("Result of file B:", result_B)