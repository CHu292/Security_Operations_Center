def caesar_decrypt(text, key):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

def decrypt_file(input_filename, output_filename, key):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            ciphertext = infile.read()
        
        plaintext = caesar_decrypt(ciphertext, key)

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(plaintext)

        print(f"Đã giải mã xong. Kết quả lưu trong '{output_filename}'.")

    except FileNotFoundError:
        print(f"Không tìm thấy file '{input_filename}'.")
    except Exception as e:
        print(f"Lỗi: {e}")

# ===============================
# Chương trình chính
# ===============================
if __name__ == "__main__":
    input_file = "caesar_encryption.txt"
    output_file = "caesar_decryption.txt"

    try:
        key = int(input("Nhập khóa giải mã Caesar (số nguyên): "))
        decrypt_file(input_file, output_file, key)
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
