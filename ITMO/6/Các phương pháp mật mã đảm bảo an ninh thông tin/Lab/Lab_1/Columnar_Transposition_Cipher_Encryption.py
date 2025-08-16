import math

# Đọc văn bản từ file input.txt
def load_plaintext(filename="input.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().replace('\n', '').replace(' ', '').upper()

# Đọc khóa từ file Columnar_Transposition_Cipher_key.txt
def load_key(filename="Columnar_Transposition_Cipher_key.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        key_line = f.read().strip()
        if ' ' in key_line:
            key = list(map(int, key_line.split()))
        else:
            key = [int(c) for c in key_line]
        return key

# Mã hóa Columnar Transposition Cipher
def columnar_encrypt(plaintext, key):
    num_cols = len(key)
    num_rows = math.ceil(len(plaintext) / num_cols)

    # Thêm padding nếu cần
    padded_len = num_cols * num_rows
    plaintext += 'X' * (padded_len - len(plaintext))

    # Tạo bảng theo hàng
    grid = []
    index = 0
    for _ in range(num_rows):
        grid.append(plaintext[index:index + num_cols])
        index += num_cols

    # Đọc theo thứ tự cột đã sắp xếp
    ciphertext = ''
    sorted_key = sorted((num, idx) for idx, num in enumerate(key))
    for _, col_idx in sorted_key:
        for row in grid:
            ciphertext += row[col_idx]

    return ciphertext

# Ghi bản mã ra file
def save_ciphertext(ciphertext, filename="Columnar_Transposition_Cipher_encryption.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(ciphertext)

# =========================
# Chạy chương trình chính
# =========================
if __name__ == "__main__":
    plaintext = load_plaintext("input.txt")
    key = load_key("Columnar_Transposition_Cipher_key.txt")
    ciphertext = columnar_encrypt(plaintext, key)
    save_ciphertext(ciphertext, "Columnar_Transposition_Cipher_encryption.txt")
    print("Đã mã hóa xong. Kết quả lưu trong 'Columnar_Transposition_Cipher_encryption.txt'")
