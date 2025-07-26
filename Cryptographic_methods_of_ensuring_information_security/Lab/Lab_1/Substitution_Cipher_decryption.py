def load_substitution_key(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            line = f.readline().strip().upper()
            if len(line) != 26 or not line.isalpha():
                raise ValueError("Khóa không hợp lệ! Phải là 26 chữ cái không trùng.")
            return line
    except FileNotFoundError:
        print(f"Không tìm thấy file '{filename}'")
        return None
    except Exception as e:
        print(f"Lỗi khi đọc khóa: {e}")
        return None

def build_reverse_key_map(key_map):
    reverse_map = [''] * 26
    for i, char in enumerate(key_map):
        idx = ord(char) - ord('A')
        reverse_map[idx] = chr(ord('A') + i)
    return reverse_map

def substitution_decrypt(text, reverse_map):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            idx = ord(char.upper()) - ord('A')
            plain_char = reverse_map[idx]
            result += plain_char if is_upper else plain_char.lower()
        else:
            result += char
    return result

def decrypt_file(input_file, key_file, output_file):
    key_map = load_substitution_key(key_file)
    if not key_map:
        return

    reverse_map = build_reverse_key_map(key_map)

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            ciphertext = f.read()

        plaintext = substitution_decrypt(ciphertext, reverse_map)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(plaintext)

        print(f"Đã giải mã xong. Kết quả lưu tại '{output_file}'.")

    except FileNotFoundError:
        print(f"Không tìm thấy file '{input_file}'")
    except Exception as e:
        print(f"Lỗi khi xử lý file: {e}")

# ===============================
# Thực thi chương trình
# ===============================
if __name__ == "__main__":
    input_file = "Substitution_Cipher_encryption.txt"
    key_file = "substitution_table_key.txt"
    output_file = "Substitution_Cipher_decryption.txt"

    decrypt_file(input_file, key_file, output_file)
