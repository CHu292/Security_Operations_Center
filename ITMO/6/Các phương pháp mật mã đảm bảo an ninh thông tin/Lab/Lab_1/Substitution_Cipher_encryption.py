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

def substitution_encrypt(text, key_map):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            idx = ord(char.upper()) - ord('A')
            sub_char = key_map[idx]
            result += sub_char if is_upper else sub_char.lower()
        else:
            result += char
    return result

def encrypt_file(input_file, key_file, output_file):
    key_map = load_substitution_key(key_file)
    if not key_map:
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            plaintext = f.read()

        ciphertext = substitution_encrypt(plaintext, key_map)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(ciphertext)

        print(f"Đã mã hóa xong. Kết quả lưu tại '{output_file}'.")

    except FileNotFoundError:
        print(f"Không tìm thấy file '{input_file}'")
    except Exception as e:
        print(f"Lỗi khi xử lý file: {e}")

# ===============================
# Thực thi chương trình
# ===============================
if __name__ == "__main__":
    input_file = "input.txt"
    key_file = "substitution_table_key.txt"
    output_file = "Substitution_Cipher_encryption.txt"

    encrypt_file(input_file, key_file, output_file)
