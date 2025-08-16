import re
from collections import defaultdict, Counter
from math import gcd
from functools import reduce

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def find_repeat_sequences(ciphertext, seq_len=3):
    """
    Tìm các cụm lặp lại có độ dài seq_len
    """
    seq_positions = defaultdict(list)
    for i in range(len(ciphertext) - seq_len + 1):
        seq = ciphertext[i:i + seq_len]
        seq_positions[seq].append(i)
    
    # Chỉ giữ lại những cụm lặp lại nhiều hơn 1 lần
    return {seq: pos for seq, pos in seq_positions.items() if len(pos) > 1}

def calculate_distances(repeats):
    """
    Tính khoảng cách giữa các lần xuất hiện lặp lại
    """
    distances = []
    for positions in repeats.values():
        for i in range(len(positions) - 1):
            dist = positions[i+1] - positions[i]
            distances.append(dist)
    return distances

def find_factors(number):
    """
    Trả về danh sách các ước số > 1 của một số
    """
    return [i for i in range(2, number + 1) if number % i == 0]

def kasiski_examination(ciphertext, min_seq_len=3, max_seq_len=5):
    """
    Thực hiện tấn công Kasiski để tìm độ dài khóa khả dĩ
    """
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    all_distances = []

    for seq_len in range(min_seq_len, max_seq_len + 1):
        repeats = find_repeat_sequences(ciphertext, seq_len)
        distances = calculate_distances(repeats)
        all_distances.extend(distances)

    # Lấy tất cả ước số của khoảng cách
    factor_counts = Counter()
    for dist in all_distances:
        factors = find_factors(dist)
        factor_counts.update(factors)

    # Trả về danh sách các độ dài khóa khả dĩ, sắp xếp theo tần suất
    most_likely = factor_counts.most_common()
    return most_likely

if __name__ == "__main__":
    ciphertext = read_file("Vigenere_encryption.txt")
    results = kasiski_examination(ciphertext)

    print("Ước lượng độ dài khóa (theo Kasiski Examination):")
    for factor, count in results:
        print(f"  - Độ dài khóa {factor}: xuất hiện {count} lần")
