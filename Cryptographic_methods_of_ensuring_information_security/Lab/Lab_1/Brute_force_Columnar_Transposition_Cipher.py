import itertools
import math

# Đọc bản mã từ file
def load_ciphertext(filename="Columnar_Transposition_Cipher_encryption.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().replace('\n', '').strip()

# Giải mã với một hoán vị (key) cụ thể
def columnar_decrypt(ciphertext, permutation):
    num_cols = len(permutation)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    total_cells = num_cols * num_rows
    padding = total_cells - len(ciphertext)

    # Tính độ dài từng cột
    col_lengths = [num_rows] * num_cols
    for i in range(padding):
        col_idx = permutation.index(num_cols - i)  # col từ 1-based
        col_lengths[col_idx] -= 1

    # Cắt bản mã thành các cột dựa vào thứ tự trong permutation
    cols = [''] * num_cols
    index = 0
    sorted_perm = sorted(range(num_cols), key=lambda x: permutation[x])
    for col_pos in sorted_perm:
        length = col_lengths[col_pos]
        cols[col_pos] = ciphertext[index:index + length]
        index += length

    # Ghép lại bản rõ theo hàng
    plaintext = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if row < len(cols[col]):
                plaintext += cols[col][row]

    return plaintext

# Thử tất cả permutation từ key length 2 đến 6, giá trị từ 1 đến n
def brute_force_columnar(ciphertext, min_key_len=2, max_key_len=6):
    results = []
    for key_len in range(min_key_len, max_key_len + 1):
        base = list(range(1, key_len + 1))  # khóa từ 1 đến n
        for perm in itertools.permutations(base):
            try:
                plaintext = columnar_decrypt(ciphertext, list(perm))
                results.append((perm, plaintext))
            except Exception:
                continue
    return results

# Ghi kết quả ra file
def save_results(results, filename="Columnar_Transposition_Brute_Force_Results.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for perm, text in results:
            f.write(f"Key permutation {perm}:\n{text}\n\n")

# =========================
# Chạy chương trình chính
# =========================
if __name__ == "__main__":
    ciphertext = load_ciphertext("Columnar_Transposition_Cipher_encryption.txt")
    results = brute_force_columnar(ciphertext, min_key_len=2, max_key_len=6)
    save_results(results)
    print("Brute-force hoàn tất. Kết quả lưu tại 'Columnar_Transposition_Brute_Force_Results.txt'")
