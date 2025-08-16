import math

# Đọc bản mã từ file
def load_ciphertext(filename="Columnar_Transposition_Cipher_encryption.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().replace('\n', '').strip()

# Đọc khóa từ file
def load_key(filename="Columnar_Transposition_Cipher_key.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        key_line = f.read().strip()
        if ' ' in key_line:
            key = list(map(int, key_line.split()))
        else:
            key = [int(c) for c in key_line]
        return key

# Giải mã Columnar Transposition
def columnar_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)

    # Tính số ô có dữ liệu thực
    total_cells = num_cols * num_rows
    padding = total_cells - len(ciphertext)

    # Tạo danh sách độ dài mỗi cột
    col_lengths = [num_rows] * num_cols
    sorted_key = sorted((num, idx) for idx, num in enumerate(key))
    for i in range(padding):
        # Cột cuối trong sorted_key sẽ thiếu 1 ký tự
        col_num = sorted_key[-(i+1)][1]
        col_lengths[col_num] -= 1

    # Cắt ciphertext thành từng cột theo đúng thứ tự
    cols = [''] * num_cols
    index = 0
    for num, idx in sorted_key:
        length = col_lengths[idx]
        cols[idx] = ciphertext[index:index+length]
        index += length

    # Đọc từng hàng để ghép lại bản rõ
    plaintext = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if row < len(cols[col]):
                plaintext += cols[col][row]

    return plaintext

# Ghi kết quả vào file
def save_plaintext(plaintext, filename="Columnar_Transposition_Cipher_Decryption.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(plaintext)

# ================================
# Chương trình chính
# ================================
if __name__ == "__main__":
    ciphertext = load_ciphertext("Columnar_Transposition_Cipher_encryption.txt")
    key = load_key("Columnar_Transposition_Cipher_key.txt")
    plaintext = columnar_decrypt(ciphertext, key)
    save_plaintext(plaintext, "Columnar_Transposition_Cipher_Decryption.txt")
    print("Đã giải mã xong. Kết quả lưu trong 'Columnar_Transposition_Cipher_Decryption.txt'")
