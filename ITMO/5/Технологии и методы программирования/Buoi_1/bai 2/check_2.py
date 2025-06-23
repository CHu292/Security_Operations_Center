import random


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



# Tính toán kết quả cho file A và B
result_A = max_sum_divisible_by_3('A.txt')
result_B = max_sum_divisible_by_3('B.txt')

# In ra kết quả
print("Tổng lớn nhất chia hết cho 3 của file A:", result_A)
print("Tổng lớn nhất chia hết cho 3 của file B:", result_B)