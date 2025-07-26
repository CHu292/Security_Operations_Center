import itertools
import math

# Đọc bản mã từ file
def load_ciphertext(filename="Columnar_Transposition_Cipher_encryption.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().replace('\n', '').strip()

# Giải mã theo hoán vị (key permutation)
def columnar_decrypt(ciphertext, permutation):
    num_cols = len(permutation)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    total_cells = num_cols * num_rows
    padding = total_cells - len(ciphertext)

    col_lengths = [num_rows] * num_cols
    for i in range(padding):
        col_idx = permutation.index(num_cols - i)
        col_lengths[col_idx] -= 1

    cols = [''] * num_cols
    index = 0
    sorted_perm = sorted(range(num_cols), key=lambda x: permutation[x])
    for col_pos in sorted_perm:
        length = col_lengths[col_pos]
        cols[col_pos] = ciphertext[index:index + length]
        index += length

    plaintext = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if row < len(cols[col]):
                plaintext += cols[col][row]
    return plaintext

# Phân tích theo Crib
def crib_attack(ciphertext, crib, min_key_len=2, max_key_len=6):
    results = []
    for key_len in range(min_key_len, max_key_len + 1):
        base = list(range(1, key_len + 1))
        for perm in itertools.permutations(base):
            try:
                plaintext = columnar_decrypt(ciphertext, list(perm))
                if crib.lower() in plaintext.lower():
                    results.append((perm, plaintext))
            except Exception:
                continue
    return results

# Ghi kết quả ra file
def save_results(results, filename="Columnar_Transposition_Crib_Results.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for perm, text in results:
            f.write(f"Key permutation {perm}:\n{text}\n\n")

# =========================
# Chương trình chính
# =========================
if __name__ == "__main__":
    ciphertext = load_ciphertext("Columnar_Transposition_Cipher_encryption.txt")
    crib = input("🔍 Nhập từ bạn nghi ngờ xuất hiện trong bản rõ (crib): ").strip()
    results = crib_attack(ciphertext, crib, min_key_len=2, max_key_len=6)
    save_results(results)
    print(f"Phân tích Crib hoàn tất. Đã lưu {len(results)} kết quả vào 'Columnar_Transposition_Crib_Results.txt'")
